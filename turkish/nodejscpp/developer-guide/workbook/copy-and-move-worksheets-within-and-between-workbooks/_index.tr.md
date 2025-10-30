---
title: Node.js ve C++ kullanarak Çalışma Kitapları İçinde ve Arasında Sayfaları Kopyalayın ve Taşıyın
linktitle: Çalışma Kitapları Arasında ve İçinde Çalışma Sayfalarını Kopyalayın ve Taşıyın
type: docs
weight: 80
url: /tr/nodejs-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Aspose.Cells for Node.js via C++ kullanarak çalışma kitaplarınızda sayfaları nasıl kopyalayacağınızı ve taşıyacağınızı öğrenin. Çalışma kitabı yapınızı verimli bir şekilde yönetin.
---

{{% alert color="primary" %}}

Bazen, ortak biçimlendirme ve veri girişi gerektiren sayısız çalışma sayfasına ihtiyacınız olabilir. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıklarını, satır başlıklarını ve formülleri içeren sayfaları olan bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunu yapmanın bir yolu vardır: bir sayfa oluşturarak ve ardından bunu üç kez kopyalayarak.

Aspose.Cells for Node.js via C++, çalışma kitapları içinde veya arasında sayfaların kopyalanmasını veya taşınmasını destekler. Veri, biçimlendirme, tablolar, matrisler, grafikler, resimler ve diğer nesneler dahil olmak üzere sayfalar en yüksek hassasiyetle kopyalanır.

{{% /alert %}}

## **Çalışma Sayfalarını Kopyalama ve Taşıma**

### **Bir Çalışma Sayfasını Bir Çalışma Kitabı İçinde Kopyalama**

Tüm örnekler için ilk adımlar aynıdır.

1. Microsoft Excel'de bazı veriler içeren iki çalış kitabı oluşturun. Bu örneğin amaçları için, Microsoft Excel'de iki yeni çalışma kitabı oluşturduk ve çalışma sayfalarına bazı veriler girdik.

- İlkÇalışmaKitabı.xlsx (3 çalışsayfası).
- İkinciÇalışmaKitabı.xlsx (1 çalışsayfası).

1. Aspose.Cells'i indirin ve kurun:
   1. [Aspose.Cells for Node.js via C++'ü İndiriniz](https://downloads.aspose.com/cells/nodejs-cpp).
   1. Geliştirme bilgisayarınıza kurun.
      Tüm [Aspose](http://www.aspose.com/) bileşenleri yüklendiğinde değerlendirme modunda çalışır. Değerlendirme modunun bir zaman limiti yoktur ve yalnızca üretilen belgelere filigran enjekte eder.
1. Bir proje oluşturun:
   1. Geliştirme ortamınızı başlatın.
   1. Yeni bir konsol uygulaması oluşturun.
1. Referanslar ekleyin:
   1. Projeye Aspose.Cells'e bir başvuru ekleyin.
      Örneğin, ...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dll referansı ekleyin.
1. Bir çalışma kitabı içindeki çalışsayfayı kopyalama
   İlk örnek, İlkÇalışmaKitabı.xlsx içindeki ilk çalışsayfayı (Kopya) kopyalar.

Kod çalıştırıldığında, Kopya adlı çalışsayfa, İlkÇalışmaKitabı.xlsx içinde Last Sheet adıyla kopyalanır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open a file into the first book.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "FirstWorkbook.xlsx"));

// Copy the first sheet of the first book within the workbook
excelWorkbook1.getWorksheets().get(2).copy(excelWorkbook1.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "FirstWorkbookCopied_out.xlsx"));
```

### **Bir Çalışma Kitabı içinde bir Çalışsayfayı Taşıma**

Aşağıdaki kod, bir çalışma kitabı içindeki bir çalışsayfayı bir konumdan başka bir konuma taşımanın nasıl yapıldığını gösterir. Kod çalıştırıldığında, İlkÇalışmaKitabı.xlsx içindeki İndex 1'de Move olarak adlandırılan çalışsayfa, İndex 2'ye taşınır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "FirstWorkbook.xlsx");
// Open a file into the first book.
const excelWorkbook2 = new AsposeCells.Workbook(filePath);

// Move the sheet
const worksheets = excelWorkbook2.getWorksheets();
const worksheet = worksheets.get(0);
worksheet.moveTo(1);

// Save the file.
excelWorkbook2.save(path.join(dataDir, "FirstWorkbookMoved_out.xlsx"));
```

### **Çalışma Kitapları Arasında Bir Çalışma Sayfası Kopylama**

Kodu yürütmek, Copy adlı sayfayı SecondWorkbook.xlsx içine Sheet2 adıyla kopyalar.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const excelWorkbook3 = new AsposeCells.Workbook();
const excelWorkbook4 = new AsposeCells.Workbook();

// Create source worksheet
excelWorkbook3.getWorksheets().add("Copy");

// Add new worksheet into second Workbook
excelWorkbook4.getWorksheets().add();

// Copy the first sheet of the first book into second book.
excelWorkbook4.getWorksheets().get(1).copy(excelWorkbook3.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook4.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xlsx"));
```

### **Çalışma Kitapları Arasında Bir Çalışma Sayfası Taşıma**

Kod çalıştırıldığında, İlkÇalışmaKitabı.xlsx içindeki Move adlı çalışsayfa, İkinciÇalışmaKitabı.xlsx içine Sheet3 adıyla taşınır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbooks instead of opening existing files
const excelWorkbook5 = new AsposeCells.Workbook();
const excelWorkbook6 = new AsposeCells.Workbook();

// Add New Worksheet
excelWorkbook6.getWorksheets().add();

// Copy the sheet from first book into second book.
excelWorkbook6.getWorksheets().get(0).copy(excelWorkbook5.getWorksheets().get(0));

// Remove the copied worksheet from first workbook
excelWorkbook5.getWorksheets().removeAt(0);

// Save the file.
excelWorkbook5.save(path.join(dataDir, "FirstWorkbookWithMove_out.xlsx"));

// Save the file.
excelWorkbook6.save(path.join(dataDir, "SecondWorkbookWithMove_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
