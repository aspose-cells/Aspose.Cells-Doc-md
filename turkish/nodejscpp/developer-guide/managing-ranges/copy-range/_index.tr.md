---
title: Node.js ile C++ kullanarak Excel Aralıklarını Kopyalama
linktitle: Kopya Aralıkları
type: docs
weight: 105
url: /tr/nodejs-cpp/copy-ranges-of-Excel/
---

## **Giriş**

Excel'de bir aralığı seçebilir, ardından bu aralığı belirli seçeneklerle aynı çalışma sayfasına, diğer çalışma sayfalarına veya diğer dosyalara yapıştırabilirsiniz.

## **Aspose.Cells for Node.js via C++ kullanarak Aralık Kopyalama**

Aspose.Cells for Node.js via C++, [Range.copy(Range, PasteOptions)](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-pasteoptions-) methodu ile bazı aşırı yükleme sağlar ve aralığı kopyalar. Ayrıca, [Range.copyStyle(Range)](https://reference.aspose.com/cells/nodejs-cpp/range/#copyStyle-range-) sadece aralığın stilini kopyalar; [Range.copyData(Range)](https://reference.aspose.com/cells/nodejs-cpp/range/#copyData-range-) sadece aralıktaki değeri kopyalar.

## **Aralık Kopyalama**

İki aralık oluşturulur: kaynak aralık ve hedef aralık, sonra `Range.copy` yöntemi ile kaynak aralık hedef aralığa kopyalanır.

Aşağıdaki kodu görün:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
let worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
let worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
let sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue(123);

// Create target range of cells.
let targetRange = worksheet.getCells().createRange("B1", "B2");

// Copy source range to target range in the same worksheet 
targetRange.copy(sourceRange);

// Create target range of cells.
workbook.getWorksheets().add();
worksheet = workbook.getWorksheets().get(1);

targetRange = worksheet.getCells().createRange("A1", "A2");
// Copy source range to target range in another worksheet 
targetRange.copy(sourceRange);

// Copy to another workbook
const anotherWorkbook = new AsposeCells.Workbook();

worksheet = workbook.getWorksheets().get(0);

targetRange = worksheet.getCells().createRange("A1", "A2");
// Copy source range to target range in another workbook 
targetRange.copy(sourceRange);
```

## **Seçeneklerle Aralık Yapıştırma**

Aspose.Cells for Node.js via C++, belirli tipe sahip yapıştırma ile aralık yapıştırmayı destekler.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into
// A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue(123);

// Create target range of cells.
const targetRange = worksheet.getCells().createRange("B1", "B2");

// Init paste options.
const options = new AsposeCells.PasteOptions();
// Set paste type.
options.setPasteType(AsposeCells.PasteType.ValuesAndFormats);
options.setSkipBlanks(true);
// Copy source range to target range
targetRange.copy(sourceRange, options);
```

## **Yalnızca Aralık Verilerini Kopyalama**

Ayrıca, aşağıdaki kodda gösterildiği gibi, `Range.copyData` yöntemi ile veriyi kopyalayabilirsiniz:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = worksheets.get(0);

// Create a range of cells.
const sourceRange = worksheet.getCells().createRange("A1", "A2");

// Input some data with some formattings into
// A few cells in the range.
sourceRange.get(0, 0).setValue("Test");
sourceRange.get(1, 0).setValue(123);

// Create target range of cells.
const targetRange = worksheet.getCells().createRange("B1", "B2");

// Copy the data of source range to target range
targetRange.copyData(sourceRange);
```

## **Gelişmiş Konular**
- [Kaynak Aralığın Satır Yüksekliklerini Hedef Aralığa Kopyalama](/cells/tr/nodejs-cpp/copy-row-heights-of-source-range-to-destination-range/)

{{< app/cells/assistant language="nodejs-cpp" >}}
