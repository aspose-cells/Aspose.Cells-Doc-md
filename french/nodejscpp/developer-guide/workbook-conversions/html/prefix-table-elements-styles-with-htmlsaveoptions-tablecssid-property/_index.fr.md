---
title: Prefixer les styles des éléments de tableau avec la propriété HtmlSaveOptions.TableCssId dans Node.js via C++
linktitle: Préfixer les styles des éléments de tableau avec la propriété HtmlSaveOptions.TableCssId
type: docs
weight: 110
url: /fr/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Apprenez à préfixer les styles des éléments de tableau dans HTML en utilisant Aspose.Cells for Node.js via C++. 
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet de préfixer les styles des éléments de tableau avec la propriété [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--). Supposons que vous définissiez cette propriété avec une valeur comme **MyTest_TableCssId**, alors vous trouverez des styles d'éléments de tableau comme ci-dessous :

{{< highlight javascript >}}
 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
{{< /highlight >}}

La capture d'écran suivante montre l'effet de l'utilisation de la propriété [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--) sur le HTML de sortie.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Préfixer les styles des éléments de table avec la propriété HtmlSaveOptions.TableCssId**

Le code d'exemple suivant montre comment utiliser la propriété [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--). Veuillez vérifier le fichier HTML de sortie (60489790.zip) généré par le code pour une référence.

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - specify table css id
const opts = new AsposeCells.HtmlSaveOptions();
opts.setTableCssId("MyTest_TableCssId");

// Save the workbook in html
wb.save("outputTableCssId.html", opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
