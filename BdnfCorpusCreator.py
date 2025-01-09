import os
import zipfile
from PIL import Image, ImageOps
from tkinter import Tk, filedialog, simpledialog

def create_bdnf_zip(input_dir, output_zip, thumbnail_size=(256, 256), detour=True):
    """
    Crée un fichier ZIP compatible BDNF avec une structure Thumbnails et Highres.

    Args:
        input_dir (str): Répertoire contenant les images source.
        output_zip (str): Nom du fichier ZIP de sortie.
        thumbnail_size (tuple): Dimensions des vignettes (largeur, hauteur).
        detour (bool): Indique si les images doivent être détourées.
    """
    thumbnails_dir = "Thumbnails"
    highres_dir = "Highres"

    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Parcourir les images dans le répertoire source
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
                    file_path = os.path.join(root, file)

                    try:
                        with Image.open(file_path) as img:
                            img = img.convert("RGBA")

                            if detour and not img.getchannel("A").getbbox() is not None:
                                # Détourer uniquement si l'image n'a pas déjà un canal alpha significatif
                                alpha = Image.new("L", img.size, 0)
                                img = ImageOps.fit(img, img.size, centering=(0.5, 0.5))
                                for x in range(img.size[0]):
                                    for y in range(img.size[1]):
                                        r, g, b, a = img.getpixel((x, y))
                                        if r > 240 and g > 240 and b > 240:  # Détection des pixels blancs
                                            alpha.putpixel((x, y), 0)
                                        else:
                                            alpha.putpixel((x, y), 255)
                                img.putalpha(alpha)

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
                    except Exception as e:
                        print(f"Erreur lors du traitement de l'image {file}: {e}")

        # Ajouter un fichier Cluster.xml vide par défaut (ou personnalisé)
        cluster_content = """<Cluster><Description>BDNF Corpus</Description></Cluster>"""
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
