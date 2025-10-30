---
title: Prefix Tabellen Element Stile mit der Eigenschaft HtmlSaveOptions.TableCssId in Node.js via C++
linktitle: Tabellenelemente Styles mit der Eigenschaft HtmlSaveOptions.TableCssId prefixieren
type: docs
weight: 110
url: /de/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Lernen Sie, wie Sie Tabellen Element Stile in HTML mit Aspose.Cells for Node.js via C++ prefixen. 
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es, Tabellen-Element-Stile mit der Eigenschaft [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--) zu prefixen. Wenn Sie diese Eigenschaft mit einem Wert wie **MyTest_TableCssId** setzen, finden Sie Tabellen-Element-Stile wie unten gezeigt:

{{< highlight javascript >}}
 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
{{< /highlight >}}

Der folgende Screenshot zeigt die Auswirkungen der Verwendung der [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--)-Eigenschaft auf die Ausgabe von HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Vorabtabellenelementstilen mit der HtmlSaveOptions.TableCssId-Eigenschaft**

Der folgende Beispielcode zeigt, wie die [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--)-Eigenschaft verwendet wird. Bitte überprüfen Sie das [Ausgabe-HTML](60489790.zip), das vom Code generiert wurde, als Referenz.

## **Beispielcode**

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
