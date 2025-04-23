---
title: Используйте пользовательские XML части в Aspose.Cells с Node.js через C++
linktitle: Использование пользовательских XML частей в Aspose.Cells
type: docs
weight: 390
url: /ru/nodejs-cpp/use-custom-xml-parts-in-aspose-cells/
description: Узнайте, как использовать пользовательские XML части в Aspose.Cells for Node.js via C++. Интегрируйте внешние XML данные в файлы Excel без усилий.
--- 

## Использование пользовательских XML-частей в Aspose.Cells

Пользовательские XML-части — это XML-данные, хранящиеся разными приложениями, такими как SharePoint и др., внутри файла Excel. Эти данные используются различными приложениями, которым они необходимы. Microsoft Excel не использует эти данные, поэтому для их добавления отсутствует графический интерфейс. Вы можете просмотреть эти данные, изменив расширение **.xlsx** на **.zip**, а затем открыть его с помощью **WinZip**. Также можно открыть ZIP-файл любым сторонним архиватором Windows, например WinRAR или WinZip. Данные находятся внутри папки **customXml**.

Вы можете добавлять пользовательские XML-части, используя Aspose.Cells через метод [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/).

Следующий пример кода использует метод [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/) и добавляет XML-данные **Book Catalog**, название которых **BookStore**. На следующем изображении показан результат этого кода. Как видно, XML **Book Catalog** добавлен внутри узла **BookStore**, который является именем этого свойства.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Код Node.js для использования пользовательских XML-частей

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "output.xlsx");

// The sample XML that will be injected to Workbook
const booksXML = `<catalog>
<book>
<title>Complete C#</title>
<price>44</price>
</book>
<book>
<title>Complete Java</title>
<price>76</price>
</book>
<book>
<title>Complete SharePoint</title>
<price>55</price>
</book>
<book>
<title>Complete PHP</title>
<price>63</price>
</book>
<book>
<title>Complete VB.NET</title>
<price>72</price>
</book>
</catalog>`;

// Create an instance of Workbook class
const workbook = new AsposeCells.Workbook();

// Add Custom XML Part to ContentTypePropertyCollection
workbook.getContentTypeProperties().add("BookStore", booksXML);

// Save the resultant spreadsheet
workbook.save(filePath);
```

## Связанная статья

- [Добавление пользовательских свойств, видимых в панели информации о документе](/cells/ru/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
