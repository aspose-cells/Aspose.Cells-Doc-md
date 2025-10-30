---
title: Aktivera CSS anpassade egenskaper vid sparande till HTML med Node.js via C++
linktitle: Aktivera CSS Anpassade Egenskaper under sparande till HTML
type: docs
weight: 320
url: /sv/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/
description: Lär dig hur du aktiverar CSS anpassade egenskaper när du sparar Excel filer till HTML med Aspose.Cells for Node.js via C++. 
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML, för scenariot att det finns flera förekomster av en bas64-bild, med anpassad egenskap behöver bilddata endast sparas en gång, vilket kan förbättra prestandan för den resulterande HTML-filen. Använd [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--)-egenskapen och ställ in den på **true** när du sparar till HTML.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **Aktivera CSS Anpassade Egenskaper under sparande till HTML**

Följande exempel visar hur [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--)-egenskapen används. Skärmkvaliteten visar effekten av denna egenskap när den inte är inställd på **true**. Vänligen ladda ner [exempel-Excelfilen](50528260.xlsx) som används i detta exempel och den [utdata-HTML](50528261.zip) som genereras för referens.



## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleEnableCssCustomProperties.xlsx"));

const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportImagesAsBase64(true);

// Enable EnableCssCustomProperties
opts.setEnableCssCustomProperties(true);

// Save the workbook in HTML
workbook.save(path.join(dataDir, "outputEnableCssCustomProperties.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
