import requests
from bs4 import BeautifulSoup

def scrape_blog(url):
    # Send an HTTP request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant information
        article_titles = [title.text for title in soup.find_all('h2', class_='article-title')]
        article_contents = [content.text for content in soup.find_all('div', class_='article-content')]

        # Return the extracted data
        return {'titles': article_titles, 'contents': article_contents}
    else:
        # If the request was not successful, print an error message
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# Example usage:
url = 'https://example-blog.com'
result = scrape_blog(url)

if result:
    for title, content in zip(result['titles'], result['contents']):
        print(f"Title: {title}\nContent: {content}\n{'=' * 30}")
