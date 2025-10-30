---
title: Prefissare gli stili degli elementi della tabella con la proprietà HtmlSaveOptions.TableCssId in Node.js tramite C++
linktitle: Prefisso degli stili degli elementi della tabella con la proprietà HtmlSaveOptions.TableCssId
type: docs
weight: 110
url: /it/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Scopri come prefissare gli stili degli elementi della tabella HTML usando Aspose.Cells for Node.js via C++. 
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells permette di prefissare gli stili degli elementi della tabella con la proprietà [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--). Supponi di impostare questa proprietà con un valore come **MyTest_TableCssId**, allora troverai gli stili degli elementi della tabella come mostrato di seguito:

{{< highlight javascript >}}
 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
{{< /highlight >}}

La seguente schermata mostra l'effetto dell'utilizzo della proprietà [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--) sull'HTML di output.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Prefisso degli stili degli elementi della tabella con la proprietà HtmlSaveOptions.TableCssId**

Il codice di esempio seguente dimostra come utilizzare la proprietà [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--). Si prega di controllare l'[output HTML](60489790.zip) generato dal codice per avere un riferimento.

## **Codice di Esempio**

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
