---  
title: Экспорт форматирования условных форматов DataBar, ColorScale и IconSet при преобразовании Excel в HTML с помощью Node.js через C++  
linktitle: Экспорт условного форматирования данных, цветовой шкалы и набора значков при преобразовании Excel в HTML  
type: docs  
weight: 30  
url: /ru/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/  
---  

{{% alert color="primary" %}} 

Вы можете экспортировать условное форматирование DataBar, ColorScale и IconSet при преобразовании файла Excel в HTML. Эта функция частично поддерживается Microsoft Excel, но Aspose.Cells for Node.js via C++ поддерживает ее полностью.

{{% /alert %}}  

## **Экспорт условного форматирования данных, цветовой шкалы и набора значков при преобразовании Excel в HTML**  
Следующий скриншот показывает [образец excel файла](5115558.xlsx) с форматированием условного оформления DataBar, ColorScale и IconSet. Вы можете скачать [образец excel файла](5115558.xlsx) по данной ссылке.  

![todo:image_alt_text](conversion_1.png)  

Следующий скриншот показывает вывод Aspose.Cells в виде HTML файла с форматированием условного оформления DataBar, ColorScale и IconSet. Как видите, он выглядит точно так же, как и [образец excel файла](5115558.xlsx).  

![todo:image_alt_text](conversion_2.png)  

### **Образец кода**  
Следующий пример кода преобразует пример файла Excel в HTML, что представляет собой просто обычное [преобразование Excel в HTML](/cells/ru/nodejs-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
