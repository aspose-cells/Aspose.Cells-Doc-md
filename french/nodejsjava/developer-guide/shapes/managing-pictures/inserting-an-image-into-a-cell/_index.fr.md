---
title: Insertion d'une image dans une cellule
description: Aspose.Cells est une bibliothèque Node.js via Java permettant de travailler avec des fichiers de feuilles de calcul. Cet article explique comment ajuster une image exactement à la taille d'une seule cellule en utilisant deux approches différentes, placer une image flottante sur la cellule, ou incorporer l'image directement dans la cellule.
keywords: Aspose.Cells, bibliothèque Node.js via Java, feuille de calcul, insérer image, incorporer image, image dans cellule, ajuster image à cellule, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/nodejs-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells offre deux façons distinctes d'associer une image à une seule cellule. Une image flottante est une forme sur la couche de dessin de la feuille de calcul qui recouvre visuellement une plage de cellules, tandis qu'une image incorporée est stockée à l'intérieur de la cellule elle-même et se met à l'échelle automatiquement selon la zone d'affichage de la cellule. Choisissez l'approche qui correspond le mieux à vos exigences de mise en page.

{{% /alert %}}

## **Introduction**

Ajuster une image exactement à une seule cellule est une exigence courante lors de la conception de feuilles de calcul servant de rapports visuels, catalogues de produits, annuaires d'employés, tableaux de bord ou listes d'inventaire. Plutôt que d'étirer une image sur plusieurs cellules ou de la placer librement sur une feuille de calcul, vous pouvez souhaiter une image nette, liée à la cellule, qui reste alignée sur la cellule qui la contient.

Aspose.Cells prend en charge ce scénario de deux manières complémentaires :

- **Approche 1 — Placer une image flottante sur une cellule.** Ajoutez une `Picture` à la feuille de calcul, définissez son `Placement` sur `MoveAndSize`, et ajustez ses cellules d'ancrage (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) afin que l'image couvre exactement une cellule.
- **Approche 2 — Incorporer une image directement dans une cellule.** Affectez les octets de l'image à la propriété `EmbeddedImage` de la cellule. L'image se met à l'échelle automatiquement pour s'adapter à la zone d'affichage de la cellule et se déplace avec la cellule.

La suite de cet article parcourt les deux approches, explique les API concernées, et montre comment les utiliser dans le code.

## **Approche 1 : Placer une image sur une cellule**

Une image flottante est un objet `Picture` qui vit sur la couche de dessin de la feuille de calcul. Bien qu'elle ne fasse partie d'aucune cellule individuelle, elle est ancrée à une plage de cellules. Les cellules d'ancrage de l'image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image fraîchement ajoutée s'étend sur plusieurs cellules.

Pour qu'une image flottante couvre **exactement une cellule**, vous devez :

1. Ajouter l'image en utilisant `worksheet.getPictures().add(int row, int column, InputStream stream)`, ce qui ancre la nouvelle image à la cellule donnée.
2. Définir les quatre propriétés d'ancrage afin que le rectangle englobant de l'image coïncide avec la cellule cible.
3. Définir `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` afin que l'image se déplace et se redimensionne avec la cellule sous-jacente lorsque l'utilisateur modifie la largeur de colonne ou la hauteur de ligne.

### **Ancrer l'image à une seule cellule**

L'ancrage de l'image est défini par quatre propriétés d'index à base zéro :

- `picture.setUpperLeftRow(int)` — l'index de ligne du bord supérieur de l'image.
- `picture.setUpperLeftColumn(int)` — l'index de colonne du bord gauche de l'image.
- `picture.setLowerRightRow(int)` — l'index de ligne du bord inférieur de l'image. Pour que le bord inférieur de l'image se trouve au bas de la ligne `r`, définissez cette valeur sur `r + 1`.
- `picture.setLowerRightColumn(int)` — l'index de colonne du bord droit de l'image. Pour que le bord droit de l'image se trouve à droite de la colonne `c`, définissez cette valeur sur `c + 1`.

Par exemple, pour ajuster l'image exactement dans la cellule **C6** (index de ligne `5`, index de colonne `2`), définissez `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6` et `LowerRightColumn = 3`.

{{% alert color="primary" %}}

Les indices de ligne et de colonne dans Aspose.Cells sont **à base zéro**. La cellule C6 a l'index de ligne 5 et l'index de colonne 2. Les erreurs d'une unité sur l'ancrage inférieur droit sont la source la plus courante d'images qui semblent déborder dans une cellule adjacente.

{{% /alert %}}

### **Contrôler le comportement de placement**

`Picture.Placement` est une énumération de type `PlacementType` qui contrôle le comportement de l'image lorsque l'utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image sur une seule cellule est `PlacementType.MoveAndSize`, qui fait que l'image se déplace et se redimensionne conjointement avec sa cellule sous-jacente, préservant ainsi l'ajustement exact.

### **Instructions étape par étape**

1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez au `Worksheet` cible via `workbook.getWorksheets().get(0)`.
3. Ouvrez le fichier image depuis le disque dans un `InputStream` (par exemple, en utilisant `FileInputStream`) afin que le flux soit correctement fermé.
4. Appelez `worksheet.getPictures().add(5, 2, stream)` pour ajouter une image ancrée à la cellule C6. Capturez la référence `Picture` renvoyée.
5. Définissez les quatre coordonnées d'ancrage afin que l'image couvre uniquement la cellule C6 : `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Définissez `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` pour maintenir l'image alignée sur C6 lorsque la colonne ou la ligne est redimensionnée.
7. Ajoutez éventuellement du texte d'exemple dans les cellules environnantes pour démontrer que seule la cellule C6 contient l'image.
8. Enregistrez le classeur sur le disque en tant que fichier `.xlsx`.

Le code suivant illustre l'approche complète.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

var picIndex = worksheet.getPictures().add(5, 2, "logo.png");
var picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);

workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Approche 2 : Incorporer une image directement dans une cellule**

Aspose.Cells expose également un mécanisme plus simple pour les images liées aux cellules : la propriété `Cell.EmbeddedImage`. Affecter des octets d'image à cette propriété attache l'image à la cellule elle-même, comme s'il s'agissait de contenu en ligne.

### **Fonctionnement des images incorporées**

- L'image est stockée dans le contenu de la cellule plutôt que sous forme de forme sur la couche de dessin.
- L'image se met à l'échelle automatiquement pour s'adapter aux limites rendues de la cellule. Aucune coordonnée d'ancrage ni paramètre de placement n'est requis.
- La cellule reste une véritable cellule avec une véritable adresse qui peut être référencée par des formules, triée dans le cadre d'une ligne, ou utilisée dans d'autres opérations au niveau de la cellule.

Cela fait de `Cell.EmbeddedImage` l'option la plus concise lorsque votre objectif est simplement « une image qui vit à l'intérieur de cette cellule ».

### **Instructions étape par étape**

1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez au `Worksheet` cible via `workbook.getWorksheets().get(0)`.
3. Lisez le fichier image depuis le disque dans un tableau d'octets (par exemple, en utilisant `Files.readAllBytes` de `java.nio.file.Files`).
4. Obtenez une référence à la cellule cible — soit via `worksheet.getCells().get("C6")`, soit via `worksheet.getCells().get(5, 2)`.
5. Affectez le tableau d'octets à la propriété `EmbeddedImage` de la cellule via `cell.setEmbeddedImage(bytes)`.
6. Ajustez éventuellement la hauteur de ligne et la largeur de colonne de la ligne et de la colonne cibles pour donner à l'image incorporée une apparence plus proéminente.
7. Enregistrez le classeur sur le disque en tant que fichier `.xlsx`.

Le code suivant illustre l'approche complète.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Obtenir la cellule cible C6
var cell = worksheet.getCells().get("C6");

// Lire le fichier image dans un tableau d'octets
var imageData = fs.readFileSync("logo.png");

// Intégrer l'image directement dans la cellule
cell.setEmbeddedImage(imageData);

// Optionnellement ajuster la hauteur de ligne et la largeur de colonne pour que l'image intégrée soit plus visible
worksheet.getCells().setColumnWidth(2, 30);   // Colonne C (index 2)
worksheet.getCells().setRowHeight(5, 100);     // Ligne 6 (index 5)

// Enregistrer le classeur résultant sous forme de fichier .xlsx
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Choisir la bonne approche**

Les deux approches produisent une image qui s'inscrit dans une seule cellule, mais elles diffèrent dans la manière dont l'image est stockée et dont elle se comporte :

- **Utilisez une image flottante (Approche 1) lorsque :**
  - Vous avez besoin d'un contrôle plus fin sur le placement, la superposition ou l'alignement avec d'autres objets de dessin.
  - Vous souhaitez que l'image se comporte comme une forme pouvant être sélectionnée, réordonnée ou regroupée avec d'autres formes.
  - Vous avez besoin d'une compatibilité héritée avec du code qui fonctionne déjà avec `PictureCollection`.
  - Vous devez calculer dynamiquement les coordonnées d'ancrage en fonction de la disposition de la feuille de calcul.

- **Utilisez une image incorporée (Approche 2) lorsque :**
  - Vous souhaitez l'insertion la plus simple possible d'une image dans une cellule.
  - L'image doit se déplacer avec la cellule comme tout autre contenu de cellule.
  - Vous n'avez pas besoin de manipuler l'image en tant que forme.

{{% alert color="primary" %}}

Les deux approches peuvent coexister dans le même classeur. Vous pouvez placer des images flottantes sur un ensemble de cellules et incorporer des images directement dans d'autres cellules, car les deux mécanismes utilisent des couches de stockage différentes dans le fichier.

{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}