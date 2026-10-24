---
title: Insertion d’une image dans une cellule
linktitle: Insertion d’une image dans une cellule
description: Aspose.Cells est une bibliothèque Python permettant de travailler avec des fichiers de tableur. Cet article explique comment ajuster une image exactement à une seule cellule, soit en plaçant une image flottante sur la cellule, soit en incorporant l’image directement dans la cellule.
keywords: Aspose.Cells, bibliothèque Python, tableur, insérer une image, incorporer une image, image dans une cellule, ajuster une image à une cellule, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/python-net/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells propose deux méthodes distinctes pour associer une image à une seule cellule. Une image flottante est une forme située sur la couche de dessin de la feuille de calcul et qui recouvre visuellement une plage de cellules, tandis qu’une image incorporée est stockée dans la cellule elle-même et s’adapte automatiquement à sa zone d’affichage. Choisissez l’approche qui répond le mieux à vos exigences de mise en page.
{{% /alert %}}

## **Introduction**
L’ajustement exact d’une image à une seule cellule est une exigence courante lors de la conception de feuilles de calcul qui servent de rapports visuels, de catalogues de produits, d’annuaires du personnel, de tableaux de bord ou de listes de stock. Au lieu d’étirer une image sur plusieurs cellules ou de la placer sans contrainte sur une feuille de calcul, vous pouvez vouloir une image nette et liée à la cellule, qui reste alignée sur la cellule qui la contient.
Aspose.Cells prend en charge ce scénario de deux façons complémentaires :
- **Approche 1 — Placer une image flottante sur une cellule.** Ajoutez un `Picture` à la feuille de calcul, définissez son `placement` sur `MOVE_AND_SIZE`, puis ajustez ses cellules d’ancrage (`upper_left_row`, `upper_left_column`, `lower_right_row`, `lower_right_column`) afin que l’image couvre exactement une cellule.
- **Approche 2 — Incorporer une image directement dans une cellule.** Attribuez des octets d’image à la propriété `embedded_image` de la cellule. L’image s’adapte automatiquement à la zone d’affichage de la cellule et se déplace avec elle.
La suite de cet article présente les deux approches, explique les API concernées et montre leur utilisation dans le code.

## **Approche 1 : Placer une image sur une cellule**
Une image flottante est un objet `Picture` qui réside sur la couche de dessin de la feuille de calcul. Bien qu’elle ne fasse pas partie d’une cellule précise, elle est ancrée à une plage de cellules. Les cellules d’ancrage de l’image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image nouvellement ajoutée s’étend sur plusieurs cellules.
Pour faire couvrir **exactement une cellule** par une image flottante, vous devez :
1. Ajouter l’image à l’aide de `Worksheet.pictures.add(row, column, stream)`, qui ancre la nouvelle image à la cellule indiquée.
2. Définir les quatre propriétés d’ancrage afin que le rectangle englobant de l’image coïncide avec la cellule cible.
3. Définir `Picture.placement` sur `PlacementType.MOVE_AND_SIZE` afin que l’image se déplace et soit redimensionnée avec la cellule sous-jacente lorsque l’utilisateur modifie la largeur de colonne ou la hauteur de ligne.

### **Ancrage de l’image à une seule cellule**
L’ancrage de l’image est défini par quatre propriétés d’index à base zéro :
- `Picture.upper_left_row` — l’index de ligne du bord supérieur de l’image.
- `Picture.upper_left_column` — l’index de colonne du bord gauche de l’image.
- `Picture.lower_right_row` — l’index de ligne du bord inférieur de l’image. Pour que le bord inférieur de l’image se situe au bas de la ligne `r`, définissez cette propriété sur `r + 1`.
- `Picture.lower_right_column` — l’index de colonne du bord droit de l’image. Pour que le bord droit de l’image se situe à droite de la colonne `c`, définissez cette propriété sur `c + 1`.

{{% alert color="primary" %}}
Les index de ligne et de colonne dans Aspose.Cells sont **à base zéro**. La cellule C6 possède l’index de ligne 5 et l’index de colonne 2. Les erreurs de décalage d’une unité sur l’ancrage inférieur droit constituent la source la plus fréquente d’images qui semblent empiéter sur une cellule adjacente.
{{% /alert %}}

### **Contrôle du comportement de placement**
`Picture.placement` est une énumération de type `PlacementType` qui contrôle le comportement de l’image lorsque l’utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image occupant une seule cellule est `PlacementType.MOVE_AND_SIZE`, qui oblige l’image à se déplacer et à être redimensionnée avec la cellule sous-jacente, tout en préservant son ajustement exact.

### **Instructions pas à pas**
1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Récupérez la `Worksheet` cible via `workbook.worksheets[0]`.
3. Ouvrez le fichier image du disque dans un flux de fichier (ou un objet `BytesIO`) à l’aide d’un bloc `with`, afin que le flux soit correctement libéré.
4. Appelez `worksheet.pictures.add(5, 2, stream)` pour ajouter une image ancrée à la cellule C6. Conservez la référence à l’objet `Picture` renvoyée.
5. Définissez les quatre coordonnées d’ancrage afin que l’image couvre uniquement la cellule C6 : `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6`, `lower_right_column = 3`.
6. Définissez `picture.placement = PlacementType.MOVE_AND_SIZE` pour maintenir l’image alignée sur C6 lorsque la colonne ou la ligne est redimensionnée.
7. Ajoutez éventuellement du texte exemple aux cellules environnantes pour démontrer que seule la cellule C6 contient l’image.
8. Enregistrez le classeur sur le disque sous forme de fichier `.xlsx`.
Le code suivant présente l’approche complète.

```python
import aspose.cells as ac
from aspose.cells.drawing import PlacementType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
with open("logo.png", "rb") as fs:
    pic_index = worksheet.pictures.add(5, 2, fs)
    picture = worksheet.pictures[pic_index]
    picture.upper_left_row = 5
    picture.upper_left_column = 2
    picture.lower_right_row = 6
    picture.lower_right_column = 3
    picture.placement = PlacementType.MOVE_AND_SIZE
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Approche 2 : Incorporer une image directement dans une cellule**
Aspose.Cells expose également un mécanisme plus simple pour les images liées aux cellules : la propriété `Cell.embedded_image`. L’attribution d’octets d’image à cette propriété associe l’image à la cellule elle-même, comme si elle constituait un contenu intégré.

### **Fonctionnement des images incorporées**
- L’image est stockée dans le contenu de la cellule plutôt que sous forme de forme sur la couche de dessin.
- L’image s’adapte automatiquement aux limites de la zone de rendu de la cellule. Aucune coordonnée d’ancrage aucun paramètre de placement n’est requis.
- La cellule reste une cellule à part entière, dont l’adresse peut être référencée par des formules, utilisée dans le tri d’une ligne ou employée dans d’autres opérations au niveau des cellules.
Cela fait de `Cell.embedded_image` l’option la plus concise lorsque votre objectif est simplement d’obtenir « une image qui réside dans cette cellule ».

### **Instructions pas à pas**
1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Récupérez la `Worksheet` cible via `workbook.worksheets[0]`.
3. Lisez le fichier image du disque dans un objet `bytes` (par exemple, en ouvrant le fichier en mode binaire et en appelant `.read()`).
4. Obtenez une référence vers la cellule cible — soit via `worksheet.cells.get("C6")`, soit via `worksheet.cells.get(5, 2)`.
5. Attribuez l’objet `bytes` à la propriété `embedded_image` de la cellule.
6. Ajustez éventuellement la hauteur de la ligne et la largeur de la colonne cibles afin de donner plus de prominence à l’image incorporée.
7. Enregistrez le classeur sur le disque sous forme de fichier `.xlsx`.
Le code suivant présente l’approche complète.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Get the target cell C6
cell = worksheet.cells.get("C6")
# Read the image file into a byte array
with open("logo.png", "rb") as f:
    imageData = f.read()
# Embed the image directly into the cell
cell.embedded_image = imageData
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.cells.set_column_width(2, 30.0)   # Column C (index 2)
worksheet.cells.set_row_height(5, 100.0)     # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Choisir l’approche adaptée**
Les deux approches permettent d’obtenir une image ajustée à une seule cellule, mais elles diffèrent par leur mode de stockage et leur comportement :
- **Utilisez une image flottante (approche 1) lorsque :**
  - Vous avez besoin d’un contrôle précis du placement, de la superposition ou de l’alignement avec d’autres objets de dessin.
  - Vous souhaitez que l’image se comporte comme une forme pouvant être sélectionnée, réordonnée ou regroupée avec d’autres formes.
  - Vous devez assurer la compatibilité avec du code existant qui fonctionne déjà avec les collections `pictures`.
  - Vous devez calculer dynamiquement les coordonnées d’ancrage en fonction de la disposition de la feuille de calcul.
- **Utilisez une image incorporée (approche 2) lorsque :**
  - Vous souhaitez insérer une image dans une cellule de la manière la plus simple possible.
  - L’image doit se déplacer avec la cellule comme tout autre contenu de cellule.

## Articles connexes
- [Caméra Excel dans Aspose.Cells for Python via .NET](/cells/fr/python-net/excel-camera/)

{{< app/cells/assistant language="python-net" >}}