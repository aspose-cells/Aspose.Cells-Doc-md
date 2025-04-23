---
title: Prefixa tabell element stilar med HtmlSaveOptions.TableCssId egenskap i Node.js via C++
linktitle: Förprefixa tabellens elementstilar med HtmlSaveOptions.TableCssId egenskapen
type: docs
weight: 110
url: /sv/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: Lär dig hur du prefixar tabell element stilar i HTML med Aspose.Cells for Node.js via C++. 
---

## **Möjliga användningsscenario**

Aspose.Cells tillåter dig att prefixa tabell element stilar med egenskapen [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--). Anta att du ställer in denna egenskap med ett värde som **MyTest_TableCssId**, då kommer du att hitta tabell-element stilar som visas nedan:

{{< highlight javascript >}}
 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
{{< /highlight >}}

Följande skärmbild visar effekten av att använda [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--)egenskap på utdata-HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Förprefixa tabellens elementstilar med HtmlSaveOptions.TableCssId-egenskapen**

Följande exempelkod visar hur man använder [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--)-egenskapen. Vänligen kontrollera [utdata-HTML-filen](60489790.zip) som genererats av koden för referens.

## **Exempelkod**

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
