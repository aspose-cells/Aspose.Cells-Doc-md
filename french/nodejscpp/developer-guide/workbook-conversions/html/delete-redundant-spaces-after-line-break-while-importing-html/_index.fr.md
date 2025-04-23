---
title: Supprimer les espaces redondants après le saut de ligne lors de l importation HTML avec Node.js via C++
linktitle: Supprimez les espaces redondants après un saut de ligne lors de l importation du HTML
type: docs
weight: 20
url: /fr/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Apprenez comment supprimer les espaces redondants après les sauts de ligne lors de l importation de HTML en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Veuillez utiliser la propriété [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--) et la définir sur **true** pour supprimer tous les espaces redondants après la balise de saut de ligne. Par défaut, cette propriété est **false** et les espaces redondants sont conservés dans les fichiers Excel en sortie.

{{% /alert %}}

## Effet de la propriété HTMLLoadOptions.deleteRedundantSpaces réglée sur false ou true

La capture d'écran suivante montre l'effet de définir cette propriété sur **false** et **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Supprimer les espaces redondants après un saut de ligne lors de l'importation du HTML

### Exemple de programmation

Le code d'exemple suivant montre l'utilisation de la propriété [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--). Veuillez la régler sur **true** ou **false** pour obtenir le résultat illustré dans la capture d'écran ci-dessus.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Sample Html containing redundant spaces after <br> tag
const html = "<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

// Convert Html to byte array
const byteArray = Buffer.from(html, 'utf-8');

// Set Html load options and keep precision true
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
loadOptions.setDeleteRedundantSpaces(true);

// Convert byte array into stream
const stream = Uint8Array.from(byteArray);

// Create workbook from stream with Html load options
const workbook = new AsposeCells.Workbook(stream, loadOptions);

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Auto fit the sheet columns
sheet.autoFitColumns();

// Save the workbook
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
