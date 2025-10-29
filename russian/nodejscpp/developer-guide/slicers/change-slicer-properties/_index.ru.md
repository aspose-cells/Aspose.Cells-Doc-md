---
title: Изменить параметры среза с помощью Node.js через C++
linktitle: Изменить свойства фильтра
type: docs
weight: 70
url: /ru/nodejs-cpp/change-slicer-properties/
---

## **Возможные сценарии использования**

Могут возникнуть ситуации, когда потребуется изменить свойства среза, такие как расположение или высота строки. Aspose.Cells for Node.js via C++ предоставляет возможность обновлять эти свойства.

## **Изменить свойства фильтра**

Пожалуйста, посмотрите следующий образец кода. Он загружает [образец файла Excel](sampleCreateSlicerToExcelTable.xlsx), содержащий таблицу. Затем создает фильтр на основе первого столбца и изменяет его свойства, такие как высота строк, ширина, печатаемость, заголовок и т. д. Затем сохраняет книгу как [outputChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx).

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file containing a table.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateSlicerToExcelTable.xlsx"));

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first table inside the worksheet.
const table = worksheet.getListObjects().get(0);

// Add slicer
const idx = worksheet.getSlicers().add(table, 0, "H5");

const slicer = worksheet.getSlicers().get(idx);
slicer.setPlacement(AsposeCells.PlacementType.FreeFloating);
slicer.setRowHeightPixel(50);
slicer.setWidthPixel(500);
slicer.setTitle("Aspose");
slicer.setAlternativeText("Alternate Text");
slicer.setIsPrintable(false);
slicer.setIsLocked(false);

// Refresh the slicer.
slicer.refresh();

// Save the workbook in output XLSX format.
workbook.save(path.join(outputDir, "outputChangeSlicerProperties.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
