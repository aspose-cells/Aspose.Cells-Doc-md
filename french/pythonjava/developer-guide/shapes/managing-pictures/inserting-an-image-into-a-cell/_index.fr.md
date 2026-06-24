---
title: Insertion d'une image dans une cellule
description: Aspose.Cells for Python via Java est une bibliothèque permettant de travailler avec des fichiers de tableur. Cet article explique comment ajuster une image exactement à la taille d'une seule cellule en utilisant deux approches différentes, placer une image flottante sur la cellule, ou intégrer l'image directement dans la cellule.
keywords: Aspose.Cells, Python via Java library, tableur, insérer image, intégrer image, image dans cellule, ajuster image à cellule, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/python-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells propose deux méthodes distinctes pour associer une image à une seule cellule. Une image flottante est une forme sur la couche de dessin de la feuille de calcul qui recouvre visuellement une plage de cellules, tandis qu'une image intégrée est stockée à l'intérieur de la cellule elle-même et se redimensionne automatiquement à la zone d'affichage de la cellule. Choisissez l'approche qui correspond le mieux à vos besoins de mise en page.

{{% /alert %}}

## **Introduction**

Ajuster une image exactement à une seule cellule est une exigence courante lors de la conception de tableurs servant de rapports visuels, de catalogues de produits, d'annuaires d'employés, de tableaux de bord ou de listes d'inventaire. Plutôt que d'étirer une image sur plusieurs cellules ou de la placer librement sur une feuille de calcul, vous pouvez souhaiter une image nette, liée à une cellule, qui reste alignée avec la cellule qui la contient.

Aspose.Cells prend en charge ce scénario de deux manières complémentaires :

- **Approche 1 — Placer une image flottante sur une cellule.** Ajoutez une `Picture` à la feuille de calcul, définissez son `setPlacement` à `MOVE_AND_SIZE`, et ajustez ses cellules d'ancrage (`setUpperLeftRow`, `setUpperLeftColumn`, `setLowerRightRow`, `setLowerRightColumn`) de sorte que l'image couvre exactement une cellule.
- **Approche 2 — Intégrer une image directement dans une cellule.** Assignez les octets de l'image à la propriété `setEmbeddedImage` de la cellule. L'image se redimensionne automatiquement pour s'adapter à la zone d'affichage de la cellule et se déplace avec la cellule.

Le reste de cet article détaille les deux approches, explique les API pertinentes et montre comment les utiliser dans le code.

## **Approche 1 : Placer une image sur une cellule**

Une image flottante est un objet `Picture` qui réside sur la couche de dessin de la feuille de calcul. Bien qu'elle ne fasse partie d'aucune cellule individuelle, elle est ancrée à une plage de cellules. Les cellules d'ancrage de l'image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image fraîchement ajoutée s'étend sur plusieurs cellules.

Pour qu'une image flottante couvre **exactement une cellule**, vous devez :

1. Ajouter l'image à l'aide de `Worksheet.getPictures().add(int row, int column, InputStream stream)`, ce qui ancre la nouvelle image à la cellule donnée.
2. Définir les quatre propriétés d'ancrage de sorte que le rectangle englobant de l'image coïncide avec la cellule cible.
3. Définir `Picture.setPlacement` à `PlacementType.MOVE_AND_SIZE` afin que l'image se déplace et se redimensionne avec la cellule sous-jacente lorsque l'utilisateur modifie la largeur de colonne ou la hauteur de ligne.

### **Ancrage de l'image à une seule cellule**

L'ancrage de l'image est défini par quatre propriétés d'index à base zéro :

- `setUpperLeftRow` — l'index de ligne du bord supérieur de l'image.
- `setUpperLeftColumn` — l'index de colonne du bord gauche de l'image.
- `setLowerRightRow` — l'index de ligne du bord inférieur de l'image. Pour que le bord inférieur de l'image se trouve au bas de la ligne `r`, définissez cette valeur à `r + 1`.
- `setLowerRightColumn` — l'index de colonne du bord droit de l'image. Pour que le bord droit de l'image se trouve à droite de la colonne `c`, définissez cette valeur à `c + 1`.

Par exemple, pour ajuster l'image exactement dans la cellule **C6** (index de ligne `5`, index de colonne `2`), définissez `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, et `setLowerRightColumn(3)`.

{{% alert color="primary" %}}

Les indices de ligne et de colonne dans Aspose.Cells sont **à base zéro**. La cellule C6 a l'index de ligne 5 et l'index de colonne 2. Les erreurs d'une unité sur l'ancrage inférieur droit sont la source la plus fréquente d'images qui semblent dépasser dans une cellule adjacente.

{{% /alert %}}

### **Contrôle du comportement de positionnement**

`getPlacement` est une énumération de type `PlacementType` qui contrôle le comportement de l'image lorsque l'utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image sur une seule cellule est `PlacementType.MOVE_AND_SIZE`, qui fait en sorte que l'image se déplace et se redimensionne avec sa cellule sous-jacente, préservant ainsi l'ajustement exact.

### **Instructions étape par étape**

1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez à la `Worksheet` cible via `workbook.getWorksheets().get(0)`.
3. Ouvrez le fichier image du disque dans un `InputStream` (généralement un `FileInputStream`) afin que le flux soit correctement fermé.
4. Appelez `worksheet.getPictures().add(5, 2, stream)` pour ajouter une image ancrée à la cellule C6. Conservez la référence `Picture` retournée.
5. Définissez les quatre coordonnées d'ancrage de sorte que l'image ne couvre que la cellule C6 : `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Définissez `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` pour maintenir l'image alignée avec C6 lorsque la colonne ou la ligne est redimensionnée.
7. Ajoutez éventuellement du texte d'exemple dans les cellules environnantes pour démontrer que seule la cellule C6 contient l'image.
8. Enregistrez le classeur sur le disque en tant que fichier `.xlsx`.

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

## **Approche 2 : Intégrer une image directement dans une cellule**

Aspose.Cells expose également un mécanisme plus simple pour les images liées à une cellule : la propriété `Cell.setEmbeddedImage`. Assigner des octets d'image à cette propriété attache l'image à la cellule elle-même, comme s'il s'agissait d'un contenu intégré.

### **Fonctionnement des images intégrées**

- L'image est stockée comme partie du contenu de la cellule plutôt que comme forme sur la couche de dessin.
- L'image se redimensionne automatiquement pour s'adapter aux limites rendues de la cellule. Aucune coordonnée d'ancrage ni paramètre de positionnement n'est requis.
- La cellule reste une vraie cellule avec une vraie adresse qui peut être référencée par des formules, triée comme partie d'une ligne, ou utilisée dans d'autres opérations au niveau de la cellule.

Cela fait de `Cell.setEmbeddedImage` l'option la plus concise lorsque votre objectif est simplement « une image qui vit dans cette cellule ».

### **Instructions étape par étape**

1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez à la `Worksheet` cible via `workbook.getWorksheets().get(0)`.
3. Lisez le fichier image du disque dans un tableau `byte[]` (par exemple, en utilisant un appel à `Files.readAllBytes` depuis `java.nio.file.Files`).
4. Obtenez une référence à la cellule cible — soit via `worksheet.getCells().get("C6")`, soit via `worksheet.getCells().get(5, 2)`.
5. Assignez le tableau d'octets à la propriété `setEmbeddedImage` de la cellule.
6. Ajustez éventuellement la hauteur de ligne et la largeur de colonne de la ligne et de la colonne cibles pour donner à l'image intégrée une apparence plus proéminente.
7. Enregistrez le classeur sur le disque en tant que fichier `.xlsx`.

Le code suivant illustre l'approche complète.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Obtenir la cellule cible C6
cell = worksheet.getCells().get("C6")

# Lire le fichier image dans un tableau d'octets
imageData = open("logo.png", "rb").read()

# Intégrer l'image directement dans la cellule
cell.setEmbeddedImage(imageData)

# Optionnellement ajuster la hauteur de ligne et la largeur de colonne pour que l'image intégrée soit plus visible
worksheet.getCells().setColumnWidth(2, 30)   # Colonne C (index 2)
worksheet.getCells().setRowHeight(5, 100)    # Ligne 6 (index 5)

# Enregistrer le classeur résultant en tant que fichier .xlsx
workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()
```

## **Choisir la bonne approche**

Les deux approches produisent une image qui s'insère dans une seule cellule, mais elles diffèrent par la manière dont l'image est stockée et par son comportement :

- **Utilisez une image flottante (Approche 1) lorsque :**
  - Vous avez besoin d'un contrôle plus fin sur le positionnement, la superposition ou l'alignement avec d'autres objets de dessin.
  - Vous souhaitez que l'image se comporte comme une forme pouvant être sélectionnée, réorganisée ou groupée avec d'autres formes.
  - Vous avez besoin d'une compatibilité avec du code existant qui fonctionne déjà avec `PictureCollection`.
  - Vous devez calculer dynamiquement les coordonnées d'ancrage en fonction de la disposition de la feuille de calcul.

- **Utilisez une image intégrée (Approche 2) lorsque :**
  - Vous souhaitez l'insertion la plus simple possible d'une image dans une cellule.
  - L'image doit se déplacer avec la cellule comme tout autre contenu de cellule.
  - Vous n'avez pas besoin de manipuler l'image comme une forme.

{{% alert color="primary" %}}

Les deux approches peuvent coexister dans le même classeur. Vous pouvez placer des images flottantes sur un ensemble de cellules et intégrer des images directement dans d'autres cellules, car les deux mécanismes utilisent des couches de stockage différentes dans le fichier.

{{% /alert %}}



{{< app/cells/assistant language="python" >}}