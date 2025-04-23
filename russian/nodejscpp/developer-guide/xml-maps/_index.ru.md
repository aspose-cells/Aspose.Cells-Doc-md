---
title: Импорт XML в книгу Excel с помощью Node.js через C++
linktitle: Сопоставления XML
type: docs
weight: 210
url: /ru/nodejs-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Импорт данных из XML файлов в Excel с помощью Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет импортировать карту XML внутри книги с помощью метода [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-). Вы можете импортировать карту XML в Microsoft Excel, следуя следующим шагам:

- Выберите вкладку **Разработчик**
- Нажмите **Импорт** в разделе XML и следуйте необходимым шагам.

Для завершения импорта вам потребуется предоставить свои XML-данные. Вот [пример XML-данных](5115037.txt), который вы можете использовать для тестирования.

{{% /alert %}}

## **Импорт XML-схемы с использованием Microsoft Excel**

На следующем скриншоте показано, как импортировать XML-схему с использованием Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Импорт карты XML с помощью Aspose.Cells for Node.js via C++**

В следующем примере кода показано, как использовать [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-). Это генерирует [выходной файл Excel](5115036.xlsx), как показано на этом снимке экрана.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Local XML file path
const XML = path.join(dataDir, "sampleXML.txt");

// Import your XML Map data starting from cell A1
workbook.importXml(XML, "Sheet1", 0, 0);

// Save workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

## **Продвинутые темы**
- [Добавление карты XML внутри книги с помощью метода XmlMapCollection.add()](/cells/ru/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Экспорт XML-данных, связанных с XML-схемой, внутри книги](/cells/ru/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Найдите имя корневого элемента XML-карты.](/cells/ru/nodejs-cpp/find-the-root-element-name-of-xml-map/)
- [Привязка ячеек к элементам XML-отображения](/cells/ru/nodejs-cpp/link-cells-to-xml-map-elements/)

