---
title: Ange hur man kryssar strängar i output HTML med HtmlCrossType med Node.js via C++
linktitle: Ange hur texten ska korsas i utdata HTML med HtmlCrossType
type: docs
weight: 140
url: /sv/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Lär dig hur man kontrollerar textöverflöd i HTML utmatning genom att specificera HtmlCrossType i Aspose.Cells for Node.js via C++. 
---

## **Möjliga användningsscenario**

När en cell innehåller text eller sträng men är större än cellens bredd, överflödar texten om nästa cell i nästa kolumn är null eller tom. När du sparar ditt Excel-fil till HTML kan du kontrollera detta överflöd genom att specificera kors-typen med hjälp av [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) enum. Den har följande värden:

- **HtmlCrossType.Default**: Visas som MS Excel; beror på nästa cell. Om nästa cell är null, kommer strängen att korsas eller klippas av.

- **HtmlCrossType.MSExport**: Visa strängen som MS Excel exporterar HTML.

- **HtmlCrossType.Cross**: Visar HTML-korsad sträng; prestandan för att skapa stora HTML-filer blir mer än tio gånger snabbare än att ställa in värdet till Default eller FitToCell.

- **HtmlCrossType.FitToCell**: Visa endast strängen inom cellens bredd.

## **Ange hur man korsar sträng i utmatnings-HTML med HtmlCrossType**

Följande kodexempel laddar [exempel-Excelfil](51740732.xlsx) och sparar den i HTML-format genom att specificera olika [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). Vänligen ladda ner de [utdata-HTMLs](51740734.zip) som genererades med denna kod. Exempel-Excelfilen innehåller en bild kantad med rött som visas i denna skärmbild, vilket visar effekten av [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype)-värdena på utdata HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHtmlCrossStringType.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify HTML Cross Type
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Default);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.MSExport);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Cross);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.FitToCell);

// Output Html
workbook.save("out" + opts.getHtmlCrossStringType() + ".htm", opts);
```
