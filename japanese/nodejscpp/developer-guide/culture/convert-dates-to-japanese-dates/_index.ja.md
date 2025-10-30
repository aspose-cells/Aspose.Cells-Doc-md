---  
title: Node.jsを使ったC++経由での日付を日本の日付に変換する  
linktitle: 日本の日付への変換  
type: docs  
weight: 350  
url: /ja/nodejs-cpp/convert-dates-to-japanese-dates/  
description: Aspose.Cells for Node.js via C++を使用して、西暦日付を日本の日付に変換する方法を学びましょう。  
---  

{{% alert color="primary" %}}  

日本のカレンダーでは、新しい天皇の即位とともに新しい元号が始まります。2019年5月1日に新しい天皇が即位し、平成時代が終了し令和時代が始まりました。  

{{% /alert %}}  

Aspose.Cellsは、西暦日付を日本の元号に変換する方法を提供します。この変換では、元号の変化も考慮されます。次のコードスニペットは、西暦日付を含む[源のExcel](90112015.xlsx)ファイルを日本の和暦付きの[出力PDF](90112016.pdf)に変換します。画像の例も示します。  

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
