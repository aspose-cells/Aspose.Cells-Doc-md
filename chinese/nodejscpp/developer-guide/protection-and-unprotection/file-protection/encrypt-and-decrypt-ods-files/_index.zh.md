---
title: 用 Node.js 和 C++ 加密与解密 ODS 文件
linktitle: 加密和解密ODS文件
type: docs
weight: 10
url: /zh/nodejs-cpp/encrypt-and-decrypt-ods-files/
description: 利用 Aspose.Cells for Node.js via C++ 密码保护和加密 ODS 文件。 
---

{{% alert color="primary" %}}
OpenOffice.org 是一个功能齐全的办公套件，支持密码保护和文件加密。但加密的 ODS 文件只能在提供密码后由 OpenOffice 打开。Excel 不能打开加密的 ODS 文件，可能会出现警告。与其他文件类型不同，ODS 文件的加密选项不适用。 
Aspose.Cells 允许你加密和解密 ODS 文件。解密的 ODS 文件可以在 Excel 和 OpenOffice 中打开。
{{% /alert %}}

## **在OpenOffice Calc中加密**
1. 选择**另存为**，并点击**带密码保存**框。
1. 点击**保存**按钮。
1. 在打开密码窗口中的**输入打开文件的密码**和**确认密码**字段中键入所需的密码。 
1. 点击**确定**按钮以保存文件。

## **用 Aspose.Cells for Node.js via C++ 加密 ODS 文件**
要加密 ODS 文件，加载文件并在保存前将 [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) 设置为实际密码。输出的加密 ODS 文件只能在 OpenOffice 中打开。

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

## **用 Aspose.Cells for Node.js via C++ 解密 ODS 文件**
要解密ODS文件，请在[**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--)中提供密码后加载文件。一旦加载完成，将[**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--)字符串设置为空。

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
