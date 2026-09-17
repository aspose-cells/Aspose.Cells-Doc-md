---
title: Insertion d'une image dans une cellule
linktitle: Insertion d'une image dans une cellule
description: Aspose.Cells est une bibliothèque Node.js via C++ pour travailler avec des fichiers de tableurs. Cet article explique comment ajuster une image exactement à une seule cellule, soit en plaçant une image flottante sur la cellule, soit en incorporant l'image directement dans la cellule.
keywords: Aspose.Cells, bibliothèque Node.js via C++, tableur, insérer une image, incorporer une image, image dans une cellule, ajuster l'image à la cellule, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/nodejs-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells propose deux façons distinctes d'associer une image à une seule cellule. Une image flottante est une forme sur la couche de dessin de la feuille de calcul qui se superpose visuellement à une plage de cellules, tandis qu'une image incorporée est stockée à l'intérieur de la cellule elle-même et s'adapte automatiquement à la zone d'affichage de la cellule. Choisissez l'approche qui correspond le mieux à vos exigences de mise en page.
{{% /alert %}}

## **Introduction**
Ajuster une image exactement à une seule cellule est une exigence courante lors de la conception de feuilles de calcul qui servent de rapports visuels, de catalogues de produits, d'annuaires d'employés, de tableaux de bord ou de listes d'inventaire. Plutôt que d'étirer une image sur plusieurs cellules ou de la placer librement sur une feuille de calcul, vous pouvez souhaiter une image nette, liée à la cellule, qui reste alignée sur la cellule qui la contient.
Aspose.Cells prend en charge ce scénario de deux manières complémentaires :
- **Approche 1 — Placer une image flottante sur une cellule.** Ajoutez un `Picture` à la feuille de calcul, définissez son `placement` sur `MoveAndSize`, et ajustez ses cellules d'ancrage (`upperLeftRow`, `upperLeftColumn`, `lowerRightRow`, `lowerRightColumn`) pour que l'image couvre exactement une cellule.
- **Approche 2 — Incorporer une image directement dans une cellule.** Assignez les octets de l'image à la propriété `embeddedImage` de la cellule. L'image s'adapte automatiquement à la zone d'affichage de la cellule et se déplace avec elle.
Le reste de cet article passe en revue les deux approches, explique les API pertinentes et montre comment les utiliser dans le code.

## **Approach 1: Place a Picture Over a Cell**
Une image flottante est un objet `Picture` qui réside sur la couche de dessin de la feuille de calcul. Bien qu'elle ne fasse partie d'aucune cellule individuelle, elle est ancrée à une plage de cellules. Les cellules d'ancrage de l'image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image fraîchement ajoutée s'étend sur plusieurs cellules.
Pour faire en sorte qu'une image flottante couvre **exactement une cellule**, vous devez :
1. Ajouter l'image à l'aide de `worksheet.pictures.add(row, column, stream)`, qui ancre la nouvelle image à la cellule donnée.
2. Définir les quatre propriétés d'ancrage pour que le rectangle englobant de l'image coïncide avec la cellule cible.
3. Définir `picture.placement` sur `PlacementType.MoveAndSize` pour que l'image se déplace et se redimensionne avec la cellule sous-jacente lorsque l'utilisateur modifie la largeur de colonne ou la hauteur de ligne.

### **Anchoring the Picture to a Single Cell**
L'ancrage de l'image est défini par quatre propriétés d'index basées sur zéro :
- `picture.upperLeftRow` — l'index de ligne du bord supérieur de l'image.
- `picture.upperLeftColumn` — l'index de colonne du bord gauche de l'image.
- `picture.lowerRightRow` — l'index de ligne du bord inférieur de l'image. Pour que le bord inférieur de l'image se situe au bas de la ligne `r`, définissez cette valeur sur `r + 1`.
- `picture.lowerRightColumn` — l'index de colonne du bord droit de l'image. Pour que le bord droit de l'image se situe à droite de la colonne `c`, définissez cette valeur sur `c + 1`.

{{% alert color="primary" %}}
Les indices de ligne et de colonne dans Aspose.Cells sont **basés sur zéro**. La cellule C6 a un index de ligne 5 et un index de colonne 2. Les erreurs d'une unité sur l'ancrage inférieur droit sont la source la plus fréquente d'images qui semblent empiéter sur une cellule adjacente.

### **Controlling Placement Behavior**
`picture.placement` est une énumération de type `PlacementType` qui contrôle le comportement de l'image lorsque l'utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image dans une seule cellule est `PlacementType.MoveAndSize`, qui fait en sorte que l'image se déplace et se redimensionne avec sa cellule sous-jacente, préservant ainsi l'ajustement exact.

### **Step-by-Step Instructions**
1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez à la `Worksheet` cible via `workbook.worksheets[0]`.
3. Ouvrez le fichier image du disque dans un flux, en veillant à ce que le flux soit correctement fermé après utilisation.
4. Appelez `worksheet.pictures.add(5, 2, stream)` pour ajouter une image ancrée à la cellule C6. Capturez la référence `Picture` renvoyée.
5. Définissez les quatre coordonnées d'ancrage pour que l'image couvre uniquement la cellule C6 : `upperLeftRow = 5`, `upperLeftColumn = 2`, `lowerRightRow = 6`, `lowerRightColumn = 3`.
6. Définissez `picture.placement = PlacementType.MoveAndSize` pour maintenir l'image alignée avec C6 lors du redimensionnement de la colonne ou de la ligne.
7. Ajoutez éventuellement du texte d'exemple dans les cellules environnantes pour démontrer que seule la cellule C6 contient l'image.
8. Enregistrez le classeur sur le disque sous forme de fichier `.xlsx`.
Le code suivant illustre l'approche complète.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const fs_stream = fs.createReadStream("logo.png");
const picIndex = worksheet.getPictures().add(5, 2, fs_stream);
const picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Approach 2: Embed an Image Directly in a Cell**
Aspose.Cells expose également un mécanisme plus simple pour les images liées à une cellule : la propriété `cell.embeddedImage`. L'assignation d'octets d'image à cette propriété attache l'image à la cellule elle-même, comme s'il s'agissait d'un contenu en ligne.

### **How Embedded Images Work**
- L'image est stockée dans le contenu de la cellule plutôt que comme une forme sur la couche de dessin.
- L'image s'adapte automatiquement aux limites rendues de la cellule. Aucune coordonnée d'ancrage ni paramètre de placement n'est requis.
- La cellule reste une véritable cellule avec une adresse réelle qui peut être référencée par des formules, triée dans le cadre d'une ligne, ou utilisée dans d'autres opérations au niveau des cellules.
Cela fait de `cell.embeddedImage` l'option la plus concise lorsque votre objectif est simplement « une image qui vit dans cette cellule ».

### **Step-by-Step Instructions**
1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez à la `Worksheet` cible via `workbook.worksheets[0]`.
3. Lisez le fichier image du disque dans un Buffer ou un tableau d'octets à l'aide des API du système de fichiers Node.js (par exemple, `fs.readFileSync`).
4. Obtenez une référence à la cellule cible — soit via `worksheet.cells["C6"]`, soit via `worksheet.cells[5, 2]`.
5. Assignez le tableau d'octets à la propriété `embeddedImage` de la cellule.
6. Ajustez éventuellement la hauteur de ligne et la largeur de colonne de la ligne et de la colonne cibles pour donner à l'image incorporée une apparence plus proéminente.
7. Enregistrez le classeur sur le disque sous forme de fichier `.xlsx`.
Le code suivant illustre l'approche complète.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Obtenir la cellule cible C6
var cell = worksheet.getCells().get("C6");
// Lire le fichier image dans un tableau d'octets
var imageData = fs.readFileSync("logo.png");
// Incorporer l'image directement dans la cellule
cell.setEmbeddedImage(imageData);
// Optionnellement ajuster la hauteur de ligne et la largeur de colonne pour que l'image incorporée soit plus visible
worksheet.getCells().setColumnWidth(2, 30);   // Colonne C (index 2)
worksheet.getCells().setRowHeight(5, 100);     // Ligne 6 (index 5)
// Enregistrer le classeur résultant en tant que fichier .xlsx
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Choosing the Right Approach**
Les deux approches produisent une image qui s'inscrit dans une seule cellule, mais elles diffèrent par la façon dont l'image est stockée et dont elle se comporte :
- **Utilisez une image flottante (Approche 1) lorsque :**
  - Vous avez besoin d'un contrôle plus fin sur le placement, la superposition ou l'alignement avec d'autres objets de dessin.
  - Vous souhaitez que l'image se comporte comme une forme qui peut être sélectionnée, réorganisée ou regroupée avec d'autres formes.
  - Vous exigez une compatibilité héritée avec du code qui fonctionne déjà avec la collection d'images.
  - Vous devez calculer dynamiquement les coordonnées d'ancrage en fonction de la disposition de la feuille de calcul.
- **Utilisez une image incorporée (Approche 2) lorsque :**
  - Vous souhaitez l'insertion la plus simple possible d'une image dans une cellule.
  - L'image doit se déplacer avec la cellule comme tout autre contenu de cellule.
{{% /alert %}}

## Related Articles
- [Excel Camera in Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/excel-camera/)
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/fr/nodejs-cpp/change-page-field-layout/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="javascript" >}}