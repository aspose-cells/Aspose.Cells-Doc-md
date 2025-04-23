---  
title: Обновление значений связанных фигур с помощью Node.js через C++  
linktitle: Обновить значения связанных форм  
type: docs  
weight: 3200  
url: /ru/nodejs-cpp/refresh-values-of-linked-shapes/  
description: Узнайте, как обновить значения связанных фигур в Excel с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Иногда в вашем файле Excel есть связанная фигура, которая связана с ячейкой. В Microsoft Excel изменение значения связанной ячейки также изменяет значение связанной фигуры. Это также работает с Aspose.Cells for Node.js via C++, если вы хотите сохранить рабочую книгу в форматах XLS или XLSX. Однако, если вы хотите сохранить рабочую книгу в PDF или HTML, вам нужно вызвать метод [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--), чтобы обновить значение связанной фигуры.  

{{% /alert %}}  

## Пример  

Следующий скриншот показывает исходный файл Excel, использованный в приведенном ниже примере кода. В нем есть связанная картинка, связанная с ячейками A1 до E4. Мы изменим значение ячейки B4 с помощью Aspose.Cells и вызовем метод [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--) для обновления значения картинки и сохранения его в PDF-формате.  

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)  

Вы можете скачать [исходный файл Excel](95584291.xlsx) и [итоговый PDF](95584292.pdf) по указанным ссылкам.  

### Код Node.js для обновления значений связанных фигур  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleRefreshValueOfLinkedShapes.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Change the value of cell B4
const cell = worksheet.getCells().get("B4");
cell.putValue(100);

// Update the value of the Linked Picture which is linked to cell B4
worksheet.getShapes().updateSelectedValue();

// Save the workbook in PDF format
workbook.save(path.join(outputDir, "outputRefreshValueOfLinkedShapes.pdf"), AsposeCells.SaveFormat.Pdf);
```  
