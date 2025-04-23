---  
title: 使用 Node.js 通过 C++ 将日期转换为日本日期  
linktitle: 将日期转换为日本日期  
type: docs  
weight: 350  
url: /zh/nodejs-cpp/convert-dates-to-japanese-dates/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 将公历日期转换为日本日期。  
---  

{{% alert color="primary" %}}  

在日本** **历法中，新的一个时代开始于新天皇的即位。2019年5月1日，新天皇即位，平成时代结束，令和时代开始。  

{{% /alert %}}  

Aspose.Cells 提供一种将公历日期转换为日本日期的方法。在此转换过程中，也考虑了时代的变化。下面的代码片段将包含公历日期的[源Excel](90112015.xlsx)文件转换为带有日本日期的[输出PDF](90112016.pdf)，如下图所示。  

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

