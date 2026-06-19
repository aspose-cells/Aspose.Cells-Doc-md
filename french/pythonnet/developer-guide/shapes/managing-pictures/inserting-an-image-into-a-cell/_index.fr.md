---
title: Insertion d'une image dans une cellule
description: Aspose.Cells est une bibliothèque Python permettant de travailler avec des fichiers de tableur. Cet article explique comment ajuster une image exactement à la taille d'une seule cellule en utilisant deux approches différentes : placer une image flottante par-dessus la cellule, ou intégrer l'image directement dans la cellule.
keywords: Aspose.Cells, Python library, spreadsheet, insert image, embed image, picture in cell, fit image to cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/python-net/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells propose deux méthodes distinctes pour associer une image à une seule cellule. Une image flottante est une forme située sur le calque de dessin de la feuille de calcul qui recouvre visuellement une plage de cellules, tandis qu'une image intégrée est stockée à l'intérieur de la cellule elle-même et s'adapte automatiquement à la zone d'affichage de la cellule. Choisissez l'approche qui correspond le mieux à vos exigences de mise en page.

{{% /alert %}}

## **Introduction**

Ajuster une image exactement à la taille d'une seule cellule est une exigence courante lors de la conception de tableurs servant de rapports visuels, de catalogues de produits, d'annuaires d'employés, de tableaux de bord ou de listes d'inventaire. Plutôt que d'étirer une image sur plusieurs cellules ou de la placer de manière approximative sur une feuille de calcul, vous pouvez souhaiter une image nette, liée à la cellule, qui reste alignée avec la cellule qui la contient.

Aspose.Cells prend en charge ce scénario de deux manières complémentaires :

- **Approche 1 — Placer une image flottante par-dessus une cellule.** Ajoutez un `Picture` à la feuille de calcul, définissez son `placement` sur `MOVE_AND_SIZE`, et ajustez ses cellules d'ancrage (`upper_left_row`, `upper_left_column`, `lower_right_row`, `lower_right_column`) de sorte que l'image couvre exactement une cellule.
- **Approche 2 — Intégrer une image directement dans une cellule.** Assignez les octets de l'image à la propriété `embedded_image` de la cellule. L'image se met automatiquement à l'échelle pour s'adapter à la zone d'affichage de la cellule et se déplace avec la cellule.

La suite de cet article présente les deux approches, explique les API concernées, et montre comment les utiliser dans le code.

## **Approche 1 : Placer une image par-dessus une cellule**

Une image flottante est un objet `Picture` qui réside sur le calque de dessin de la feuille de calcul. Bien qu'elle ne fasse partie d'aucune cellule spécifique, elle est ancrée à une plage de cellules. Les cellules d'ancrage de l'image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image fraîchement ajoutée s'étend sur plusieurs cellules.

Pour qu'une image flottante couvre **exactement une cellule**, vous devez :

1. Ajouter l'image à l'aide de `Worksheet.pictures.add(row, column, stream)`, ce qui ancre la nouvelle image à la cellule indiquée.
2. Définir les quatre propriétés d'ancrage de sorte que le rectangle englobant de l'image coïncide avec la cellule cible.
3. Définir `Picture.placement` sur `PlacementType.MOVE_AND_SIZE` afin que l'image se déplace et se redimensionne avec la cellule sous-jacente lorsque l'utilisateur modifie la largeur de colonne ou la hauteur de ligne.

### **Ancrer l'image à une seule cellule**

L'ancrage de l'image est défini par quatre propriétés d'index basées sur zéro :

- `Picture.upper_left_row` — l'index de ligne du bord supérieur de l'image.
- `Picture.upper_left_column` — l'index de colonne du bord gauche de l'image.
- `Picture.lower_right_row` — l'index de ligne du bord inférieur de l'image. Pour que le bord inférieur de l'image se trouve au bas de la ligne `r`, définissez cette valeur sur `r + 1`.
- `Picture.lower_right_column` — l'index de colonne du bord droit de l'image. Pour que le bord droit de l'image se trouve à droite de la colonne `c`, définissez cette valeur sur `c + 1`.

Par exemple, pour ajuster l'image exactement dans la cellule **C6** (index de ligne `5`, index de colonne `2`), définissez `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6`, et `lower_right_column = 3`.

{{% alert color="primary" %}}

Les index de ligne et de colonne dans Aspose.Cells sont **basés sur zéro**. La cellule C6 a l'index de ligne 5 et l'index de colonne 2. Les erreurs d'une unité sur l'ancrage inférieur droit sont la source la plus fréquente d'images qui semblent dépasser dans une cellule adjacente.

{{% /alert %}}

### **Contrôler le comportement de placement**

`Picture.placement` est une énumération de type `PlacementType` qui contrôle le comportement de l'image lorsque l'utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image sur une seule cellule est `PlacementType.MOVE_AND_SIZE`, qui provoque le déplacement et le redimensionnement de l'image conjointement avec sa cellule sous-jacente, préservant ainsi l'ajustement exact.

### **Instructions étape par étape**

1. Créez un nouveau `Workbook` (ou ouvrez un fichier existant).
2. Accédez à la `Worksheet` cible via `workbook.worksheets[0]`.
3. Ouvrez le fichier image depuis le disque dans un flux de fichier (ou un objet `BytesIO`) à l'aide d'un bloc `with` afin que le flux soit correctement libéré.
4. Appelez `worksheet.pictures.add(5, 2, stream)` pour ajouter une image ancrée à la cellule C6. Capturez la référence `Picture` renvoyée.
5. Définissez les quatre coordonnées d'ancrage de sorte que l'image ne couvre que la cellule C6 : `upper_left_row = 5`, `upper_left_column = 2`, `lower_right_row = 6`, `lower_right_column = 3`.
6. Définissez `picture.placement = PlacementType.MOVE_AND_SIZE` pour maintenir l'image alignée avec C6 lorsque la colonne ou la ligne est redimensionnée.
7. Ajoutez éventuellement du texte d'exemple dans les cellules environnantes pour démontrer que seule la cellule C6 contient l'image.
8. Enregistrez le classeur sur le disque sous forme de fichier `.xlsx`.

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

Aspose.Cells expose également un mécanisme plus simple pour les images liées à une cellule : la propriété `Cell.embedded_image`. Assigner des octets d'image à cette propriété attache l'image à la cellule elle-même, comme s'il s'agissait d'un contenu en ligne.

### **Comment fonctionnent les images intégrées**

- L'image est stockée dans le contenu de la cellule plutôt que comme une forme sur le calque de dessin.
- L'image se met automatiquement à l'échelle pour s'adapter aux limites rendues de la cellule. Aucune coordonnée d'ancrage ni paramètre de placement n'est requis.
- La cellule reste une véritable cellule avec une véritable adresse qui peut être référencée par des formules, triée dans le cadre d'une ligne, ou utilisée dans d'autres opérations au niveau de la cellule.

Cela fait de `Cell.embedded_image` l'option la plus concise lorsque votre objectif est simplement « une image qui vit dans cette cellule ».

### **Instructions étape par étape**

1. Créez un nouveau `Workbook` (ou ouvrez un fichier existant).
2. Accédez à la `Worksheet` cible via `workbook.worksheets[0]`.
3. Lisez le fichier image depuis le disque dans un objet `bytes` (par exemple, en ouvrant le fichier en mode binaire et en appelant `.read()`).
4. Obtenez une référence à la cellule cible — soit via `worksheet.cells["C6"]`, soit via `worksheet.cells[5, 2]`.
5. Assignez l'objet `bytes` à la propriété `embedded_image` de la cellule.
6. Ajustez éventuellement la hauteur de ligne et la largeur de colonne de la ligne et de la colonne cibles pour donner à l'image intégrée une apparence plus proéminente.
7. Enregistrez le classeur sur le disque sous forme de fichier `.xlsx`.

Le code suivant illustre l'approche complète.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Obtenir la cellule cible C6
cell = worksheet.cells["C6"]

# Lire le fichier image dans un tableau d'octets
with open("logo.png", "rb") as f:
    imageData = f.read()

# Incorporer l'image directement dans la cellule
cell.embedded_image = imageData

# Ajuster éventuellement la hauteur de ligne et la largeur de colonne pour que l'image incorporée soit plus visible
worksheet.cells.set_column_width(2, 30)   # Colonne C (index 2)
worksheet.cells.set_row_height(5, 100)     # Ligne 6 (index 5)

# Enregistrer le classeur résultant en tant que fichier .xlsx
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **Choisir la bonne approche**

Les deux approches produisent une image qui s'adapte à une seule cellule, mais elles diffèrent par la manière dont l'image est stockée et dont elle se comporte :

- **Utilisez une image flottante (Approche 1) lorsque :**
  - Vous avez besoin d'un contrôle plus fin sur le placement, la superposition ou l'alignement avec d'autres objets de dessin.
  - Vous souhaitez que l'image se comporte comme une forme pouvant être sélectionnée, réordonnée ou regroupée avec d'autres formes.
  - Vous exigez une compatibilité ascendante avec du code qui fonctionne déjà avec les collections `pictures`.
  - Vous devez calculer dynamiquement les coordonnées d'ancrage en fonction de la disposition de la feuille de calcul.

- **Utilisez une image intégrée (Approche 2) lorsque :**
  - Vous souhaitez l'insertion la plus simple possible d'une image dans une cellule.
  - L'image doit se déplacer avec la cellule comme tout autre contenu de cellule.
  - Vous n'avez pas besoin de manipuler l'image comme une forme.

{{% alert color="primary" %}}

Les deux approches peuvent coexister dans le même classeur. Vous pouvez placer des images flottantes sur un certain ensemble de cellules et intégrer des images directement dans d'autres cellules, car les deux mécanismes utilisent des couches de stockage différentes dans le fichier.

{{% /alert %}}

## **Articles connexes**

- [Comment insérer une image dans une cellule](/cells/fr/python-net/how-to-place-image-to-cell/)
- [Ajouter des hyperliens d'image](/cells/fr/python-net/add-image-hyperlinks/)
- [Charger une image web à partir d'une URL dans une feuille de calcul Excel](/cells/fr/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipuler la position, la taille et le graphique du concepteur](/cells/fr/python-net/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="python" >}}