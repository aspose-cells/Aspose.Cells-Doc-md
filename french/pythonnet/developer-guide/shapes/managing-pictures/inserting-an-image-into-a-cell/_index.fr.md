---
title: Insertion d'une image dans une cellule
linktitle: Insertion d'une image dans une cellule
description: Aspose.Cells est une bibliothèque Python permettant de travailler avec des fichiers de feuilles de calcul. Cet article explique comment ajuster une image exactement à une seule cellule, soit en plaçant une image flottante sur la cellule, soit en intégrant l'image directement dans la cellule.
keywords: Aspose.Cells, bibliothèque Python, feuille de calcul, insérer image, intégrer image, image dans cellule, ajuster image à cellule, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/python-net/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells propose deux méthodes distinctes pour associer une image à une seule cellule. Une image flottante est une forme située sur la couche de dessin de la feuille de calcul qui se superpose visuellement à une plage de cellules, tandis qu'une image intégrée est stockée à l'intérieur de la cellule elle-même et s'adapte automatiquement à la zone d'affichage de la cellule. Choisissez l'approche qui correspond le mieux à vos besoins de mise en page.

## **Introduction**
Ajuster une image exactement à une seule cellule est une exigence courante lors de la conception de feuilles de calcul servant de rapports visuels, de catalogues de produits, d'annuaires d'employés, de tableaux de bord ou de listes d'inventaire. Plutôt que d'étirer une image sur plusieurs cellules ou de la placer de manière lâche sur une feuille de calcul, vous pouvez souhaiter une image nette, liée à la cellule, qui reste alignée avec la cellule qui la possède.
Aspose.Cells prend en charge ce scénario de deux manières complémentaires :
- **Approche 1 — Placer une image flottante sur une cellule.** Ajoutez un `Picture` à la feuille de calcul, définissez son `placement` sur `MOVE_AND_SIZE`, et ajustez ses cellules d'ancrage (`upper_left_row`, `upper_left_column`, `lower_right_row`, `lower_right_column`) pour que l'image couvre exactement une cellule.
- **Approche 2 — Intégrer une image directement dans une cellule.** Affectez les octets de l'image à la propriété `embedded_image` de la cellule. L'image s'adapte automatiquement à la zone d'affichage de la cellule et se déplace avec la cellule.
Le reste de cet article détaille les deux approches, explique les API pertinentes et montre comment les utiliser dans le code.

## **Approche 1 : Placer une image sur une cellule**
Une image flottante est un objet `Picture` qui se trouve sur la couche de dessin de la feuille de calcul. Bien qu'elle ne fasse partie d'aucune cellule unique, elle est ancrée à une plage de cellules. Les cellules d'ancrage de l'image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image fraîchement ajoutée s'étend sur plusieurs cellules.
Pour qu'une image flottante couvre **exactement une cellule**, vous devez :
1. Ajouter l'image en utilisant `Worksheet.pictures.add(row, column, stream)`, qui ancre la nouvelle image à la cellule donnée.
2. Définir les quatre propriétés d'ancrage pour que le rectangle englobant de l'image coïncide avec la cellule cible.
3. Définir `Picture.placement` sur `PlacementType.MOVE_AND_SIZE` afin que l'image se déplace et se redimensionne avec la cellule sous-jacente lorsque l'utilisateur modifie la largeur de colonne ou la hauteur de ligne.

### **Ancrage de l'image à une seule cellule**
L'ancrage de l'image est défini par quatre propriétés d'index à base zéro :
- `Picture.upper_left_row` — l'index de ligne du bord supérieur de l'image.
- `Picture.upper_left_column` — l'index de colonne du bord gauche de l'image.
- `Picture.lower_right_row` — l'index de ligne du bord inférieur de l'image. Pour que le bord inférieur de l'image se trouve au bas de la ligne `r`, définissez cette valeur sur `r + 1`.
- `Picture.lower_right_column` — l'index de colonne du bord droit de l'image. Pour que le bord droit de l'image se trouve à droite de la colonne `c`, définissez cette valeur sur `c + 1`.

{{% alert color="primary" %}}
Les indices de ligne et de colonne dans Aspose.Cells sont **à base zéro**. La cellule C6 a l'index de ligne 5 et l'index de colonne 2. Les erreurs d'une unité sur l'ancre inférieure droite sont la source la plus fréquente d'images qui semblent empiéter sur une cellule adjacente.

### **Contrôle du comportement de placement**
`Picture.placement` est une énumération de type `PlacementType` qui contrôle le comportement de l'image lorsque l'utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image dans une seule cellule est `PlacementType.MOVE_AND_SIZE`, ce qui fait que l'image se déplace et se redimensionne avec sa cellule sous-jacente, en préservant l'ajustement exact.

### **Instructions étape par étape**
1. Créer un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accéder à la `Worksheet` cible depuis `workbook.worksheets[0]`.
3. Ouvrir le fichier image du disque dans un flux de fichier (ou un objet `BytesIO`) à l'aide d'un bloc `with` afin que le flux soit correctement libéré.
4. Appeler `worksheet.pictures.add(5, 2, stream)` pour ajouter une image ancrée à la cellule C6. Capturer la référence `Picture` renvoyée.
5. Définir les quatre coordonnées d'ancrage pour que l'image couvre uniquement la cellule C6 : `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6`, `lower_right_column = 3`.
6. Définir `picture.placement = PlacementType.MOVE_AND_SIZE` pour maintenir l'alignement de l'image avec C6 lorsque la colonne ou la ligne est redimensionnée.
7. Optionnellement, ajouter du texte d'exemple aux cellules environnantes pour démontrer que seule la cellule C6 contient l'image.
8. Enregistrer le classeur sur le disque sous forme de fichier `.xlsx`.
Le code suivant illustre l'approche complète.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
with open("logo.png", "rb") as fs:
    pic_index = worksheet.pictures.add(5, 2, fs)
    picture = worksheet.pictures[pic_index]
    picture.upper_left_row = 5
    picture.upper_left_column = 2
    picture.lower_right_row = 6
    picture.lower_right_column = 3
    picture.placement = ac.PlacementType.MOVE_AND_SIZE
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Approche 2 : Intégrer une image directement dans une cellule**
Aspose.Cells expose également un mécanisme plus simple pour les images liées aux cellules : la propriété `Cell.embedded_image`. Affecter des octets d'image à cette propriété attache l'image à la cellule elle-même, comme s'il s'agissait d'un contenu en ligne.

### **Fonctionnement des images intégrées**
- L'image est stockée dans le contenu de la cellule plutôt que comme une forme sur la couche de dessin.
- L'image s'adapte automatiquement aux limites rendues de la cellule. Aucune coordonnée d'ancrage ni paramètre de placement n'est requis.
- La cellule reste une vraie cellule avec une vraie adresse qui peut être référencée par des formules, triée dans le cadre d'une ligne, ou utilisée dans d'autres opérations au niveau de la cellule.
Cela fait de `Cell.embedded_image` l'option la plus concise lorsque votre objectif est simplement « une image qui vit à l'intérieur de cette cellule ».

### **Instructions étape par étape**
1. Créer un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accéder à la `Worksheet` cible depuis `workbook.worksheets[0]`.
3. Lire le fichier image du disque dans un objet `bytes` (par exemple, en ouvrant le fichier en mode binaire et en appelant `.read()`).
4. Obtenir une référence à la cellule cible — soit via `worksheet.cells["C6"]`, soit via `worksheet.cells[5, 2]`.
5. Affecter l'objet bytes à la propriété `embedded_image` de la cellule.
6. Optionnellement, ajuster la hauteur de ligne et la largeur de colonne de la ligne et de la colonne cibles pour donner à l'image intégrée une apparence plus proéminente.
7. Enregistrer le classeur sur le disque sous forme de fichier `.xlsx`.
Le code suivant illustre l'approche complète.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Get the target cell C6
cell = worksheet.cells["C6"]
# Read the image file into a byte array
with open("logo.png", "rb") as f:
    imageData = f.read()
# Embed the image directly into the cell
cell.embedded_image = imageData
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.cells.set_column_width(2, 30)   # Column C (index 2)
worksheet.cells.set_row_height(5, 100)     # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Choisir la bonne approche**
Les deux approches produisent une image qui s'inscrit dans une seule cellule, mais elles diffèrent dans la manière dont l'image est stockée et dont elle se comporte :
- **Utilisez une image flottante (Approche 1) lorsque :**
  - Vous avez besoin d'un contrôle plus fin sur le placement, la superposition ou l'alignement avec d'autres objets de dessin.
  - Vous souhaitez que l'image se comporte comme une forme pouvant être sélectionnée, réordonnée ou regroupée avec d'autres formes.
  - Vous avez besoin d'une compatibilité avec du code existant qui fonctionne déjà avec les collections `pictures`.
  - Vous avez besoin de calculer les coordonnées d'ancrage dynamiquement en fonction de la disposition de la feuille de calcul.
- **Utilisez une image intégrée (Approche 2) lorsque :**
  - Vous souhaitez l'insertion la plus simple possible d'une image dans une cellule.
  - L'image doit se déplacer avec la cellule comme tout autre contenu de cellule.
  - Vous n'avez pas besoin de manipuler l'image comme une forme.
{{% /alert %}}

{{% /alert %}}

## Articles connexes
- [Excel Camera in Aspose.Cells for Python via .NET](/cells/fr/python-net/excel-camera/)
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via .NET](/cells/fr/python-net/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via .NET](/cells/fr/python-net/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/fr/python-net/change-page-field-layout/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for Python via .NET](/cells/fr/python-net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="python" >}}