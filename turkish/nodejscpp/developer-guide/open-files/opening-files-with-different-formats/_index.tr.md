---
title: Node.js üzerinden C++ ile Farklı Formatlardaki Dosyaları Açma
linktitle: Farklı Formatlardaki Dosyaları Açma
type: docs
weight: 30
url: /tr/nodejs-cpp/opening-files-with-different-formats/
description: Aspose.Cells for Node.js via C++ API, XLSX, HTML, CSV, ODS, TSV, SXC, FODS vb. gibi farklı formatlarda dosyaları açıp okumanıza izin verir.
keywords: xlsx dosyalarını aç, html dosyalarını aç, fods dosyalarını oku, ods dosyalarını oku, sxc dosyalarını oku, csv dosyalarını aç, Tab Delimited, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak, farklı formatlarda dosyalar açabilirsiniz. **Aspose.Cells**, Microsoft Excel çalışma sayfaları (XLS, XLSX, XLSM, XLSB), SpreadsheetML, Virgülle Ayrılmış Değerler (CSV), Sekme ile Ayrılmış veya Sekme ile Ayrılmış Değerler (TSV) dosyaları vb. gibi çeşitli dosya biçimlerini açabilir.

Desteklenen tüm dosya formatlarını öğrenmeniz gerekiyorsa lütfen aşağıdaki sayfalara bakın:
[Desteklenen Dosya Formatları](https://docs.aspose.com/cells/nodejs-cpp/supported-file-formats/)

{{% /alert %}}

## **Farklı Biçimlerde Dosyaları Açma**

Aspose.Cells, Elektronik Tablo Dosyalarını Elektronik Tablo Dili (SpreadsheetML), Virgülle Ayrılmış Değerler (CSV), Sekmeyle Ayrılmış veya Sekmeyle Ayrılmış Değerler (TSV), ODS dosyaları gibi farklı biçimlerde açmak için geliştiricilere olanak tanır. Bu tür dosyaları açmak için geliştiriciler, farklı Microsoft Excel sürümlerini açarken kullandıkları metodolojiyi kullanabilirler.

### **Elektronik Tablo Dili (SpreadsheetML) Dosyalarını Açma**

SpreadsheetML dosyaları, biçimlendirme, formüller ve vb. dahil olmak üzere tüm bilgilerle birlikte elektronik tablo dosyalarının XML temsilleridir. Microsoft Excel XP'den itibaren, Microsoft Excel'e eklenen XML dışa aktarma seçeneği, elektronik tablolarınızı SpreadsheetML dosyalarına dışa aktarır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening SpreadsheetML Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions3 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.SpreadsheetML);

// Create a Workbook object and opening the file from its path
const wbSpreadSheetML = new AsposeCells.Workbook(path.join(dataDir, "Book3.xml"), loadOptions3);
console.log("SpreadSheetML file opened successfully!");
```

### **HTML Dosyalarını Açma**

Aspose.Cells, bir HTML dosyasını bir Çalışma Kitabı nesnesine açmanıza izin verir. HTML dosyası Microsoft Excel odaklı olmalı, yani MS-Excel tarafından açılabilmelidir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.html");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath, loadOptions);

// Save the MHT file
wb.save(`${filePath}output.xlsx`);
```

### **CSV Dosyalarını Açma**

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerlerin virgüllerle ayrıldığı kayıtlar içerir. Veriler, her sütunun virgül karakteriyle ayrıldığı ve çift tırnak karakteriyle alıntılanmış bir tabloda saklanır. Bir alan değeri çift tırnak karakteri içeriyorsa, çift tırnak karakteriyle kaçış yapılır. Ayrıca, Excel'i kullanarak elektronik tablo verilerinizi CSV'ye dışa aktarabilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book_CSV.csv");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions4 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);

// Create a Workbook object and opening the file from its path
const wbCSV = new AsposeCells.Workbook(filePath, loadOptions4);
console.log("CSV file opened successfully!");
```

#### **CSV Dosyalarını Açma ve Geçersiz Karakterleri Değiştirme**

Excel'de, özel karakterlerle dolu bir CSV dosyasını açarken, karakterler otomatik olarak değiştirilir. Aynı işlem, aşağıda gösterilen API ile de yapılır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "[20180220142533][ASPOSE_CELLS_TEST].csv");

const loadOptions = new AsposeCells.TxtLoadOptions();
loadOptions.setSeparator(';');
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));
loadOptions.setCheckExcelRestriction(false);
loadOptions.setConvertNumericData(false);
loadOptions.setConvertDateTimeData(false);

// Load CSV file
const workbook = new AsposeCells.Workbook(filePath, loadOptions);


console.log(workbook.getWorksheets().get(0).getName()); // (20180220142533)(ASPOSE_CELLS_T
console.log(workbook.getWorksheets().get(0).getName().length); // 31
console.log("CSV file opened successfully!");
```

### **Özel Ayraçlı Metin Dosyalarını Açma**

Metin dosyaları biçimlendirme olmadan elektronik tablo verilerini tutmak için kullanılır. Dosya, özelleştirilmiş ayraçlar içerebilen bir tür düz metin dosyasıdır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book11.csv");

// Instantiate Text File's LoadOptions
const txtLoadOptions = new AsposeCells.TxtLoadOptions();

// Specify the separator
txtLoadOptions.setSeparator(",");

// Specify the encoding type
txtLoadOptions.setEncoding(AsposeCells.EncodingType.UTF8);

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath, txtLoadOptions);

// Save file
wb.save(path.join(dataDir, "output.txt"));
```

### **Sekmeyle Ayrılmış Dosyaları Açma**

Sekmeli ayırıcılar ile (Text) dosyalar elektronik tablo verilerini içerir, ancak hiçbir biçimlendirme içermez. Veriler, tablolar ve elektronik tablolar gibi satır ve sütunlar halinde düzenlenmiştir. Temelde, sekmeli ayırıcılar ile dosya, her sütun arasında sekme bulunan düz metin dosyasıdır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1TabDelimited.txt");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(filePath, loadOptions5);
console.log("Tab delimited file opened successfully!");
```

### **Sekmeyle Ayrılmış Değerler (TSV) Dosyalarını Açma**

Sekme ile ayrılmış değerler (TSV) dosyası, biçimlendirme olmadan elektronik tablo verileri içerir. Bu, verilerin satır ve sütunlar halinde düzenlendiği Sekme ile Ayrılmış dosyayla aynıdır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Tsv);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTSVFile.tsv"), loadOptions);

// Using the Sheet 1 in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Accessing a cell using its name
const cell = worksheet.getCells().get("C3");

console.log(`Cell Name: ${cell.getName()} Value: ${cell.getStringValue()}`);
```

### **SXC Dosyalarını Açma**

StarOffice Calc, Microsoft Excel'e benzer ve formüller, grafikler, fonksiyonlar ve makroları destekler. Bu yazılım ile oluşturulan elektronik tablolar SXC uzantısıyla kaydedilir. SXC dosyası ayrıca OpenOffice.org Calc elektronik tablo dosyaları için de kullanılır. Aspose.Cells, SXC dosyalarını okuyabilir; aşağıdaki kod örneğiyle gösterildiği gibi.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Sxc);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleSXC.sxc"), loadOptions);

// Using the Sheet 1 in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Accessing a cell using its name
const cell = worksheet.getCells().get("C3");

console.log(`Cell Name: ${cell.getName()} Value: ${cell.getStringValue()}`);
```

### **FODS Dosyalarını Açma**

FODS dosyası, sıkıştırma olmadan OpenDocument XML olarak kaydedilmiş bir elektronik tablodur. Aspose.Cells, FODS dosyalarını aşağıdaki kod örneğiyle okuyabilir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Fods);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleFods.fods"), loadOptions);

console.log("FODS file opened successfully!");
```

