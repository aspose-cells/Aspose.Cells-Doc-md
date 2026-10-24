---
title: Insertion d'une image dans une cellule
linktitle: Insertion d'une image dans une cellule
description: Aspose.Cells est une bibliothèque Node.js via C++ spécialisée dans le traitement des fichiers tableurs. Cet article explique comment ajuster précisément une image à une seule cellule, soit en plaçant une image flottante au-dessus de la cellule, soit en intégrant l'image directement dans la cellule.
keywords: Aspose.Cells, bibliothèque Node.js via C++, tableur, insérer une image, intégrer une image, image dans une cellule, ajuster une image à une cellule, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/nodejs-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells propose deux méthodes distinctes pour associer une image à une seule cellule. Une image flottante est une forme située sur la couche de dessin de la feuille de calcul qui recouvre visuellement une plage de cellules, tandis qu'une image intégrée est stockée à l'intérieur de la cellule elle-même et s'ajuste automatiquement à la zone d'affichage de la cellule. Choisissez l'approche qui correspond le mieux à vos besoins de mise en page.
{{% /alert %}}

## **Introduction**
Ajuster précisément une image à une seule cellule est une exigence courante lors de la conception de tableurs servant de rapports visuels, catalogues de produits, annuaires du personnel, tableaux de bord ou listes d'inventaire. Plutôt que d'étirer une image sur plusieurs cellules ou de la placer de manière approximative sur une feuille de calcul, vous pouvez souhaiter une image nette et liée à la cellule, qui reste alignée avec la cellule qui la contient.
Aspose.Cells prend en charge ce scénario de deux manières complémentaires :
- **Approche 1 — Placer une image flottante au-dessus d'une cellule.** Ajoutez une `Picture` à la feuille de calcul, définissez son `placement` à `MoveAndSize`, et ajustez ses cellules d'ancrage (`upperLeftRow`, `upperLeftColumn`, `lowerRightRow`, `lowerRightColumn`) de sorte que l'image couvre exactement une cellule.
- **Approche 2 — Intégrer une image directement dans une cellule.** Affectez les octets de l'image à la propriété `embeddedImage` de la cellule. L'image s'ajuste automatiquement à la zone d'affichage de la cellule et se déplace avec elle.
La suite de cet article détaille ces deux approches, explique les API concernées et montre comment les utiliser dans le code.

## **Approach 1: Place a Picture Over a Cell**
Une image flottante est un objet `Picture` qui réside sur la couche de dessin de la feuille de calcul. Bien qu'elle ne fasse partie d'aucune cellule à proprement parler, elle est ancrée à une plage de cellules. Les cellules d'ancrage de l'image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image nouvellement ajoutée s'étend sur plusieurs cellules.
Pour faire en sorte qu'une image flottante couvre **exactement une cellule**, vous devez :
1. Ajouter l'image à l'aide de `worksheet.pictures.add(row, column, stream)`, ce qui ancre la nouvelle image à la cellule indiquée.
2. Définir les quatre propriétés d'ancrage de sorte que le rectangle englobant de l'image coïncide avec la cellule cible.
3. Définir `picture.placement` à `PlacementType.MoveAndSize` afin que l'image se déplace et se redimensionne avec la cellule sous-jacente lorsque l'utilisateur modifie la largeur de colonne ou la hauteur de ligne.

### **Anchoring the Picture to a Single Cell**
L'ancrage de l'image est défini par quatre propriétés d'index de base zéro :
- `picture.upperLeftRow` — l'index de ligne du bord supérieur de l'image.
- `picture.upperLeftColumn` — l'index de colonne du bord gauche de l'image.
- `picture.lowerRightRow` — l'index de ligne du bord inférieur de l'image. Pour que le bord inférieur de l'image se situe en bas de la ligne `r`, définissez cette valeur à `r + 1`.
- `picture.lowerRightColumn` — l'index de colonne du bord droit de l'image. Pour que le bord droit de l'image se situe à droite de la colonne `c`, définissez cette valeur à `c + 1`.

{{% alert color="primary" %}}
Les index de ligne et de colonne dans Aspose.Cells sont **de base zéro**. La cellule C6 a pour index de ligne 5 et pour index de colonne 2. Les erreurs de décalage d'une unité sur l'ancrage inférieur droit sont la source la plus fréquente d'images qui semblent empiéter sur une cellule adjacente.
{{% /alert %}}

### **Controlling Placement Behavior**
`picture.placement` est une énumération de type `PlacementType` qui contrôle le comportement de l'image lorsque l'utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image sur une seule cellule est `PlacementType.MoveAndSize`, qui fait en sorte que l'image se déplace et se redimensionne avec la cellule sous-jacente, en préservant l'ajustement exact.

### **Step-by-Step Instructions**
1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez à la `Worksheet` cible via `workbook.worksheets[0]`.
3. Ouvrez le fichier image depuis le disque dans un flux, en veillant à ce que le flux soit correctement fermé après utilisation.
4. Appelez `worksheet.pictures.add(5, 2, stream)` pour ajouter une image ancrée à la cellule C6. Récupérez la référence `Picture` renvoyée.
5. Définissez les quatre coordonnées d'ancrage de sorte que l'image ne couvre que la cellule C6 : `upperLeftRow = 5`, `upperLeftColumn = 2`, `lowerRightRow = 6`, `lowerRightColumn = 3`.
6. Définissez `picture.placement = PlacementType.MoveAndSize` pour maintenir l'image alignée avec C6 lors du redimensionnement de la colonne ou de la ligne.
7. Vous pouvez, si vous le souhaitez, ajouter du texte d'exemple dans les cellules environnantes pour démontrer que seule la cellule C6 contient l'image.
8. Enregistrez le classeur sur le disque en tant que fichier `.xlsx`.
Le code suivant illustre l'approche complète.

```javascript
const AsposeCells = require("aspose.cells.node");
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
Aspose.Cells expose également un mécanisme plus simple pour les images liées à une cellule : la propriété `cell.embeddedImage`. Affecter des octets d'image à cette propriété attache l'image à la cellule elle-même, comme s'il s'agissait d'un contenu incorporé.

### **How Embedded Images Work**
- L'image est stockée comme faisant partie du contenu de la cellule plutôt que comme une forme sur la couche de dessin.
- L'image s'ajuste automatiquement aux limites rendues de la cellule. Aucune coordonnée d'ancrage ni paramètre de placement n'est requis.
- La cellule reste une véritable cellule, avec une véritable adresse, qui peut être référencée par des formules, triée au sein d'une ligne, ou utilisée dans d'autres opérations au niveau de la cellule.
Cela fait de `cell.embeddedImage` l'option la plus concise lorsque votre objectif est simplement « une image qui réside dans cette cellule ».

### **Step-by-Step Instructions**
1. Créez un nouveau `Workbook` (ou ouvrez-en un existant).
2. Accédez à la `Worksheet` cible via `workbook.worksheets[0]`.
3. Lisez le fichier image depuis le disque dans un Buffer ou un tableau d'octets à l'aide des API du système de fichiers Node.js (par exemple, `fs.readFileSync`).
4. Obtenez une référence à la cellule cible — soit via `worksheet.cells["C6"]`, soit via `worksheet.cells[5, 2]`.
5. Affectez le tableau d'octets à la propriété `embeddedImage` de la cellule.
6. Vous pouvez, si vous le souhaitez, ajuster la hauteur de ligne et la largeur de colonne de la ligne et de la colonne cibles pour donner à l'image intégrée une apparence plus visible.
7. Enregistrez le classeur sur le disque en tant que fichier `.xlsx`.
Le code suivant illustre l'approche complète.

```javascript
const AsposeCells = require("aspose.cells.node");
const fs = require("fs");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Get the target cell C6
var cell = worksheet.getCells().get("C6");
// Read the image file into a byte array
var imageData = fs.readFileSync("logo.png");
// Embed the image directly into the cell
cell.setEmbeddedImage(imageData);
// Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30);   // Column C (index 2)
worksheet.getCells().setRowHeight(5, 100);     // Row 6 (index 5)
// Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Choosing the Right Approach**
Les deux approches produisent une image qui s'inscrit dans une seule cellule, mais elles diffèrent dans la façon dont l'image est stockée et dont elle se comporte :
- **Utilisez une image flottante (Approche 1) lorsque :**
  - Vous avez besoin d'un contrôle plus fin sur le placement, la superposition ou l'alignement avec d'autres objets de dessin.
  - Vous souhaitez que l'image se comporte comme une forme pouvant être sélectionnée, réorganisée ou groupée avec d'autres formes.
  - Vous avez besoin d'une compatibilité avec du code existant qui fonctionne déjà avec la collection de pictures.
  - Vous devez calculer dynamiquement les coordonnées d'ancrage en fonction de la disposition de la feuille de calcul.
- **Utilisez une image intégrée (Approche 2) lorsque :**
  - Vous souhaitez l'insertion la plus simple possible d'une image dans une cellule.
  - L'image doit se déplacer avec la cellule comme tout autre contenu de cellule.

## Related Articles
- [Excel Camera dans Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/excel-camera/)
- [Ajouter des champs de filtre à un Tableau Croisé Dynamique dans Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/add-page-field-in-pivot-table/)
- [Appliquer des styles aux Tableaux Croisés Dynamiques dans Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/apply-style-to-pivot-table/)
- [Modifier la disposition des champs de page dans un Tableau Croisé Dynamique](/cells/fr/nodejs-cpp/change-page-field-layout/)
- [Convertir une Sparkline en image et HTML dans Aspose.Cells for Node.js via C++](/cells/fr/nodejs-cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="nodejs-cpp" >}}