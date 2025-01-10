import os
import zipfile
import io
from PIL import Image
from rembg import remove
from tkinter import Tk, filedialog, simpledialog

def resize_image(img, max_size):
    """
    Redimensionne une image si elle dépasse une taille maximale.

    Args:
        img (PIL.Image): L'image à redimensionner.
        max_size (tuple): Taille maximale (largeur, hauteur).

    Returns:
        PIL.Image: L'image redimensionnée ou originale.
    """
    if img.width > max_size[0] or img.height > max_size[1]:
        img.thumbnail(max_size)
    return img

def create_bdnf_zip(input_dir, output_zip, thumbnail_size=(256, 256), max_image_size=(1920, 1080), detour=True):
    """
    Crée un fichier ZIP compatible BDNF avec une structure Thumbnails et Highres.

    Args:
        input_dir (str): Répertoire contenant les images source.
        output_zip (str): Nom du fichier ZIP de sortie.
        thumbnail_size (tuple): Dimensions des vignettes (largeur, hauteur).
        max_image_size (tuple): Taille maximale des images (largeur, hauteur).
        detour (bool): Indique si les images doivent être détourées.
    """
    thumbnails_dir = "Thumbnails"
    highres_dir = "Highres"
    clusters = []

    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Parcourir les images dans le répertoire source
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
                    file_path = os.path.join(root, file)

                    try:
                        with Image.open(file_path) as img:
                            img = img.convert("RGBA")

                            if detour:
                                # Utiliser rembg pour supprimer le fond
                                img_bytes = remove(open(file_path, "rb").read())
                                img = Image.open(io.BytesIO(img_bytes)).convert("RGBA")

                            # Redimensionner l'image si elle dépasse la taille maximale
                            img = resize_image(img, max_image_size)

                            # Enregistrer l'image haute résolution
                            temp_highres_path = os.path.join(os.getcwd(), f"{file}.highres")
                            img.save(temp_highres_path, format="PNG")
                            highres_path = os.path.join(highres_dir, file)
                            zipf.write(temp_highres_path, highres_path)
                            os.remove(temp_highres_path)

                            # Créer une vignette
                            img.thumbnail(thumbnail_size)
                            temp_thumb_path = os.path.join(os.getcwd(), f"{file}.thumbnail")
                            img.save(temp_thumb_path, format="PNG")
                            thumbnail_path = os.path.join(thumbnails_dir, file)
                            zipf.write(temp_thumb_path, thumbnail_path)
                            os.remove(temp_thumb_path)

                            # Ajouter les informations au fichier XML
                            clusters.append(f"<Cluster><Name>{file}</Name><Path>{highres_path}</Path></Cluster>")
                    except Exception as e:
                        print(f"Erreur lors du traitement de l'image {file}: {e}")

        # Ajouter un fichier Cluster.xml avec une structure compatible
        cluster_content = """<Clusters>
{}</Clusters>""".format("\n".join(clusters))
        zipf.writestr("Cluster.xml", cluster_content)

    print(f"Fichier ZIP créé : {output_zip}")

if __name__ == "__main__":
    # Interface utilisateur pour choisir le répertoire source et le fichier ZIP de sortie
    Tk().withdraw()  # Masquer la fenêtre principale de Tkinter
    print("Créateur de Corpus pour BDNF: choisissez le répertoire où se trouve vos photos détourées par canal alpha")
    input_directory = filedialog.askdirectory(title="Choisissez le répertoire contenant les images")

    if not input_directory:
        print("Aucun répertoire sélectionné. Opération annulée.")
    else:
        detour_choice = simpledialog.askstring(
            "Détourage des images",
            "Voulez-vous détourer les images avant la création du corpus ? (oui/non)"
        )
        detour = detour_choice.lower() == "oui"

        output_zip_file = filedialog.asksaveasfilename(
            title="Choisissez l'emplacement du fichier ZIP de sortie",
            defaultextension=".zip",
            filetypes=[("Fichiers ZIP", "*.zip")]
        )

        if not output_zip_file:
            print("Aucun emplacement de fichier sélectionné. Opération annulée.")
        else:
            create_bdnf_zip(input_directory, output_zip_file, detour=detour)
