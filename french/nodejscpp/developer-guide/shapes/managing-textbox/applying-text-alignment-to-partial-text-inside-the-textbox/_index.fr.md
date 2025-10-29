---
title: Comment appliquer/définir l alignement du texte dans la zone de texte avec Node.js via C++
linktitle: Appliquer/Définir l alignement du texte à une zone de texte
type: docs
weight: 20
url: /fr/nodejs-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Comment appliquer/définir l alignement du texte dans la zone de texte en Aspose.Cells for Node.js via C++.
keywords: appliquer/définir l alignement dans la zone de texte, feuille de calcul, Excel, Aspose, Node.js via C++
---

Les zones de texte peuvent améliorer l'expressivité de nos documents et diagrammes, et appliquer différents alignements à différentes parties d'une zone de texte peut aider à mettre en évidence des points d'intérêt pour les lecteurs. Mais l'alignement par défaut de la zone de texte ne répond pas à tous nos besoins. Pour cela, vous devrez peut-être ajuster chaque zone de texte pour répondre à vos exigences cibles. Si vous n'avez pas beaucoup d'objets Zone de texte à ajuster, cela ne vous posera pas de problème. Si vous avez tellement de zones de texte à ajuster, je pense que vous aurez des difficultés. Ne vous inquiétez pas maintenant, [Aspose.Cells](https://products.aspose.com/cells/) offre une API pour vous aider à faire cela.

Le code d'exemple suivant applique l'alignement du texte à une zone de texte.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
const shapes = workbook.getWorksheets().get(0).getShapes();

// add a TextBox
const shape = shapes.addTextBox(2, 0, 2, 0, 50, 120);
shape.setText("This is a test.");

// set alignment
shape.setTextHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
shape.setTextVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Save the excel file.
workbook.save(path.join(dataDir, "result.xlsx"));
```

Vous pouvez également modifier l'alignement du texte à l'intérieur d'une zone de texte avec le code HTML approprié. Le code exemple suivant applique l'alignement du texte à un texte partiel à l'intérieur de la zone de texte.

[fichier source](SampleTextboxExcel2016.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "SampleTextboxExcel2016.xlsx");

// Initialize an object of the Workbook class to load the template file
const sourceWb = new AsposeCells.Workbook(sourceFilePath);

// Access the target textbox whose text is to be aligned
const sourceTextBox = sourceWb.getWorksheets().get(0).getShapes().get(0);

// Create an object of the target workbook
const destWb = new AsposeCells.Workbook();

// Access the first worksheet from the collection
const _sheet = destWb.getWorksheets().get(0);

// Create new textbox
const _textBox = _sheet.getShapes().addShape(AsposeCells.MsoDrawingType.TextBox, 1, 0, 1, 0, 200, 200);

// Alternatively text box can be added using the following line as well
// const _textBox = _sheet.getShapes().addTextBox(1, 0, 1, 0, 200, 200);

// Use Html string from a template file textbox
_textBox.setHtmlText(sourceTextBox.getHtmlText());

// Save the workbook on disk
destWb.save("Output.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
