---  
title: Json с Node.js через C++  
linktitle: Json  
type: docs  
weight: 300  
url: /ru/nodejs-cpp/convert-workbook-to-json/  
description: Узнайте, как преобразовать рабочую книгу Excel в JSON с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
API Aspose.Cells поддерживает преобразование книги в Json (JavaScript Object Notation).  
{{% /alert %}}  

## **Конвертировать книгу Excel в JSON**  

API Aspose.Cells поддерживает преобразование таблиц в формат JSON. Для экспорта рабочей книги в JSON передайте [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) в качестве второго параметра метода [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-). Также можно использовать класс [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions) для задания дополнительных настроек при экспорте рабочего листа в JSON.  

Следующий пример демонстрирует экспорт активного листа в JSON с использованием члена перечисления [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/#json). Проверьте код преобразования [исходного файла](book1.xlsx) в [выходной Json](book1.Json), сгенерированный кодом.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```  

## **Продвинутые темы**  
- [Преобразовать CSV в JSON](/cells/ru/nodejs-cpp/convert-csv-to-json/)  
- [Преобразовать Excel в JSON](/cells/ru/nodejs-cpp/convert-excel-to-json/)  
- [Преобразовать JSON в CSV](/cells/ru/nodejs-cpp/convert-json-to-csv/)  
- [Преобразовать JSON в Excel](/cells/ru/nodejs-cpp/convert-json-to-excel/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
