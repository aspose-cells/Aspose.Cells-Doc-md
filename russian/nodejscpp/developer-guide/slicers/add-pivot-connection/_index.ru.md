---
title: Добавить соединение сводной таблицы с помощью Node.js через C++
linktitle: Добавить связь сводной таблицы
type: docs
weight: 30
url: /ru/nodejs-cpp/add-pivot-connection/
description: Узнайте, как добавить соединение сводной таблицы с помощью Aspose.Cells for Node.js via C++.
keywords: Добавление соединения сводной таблицы без Office 2013, 2016, 2019 и Office 365 Node.js через C++.
---

## **Возможные сценарии использования**

Если вы хотите связать срез и сводную таблицу в Excel, ПКМ по срезу и выберите пункт "Связи отчета...". В списке опций можно управлять флажками. Аналогично, для программного связывания среза и сводной таблицы через API Aspose.Cells используйте метод [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#addPivotConnection-PivotTable-). Он свяжет срез и сводную таблицу.

## **Ассоциировать фильтр и сводную таблицу**

Следующий пример кода загружает [образец файла Excel](add-pivot-connection.xlsx), содержащий существующий срез. Он получает доступ к срезу и затем связывает его со сводной таблицей. В конце сохраняет рабочую книгу как [выходной файл Excel](add-pivot-connection-out.xlsx).

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "add-pivot-connection.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0); 

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Adds PivotTable connection.
slicer.addPivotConnection(pivotTable);

workbook.save(path.join(dataDir, "add-pivot-connection-out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
