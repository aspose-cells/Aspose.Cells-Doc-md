---
title: Экспортировать XML данные, связанные с XML картой внутри книги, с помощью Node.js и C++
linktitle: Экспорт данных XML, связанных с XML схемой внутри книги
type: docs
weight: 20
url: /ru/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/
description: Узнайте, как экспортировать XML данные, связанные с XML картами внутри вашей книги, с помощью Aspose.Cells for Node.js via C++. 
---

## **Экспорт XML-данных, связанных с XML-схемой, внутри книги**

Пожалуйста, используйте метод [**Workbook.exportXml()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#exportXml-string-) для экспорта XML-данных, связанных с вашими XML-картами внутри рабочей книги. Следующий пример кода экспортирует XML-данные всех XML-карт из рабочей книги по очереди. Пожалуйста, проверьте [пример файла Excel](5115497.xlsx), используемый в этом коде, и [экспортированные XML-данные первой XML-карты](5472487.xml).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Export all XML data from all XML Maps from the Workbook.
for (let i = 0; i < workbook.getWorksheets().getXmlMaps().getCount(); i++) {
// Access the XML Map.
const map = workbook.getWorksheets().getXmlMaps().get(i);

// Exports its XML Data to file.
workbook.exportXml(map.getName(), path.join(dataDir, `${map.getName()}.xml`));
}
```
