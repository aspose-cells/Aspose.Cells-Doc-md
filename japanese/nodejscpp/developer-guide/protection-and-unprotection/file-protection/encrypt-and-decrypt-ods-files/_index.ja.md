---
title: Node.js経由のC++を使用してODSファイルを暗号化および復号化する
linktitle: ODSファイルの暗号化と複合化
type: docs
weight: 10
url: /ja/nodejs-cpp/encrypt-and-decrypt-ods-files/
description: Aspose.Cells for Node.js via C++を使用してODSファイルをパスワード保護および暗号化します。 
---

{{% alert color="primary" %}}
OpenOffice.orgは、パスワード保護とファイルの暗号化をサポートするフル機能のオフィススイートです。ただし、暗号化されたODSファイルは、パスワードを提供した後にのみOpenOfficeで開くことができます。Excelは暗号化されたODSファイルを開けず、警告メッセージを表示する場合があります。暗号化オプションは他のファイルタイプとは異なり、ODSファイルには適用されません。 
Aspose.Cellsを使用すれば、ODSファイルの暗号化と復号化が可能です。復号化されたODSファイルはExcelとOpenOfficeの両方で開くことができます。
{{% /alert %}}

## **OpenOffice Calcで暗号化**
1. **名前を付けて保存**を選択し、**パスワードを設定して保存**ボックスをクリックします。
1. **保存**ボタンをクリックします。
1. 開いた「パスワードの設定」ウィンドウの「開くためのパスワードを入力」および「パスワードを確認」フィールドに希望するパスワードを入力します。 
1. ファイルを保存するために **OK** ボタンをクリックします。

## **Aspose.Cells for Node.js via C++を用いてODSファイルを暗号化する**
ODSファイルを暗号化するには、ファイルを読み込み、[**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--)の値を実際のパスワードに設定して保存します。出力される暗号化されたODSファイルはOpenOfficeでのみ開くことができます。

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

## **Aspose.Cells for Node.js via C++を用いてODSファイルを復号化する**
ODSファイルを復号化するには、[**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--)にパスワードを入力してファイルを読み込みます。ファイルが読み込まれたら、[**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--)の文字列をnullに設定してください。

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
