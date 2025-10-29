---  
title: Укажите версию документа Excel с помощью встроенных свойств документа в Node.js через C++  
linktitle: Указание версии документа Excel с использованием встроенных свойств документа  
type: docs  
weight: 20  
url: /ru/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/  
description: Узнайте, как программно указывать версию документа файла Excel с помощью встроенных свойств документа в Node.js через C++.  
---  

## **Возможные сценарии использования**  

Вы можете изменить **номер версии** файла Excel, щелкнув правой кнопкой мыши по файлу и выбрав Свойства > Детали, затем отредактировав поле **Номер версии**. Пожалуйста, используйте свойство [**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--) для выбора этого программно через API Aspose.Cells.  

## **Указание версии документа Excel с использованием встроенных свойств документа**  

Следующий пример кода создает книгу и изменяет её встроенные свойства документа, включая название, авторов и номер версии. Посмотрите сгенерированный этим кодом [выходной файл Excel](64716811.xlsx) и скриншот, показывающий изменённый номер версии с помощью свойства [**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--).  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "outputSpecifyDocumentVersionOfExcelFile.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access built-in document property collection
const bdpc = wb.getBuiltInDocumentProperties();

// Set the title
bdpc.setTitle("Aspose File Format APIs");

// Set the author
bdpc.setAuthor("Aspose APIs Developers");

// Set the document version
bdpc.setDocumentVersion("Aspose.Cells Version - 18.3");

// Save the workbook in xlsx format
wb.save(filePath, AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
