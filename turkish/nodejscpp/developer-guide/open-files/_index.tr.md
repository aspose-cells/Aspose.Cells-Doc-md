---
title: Excel, OpenOffice, Json, Csv ve Html dosyalarını yükleme ve yönetme
linktitle: Dosyaları Açma
type: docs
weight: 20
url: /tr/nodejs-cpp/loading-saving-and-managing/
description: Aspose.Cells ile, Node.js üzerinden C++ kullanarak Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, Pdf, Jpg, Tiff, Görüntü, Mht ve XPS dosyalarını oluşturmak, açmak ve yönetmek çok basittir.
---

{{% alert color="primary" %}}

Aspose.Cells ile, örneğin verileri almak veya geliştirme sürecini hızlandırmak için tasarımcı şablonu kullanmak gibi, Excel dosyalarını oluşturmak, açmak ve yönetmek çok basittir.

{{% /alert %}}

## **Yeni Bir Çalışma Kitabı Oluşturma**
Aşağıdaki örnek sıfırdan yeni bir çalışma kitabı oluşturur.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const licensePath = path.join(dataDir, "Aspose.Cells.lic");

try {
// Create a License object
const license = new AsposeCells.License();

// Set the license of Aspose.Cells to avoid the evaluation limitations
license.setLicense(licensePath);
} catch (ex) {
console.log(ex.message);
}

// Instantiate a Workbook object that represents Excel file.
const wb = new AsposeCells.Workbook();

// When you create a new workbook, a default "Sheet1" is added to the workbook.
const sheet = wb.getWorksheets().get(0);

// Access the "A1" cell in the sheet.
const cell = sheet.getCells().get("A1");

// Input the "Hello World!" text into the "A1" cell
cell.putValue("Hello World!");

// Save the Excel file.
wb.save(path.join(dataDir, "MyBook_out.xlsx"));
```

## **Bir Dosyayı Açma ve Kaydetme**
Aspose.Cells ile, Excel dosyalarını açmak, kaydetmek ve yönetmek çok basittir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Adding new sheet
const sheet = workbook1.getWorksheets().add("MySheet");
// Setting active sheet
workbook1.getWorksheets().setActiveSheetIndex(1);
// Setting values.
const cells = sheet.getCells();
// Setting text
cells.get("A1").putValue("Hello!");
// Setting number
cells.get("A2").putValue(1000);
// Setting Date Time
const cell = cells.get("A3");
cell.putValue(new Date());
const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);
// Setting formula
cells.get("A4").setFormula("=SUM(A1:A3)");
// Saving the workbook to disk.
workbook1.save(path.join(dataDir, "dest.xlsx"));
```

## **Gelişmiş Konular**
- [Dosyaları Açmanın Farklı Yolları](/cells/tr/nodejs-cpp/different-ways-to-open-files/)
- [Çalışma Kitabını yüklerken Tanımlanmış Adları Filtrele](/cells/tr/nodejs-cpp/filter-defined-names-while-loading-workbook/)
- [Çalışma Kitabını veya Çalışma Sayfasını Yüklerken Nesneleri Filtrele](/cells/tr/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Şablon dosyasından çalışma kitabını yüklerken veri türünü filtreleme](/cells/tr/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Excel Dosyası Yüklenirken Uyarıları Al](/cells/tr/nodejs-cpp/get-warnings-while-loading-excel-file/)
- [Grafikleri Olmadan Kaynak Excel Dosyasını Yükleme](/cells/tr/nodejs-cpp/load-source-excel-file-without-charts/)
- [Bir Çalışma Kitabındaki Belirli Çalışma Sayfalarını Yükleme](/cells/tr/nodejs-cpp/load-specific-worksheets-in-a-workbook/)
- [Belirtilen Yazıcı Kağıdı Boyutuyla Çalışma Kitabı Yükle](/cells/tr/nodejs-cpp/load-workbook-with-specified-printer-paper-size/)
- [Farklı Microsoft Excel Sürümlerini Açma](/cells/tr/nodejs-cpp/opening-different-microsoft-excel-versions-files/)
- [Farklı Biçimlerde Dosyaları Açma](/cells/tr/nodejs-cpp/opening-files-with-different-formats/)
- [Büyük Veri Kümesine Sahip Büyük Dosyalarla Çalışırken Hafıza Kullanımını Optimize Etme](/cells/tr/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Numbers Elektronik Tablosu, Apple Inc. tarafından geliştirildi.](/cells/tr/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Çok uzun sürüyorsa, Duraklatma İzleyiciyi kullanarak dönüşümü veya yüklemeyi durdurun](/cells/tr/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [LightCells API'sını Kullanma](/cells/tr/nodejs-cpp/using-lightcells-api/)
- [CSV'yi JSON'a dönüştür](/cells/tr/nodejs-cpp/convert-csv-to-json/)
- [Excel’i JSON’a dönüştürmek](/cells/tr/nodejs-cpp/convert-excel-to-json/)
- [JSON'ı CSV'ye dönüştür](/cells/tr/nodejs-cpp/convert-json-to-csv/)
- [JSON’u Excel’e dönüştürmek](/cells/tr/nodejs-cpp/convert-json-to-excel/)
- [Excel’i Html’e dönüştürmek](/cells/tr/nodejs-cpp/convert-excel-to-html/)
{{< app/cells/assistant language="nodejs-cpp" >}}
