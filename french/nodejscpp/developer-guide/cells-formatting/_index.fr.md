---
title: Formatage des cellules avec Node.js via C++
description: Apprenez comment formater et styliser les cellules dans Aspose.Cells for Node.js via C++, y compris le formatage numérique, le formatage de date, les styles de police, et autres options de style de cellule. Notre guide vous aidera à créer des feuilles de calcul attrayantes et professionnelles.
keywords: Aspose.Cells for Node.js via C++, formatage de cellules, stylisation, formatage numérique, formatage de date, style de police, options de style de cellule, feuille de calcul, création, aspect professionnel, mise en forme des lignes et colonnes.
linktitle: Formater les cellules
type: docs
weight: 120
url: /fr/nodejs-cpp/cells-formatting/
---

## **Introduction**

{{% alert color="primary" %}}

Aspose.Cells fournit les méthodes [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) et [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) de la classe [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell), utilisées pour obtenir/modifier le style de formatage d'une cellule. Aspose.Cells fournit également une classe [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{% /alert %}}

## **Comment formater les cellules en utilisant les méthodes GetStyle et SetStyle**

Appliquer différents types de styles de formatage sur les cellules pour définir des couleurs de fond ou de premier plan, des bordures, des polices, des alignements horizontaux et verticaux, le niveau d'indentation, la direction du texte, l'angle de rotation et bien plus encore.

### **Comment utiliser les méthodes GetStyle et SetStyle**

Si les développeurs doivent appliquer différents styles de mise en forme à différentes cellules, il est préférable d'obtenir [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) de la cellule en utilisant la méthode [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--), de spécifier les attributs de style et ensuite d'appliquer la mise en forme avec la méthode [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-). Un exemple est donné ci-dessous pour illustrer cette approche d'application de divers styles à une cellule.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Defining a Style object
let style;

// Get the style from A1 cell
style = cell.getStyle();

// Setting the vertical alignment
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text
style.getFont().setColor(AsposeCells.Color.Green);

// Setting to shrink according to the text contained in it
style.setShrinkToFit(true);

// Setting the bottom border color to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Applying the style to A1 cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Comment utiliser l'objet de style pour formater différentes cellules**

Si les développeurs doivent appliquer le même style de mise en forme à différentes cellules, ils peuvent utiliser l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Veuillez suivre les étapes ci-dessous pour utiliser l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style):

1. Ajoutez un objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) en appelant la méthode [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--) de la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)
2. Accédez à l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) récemment ajouté
3. Définissez les propriétés/attributs souhaités de l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) pour appliquer les paramètres de formatage souhaités
4. Assignez l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) configuré à vos cellules souhaitées

Cette approche peut grandement améliorer l'efficacité de vos applications et économiser de la mémoire également.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the first worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Adding a new Style
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Assigning the Style object to the "A1" cell
cell.setStyle(style);

// Apply the same style to some other cells
worksheet.getCells().get("B1").setStyle(style);
worksheet.getCells().get("C1").setStyle(style);
worksheet.getCells().get("D1").setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Comment utiliser les styles prédéfinis de Microsoft Excel 2007**

Si vous avez besoin d'appliquer différents styles de formatage pour Microsoft Excel 2007, appliquez les styles en utilisant l'API Aspose.Cells. Un exemple est donné ci-dessous pour illustrer cette approche d'application d'un style prédéfini sur une cellule.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");


// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Create a style object.
const style = workbook.createStyle();

// Input a value to A1 cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Test");

// Apply the style to the cell.
workbook.getWorksheets().get(0).getCells().get("A1").setStyle(style);

// Save the Excel 2007 file.
workbook.save(path.join(dataDir, "book1.out.xlsx"));
```



## **Comment formater des caractères sélectionnés dans une cellule**

La gestion des paramètres de police explique comment formater du texte dans les cellules, mais cela explique seulement comment formater tout le contenu de la cellule. Et si vous voulez formater uniquement des caractères sélectionnés ?

Aspose.Cells prend également en charge cette fonctionnalité. Ce sujet explique comment utiliser cette fonctionnalité efficacement.

### **Comment formater des caractères sélectionnés**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient la collection [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre une collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Chaque élément dans la collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

La classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) fournit la méthode [**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-) qui prend les paramètres suivants pour sélectionner une plage de caractères à l'intérieur d'une cellule :

- **Index de début**, l'index du caractère à partir duquel la sélection commence.
- **Nombre de caractères**, le nombre de caractères à sélectionner.

La méthode [**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-) retourne une instance de la classe [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) qui permet aux développeurs de formater les caractères de la même manière qu'une cellule, comme illustré ci-dessous dans l'exemple de code. Dans le fichier de sortie, dans la cellule A1, le mot 'Visit' sera formaté avec la police par défaut, mais 'Aspose!' sera en gras et en bleu.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first(default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Visit Aspose!");

// Setting the font of selected characters to bold
const font = cell.characters(6, 7).getFont();
font.isBold = true;

// Setting the font color of selected characters to blue
font.color = AsposeCells.Color.Blue;

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

{{% alert color="primary" %}}

Si vous souhaitez formater une partie du texte enrichi dans une cellule, envisagez d'utiliser les méthodes [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) & [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-). La méthode [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) est utilisée pour accéder aux parties du texte, puis des modifications peuvent être apportées à l'aide de la méthode [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-), tandis que la méthode **Get** retourne un tableau d'objets [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) qui peuvent être manipulés pour définir diverses propriétés telles que le nom de la police, la couleur de la police, le gras, etc. La méthode **Set** peut être utilisée pour appliquer les modifications.

{{% /alert %}}

## **Comment formater les lignes et les colonnes**

Parfois, les développeurs doivent appliquer le même formatage sur des lignes ou des colonnes. Appliquer le formatage sur chaque cellule prend souvent plus de temps et n'est pas une bonne solution.
Pour résoudre ce problème, Aspose.Cells offre une solution simple et rapide qui est discutée en détail dans cet article.

### **Mise en forme des lignes & colonnes**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre une collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). La collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) offre une collection [**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--).

### **Comment formater une ligne**

Chaque élément de la collection [**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--) représente un objet [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row). L'objet [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row) offre la méthode [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) utilisée pour définir la mise en forme de la ligne. Pour appliquer la même mise en forme à une ligne, utilisez l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Les étapes ci-dessous montrent comment l'utiliser.

1. Ajoutez un objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) à la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) en appelant sa méthode [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--).
2. Définissez les propriétés de l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) pour appliquer les paramètres de mise en forme.
3. Activez les attributs pertinents pour l'objet [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag).
4. Assignez l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) configuré à l'objet [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a row from the Rows collection
const row = worksheet.getCells().getRows().get(0);

// Assigning the Style object to the Style property of the row
row.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Comment formater une colonne**

La collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) offre également une collection [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--). Chaque élément dans la collection [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--) représente un objet [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column). Semblable à un objet [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row), l'objet [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column) offre également la méthode [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) pour formater une colonne.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a column from the Columns collection
const column = worksheet.getCells().getColumns().get(0);

// Applying the style to the column
column.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Sujets avancés**
- [Paramètres d'alignement](/cells/fr/nodejs-cpp/cells-alignment-settings/)
- [Paramètres de bordure](/cells/fr/nodejs-cpp/cells-border-settings/)
- [Définir les formats conditionnels des fichiers Excel et ODS.](/cells/fr/nodejs-cpp/conditional-formatting/)
- [Thèmes et couleurs d'Excel](/cells/fr/nodejs-cpp/excel-themes-and-colors/)
- [Paramètres de remplissage](/cells/fr/nodejs-cpp/cells-fill-settings/)
- [Paramètres de police](/cells/fr/nodejs-cpp/cells-font-settings/)
- [Formater les cellules de feuille de calcul dans un classeur](/cells/fr/nodejs-cpp/format-worksheet-cells-in-a-workbook/)
- [Mise en œuvre du système de date 1904](/cells/fr/nodejs-cpp/implement-1904-date-system/)
- [Fusionner et scinder des cellules](/cells/fr/nodejs-cpp/merging-and-unmerging-cells/)
- [Paramètres de nombre](/cells/fr/nodejs-cpp/cells-number-settings/)
- [Obtenir et définir le style des cellules](/cells/fr/nodejs-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="nodejs-cpp" >}}
