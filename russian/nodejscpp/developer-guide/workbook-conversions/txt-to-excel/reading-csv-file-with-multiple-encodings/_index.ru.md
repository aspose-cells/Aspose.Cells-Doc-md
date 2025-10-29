---
title: Чтение CSV файла с различными кодировками с помощью Node.js через C++
linktitle: Чтение CSV файла с несколькими кодировками
type: docs
weight: 200
url: /ru/nodejs-cpp/reading-csv-file-with-multiple-encodings/
description: Узнайте, как правильно читать CSV файлы с несколькими кодировками с помощью Aspose.Cells for Node.js via C++.
---


{{% alert color="primary" %}}

 Иногда ваши CSV-файлы содержат несколько кодировок (Unicode, ANSI, UTF8, UTF7 и т. д.). Aspose.Cells позволяет загружать такие CSV-файлы и преобразовывать их в другие форматы, например, PDF или XLSX.

{{% /alert %}}

Для этого используйте свойство [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--), установив его в значение **true** для правильной загрузки CSV с несколькими кодировками.

На следующем скриншоте показан пример CSV-файла, который содержит две строки. Первая строка в кодировке **ANSI**, а вторая строка в кодировке **Unicode**.

|**Входной файл**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Следующий снимок показывает файл XLSX, преобразованный из вышеуказанного CSV-файла без установки свойства [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) в **true**. Как видите, Unicode-текст был преобразован неправильно.

|**Файл вывода 1: не предусмотрены множественные кодировки**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

 Следующий скриншот показывает XLSX-файл, преобразованный из указанного CSV-файла после установки свойства [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) в **true**. Теперь Unicode-текст отображается правильно.

|**Файл вывода 2: IsMultiEncoded установлен в true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Ниже приведен образец кода, преобразующий вышеуказанный файл CSV в формат XLSX правильно.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "MultiEncoded.csv");

// Set Multi Encoded Property to True
const options = new AsposeCells.TxtLoadOptions();
options.setIsMultiEncoded(true);

// Load the CSV file into Workbook
const workbook = new AsposeCells.Workbook(filePath, options);

// Save it in XLSX format
workbook.save(path.join(dataDir, "MultiEncoded.csv.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## Связанные статьи

- [Открытие файлов CSV](/cells/ru/nodejs-cpp/opening-files-with-different-formats/#opening-csv-files)
{{< app/cells/assistant language="nodejs-cpp" >}}
