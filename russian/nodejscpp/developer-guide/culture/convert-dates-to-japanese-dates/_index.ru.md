---  
title: Преобразование дат в японские даты с помощью Node.js через C++  
linktitle: Преобразование дат в японские даты  
type: docs  
weight: 350  
url: /ru/nodejs-cpp/convert-dates-to-japanese-dates/  
description: Узнайте, как конвертировать григорианские даты в японские, используя Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

В японском календаре новая эра начинается с царствования нового императора. 1 мая 2019 года новый император пришел к власти, и эра Хейсэи закончилась, началась эра Рэйва.  

{{% /alert %}}  

Aspose.Cells предоставляет способ конвертировать григорианские даты в японские. Во время этой конвертации также учитываются изменения в эпохе. Следующий пример кода преобразует исходный Excel-файл (90112015.xlsx) с григорианскими датами в PDF (90112016.pdf) с японскими датами, как показано на изображении ниже.  

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
