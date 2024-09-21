import requests
from bs4 import BeautifulSoup
import os


# Function for parsing links
def parse_links(soup):
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return "\n".join(links)


# Function for parsing HTML code
def parse_html(soup):
    return soup.prettify()


# Main function
def main():
    # Enter the link
    url = input("Enter the link to the site (for example, https://example.com): ")

    try:
        # Request the page content
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return

    # Parse the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # We ask what needs to be parsed
    choice = input("What do you want to parse? Enter 'links' for links or 'HTML' for code:").strip().lower()

    # Depending on the choice, we parse links or HTML code
    if choice == 'links':
        result = parse_links(soup)
        file_name = "parsed_links.txt"
    elif choice == 'html':
        result = parse_html(soup)
        file_name = "parsed_html.txt"
    else:
        print("Incorrect choice. Try again.")
        return

    # Save the result to a file
    with open(file_name, "w", encoding='utf-8') as file:
        file.write(result)

    print(f"The result is saved to file: {file_name}")


# Launch the program
if __name__ == "__main__":
    main()
