---
title: Укажите язык файла Excel с помощью встроенных свойств документа в Node.js через C++
linktitle: Указание языка документа Excel с использованием встроенных свойств документа
type: docs
weight: 30
url: /ru/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **Возможные сценарии использования**

Вы можете изменить язык файла Excel, щелкнув по файлу правой кнопкой мыши и выбрав Свойства > Детали, затем отредактировав поле Язык. Пожалуйста, используйте свойство [**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--) для изменения программным путём через API Aspose.Cells for Node.js via C++.

## **Указание языка файла Excel с использованием встроенных свойств документа**

Следующий пример кода создает книгу и изменяет её встроенное свойство документа с именем язык. Посмотрите сгенерированный этим кодом [выходной файл Excel](64716891.xlsx) и скриншот, показывающий изменённое поле Язык с помощью свойства [**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--).

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object.
const wb = new AsposeCells.Workbook();

// Access built-in document property collection.
const bdpc = wb.getBuiltInDocumentProperties();

// Set the language of the Excel file.
bdpc.setLanguage("German, French");

// Save the workbook in xlsx format.
wb.save(path.join(outputDir, "outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
