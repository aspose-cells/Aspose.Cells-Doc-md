---
title: Node.js ve C++ kullanarak Sayfaları kopyalama ve taşıma
linktitle: Çalışsayfa Kopyalama ve Taşıma
type: docs
weight: 10
url: /tr/nodejs-cpp/copying-and-moving-worksheets/
description: Bu makale, örnek kodlar ve Node.js API si ile Excel çalışma kitabı içinde ve arasında çalışma sayfalarını kopyalama ve taşıma işlemlerinin nasıl yapıldığını anlatır.
keywords: İş Sayfasını Kopyala Node.js, İş Sayfasını Taşı Node.js
---

{{% alert color="primary" %}}

Bazen ortak biçimlendirme ve veriye sahip bir dizi çalışma sayfasına ihtiyaç duyarsınız. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfalara sahip bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunun bir yolu var: bir sayfa oluşturduktan sonra onu kopyalayarak.

Aspose.Cells for Node.js via C++, çalışma kitapları arasında veya içinde çalışma sayfalarını kopyalama ve taşımayı destekler. İş sayfası, veriler, biçimlendirme, tablolar, matrisler, grafikler, resimler ve diğer nesnelerle birlikte yüksek hassasiyetle kopyalanır.

{{% /alert %}}

## **Microsoft Excel Kullanarak Sayfaları Taşıma veya Kopyalama**

Microsoft Excel'de çalışma kitapları arasında veya içinde çalışma sayfalarını kopyalama ve taşıma için gereken adımlar aşağıda listelenmiştir.

1. Sayfaları başka bir çalışma kitabına taşımak veya kopyalamak için, sayfaları alacak olan çalışma kitabını açın.
1. Taşımak veya kopyalamak istediğiniz sayfaları içeren çalışma kitabına geçin ve ardından sayfaları seçin.
1. **Düzenle** menüsünde, **Sayfayı Taşı veya Kopyala**'yı tıklayın.
1. **Kitapçığa** iletişim kutusunda, sayfaların alınacağı çalışma kitabını tıklayın.
1. Seçili sayfaları yeni bir kitapçığa taşımak veya kopyalamak için **Yeni Kitap**'a tıklayın.
1. **Önceki sayfa** kutusunda, taşınan veya kopyalanan sayfaların nereden önce ekleneceğini tıklayın.
1. Sayfaları taşımak yerine kopyalamak için **Kopyasını Oluştur** onay kutusunu seçin.

### **Aspose.Cells for Node.js via C++ ile Bir Çalışma Kitabı İçinde İş Sayfalarını Kopyalayın**

Aspose.Cells, mevcut bir çalışma sayfasından veri kopyalamak için kullanılan ve çalışma sayfasının bir kopyasını eklemek için kullanılan [**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#addCopy-number-) adlı aşırı yüklü bir yöntem sağlar. Yöntemin bir sürümü, kaynak çalışma sayfasının endeksini parametre olarak alır. Diğer sürüm, kaynak çalışma sayfasının adını alır.

Aşağıdaki örnek, bir çalışma kitabı içinde mevcut bir çalışma sayfasının nasıl kopyalanacağını gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Open an existing Excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to
// the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Copy data to a new sheet from an existing
// sheet within the Workbook.
sheets.addCopy("Sheet1");

// Save the Excel file.
wb.save(path.join(dataDir, "CopyWithinWorkbook_out.xls"));
```

### **Çalışma Kitapları Arasında Çalışma Sayfalarını Kopyalama**

Aspose.Cells, kaynak iş sayfasından başka bir iş sayfasına veya çalışma kitabı içinde veya arasında veri ve biçimlendirmeyi kopyumak için kullanılan [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-) yöntemi sağlar. Bu yöntem, kaynak iş sayfası nesnesini parametre olarak alır.

Aşağıdaki örnek, bir çalışma kitabından diğer bir çalışma kitabına sayfa kopyalamanın nasıl yapılacağını gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Create a Workbook.
// Open a file into the first book.
const excelWorkbook0 = new AsposeCells.Workbook(inputPath);

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Copy the first sheet of the first book into second book.
excelWorkbook1.getWorksheets().get(0).copy(excelWorkbook0.getWorksheets().get(0));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xls"));
```

Aşağıdaki örnek, bir çalışma kitabından başka bir çalışma kitabına bir çalışma sayfasını kopyalamayı göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook.
const excelWorkbook0 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws0 = excelWorkbook0.getWorksheets().get(0);

// Put some data into header rows (A1:A4)
for (let i = 0; i < 5; i++) {
ws0.getCells().get(i, 0).putValue(`Header Row ${i}`);
}

// Put some detail data (A5:A999)
for (let i = 5; i < 1000; i++) {
ws0.getCells().get(i, 0).putValue(`Detail Row ${i}`);
}

// Define a pagesetup object based on the first worksheet.
const pagesetup = ws0.getPageSetup();

// The first five rows are repeated in each page...
// It can be seen in print preview.
pagesetup.setPrintTitleRows("$1:$5");

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Name the worksheet.
ws1.setName("MySheet");

// Copy data from the first worksheet of the first workbook into the
// first worksheet of the second workbook.
ws1.copy(ws0);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetFromWorkbookToOther_out.xls"));
```

### **Çalışma Kitabı İçinde Sayfaları Taşıma**

Aspose.Cells, aynı elektronik tablo içinde bir iş sayfasını başka bir konuma taşımak için [**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#moveto-number-) yöntemini sağlar. Bu yöntem, hedef iş sayfası indeksini parametre olarak alır.

Aşağıdaki örnek, bir çalışma kitabı içinde bir çalışma sayfasının başka bir konuma nasıl taşınacağını gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "sample1.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get the first worksheet.
const worksheet = sheets.get(0);

// Move the first sheet to the third position in the workbook.
worksheet.moveTo(2);

// Save the excel file.
wb.save(path.join(dataDir, "MoveWorksheet_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
