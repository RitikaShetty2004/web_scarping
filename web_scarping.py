import requests
from bs4 import BeautifulSoup

# Define the Wikipedia page URL
url = "https://en.wikipedia.org/wiki/Web_scraping"

# Send a GET request to fetch the HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract the title of the page
    title = soup.title.text
    print("Page Title:", title)
    
    # Extract the first paragraph
    first_paragraph = soup.find("p").text
    print("\nFirst Paragraph:\n", first_paragraph)

    # Extract all headings (h2 tags)
    headings = soup.find_all("h2")
    print("\nHeadings:")
    for h in headings:
        print("-", h.text.strip())

    # Extract first 5 links
    links = soup.find_all("a", href=True)
    print("\nFirst 5 Links:")
    for link in links[:5]:
        print(link['href'])

else:
    print("Failed to fetch data. Status code:", response.status_code)
    