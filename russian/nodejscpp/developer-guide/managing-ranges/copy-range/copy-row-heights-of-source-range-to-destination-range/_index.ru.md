---  
title: Копировать высоты строк из исходного диапазона в целевой диапазон с помощью Node.js и C++  
linktitle: Копировать высоту строк исходного диапазона в целевой диапазон  
type: docs  
weight: 590  
url: /ru/nodejs-cpp/copy-row-heights-of-source-range-to-destination-range/  
---  

{{% alert color="primary" %}}  

Иногда пользователи должны копировать высоты строк из исходного диапазона в целевой. Aspose.Cells for Node.js via C++ предоставляет перечисление [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) для этой цели. Установив свойство [**PasteOptions.getPasteType()**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/#getPasteType--) равным [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/), высоты всех строк внутри исходного диапазона будут скопированы в целевой диапазон.  

{{% /alert %}}  

Следующий пример кода объясняет, как использовать перечисление [**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/) для копирования высот строк исходного диапазона в целевой. После открытия сгенерированного файла Excel в Microsoft Excel вы увидите, что высоты строк целевого диапазона точно такие же, как и исходного.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Source worksheet
const srcSheet = workbook.getWorksheets().get(0);

// Add destination worksheet
const dstSheet = workbook.getWorksheets().add("Destination Sheet");

// Set the row height of the 4th row. This row height will be copied to destination range
srcSheet.getCells().setRowHeight(3, 50);

// Create source range to be copied
const srcRange = srcSheet.getCells().createRange("A1:D10");

// Create destination range in destination worksheet
const dstRange = dstSheet.getCells().createRange("A1:D10");

// PasteOptions, we want to copy row heights of source range to destination range
const opts = new AsposeCells.PasteOptions();
opts.setPasteType(AsposeCells.PasteType.RowHeights);

// Copy source range to destination range with paste options
dstRange.copy(srcRange, opts);

// Write informative message in cell D4 of destination worksheet
dstSheet.getCells().get("D4").putValue("Row heights of source range copied to destination range");

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
