---
title: Excelファイルの暗号化にはNode.jsとC++を使用して暗号化とパスワード保護を行う方法を学びます。
linktitle: Excelファイルの暗号化
type: docs
weight: 90
url: /ja/nodejs-cpp/encrypting-excel-files/
description: Aspose.Cells for Node.js via C++を使用した暗号化 
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365)を使用して、スプレッドシートを暗号化およびパスワード保護することができます。暗号化には、暗号化サービスプロバイダー（CSP）によって提供されるアルゴリズムが使用されます。暗号化キーの長さを適切に選択することが重要です。一部のCSPは40ビットまたは56ビットを超える長さをサポートしていません。これは弱い暗号化と見なされます。強力な暗号化には、最小128ビットのキー長が必要です。Microsoft Windowsには、強力な暗号化タイプを提供するCSPも含まれています。例えば、「Microsoft Strong Cryptographic Provider」などです。128ビットの暗号化は、銀行がインターネットバンキングシステムとの接続を暗号化する際に使用するものです。

Aspose.Cellsを使用すると、任意の暗号化タイプでMicrosoft Excelファイルを暗号化およびパスワード保護することができます。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel（ここではMicrosoft Excel 2003）でファイルの暗号化設定を行うには：

1. **ツール**メニューから**オプション**を選択します。ダイアログが表示されます。
1. **セキュリティ**タブを選択します。
1. パスワードを入力し、**詳細**をクリックします。
1. 暗号化方式を選択し、パスワードを確認します。

## **暗号化されたファイルのパスワード検証には、Aspose.Cells for Node.js via C++が{0}メソッドを提供しています。これらのメソッドは、ファイルストリームと検証したいパスワードの2つのパラメータを受け取ります。**

次の例は、Aspose.Cells APIを使用してExcelファイルを暗号化およびパスワード保護する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Specify XOR encryption type.
workbook.setEncryptionOptions(AsposeCells.EncryptionType.XOR, 40);

// Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);

// Password protect the file.
workbook.getSettings().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```

### **修正パスワードを指定するオプション**

次の例は、Aspose.Cells APIを使用して既存のファイルの**修正パスワード**Microsoft Excelオプションを設定する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```

## **暗号化されたファイルのパスワードを確認します**

暗号化されたファイルのパスワードを検証するには、Aspose.Cells for Node.js via C++ が [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) メソッドを提供します。これらのメソッドは、ファイルストリームと検証したいパスワードの2つのパラメータを受け取ります。
以下のコードスニペットは、提供されたパスワードが有効かどうかを確認する[**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-)メソッドの使用を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "EncryptedBook1.xlsx");

// Create a Stream object
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

const isPasswordValid = AsposeCells.FileFormatUtil.verifyPassword(fstream, "1234");

console.log("Password is Valid: " + isPasswordValid);
```

## **Aspose.Cells を使用して ODS ファイルの暗号化/復号化**

Aspose.Cellsは、ODSファイルの暗号化と復号化を可能にします。復号化されたODSファイルはExcelとOpenOfficeの両方で開くことができますが、暗号化されたODSファイルはパスワードを入力しないとOpenOfficeでのみ開くことができ、Excelは開けません。暗号化されたODSファイルは、他のファイル種と異なり、直接開くことができません。暗号化したい場合は、ファイルをロードし、保存前に[**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--)値を実際のパスワードに設定してください。出力された暗号化ODSファイルはOpenOfficeでのみ開くことができます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = RunExamples.Get_SourceDirectory();
// Output directory
const outputDir = RunExamples.Get_OutputDirectory();

// Open an ODS file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleODSFile.ods"));

// Password protect the file
workbook.getSettings().setPassword("1234");

// Save the ODS file
workbook.save(path.join(outputDir, "outputEncryptedODSFile.ods"));
```

ODSファイルを復号化するには、[**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--)によるパスワードの提供でファイルを読み込みます。ファイルが読み込まれたら、[**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--)文字列をnullに設定します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

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
