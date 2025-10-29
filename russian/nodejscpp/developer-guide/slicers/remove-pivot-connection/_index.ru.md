---
title: Удалить соединение сводной таблицы с помощью Node.js через C++
linktitle: Удалить связь сводной таблицы
type: docs
weight: 30
url: /ru/nodejs-cpp/remove-pivot-connection/
description: Узнайте, как удалять соединение сводных таблиц с помощью Aspose.Cells for Node.js via C++.
keywords: Удаление соединения сводных таблиц без Office 2013, 2016, 2019 и Office 365 Node.js через C++.
---

## **Возможные сценарии использования**

Если вы хотите разорвать связь между сегментатором и сводной таблицей в Excel, нужно щелкнуть правой кнопкой по сегментатору и выбрать пункт «Соединения отчета...». В списке опций можно управлять флажками. Аналогично, чтобы разорвать связь сегментатора и сводной таблицы с помощью API Aspose.Cells программным путем, используйте метод [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#removePivotConnection-pivottable-). Он разорвет связь сегментатора и сводной таблицы.

## **Отсоединить срезку и сводную таблицу**

Следующий пример кода загружает [пример файла Excel](remove-pivot-connection.xlsx), содержащий существующий сегментатор. Он обращается к сегментаторам и затем разрывает связь сегментатора и сводной таблицы. В конце он сохраняет рабочую книгу как [выходной файл Excel](remove-pivot-connection-out.xlsx).

## **Образец кода**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "remove-pivot-connection.xlsx");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Remove PivotTable connection.
slicer.removePivotConnection(pivotTable);
// Save the workbook in output XLSX format.
workbook.save(path.join(dataDir, "remove-pivot-connection-out.xlsx"));
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
