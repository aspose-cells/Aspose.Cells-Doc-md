---
title: Insertion d'une image dans une cellule
description: Aspose.Cells est une bibliothèque Node.js via C++ pour travailler avec des fichiers de feuilles de calcul. Cet article explique comment ajuster une image exactement à la taille d'une seule cellule en utilisant deux approches différentes, placer une image flottante sur la cellule ou intégrer l'image directement dans la cellule.
keywords: Aspose.Cells, bibliothèque Node.js via C++, feuille de calcul, insérer image, intégrer image, image dans cellule, ajuster image à cellule, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /fr/nodejs-cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells propose deux méthodes distinctes pour associer une image à une seule cellule. Une image flottante est une forme située sur le calque de dessin de la feuille de calcul qui recouvre visuellement une plage de cellules, tandis qu'une image intégrée est stockée à l'intérieur de la cellule elle-même et s'adapte automatiquement à la zone d'affichage de la cellule. Choisissez l'approche qui correspond le mieux à vos besoins de mise en page.

{{% /alert %}}

## **Introduction**

Ajuster une image exactement à une seule cellule est une exigence courante lors de la conception de feuilles de calcul servant de rapports visuels, de catalogues de produits, d'annuaires d'employés, de tableaux de bord ou de listes d'inventaire. Plutôt que d'étirer une image sur plusieurs cellules ou de la placer de manière approximative sur une feuille de calcul, vous pouvez souhaiter une image nette, liée à la cellule, qui reste alignée avec la cellule qui la contient.

Aspose.Cells prend en charge ce scénario de deux manières complémentaires :

- **Approche 1 — Placer une image flottante sur une cellule.** Ajoutez une `Picture` à la feuille de calcul, définissez son `placement` sur `MoveAndSize`, puis ajustez ses cellules d'ancrage (`upperLeftRow`, `upperLeftColumn`, `lowerRightRow`, `lowerRightColumn`) pour que l'image couvre exactement une cellule.
- **Approche 2 — Intégrer une image directement dans une cellule.** Assignez les octets de l'image à la propriété `embeddedImage` de la cellule. L'image s'adapte automatiquement à la zone d'affichage de la cellule et se déplace avec la cellule.

La suite de cet article détaille les deux approches, explique les API concernées et montre comment les utiliser dans le code.

## **Approche 1 : Placer une image sur une cellule**

Une image flottante est un objet `Picture` qui réside sur le calque de dessin de la feuille de calcul. Bien qu'elle ne fasse partie d'aucune cellule individuelle, elle est ancrée à une plage de cellules. Les cellules d'ancrage de l'image — ses coins supérieur gauche et inférieur droit — déterminent son étendue visuelle sur la feuille de calcul. Par défaut, une image nouvellement ajoutée s'étend sur plusieurs cellules.

Pour qu'une image flottante couvre **exactement une seule cellule**, vous devez :

1. Ajouter l'image à l'aide de `worksheet.pictures.add(row, column, stream)`, ce qui ancre la nouvelle image à la cellule indiquée.
2. Définir les quatre propriétés d'ancrage pour que le rectangle de délimitation de l'image coïncide avec la cellule cible.
3. Définir `picture.placement` sur `PlacementType.MoveAndSize` afin que l'image se déplace et se redimensionne avec la cellule sous-jacente lorsque l'utilisateur modifie la largeur de colonne ou la hauteur de ligne.

### **Ancrer l'image à une seule cellule**

L'ancrage de l'image est défini par quatre propriétés d'index base zéro :

- `picture.upperLeftRow` — l'index de ligne du bord supérieur de l'image.
- `picture.upperLeftColumn` — l'index de colonne du bord gauche de l'image.
- `picture.lowerRightRow` — l'index de ligne du bord inférieur de l'image. Pour que le bord inférieur de l'image se trouve au bas de la ligne `r`, définissez cette valeur sur `r + 1`.
- `picture.lowerRightColumn` — l'index de colonne du bord droit de l'image. Pour que le bord droit de l'image se trouve à droite de la colonne `c`, définissez cette valeur sur `c + 1`.

Par exemple, pour ajuster l'image exactement dans la cellule **C6** (index de ligne `5`, index de colonne `2`), définissez `upperLeftRow = 5`, `upperLeftColumn = 2`, `lowerRightRow = 6` et `lowerRightColumn = 3`.

{{% alert color="primary" %}}

Les indices de ligne et de colonne dans Aspose.Cells sont **base zéro**. La cellule C6 a l'index de ligne 5 et l'index de colonne 2. Les erreurs de décalage d'une unité sur l'ancrage inférieur droit sont la source la plus fréquente d'images qui semblent empiéter sur une cellule adjacente.

{{% /alert %}}

### **Contrôler le comportement de placement**

`picture.placement` est une énumération de type `PlacementType` qui contrôle la manière dont l'image se comporte lorsque l'utilisateur redimensionne la ligne ou la colonne située en dessous. La valeur recommandée pour une image sur une seule cellule est `PlacementType.MoveAndSize`, qui fait que l'image se déplace et se redimensionne conjointement avec la cellule sous-jacente, en préservant l'ajustement exact.

### **Instructions étape par étape**

1. Créez un nouveau `Workbook` (ou ouvrez un classeur existant).
2. Accédez au `Worksheet` cible via `workbook.worksheets[0]`.
3. Ouvrez le fichier image depuis le disque dans un flux, en veillant à fermer correctement le flux après utilisation.
4. Appelez `worksheet.pictures.add(5, 2, stream)` pour ajouter une image ancrée à la cellule C6. Conservez la référence `Picture` retournée.
5. Définissez les quatre coordonnées d'ancrage pour que l'image ne couvre que la cellule C6 : `upperLeftRow = 5`, `upperLeftColumn = 2`, `lowerRightRow = 6`, `lowerRightColumn = 3`.
6. Définissez `picture.placement = PlacementType.MoveAndSize` pour conserver l'alignement de l'image avec C6 lorsque la colonne ou la ligne est redimensionnée.
7. Vous pouvez, facultativement, ajouter du texte d'exemple dans les cellules environnantes pour démontrer que seule la cellule C6 contient l'image.
8. Enregistrez le classeur sur le disque en tant que fichier `.xlsx`.

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

## **Approche 2 : Intégrer une image directement dans une cellule**

Aspose.Cells expose également un mécanisme plus simple pour les images liées à une cellule : la propriété `cell.embeddedImage`. Assigner les octets de l'image à cette propriété attache l'image à la cellule elle-même, comme s'il s'agissait de contenu inline.

### **Comment fonctionnent les images intégrées**

- L'image est stockée dans le contenu de la cellule plutôt que comme forme sur le calque de dessin.
- L'image s'adapte automatiquement aux limites rendues de la cellule. Aucune coordonnée d'ancrage ni paramètre de placement n'est requis.
- La cellule reste une véritable cellule, avec une véritable adresse, qui peut être référencée par des formules, triée comme élément d'une ligne, ou utilisée dans d'autres opérations au niveau de la cellule.

Cela fait de `cell.embeddedImage` l'option la plus concise lorsque votre objectif est simplement « une image qui réside à l'intérieur de cette cellule ».

### **Instructions étape par étape**

1. Créez un nouveau `Workbook` (ou ouvrez un classeur existant).
2. Accédez au `Worksheet` cible via `workbook.worksheets[0]`.
3. Lisez le fichier image depuis le disque dans un Buffer ou un tableau d'octets en utilisant les API du système de fichiers de Node.js (par exemple, `fs.readFileSync`).
4. Obtenez une référence à la cellule cible — soit via `worksheet.cells["C6"]`, soit via `worksheet.cells[5, 2]`.
5. Assignez le tableau d'octets à la propriété `embeddedImage` de la cellule.
6. Vous pouvez, facultativement, ajuster la hauteur de ligne et la largeur de colonne de la ligne et de la colonne cibles pour donner à l'image intégrée une apparence plus marquée.
7. Enregistrez le classeur sur le disque en tant que fichier `.xlsx`.

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

// Optionnellement ajuster la hauteur de ligne et la largeur de colonne pour que l'image intégrée soit plus visible
worksheet.getCells().setColumnWidth(2, 30);   // Colonne C (index 2)
worksheet.getCells().setRowHeight(5, 100);     // Ligne 6 (index 5)

// Enregistrer le classeur résultant en tant que fichier .xlsx
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Choisir la bonne approche**

Les deux approches produisent une image qui s'insère dans une seule cellule, mais elles diffèrent dans la manière dont l'image est stockée et dans son comportement :

- **Utilisez une image flottante (Approche 1) lorsque :**
  - Vous avez besoin d'un contrôle plus fin sur le placement, la superposition ou l'alignement avec d'autres objets de dessin.
  - Vous souhaitez que l'image se comporte comme une forme pouvant être sélectionnée, réordonnée ou regroupée avec d'autres formes.
  - Vous exigez une compatibilité descendante avec du code qui fonctionne déjà avec la collection de pictures.
  - Vous devez calculer les coordonnées d'ancrage dynamiquement en fonction de la disposition de la feuille de calcul.

- **Utilisez une image intégrée (Approche 2) lorsque :**
  - Vous souhaitez l'insertion la plus simple possible d'une image dans une cellule.
  - L'image doit se déplacer avec la cellule comme tout autre contenu de cellule.
  - Vous n'avez pas besoin de manipuler l'image en tant que forme.

{{% alert color="primary" %}}

Les deux approches peuvent coexister dans le même classeur. Vous pouvez placer des images flottantes sur un ensemble de cellules et intégrer des images directement dans d'autres cellules, car les deux mécanismes utilisent des couches de stockage différentes dans le fichier.

{{% /alert %}}

## **Articles connexes**

- [Comment insérer une image dans une cellule](/cells/fr/nodejs-cpp/how-to-place-image-to-cell/)
- [Ajouter des hyperliens d'image](/cells/fr/nodejs-cpp/add-image-hyperlinks/)
- [Charger une image Web à partir d'une URL dans une feuille de calcul Excel](/cells/fr/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipuler la position, la taille et le graphique du concepteur](/cells/fr/nodejs-cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="javascript" >}}