---  
title: Node.js kullanarak CSV, TSV ve TXT yi Excel e dönüştürün  
linktitle: CSV, TSV ve Txt yi Excel e dönüştür  
type: docs  
weight: 30  
url: /tr/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/  
---  

{{% alert color="primary" %}}  
Aspose.Cells kullanarak, CSV dosyalarını Excel, OpenOffice, PDF, JSON ve birçok başka formata dönüştürebilirsiniz.  
{{% /alert %}}  

## **CSV Dosyalarını Açma**  

Virgülle Ayrılmış Değerler (CSV) dosyaları, değerlerin virgülle ayrıldığı kayıtları içerir. Veri, her sütunun virgül karakteriyle ayrıldığı ve çift tırnak karakteriyle alıntılanmış bir tablo olarak saklanır. Bir alan değeri çift tırnak karakteri içeriyorsa, çift tırnak karakteriyle kaçış yapılır. Elektronik tablo verilerini CSV'ye aktarmak için Microsoft Excel'i de kullanabilirsiniz.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions4 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);
// Create a Workbook object and opening the file from its path
const wbCSV = new AsposeCells.Workbook(path.join(dataDir, "Book_CSV.csv"), loadOptions4);
console.log("CSV file opened successfully!");
```  

## **CSV Dosyalarını Açma ve Geçersiz Karakterleri Değiştirme**  

Excel'de, özel karakterlerle dolu bir CSV dosyasını açarken, karakterler otomatik olarak değiştirilir. Aynı işlem, aşağıda gösterilen API ile de yapılır.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "[20180220142533][ASPOSE_CELLS_TEST].csv");

const options = new AsposeCells.TxtLoadOptions();
options.setSeparator(",");
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));
options.setCheckExcelRestriction(false);
options.setConvertNumericData(false);
options.setConvertDateTimeData(false);
// Load CSV file
const workbook = new AsposeCells.Workbook(filePath, options);

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
// Opening Tab Delimited Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(path.join(dataDir, "Book1TabDelimited.txt"), loadOptions5);
console.log("Tab delimited file opened successfully!");
```  

### **Sekmeyle Ayrılmış Değerler (TSV) Dosyalarını Açma**  

Sekmeli ayırma değerleri (TSV) dosyaları, elektronik tablo verilerini içerir ancak hiçbir biçimlendirme içermez. Bu, Tab Delimited dosya ile aynıdır ve veriler satır ve sütunlar halinde düzenlenir.  

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

console.log("Cell Name: " + cell.getName() + " Value: " + cell.getStringValue());
```  

## **Gelişmiş Konular**  
- [Formülleri Yükle veya İçe Aktar CSV Dosyası](/cells/tr/nodejs-cpp/load-or-import-csv-file-with-formulas/)  
- [Çeşitli Kodlamalarla CSV Dosyası Okuma](/cells/tr/nodejs-cpp/reading-csv-file-with-multiple-encodings/)  


