---
title: Управление свойствами документа с помощью Node.js через C++
linktitle: Свойства документа
type: docs
weight: 80
url: /ru/nodejs-cpp/managing-document-properties/
description: Научитесь управлять свойствами документа через API Aspose.Cells for Node.js via C++.
keywords: Как управлять свойствами документа в Node.js через C++, Получить или установить свойства документа с помощью Node.js через C++, Добавить или удалить свойства документа через Node.js через C++, Вставить или удалить свойства документа с помощью Node.js через C++, Как получить доступ к свойствам документа с помощью API Aspose.Cells for Node.js via C++.
---


## **Введение**

Microsoft Excel предоставляет возможность добавлять свойства к файлам электронных таблиц. Эти свойства документов предоставляют полезную информацию и делятся на 2 категории, как описано ниже.

- Системные (встроенные) свойства: Встроенные свойства содержат общую информацию о документе, такую как название документа, имя автора, статистику документа и т. д.
- Пользовательские (пользовательские) свойства: Пользовательские свойства, определенные конечным пользователем в виде пары имя-значение.

{{% alert color="primary" %}}

Самый важный момент, который нужно знать о встроенных и пользовательских свойствах, заключается в том, что встроенные свойства можно получить доступ, изменить, но не создать или удалить. Однако пользовательские свойства можно создавать и управлять ими.

{{% /alert %}}

## **Как управлять свойствами документа с помощью Microsoft Excel**

Microsoft Excel позволяет управлять свойствами документа Excel в WYSIWYG-режиме. Пожалуйста, выполните следующие шаги, чтобы открыть диалог **Свойства** в Excel 2016.

1. В меню **Файл** выберите **Сведения**.

|**Выбор меню Сведения**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. Нажмите на заголовок **Свойства** и выберите "Расширенные свойства".

|**Нажмите на выбор расширенных свойств**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Управляйте свойствами документа файла.

|**Диалоговое окно свойств**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
В диалоговом окне свойств есть различные вкладки, такие как Общее, Резюме, Статистика, Содержание и Пользовательские. Каждая вкладка помогает настраивать различные виды информации, связанные с файлом. Вкладка Пользовательские используется для управления пользовательскими свойствами.

## **Как работать со свойствами документа с помощью Aspose.Cells**

Разработчики могут динамически управлять свойствами документа с помощью API Aspose.Cells. Эта функция помогает разработчикам сохранять полезную информацию вместе с файлом, такую как время получения файла, обработки, отметки времени и т. д.

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ напрямую записывает информацию о API и номере версии в выходные документы. Например, при преобразовании документа в PDF, Aspose.Cells for Node.js via C++ заполняет поле **Приложение** значением 'Aspose.Cells', а поле **Производитель PDF** — значением, например, 'Aspose.Cells v17.9'.

Обратите внимание, что вы не можете инструктировать Aspose.Cells for Node.js via C++ изменять или удалять эту информацию из выходных документов.

{{% /alert %}}

### **Как получить доступ к свойствам документа**

API Aspose.Cells поддерживают оба типа свойств документа: встроенные и пользовательские. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) в Aspose.Cells представляет файл Excel и, как и файл Excel, класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) может содержать несколько листов, каждый из которых представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet), а коллекция листов — классом [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection).

Используйте [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) для получения доступа к свойствам файла, как описано ниже.

- Чтобы получить доступ к встроенным свойствам документа, используйте [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--).
- Чтобы получить доступ к настраиваемым свойствам документа, используйте [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--).

Иметь тож экземпляры [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--) и [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--) возвращают экземпляр [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/). Эта коллекция содержит [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) объектов, каждый из которых представляет отдельное встроенное или пользовательское свойство документа.

Ответ на вопрос, как получить свойство, зависит от требований приложения: можно использовать индекс или имя свойства из [**DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/), как показано в примере ниже.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property by using the property name
const customProperty1 = customProperties.get("ContentTypeId");
console.log(`${customProperty1.getName()} ${customProperty1.getValue()}`);

// Accessing the same custom document property by using the property index
const customProperty2 = customProperties.get(0);
console.log(`${customProperty2.getName()} ${customProperty2.getValue()}`);
```

Класс [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) позволяет получать имя, значение и тип свойства документа:

- Чтобы получить имя свойства, используйте [**DocumentProperty.getName()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getName--).
- Для получения значения свойства используйте [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--) возвращает значение в виде объекта.
- Для получения типа свойства используйте [**DocumentProperty.getType()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getType--). Это возвращает одно из значений перечисления [**PropertyType**](https://reference.aspose.com/cells/nodejs-cpp/propertytype/). После определения типа свойства используйте один из методов **DocumentProperty.ToXXX** для получения значения соответствующего типа вместо [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). Методы **DocumentProperty.ToXXX** описаны в таблице ниже.

{{% alert color="primary" %}}

Класс [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) также предоставляет набор методов, возвращающих значения других типов данных.

{{% /alert %}}

|**Имя участника**|**Описание**|**Метод ToXXX**|
| :- | :- | :- |
|Boolean|Тип данных свойства - Логический|ToBool|
|Date|Тип данных свойства - Дата и время. Обратите внимание, что Microsoft Excel сохраняет только <br>часть даты, не сохраняется время в настраиваемом свойстве этого типа|ToDateTime|
|Float|Тип данных свойства - Число двойной точности|ToDouble|
|Number|Тип данных свойства - Int32|ToInt|
|String|Тип данных свойства — string|ToString|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property
const customProperty1 = customProperties.get(0);

// Storing the value of the document property as an object
const objectValue = customProperty1.getValue();

// Accessing a custom document property
const customProperty2 = customProperties.get(1);

// Checking the type of the document property and then storing the value of the
// document property according to that type
if (customProperty2.getType() === AsposeCells.PropertyType.String) {
const value = customProperty2.getValue().toString();
console.log(`${customProperty2.getName()} : ${value}`);
}
```

### **Как добавить или удалить пользовательские свойства документа**

Как мы уже описывали ранее в начале этой темы, разработчики не могут добавлять или удалять встроенные свойства, потому что эти свойства определены системой, но возможно добавить или удалить пользовательские свойства, потому что они определены пользователем.

### **Как добавить пользовательские свойства**

API Aspose.Cells предоставили метод [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) для класса [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/) для добавления пользовательских свойств в коллекцию. Метод [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) добавляет свойство в файл Excel и возвращает ссылку на новое свойство документа в виде объекта [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Adding a custom document property to the Excel file
customProperties.add("Publisher", "Aspose");

// Saving resultant spreadsheet
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **Как настроить пользовательское свойство 'Ссылка на содержимое'**

Чтобы создать пользовательское свойство, связанное с содержанием выбранного диапазона, вызовите метод [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-) и передайте название свойства и источник. Проверить, настроено ли свойство как связанное с содержимым, можно с помощью свойства [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#isLinkedToContent--). Также возможно получить исходный диапазон с помощью свойства [**getSource()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getSource--) класса [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/).

Мы используем простой шаблон файла Microsoft Excel в примере. Рабочая книга содержит определенный именованный диапазон с меткой '**MyRange**', который ссылается на значение ячейки.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate an object of Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getWorksheets().getCustomDocumentProperties();

// Add link to content.
customProperties.addLinkToContent("Owner", "MyRange");

// Accessing the custom document property by using the property name
const customProperty1 = customProperties.get("Owner");

// Check whether the property is linked to content
const isLinkedToContent = customProperty1.isLinkedToContent();

// Get the source for the property
const source = customProperty1.getSource();

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **Как удалить пользовательские свойства**

Чтобы удалить пользовательские свойства через Aspose.Cells, вызовите метод [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/#remove-string-) и передайте название свойства документа, которое нужно удалить.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Removing a custom document property
customProperties.remove("Publisher");

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

## **Продвинутые темы**
- [Добавление пользовательских свойств, видимых в панели информации о документе](/cells/ru/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа](/cells/ru/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Указание версии документа Excel с использованием встроенных свойств документа](/cells/ru/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Указание языка файла Excel с использованием встроенных свойств документа](/cells/ru/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
