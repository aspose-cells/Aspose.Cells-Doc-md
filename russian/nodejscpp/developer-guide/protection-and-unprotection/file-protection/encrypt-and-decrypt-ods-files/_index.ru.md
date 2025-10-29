---
title: Шифрование и дешифрование файлов ODS с Node.js через C++
linktitle: Шифрование и дешифрование файлов ODS
type: docs
weight: 10
url: /ru/nodejs-cpp/encrypt-and-decrypt-ods-files/
description: Защита паролем и шифрование файлов ODS с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}
OpenOffice.org — полнофункциональный офисный пакет, который поддерживает защиту паролем и шифрование файлов. Но зашифрованный файл ODS можно открыть только в OpenOffice после ввода пароля. Excel не может открыть зашифрованный файл ODS и может вывести предупреждающие сообщения. Опции шифрования не применимы к файлам ODS, в отличие от других типов файлов. 
 Aspose.Cells позволяет шифровать и дешифровать файлы ODS. Расшифрованные файлы ODS могут быть открыты как в Excel, так и в OpenOffice.
{{% /alert %}}

## **Шифровать с помощью OpenOffice Calc**
1. Выберите **Сохранить как** и установите флажок **Сохранить с паролем**.
1. Нажмите кнопку **Сохранить**.
1. Введите желаемый пароль в поля **Введите пароль для открытия** и **Подтвердите пароль** в окне установки пароля, которое откроется. 
1. Нажмите кнопку **OK**, чтобы сохранить файл.

## **Зашифровать файл ODS с помощью Aspose.Cells for Node.js via C++**
Для шифрования файла ODS загрузите файл и установите значение [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) в фактический пароль перед сохранением. Полученный зашифрованный файл ODS можно открыть только в OpenOffice.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "source");
const outputDir = path.join(__dirname, "output");

// Open an ODS file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleODSFile.ods"));

// Password protect the file
workbook.getSettings().setPassword("1234");

// Save the ODS file
workbook.save(path.join(outputDir, "outputEncryptedODSFile.ods"));
```

## **Расшифровать файл ODS с помощью Aspose.Cells for Node.js via C++**
Для расшифровки файла ODS загрузите файл, указав пароль в [**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--). После загрузки файла установите строку [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) в null.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open an encrypted ODS file
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Ods);

// Set original password
loadOptions.setPassword("1234");

// Load the encrypted ODS file with the appropriate load options
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleEncryptedODSFile.ods"), loadOptions);

// Set the password to null
workbook.getSettings().setPassword(null);

// Save the decrypted ODS file
workbook.save(outputDir + "outputDecryptedODSFile.ods");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
