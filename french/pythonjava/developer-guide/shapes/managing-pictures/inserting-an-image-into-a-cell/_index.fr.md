---
title: Insertion d'une image dans une cellule
linktitle: Insertion d'une image dans une cellule
description: Aspose.Cells for Python via Java est une bibliothèque permettant de travailler avec des fichiers de tableurs. Cet article explique comment ajuster précisément une image à une seule cellule, soit en plaçant une image flottante au-dessus de la cellule, soit en incorporant directement l'image dans la cellule.
keywords: Aspose.Cells, Python via Java bibliothèque, tableur, insérer image, incorporer image, image dans cellule, ajuster image à cellule, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/python-java/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells propose deux méthodes distinctes pour associer une image à une seule cellule. Une image flottante est une forme située sur le calque de dessin de la feuille de calcul qui recouvre visuellement une plage de cellules, tandis qu'une image incorporée est stockée à l'intérieur de la cellule elle-même et s'adapte automatiquement à la zone d'affichage de la cellule. Choisissez l'approche qui correspond le mieux à vos exigences de mise en page.

## **Introduction**
Ajuster précisément une image à une seule cellule est une exigence courante lors de la conception de tableurs servant de rapports visuels, de catalogues de produits, d'annuaires d'employés, de tableaux de bord ou de listes d'inventaire. Plutôt que d'étirer une image sur plusieurs cellules ou de la placer de manière approximative sur une feuille de calcul, vous pouvez souhaiter obtenir une image nette, liée à la cellule, qui reste alignée avec la cellule à laquelle elle appartient.
Aspose.Cells prend en charge ce scénario de deux manières complémentaires :
- **Approche 1 — Placer une image flottante au-dessus d'une cellule.** Ajoutez une `Picture` à la feuille de calcul, définissez son `setPlacement` sur `MOVE_AND_SIZE`, puis ajustez ses cellules d'ancrage (`setUpperLeftRow`, `setUpperLeftColumn`, `setLowerRightRow`, `setLowerRightColumn`) afin que l'image couvre exactement une cellule.
- **Approche 2 — Incorporer une image directement dans une cellule.** Affectez les octets de l'image à la propriété `setEmbeddedImage` de la cellule. L'image s'adapte automatiquement à la zone d'affichage de la cellule et se déplace avec elle.
La suite de cet article détaille les deux approches, explique les API concernées et montre comment les utiliser en code.

## **Approche 1 : Placer une image au-dessus d'une cellule**
Une image flottante est un objet `Picture` qui réside sur le calque de dessin de la feuille de calcul. Bien qu'elle ne fasse partie d'aucune cellule individuelle, elle est ancrée à une plage de cellules. Les cellules d'ancrage de l'image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image nouvellement ajoutée s'étend sur plusieurs cellules.
Pour qu'une image flottante couvre **exactement une seule cellule**, vous devez :
1. Ajouter l'image à l'aide de `Worksheet.getPictures().add(int row, int column, InputStream stream)`, qui ancre la nouvelle image à la cellule indiquée.
2. Définir les quatre propriétés d'ancrage afin que le rectangle englobant de l'image coïncide avec la cellule cible.
3. Définir `Picture.setPlacement` sur `PlacementType.MOVE_AND_SIZE` afin que l'image se déplace et se redimensionne avec la cellule sous-jacente lorsque l'utilisateur modifie la largeur de la colonne ou la hauteur de la ligne.

### **Ancrage de l'image à une seule cellule**
L'ancrage de l'image est défini par quatre propriétés d'index de base zéro :
- `setUpperLeftRow` — l'index de la ligne du bord supérieur de l'image.
- `setUpperLeftColumn` — l'index de la colonne du bord gauche de l'image.
- `setLowerRightRow` — l'index de la ligne du bord inférieur de l'image. Pour que le bord inférieur de l'image se trouve au bas de la ligne `r`, définissez cette valeur sur `r + 1`.
- `setLowerRightColumn` — l'index de la colonne du bord droit de l'image. Pour que le bord droit de l'image se trouve à droite de la colonne `c`, définissez cette valeur sur `c + 1`.

{{% alert color="primary" %}}
Les index de lignes et de colonnes dans Aspose.Cells sont **de base zéro**. La cellule C6 a pour index de ligne 5 et pour index de colonne 2. Les erreurs de décalage d'une unité sur l'ancrage inférieur droit sont la source la plus fréquente d'images qui semblent empiéter sur une cellule adjacente.

### **Contrôle du comportement de positionnement**
`getPlacement` est une énumération de type `PlacementType` qui contrôle le comportement de l'image lorsque l'utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image dans une seule cellule est `PlacementType.MOVE_AND_SIZE`, qui provoque le déplacement et le redimensionnement simultanés de l'image avec sa cellule sous-jacente, en préservant l'ajustement exact.

### **Instructions étape par étape**
1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez au `Worksheet` cible via `workbook.getWorksheets().get(0)`.
3. Ouvrez le fichier image du disque dans un `InputStream` (généralement un `FileInputStream`) afin que le flux soit correctement fermé.
4. Appelez `worksheet.getPictures().add(5, 2, stream)` pour ajouter une image ancrée à la cellule C6. Récupérez la référence `Picture` renvoyée.
5. Définissez les quatre coordonnées d'ancrage afin que l'image couvre uniquement la cellule C6 : `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Définissez `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` pour maintenir l'image alignée avec C6 lors du redimensionnement de la colonne ou de la ligne.
7. Vous pouvez éventuellement ajouter du texte d'exemple dans les cellules environnantes pour démontrer que seule la cellule C6 contient l'image.
8. Enregistrez le classeur sur le disque sous forme de fichier `.xlsx`.
Le code suivant illustre l'approche complète.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, SaveFormat, PlacementType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
FileInputStream = jpype.JClass("java.io.FileInputStream")
fs = FileInputStream("logo.png")
try:
    picIndex = worksheet.getPictures().add(5, 2, fs)
    picture = worksheet.getPictures().get(picIndex)
    picture.setUpperLeftRow(5)
    picture.setUpperLeftColumn(2)
    picture.setLowerRightRow(6)
    picture.setLowerRightColumn(3)
    picture.setPlacement(PlacementType.MoveAndSize)
finally:
    fs.close()
workbook.save("output.xlsx", SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **Approche 2 : Incorporer une image directement dans une cellule**
Aspose.Cells expose également un mécanisme plus simple pour les images liées à une cellule : la propriété `Cell.setEmbeddedImage`. Affecter des octets d'image à cette propriété attache l'image à la cellule elle-même, comme s'il s'agissait d'un contenu en ligne.

### **Fonctionnement des images incorporées**
- L'image est stockée dans le contenu de la cellule plutôt que sous forme de forme sur le calque de dessin.
- L'image s'adapte automatiquement aux limites rendues de la cellule. Aucune coordonnée d'ancrage ni paramètre de positionnement n'est requis.
- La cellule reste une vraie cellule avec une adresse réelle qui peut être référencée par des formules, triée dans le cadre d'une ligne, ou utilisée dans d'autres opérations au niveau de la cellule.
Cela fait de `Cell.setEmbeddedImage` l'option la plus concise lorsque votre objectif est simplement « une image qui réside à l'intérieur de cette cellule ».

### **Instructions étape par étape**
1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez au `Worksheet` cible via `workbook.getWorksheets().get(0)`.
3. Lisez le fichier image du disque dans un tableau `byte[]` (par exemple, en utilisant un appel `Files.readAllBytes` depuis `java.nio.file.Files`).
4. Obtenez une référence à la cellule cible — soit via `worksheet.getCells().get("C6")`, soit via `worksheet.getCells().get(5, 2)`.
5. Affectez le tableau d'octets à la propriété `setEmbeddedImage` de la cellule.
6. Vous pouvez éventuellement ajuster la hauteur de la ligne et la largeur de la colonne cibles pour donner à l'image incorporée une apparence plus proéminente.
7. Enregistrez le classeur sur le disque sous forme de fichier `.xlsx`.
Le code suivant illustre l'approche complète.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Get the target cell C6
cell = worksheet.getCells().get("C6")
# Read the image file into a byte array
imageData = open("logo.png", "rb").read()
# Embed the image directly into the cell
cell.setEmbeddedImage(imageData)
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30)   # Column C (index 2)
worksheet.getCells().setRowHeight(5, 100)    # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **Choisir la bonne approche**
Les deux approches produisent une image qui s'ajuste à l'intérieur d'une seule cellule, mais elles diffèrent par la manière dont l'image est stockée et dont elle se comporte :
- **Utilisez une image flottante (Approche 1) lorsque :**
  - Vous avez besoin d'un contrôle plus fin sur le positionnement, la superposition ou l'alignement avec d'autres objets de dessin.
  - Vous souhaitez que l'image se comporte comme une forme pouvant être sélectionnée, réorganisée ou groupée avec d'autres formes.
  - Vous avez besoin d'une compatibilité ascendante avec du code qui fonctionne déjà avec `PictureCollection`.
  - Vous devez calculer les coordonnées d'ancrage de manière dynamique en fonction de la mise en page de la feuille de calcul.
- **Utilisez une image incorporée (Approche 2) lorsque :**
  - Vous souhaitez l'insertion la plus simple possible d'une image dans une cellule.
  - L'image doit se déplacer avec la cellule comme n'importe quel autre contenu de cellule.
  - Vous n'avez pas besoin de manipuler l'image comme une forme.
{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="python" >}}