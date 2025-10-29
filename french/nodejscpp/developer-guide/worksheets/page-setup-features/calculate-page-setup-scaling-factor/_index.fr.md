---
title: Calculer le facteur d’échelle de la mise en page avec Node.js via C++
linktitle: Calculer le facteur d échelle de la mise en page
type: docs
weight: 300
url: /fr/nodejs-cpp/calculate-page-setup-scaling-factor/
description: Cet article fournit un exemple de code expliquant comment utiliser l’API Node.js avec C++ pour calculer le facteur d’échelle de la mise en page en utilisant l’option Ajuster à n page(s) en largeur par m en hauteur de la feuille Excel de manière programmatique.
keywords: Ajuster à n pages en largeur par m en hauteur Excel Node.js via C++, calculer le facteur d’échelle de la mise en page Node.js via C++
---

{{% alert color="primary" %}}

Lorsque vous définissez la mise à l’échelle de la mise en page en utilisant l’option **Ajuster à n page(s) en largeur par m en hauteur**, Microsoft Excel calcule le facteur d’échelle de la mise en page. Vous pouvez calculer la même chose en utilisant la propriété [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--). Cette propriété retourne une valeur double qui peut être convertie en pourcentage. Par exemple, si elle retourne 0,5 cela signifie que le facteur d’échelle est de 50%.

{{% /alert %}}

Le code d'exemple suivant illustre comment calculer le facteur d'échelle de la mise en page en utilisant la propriété [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some data in these cells
worksheet.getCells().get("A4").putValue("Test");
worksheet.getCells().get("S4").putValue("Test");

// Set paper size
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Set fit to pages wide as 1
worksheet.getPageSetup().setFitToPagesWide(1);

// Calculate page scale via sheet render
const sr = new AsposeCells.SheetRender(worksheet, new AsposeCells.ImageOrPrintOptions());

// Convert page scale double value to percentage
const strPageScale = (sr.getPageScale() * 100).toFixed(0) + "%";

// Write the page scale value
console.log(strPageScale);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
