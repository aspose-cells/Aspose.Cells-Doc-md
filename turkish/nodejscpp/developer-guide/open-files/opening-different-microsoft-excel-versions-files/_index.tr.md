---
title: Node.js ve C++ kullanarak Farklı Microsoft Excel Sürümleri Dosyasını Açın
linktitle: Farklı Microsoft Excel Sürümleri Dosyalarını Açın
type: docs
weight: 20
url: /tr/nodejs-cpp/opening-different-microsoft-excel-versions-files/
description: Bu makale, farklı Excel sürümleri kullanan dosyaları nasıl açacağınızı açıklar, Aspose.Cells for Node.js via C++ kullanarak.
keywords: Node.js ile C++ kullanarak Farklı Microsoft Excel dosyasını açma, Şifrelenmiş Excel Dosyalarını Node.js ve C++ kullanarak nasıl açarım
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel 95/97 - 2003, SpreadsheetML, Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX veya Şifreli Excel Dosyaları gibi çeşitli farklı Microsoft Excel Sürümlerini açabilir.

{{% /alert %}}

## **Farklı Microsoft Excel Sürümleri Dosyalarını Açma**

Bir uygulama genellikle, farklı sürümlerde oluşturulan Microsoft Excel dosyalarını açabilmelidir. Örneğin, Microsoft Excel 95, 97 veya Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365. Bir dosyayı, XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited veya TSV, CSV, ODS ve diğer formatlarda yüklemeniz gerekebilir. Yükleyiciyi kullanın veya [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının [**getFileFormat()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFileFormat--) tip özniteliğini belirterek formatı [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype) enumuyla belirtin.

[**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype) enumu, aşağıda verilen bazı önceden tanımlanmış dosya formatlarını içerir.

|**Dosya Biçimi Türleri**|**Açıklama**|
| :- | :- |
|Csv|CSV dosyasını temsil eder|
|Excel97To2003|Excel 97 - 2003 dosyasını temsil eder|
|Xlsx|Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX dosyasını temsil eder|
|Xlsm|Excel 2007/2010/2013/2016/2019 ve Office 365 XLSM dosyasını temsil eder|
|Xltx|Excel 2007/2010/2013/2016/2019 ve Office 365 şablonu XLTX dosyasını temsil eder|
|Xltm|Excel 2007/2010/2013/2016/2019 ve Office 365 makro etkin XLTM dosyasını temsil eder|
|Xlsb|Excel 2007/2010/2013/2016/2019 ve Office 365 binary XLSB dosyasını temsil eder|
|SpreadsheetML|SpreadsheetML dosyasını temsil eder|
|Tsv|TSV dosyasını temsil eder|
|TabDelimited|Tab Delimited metin dosyasını temsil eder|
|Ods|ODS dosyasını temsil eder|
|Html|HTML dosyasını temsil eder|
|Mhtml|MHTML dosyasını temsil eder|

### **Microsoft Excel 95/5.0 Dosyalarını Aç**

Bir Microsoft Excel 95/5.0 dosyasını açmak için [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) kullanın ve yüklenmek üzere şablon dosyası için [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) sınıfının ilgili özniteliğini ayarlayın. Bu özelliği test etmek için örnek bir dosya aşağıdaki bağlantıdan indirilebilir:

[Excel95 Dosyası](Excel95.xls)

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

### **Microsoft Excel 97 - 2003 Dosyalarını Aç**

Bir Microsoft Excel 97 - 2003 dosyasını açmak için [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) kullanın ve yüklenmek üzere şablon dosyası için [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) sınıfının ilgili özniteliğini ayarlayın.

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

### **Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 XLSX Dosyalarını Aç**

XLSX veya XLSB formatında, yani Microsoft Excel 2007/2010/2013/2016/2019 ve Office 365 formatında bir dosya açmak için dosya yolunu belirtin. Ayrıca [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) kullanabilir ve yüklenmek üzere şablon dosyası için [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) sınıfının ilgili özniteliğini/ayrıcalıklarını ayarlayabilirsiniz.

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

### **Şifreli Excel Dosyalarını Aç**

Microsoft Excel kullanarak şifrelenmiş Excel dosyaları oluşturmak mümkündür. Şifrelenmiş bir dosyayı açmak için [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) kullanın ve şablon dosyası için özniteliklerini ve seçeneklerini (örneğin, bir şifre verin) ayarlayın.
Bu özelliği test etmek için bir örnek dosya aşağıdaki bağlantıdan indirilebilir:

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

Aspose.Cells ayrıca şifre korumalı Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 dosyalarını açmayı destekler.


