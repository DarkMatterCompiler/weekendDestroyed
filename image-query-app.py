import streamlit as st
import requests
from duckduckgo_search import DDGS

import requests

def brave_search(query, api_key, max_results=5):
    """
    Perform a web and image search using the Brave Search API.
    
    :param query: The search query string
    :param api_key: Your Brave Search API key
    :param country: The country code for localized results (default: 'US')
    :param max_results: Maximum number of results to return for each type (default: 5)
    :return: A tuple containing two lists: web results and image results
    """
    base_url = "https://api.search.brave.com/res/v1"
    
    headers = {
        "Accept": "application/json",
        "X-Subscription-Token": api_key
    }
    
    params = {
        "q": query,
        "count": max_results
    }
    
    web_results = []
    image_results = []
    
    try:
        # Web search
        web_response = requests.get(f"{base_url}/web/search", headers=headers, params=params)
        web_response.raise_for_status()
        web_data = web_response.json()
        
        for item in web_data.get('web', {}).get('results', []):
            web_results.append({
                'title': item.get('title', ''),
                'url': item.get('url', ''),
                'description': item.get('description', '')
            })
        
        # Image search
        image_response = requests.get(f"{base_url}/images/search", headers=headers, params=params)
        image_response.raise_for_status()
        image_data = image_response.json()
        
        for item in image_data.get('images', []):
            image_results.append({
                'title': item.get('title', ''),
                'url': item.get('url', ''),
                'image_url': item.get('image_url', ''),
                'source': item.get('source', '')
            })
        
        return web_results, image_results
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return ['didnt work'], ['hah']

# Define the external URLs
url = "https://2ff5-34-124-176-162.ngrok-free.app//rag_pipeline"
url2 = "https://e450-34-125-122-228.ngrok-free.app//web_search"

def search_with_custom_user_agent(query, max_results=5):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    headers = {"User-Agent": user_agent}
    ddgs = DDGS(headers=headers)
    try:
        results_text = ddgs.text(query, max_results=max_results)
        return list(results_text)
    except Exception as e:
        st.error(f"An error occurred during search: {e}")
        return []

def main_function(img, inp, api_key):
    try:
        description = requests.post(url, json={"query": img}).json()['final_answer']
        st.write("Description:", description)
        
        final = description + "||" + inp
        response = requests.post(url2, json={"query": final}).json()['final_answer']

        web_results, image_results = brave_search(response, api_key)
        return response, web_results, image_results
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "", [], []

st.title("Image Query App")

img_url = st.text_input("Enter image URL:")
query = st.text_input("Enter your query:")
api_key = st.text_input("Enter your Brave Search API key:", type="password")

if st.button("Submit"):
    if img_url and query and api_key:
        with st.spinner("Processing..."):
            web_search_query, web_results, image_results = main_function(img_url, query, api_key)
        
        st.subheader("Web Search Query:")
        st.text_area("Generated query:", value=web_search_query, height=100, disabled=True)
        
        if web_results:
            st.subheader("Web Search Results:")
            for idx, result in enumerate(web_results, 1):
                st.markdown(f"**Result {idx}: [{result['title']}]({result['url']})**")
                st.write(result['description'])
        else:
            st.warning("No web results found.")
        
        if image_results:
            st.subheader("Image Search Results:")
            cols = st.columns(5)  # Create 5 columns for images
            for idx, result in enumerate(image_results):
                with cols[idx % 5]:
                    st.image(result['image_url'], caption=result['title'], use_column_width=True)
                    st.markdown(f"[Source]({result['url']})")
        else:
            st.warning("No image results found.")
    else:
        st.warning("Please enter image URL, query, and API key.")