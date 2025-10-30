---  
title: Konvertera datum till japanska datum med Node.js via C++  
linktitle: Konvertera datum till japanska datum  
type: docs  
weight: 350  
url: /sv/nodejs-cpp/convert-dates-to-japanese-dates/  
description: Lär dig hur du konverterar gregorianska datum till japanska datum med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

I den japanska** **kalendern börjar en ny era med regeringen av en ny kejsare. Den 1 maj 2019 tillträdde en ny kejsare med vilken Heisei-eran avslutades och Reiwa-eran började.  

{{% /alert %}}  

Aspose.Cells ger en metod för att konvertera gregorianska datum till japanska datum. Under denna konvertering beaktas även eraändringarna. Följande kodstycke konverterar en [källa Excel](90112015.xlsx) fil med gregorianska datum till en [utdata PDF](90112016.pdf) med japanska datum enligt bilden nedan.  

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const options = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
options.setLanguageCode(AsposeCells.CountryCode.Japan);
options.setRegion(AsposeCells.CountryCode.Japan);

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "JapaneseDates.xlsx"), options);
workbook.save(outputDir + "JapaneseDates.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
