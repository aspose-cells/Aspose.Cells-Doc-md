---
title: Node.jsを介してC++で異なるMicrosoft Excelバージョンのファイルを開く
linktitle: 異なるMicrosoft Excelバージョンのファイルを開く
type: docs
weight: 20
url: /ja/nodejs-cpp/opening-different-microsoft-excel-versions-files/
description: この記事は、Aspose.Cells for Node.js via C++を使用して異なるExcelバージョンのファイルを開く方法を説明します。
keywords: Node.jsからC++を介して異なるMicrosoft Excelファイルを開く方法、暗号化されたExcelファイルをNode.jsからC++で開くにはどうすればよいですか？
---

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft Excel 95/97 - 2003、SpreadsheetML、Microsoft Excel 2007/2010/2013/2016/2019およびOffice 365のXLSXまたは暗号化されたExcelファイルなど、さまざまなMicrosoft Excelバージョンのファイルを開くことができます。

{{% /alert %}}

## **異なるMicrosoft Excelバージョンのファイルを開く方法**

アプリケーションは通常、Microsoft Excel 95、97、またはMicrosoft Excel 2007/2010/2013/2016/2019やOffice 365で作成されたさまざまなバージョンのMicrosoft Excelファイルを開く必要があります。XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimitedまたはTSV、CSV、ODSなど、多くの形式のいずれかでロードする必要があります。コンストラクターを使用するか、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスの[**getFileFormat()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFileFormat--)タイプ属性を指定して、[**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype)列挙体を使用してフォーマットを指定します。

[**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype)列挙体には多くの事前定義されたファイル形式が含まれており、その一部は以下に示します。

|**ファイルの形式の種類**|**説明**|
| :- | :- |
|Csv|はCSVファイルを表します
|Excel97To2003|はExcel 97-2003ファイルを表します
|Xlsx|はExcel 2007/2010/2013/2016/2019およびOffice 365 XLSXファイルを表します
|Xlsm|はExcel 2007/2010/2013/2016/2019およびOffice 365 XLSMファイルを表します
|Xltx|はExcel 2007/2010/2013/2016/2019およびOffice 365テンプレートXLTXファイルを表します
|Xltm|はExcel 2007/2010/2013/2016/2019およびOffice 365マクロ有効なXLTMファイルを表します
|Xlsb|はExcel 2007/2010/2013/2016/2019およびOffice 365バイナリXLSBファイルを表します
|SpreadsheetML|はSpreadsheetMLファイルを表します
|Tsv|はタブ区切りの値ファイルを表します
|TabDelimited|はタブ区切りのテキストファイルを表します
|Ods|はODSファイルを表します
|Html|はHTMLファイルを表します
|Mhtml|はMHTMLファイルを表します

### **Microsoft Excel 95/5.0ファイルを開く**

Microsoft Excel 95/5.0ファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)を使用し、ロードするテンプレートファイルのために[**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)クラスの関連属性を設定します。この機能のテスト用サンプルファイルは以下のリンクからダウンロードできます：

[Excel95 File](Excel95.xls)

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Excel95_5.0.xls");

// Get the Excel file into stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);

// Create a Workbook object and opening the file from the stream
const wbExcel95 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 95/5.0 workbook opened successfully!");
```

### **Microsoft Excel 97-2003ファイルを開く**

Microsoft Excel 97 - 2003ファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)を使用し、ロードするテンプレートファイルのために[**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)クラスの関連属性を設定します。

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book_Excel97_2003.xls");
// Get the Excel file into stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Excel97To2003);

// Create a Workbook object and opening the file from the stream
const wbExcel97 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 97 - 2003 workbook opened successfully!");
```

### **Microsoft Excel 2007/2010/2013/2016/2019およびOffice 365 XLSXファイルを開く**

Microsoft Excel 2007/2010/2013/2016/2019、またはOffice 365のフォーマット（XLSXまたはXLSB）を開くには、ファイルパスを指定します。さらに、[**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)を使用し、ロードするテンプレートファイルのために[**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)クラスの関連属性/オプションを設定することもできます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening Microsoft Excel 2007 Xlsx Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book_Excel2007.xlsx"), loadOptions);
console.log("Microsoft Excel 2007 - Office365 workbook opened successfully!");
```

### **暗号化されたExcelファイルを開く**

Microsoft Excelで暗号化されたExcelファイルを作成することが可能です。暗号化されたファイルを開くには、[**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)を使用し、その属性とオプション（例：パスワードの設定）をテンプレートファイルに設定します。
この機能のテスト用のサンプルファイルは、以下のリンクからダウンロードできます:

[Encrypted Excel](EncryptedExcel.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "encryptedBook.xls");

// Instantiate LoadOptions
const loadOptions = new AsposeCells.LoadOptions();

// Specify the password
loadOptions.setPassword("1234");

// Create a Workbook object and opening the file from its path
const wbEncrypted = new AsposeCells.Workbook(filePath, loadOptions);
console.log("Encrypted excel file opened successfully!");
```

Aspose.Cells は、パスワードで保護された Microsoft Excel 2007 年、2010 年、2013 年、2016 年、2019 年、Office 365 ファイルを開くこともサポートしています。


{{< app/cells/assistant language="nodejs-cpp" >}}
