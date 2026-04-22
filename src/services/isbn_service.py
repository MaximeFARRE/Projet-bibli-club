import requests
import logging

def fetch_book_info_by_isbn(isbn: str) -> dict:
    """
    Récupère les informations d'un livre à partir de son ISBN via l'API Google Books.
    Retourne un dictionnaire avec titre, auteur, resume et couverture, ou None si non trouvé.
    """
    clean_isbn = "".join(filter(str.isdigit, isbn))
    if not clean_isbn:
        return None
        
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{clean_isbn}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        if "items" not in data or len(data["items"]) == 0:
            return None
            
        volume_info = data["items"][0].get("volumeInfo", {})
        
        titre = volume_info.get("title", "")
        auteurs = volume_info.get("authors", [])
        auteur = ", ".join(auteurs) if auteurs else ""
        resume = volume_info.get("description", "")
        
        image_links = volume_info.get("imageLinks", {})
        couverture = image_links.get("thumbnail", image_links.get("smallThumbnail", ""))
        
        if couverture and couverture.startswith("http://"):
            couverture = couverture.replace("http://", "https://")
            
        return {
            "titre": titre,
            "auteur": auteur,
            "resume": resume,
            "couverture": couverture
        }
    except Exception as e:
        logging.error(f"Erreur lors de la récupération de l'ISBN {isbn}: {e}")
        return None
