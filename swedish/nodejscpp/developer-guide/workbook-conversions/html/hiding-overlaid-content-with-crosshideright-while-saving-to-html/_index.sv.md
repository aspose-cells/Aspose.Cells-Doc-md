---
title: Dölja överlagt innehåll med CrossHideRight vid sparande till HTML med Node.js via C++
linktitle: Dölja överlagt innehåll med CrossHideRight medan du sparar till HTML
type: docs
weight: 100
url: /sv/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---


## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML kan du ange olika kors-typer för cellsträngar. Som standard genererar Aspose.Cells HTML enligt Microsoft Excel, men när du ändrar kors-typen till [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype), döljer den alla strängar på höger sida av cellen som är överlagrade eller överlappar cellsträngen.

## **Dölja överlagt innehåll med CrossHideRight vid sparning till Html**

Följande exempel kod laddar den [exempel Excel-filen](64716894.xlsx) och sparar den till [utdata HTML](64716893.zip) efter att ha ställt in [**HtmlSaveOptions.getHtmlCrossStringType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getHtmlCrossStringType--) som [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). Skärmbilden förklarar hur [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) påverkar utdata HTML från standardutdata.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.CrossHideRight);

// Save to HTML with HtmlSaveOptions
workbook.save(path.join(dataDir, "outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html"), opts);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
