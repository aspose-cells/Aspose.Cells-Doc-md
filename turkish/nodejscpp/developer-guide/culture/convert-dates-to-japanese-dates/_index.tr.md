---  
title: Tarihleri Japonya tarihine dönüştürmek için Node.js kullanarak C++ ile  
linktitle: Japon Tarihlerine Dönüştür  
type: docs  
weight: 350  
url: /tr/nodejs-cpp/convert-dates-to-japanese-dates/  
description: Aspose.Cells for Node.js via C++ kullanarak Gregoryen tarihlerini Japon tarihine dönüştürmeyi öğrenin.  
---  

{{% alert color="primary" %}}  

Japon Takviminde, yeni bir imparatorun saltanatıyla yeni bir çağ başlar. 1 Mayıs 2019'da, Heisei çağı sona erdi ve Reiwa çağı başladı.  

{{% /alert %}}  

 Aspose.Cells, Gregoriyen tarihlerini Japon tarihine dönüştürmenin bir yolunu sağlar. Bu dönüşüm sırasında, çağdaki değişiklikler de dikkate alınır. Aşağıdaki kod parçası, Gregoriyen tarihleri içeren [kaynak Excel](90112015.xlsx) dosyasını Japon tarihleriyle [çıktı PDF](90112016.pdf) haline dönüştürür, aşağıdaki görselde gösterildiği gibi.  

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
