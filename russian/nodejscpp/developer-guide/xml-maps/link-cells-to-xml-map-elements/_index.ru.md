---
title: Связать ячейки с элементами XML карты через Node.js с помощью C++
linktitle: Привязка ячеек к элементам XML отображения
type: docs
weight: 50
url: /ru/nodejs-cpp/link-cells-to-xml-map-elements/
---

## **Возможные сценарии использования**

Вы можете связать ваши ячейки с элементами XML-карты с помощью Aspose.Cells for Node.js via C++. Используйте метод [**Cells.linkToXmlMap(string, number, number, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#linkToXmlMap-string-number-number-string-) для этой цели.

## **Привязка ячеек к элементам XML-отображения**

Следующий образец кода загружает [исходный Excel-файл](5115471.xlsx), который содержит XML-карту, затем связывает ячейки A1, B2, C3, D4, E5 и F6 с элементами XML-карты FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 и FIELD8 соответственно, а затем сохраняет книгу Excel в [выходной Excel-файл](5115467.xlsx).

Если вы откроете [выходной Excel-файл](5115467.xlsx) и нажмете кнопку Developer > Source, вы увидите, что ячейки связаны с элементами XML-карты, и они также будут выделены Microsoft Excel, как показано на этом изображении.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-xml-map.xlsx"));

// Access the Xml Map inside it
const map = workbook.getWorksheets().getXmlMaps().get(0);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Map FIELD1 and FIELD2 to cell A1 and B2
ws.getCells().linkToXmlMap(map.getName(), 0, 0, "/root/row/FIELD1");
ws.getCells().linkToXmlMap(map.getName(), 1, 1, "/root/row/FIELD2");

// Map FIELD4 and FIELD5 to cell C3 and D4
ws.getCells().linkToXmlMap(map.getName(), 2, 2, "/root/row/FIELD4");
ws.getCells().linkToXmlMap(map.getName(), 3, 3, "/root/row/FIELD5");

// Map FIELD7 and FIELD8 to cell E5 and F6
ws.getCells().linkToXmlMap(map.getName(), 4, 4, "/root/row/FIELD7");
ws.getCells().linkToXmlMap(map.getName(), 5, 5, "/root/row/FIELD8");

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
