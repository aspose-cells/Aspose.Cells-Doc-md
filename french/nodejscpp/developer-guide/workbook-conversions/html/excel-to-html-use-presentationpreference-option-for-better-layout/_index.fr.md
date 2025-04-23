---
title: Conversion Excel en HTML  Utiliser l option PresentationPreference pour une meilleure disposition avec Node.js via C++
linktitle: Excel en HTML  Utiliser l option PresentationPreference pour une meilleure mise en page
type: docs
weight: 220
url: /fr/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
---

{{% alert color="primary" %}} 

Aspose.Cells fournit une propriété utile HtmlSaveOptions.presentationPreference pour les développeurs qui ont besoin d'un meilleur rendu lors de la sauvegarde d'un fichier Microsoft Excel en HTML ou MHT. La valeur par défaut de la propriété est false. Nous recommandons de définir cette propriété à true pour obtenir une présentation plus attractive des rapports Excel.

{{% /alert %}} 

Veuillez voir le code d'exemple ci-dessous qui démontre comment rendre un fichier HTML à partir d'un rapport Excel avec la préférence de présentation activée.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate the Workbook
// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Create HtmlSaveOptions object
const options = new AsposeCells.HtmlSaveOptions();
// Set the Presentation preference option
options.setPresentationPreference(true);

// Save the Excel file to HTML with specified option
workbook.save(path.join(dataDir, "outPresentationlayout1.out.html"), options);
```
