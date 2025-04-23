---  
title: Node.js ve C++ kullanarak Bir Çalışma Sayfasında En Büyük Aralığı Alma  
linktitle: Çalışma sayfasındaki Maksimum Aralığı Al  
type: docs  
weight: 360  
url: /tr/nodejs-cpp/get-max-range-in-a-worksheet/  
description: Bu makale, Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarının maksimum aralık, maksimum veri aralığı ve maksimum görüntüleme aralığını nasıl alacağınızı açıklar.  
---  

{{% alert color="primary" %}}  

Çalışma sayfasından veri okurken, maksimum alanı bilmemiz gerekmektedir.  

Tüm verileri bir çalışma sayfasından kopyalarken, maksimum alanı bilmemiz gerekmektedir.  

Belirli bir alanın HTML ve PDF'ye dışa aktarılırken, maksimum alanı bilmemiz gerekir.  

Aspose.Cells for Node.js via C++, bir çalışma sayfasında maksimum aralığı bulmak için farklı yollar içerir.  

{{% /alert %}}  

## **Maksimum aralığı almak**  
Aspose.Cells'te, [**row**](https://reference.aspose.com/cells/nodejs-cpp/row/) ve [**column**](https://reference.aspose.com/cells/nodejs-cpp/column/) nesneleri başlatılmışsa, bunlar boş satır veya sütunlar olmasa bile maksimum alan olarak sayılır.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxRow();
let maxColumn = sheet.getCells().getMaxColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxRow();
maxColumn = sheet.getCells().getMaxColumn();
// The range is updated to A1:B10.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **Maksimum veri aralığını almak**  
Çoğu durumda, yalnızca tüm verileri içeren tüm aralıkları elde etmemiz yeterlidir, aralık dışındaki boş hücreler biçimlendirilse bile.  
Ve şekiller, tablolar ve pivot tablolar ile ilgili ayarlar göz ardı edilecektir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxDataRow();
let maxColumn = sheet.getCells().getMaxDataColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxDataRow();
maxColumn = sheet.getCells().getMaxDataColumn();
// The range is still A1:B3.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **Maksimum görüntü aralığını almak**  
Çalışma sayfasındaki tüm verileri HTML, PDF veya görüntülere dışa aktardığımızda, veri, stiller, grafikler, tablolar ve özet tablolar da dahil olmak üzere tüm görünür nesneleri içeren bir alan elde etmemiz gerekmektedir.  
Aşağıdaki kodlar, maksimum görüntüleme alanını HTML'ye nasıl aktaracağını gösterir:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Gets the max display range.
const range = worksheets.get(0).getCells().getMaxDisplayRange();

// Save the range to html
const saveOptions = new AsposeCells.HtmlSaveOptions();
saveOptions.setExportActiveWorksheetOnly(true);
saveOptions.setExportArea(AsposeCells.CellArea.createCellArea(range.getFirstRow(), range.getFirstColumn(), range.getFirstRow() + range.getRowCount() - 1, range.getFirstColumn() + range.getColumnCount() - 1));

// Save the range.
workbook.save("html.html", saveOptions);
```  

İşte [kaynak excel dosyası](Book1.xlsx).  

