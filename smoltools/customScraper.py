from bs4 import BeautifulSoup
from smolagents import tool
import requests


@tool
def scrape_page_with_python(url: str) -> str:
    """Scrapes content from a webpage using Python libraries (requests and BeautifulSoup).

    Args:
        url: The URL of the webpage to scrape. Must be a valid web address to extract content from.

    Returns:
        str: The scraped content in markdown format.
    """
    print(f"Scraping content from: {url}")

    try:
        # Effettua la richiesta HTTP
        response = requests.get(url)
        response.raise_for_status()  # Controlla eventuali errori HTTP

        # Analizza il contenuto HTML della pagina
        soup = BeautifulSoup(response.text, "html.parser")

        # Estrae il testo visibile dalla pagina
        text_content = soup.get_text(separator="\n", strip=True)

        # (Facoltativo) Converte il testo in Markdown
        # Per esempio, puoi aggiungere titoli o elenchi in formato Markdown
        markdown_content = text_content  # Puoi formattare ulteriormente se necessario

        return markdown_content

    except requests.exceptions.RequestException as e:
        return f"Error fetching the webpage: {e}"
    except Exception as e:
        return f"An error occurred: {e}"