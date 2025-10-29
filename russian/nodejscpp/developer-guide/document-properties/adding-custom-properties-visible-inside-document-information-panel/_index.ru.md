---
title: Добавление пользовательских свойств, видимых внутри панели информации о документе, с помощью Node.js через C++
linktitle: Добавление пользовательских свойств, видимых в панели информации о документе
type: docs
weight: 300
url: /ru/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Узнайте, как добавлять пользовательские свойства в объект книги с помощью Aspose.Cells for Node.js via C++. Эти свойства можно просматривать в Панели информации о документе.
---

## **Добавление пользовательских свойств, видимых в панели информации о документе**

Aspose.Cells for Node.js via C++ можно использовать для добавления пользовательских свойств внутри объекта книги, которые отображаются в Панели информации о документе. Вы можете открыть Панель информации о документе в Microsoft Excel, используя команды меню Файл > Info > Properties > Show Document Panel.

Пожалуйста, используйте метод [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/#add-string-string-) для добавления пользовательского свойства, которое будет отображаться в Панели информации о документе.

Следующий пример кода добавляет два пользовательских свойства. Первое свойство без типа, а второе с типом DateTime. После открытия созданного этим кодом файла Excel вы увидите эти два свойства в Панели информации о документе.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Add simple property without any type
workbook.getContentTypeProperties().add("MK31", "Simple Data");

// Add date time property with type
workbook.getContentTypeProperties().add("MK32", "04-Mar-2015", "DateTime");

// Save the workbook
workbook.save(path.join(dataDir, "AddingCustomPropertiesVisible_out.xlsx"));
```

### **Связанная статья**

{{% alert color="primary" %}}

- [Использование пользовательских XML-частей в Aspose.Cells](/cells/ru/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
