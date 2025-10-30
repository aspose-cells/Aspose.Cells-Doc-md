---
title: Node.js ile C++ kullanarak Yazdırma Seçeneklerini Ayarlama
linktitle: Baskı Seçeneklerini Ayarlama
type: docs
weight: 40
url: /tr/nodejs-cpp/setting-print-options/
description: Bu makale, Node.js API ve C++ Kütüphanesi kullanarak Excel Çalışma Sayfası Sayfa Yapısı Özelliğinin Yazdırma Seçeneklerini programatik olarak nasıl ayarlayacağınızı gösterir. Yazdırma Alanını, Yazdırma Başlıklarını ve Sayfa Sırasını ayarlayabilirsiniz.
keywords: Node.js ile C++ kullanarak excel yazdırma alanı ayarla, Node.js ile C++ kullanarak excel yazdırma başlıklarını ayarla, Node.js ile C++ kullanarak excel sayfa sırasını ayarla
---

{{% alert color="primary" %}}

Microsoft Excel'in sayfa düzeni ayarları, kullanıcıların çalışma sayfalarının nasıl basılacağını kontrol etmelerini sağlayan birkaç baskı seçeneği (ayrıca sayfa seçenekleri olarak da adlandırılır) sunar.

{{% /alert %}}

## **Baskı Seçeneklerini Ayarlama**

Bu baskı seçenekleri, kullanıcıların şunları yapmalarını sağlar:

- Çalışma sayfasında belirli bir baskı alanı seçin.
- Başlıkları yazdırın.
- Izgaraları yazdırın.
- Satır/sütun başlıklarını yazdırın.
- Taslak kalitesine ulaşın.
- Yorumları yazdırın.
- Hücre hatalarını yazdırın.
- Sayfa sıralamasını tanımlayın.

Aspose.Cells for Node.js via C++, Microsoft Excel tarafından sunulan tüm yazdırma seçeneklerini destekler ve geliştiriciler, [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) sınıfının sunduğu özellikleri kullanarak bu seçenekleri çalışma sayfaları için kolayca yapılandırabilir. Bu özelliklerin nasıl kullanılacağı daha ayrıntılı olarak aşağıda anlatılmaktadır.

### **Baskı Alanı Belirle**

Varsayılan olarak, baskı alanı veri içeren çalışma sayfasının tüm alanlarını içerir. Geliştiriciler, çalışma sayfasının belirli bir baskı alanını belirleyebilirler.

Belirli bir baskı alanı seçmek için, [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) sınıfının [**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--) özelliğini kullanın. Bu özelliğe baskı alanını tanımlayan bir hücre aralığı atayın.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Specifying the cells range (from A1 cell to T35 cell) of the print area
pageSetup.setPrintArea("A1:T35");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintArea_out.xls"));
```

### **Başlıkları Yazdırma**

Aspose.Cells, basılı bir çalışma sayfasının tüm sayfalarında tekrarlanacak satır ve sütun başlıklarını belirlemenize izin verir. Bunu yapmak için [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) sınıfının [**PageSetup.getPrintTitleColumns()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleColumns--) ve [**PageSetup.getPrintTitleRows()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleRows--) özelliklerini kullanın.

Tekrar edilecek satırlar veya sütunlar, satır veya sütun numaralarını geçirerek tanımlanır. Örneğin satırlar $1:$2 ve sütunlar $A:$B olarak tanımlanır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Defining column numbers A & B as title columns
pageSetup.setPrintTitleColumns("$A:$B");

// Defining row numbers 1 & 2 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintTitle_out.xls"));
```

### **Diğer Yazdırma Seçeneklerini Belirleme**

[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) sınıfı ayrıca aşağıdaki genel yazdırma seçeneklerini ayarlamak için birkaç başka özellik sunar:

- [**PageSetup.getPrintGridlines()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintGridlines--): yazdırıp yazdırmamayı belirleyen bir Boolean özelliği.
- [**PageSetup.getPrintHeadings()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintHeadings--): satır ve sütun başlıklarının yazdırılıp yazdırılmayacağını belirleyen bir Boolean özelliği.
- [**PageSetup.getBlackAndWhite()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBlackAndWhite--): çalışma sayfasını siyah beyaz modda yazdırıp yazdırmayacağını belirleyen bir Boolean özellik.
- [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--): çalışma sayfasında yazdırma yorumlarını göstermenip göstermeyeceğini veya sayfanın sonunda gösterip göstermeyeceğini tanımlar.
- [**PageSetup.getPrintDraft()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintDraft--): grafikleri olmadan sayfayı yazdırıp yazdırmayacağını tanımlayan bir boolean özelliği.
- [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--): Hücre hatalarını, görüntülendiği gibi, boş, çizgi veya N/A olarak yazdırmayı tanımlar.

[**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) ve [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) özelliklerini ayarlamak için, Aspose.Cells for Node.js via C++ ayrıca [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) ve [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype) adlı iki enum sağlar; bunlar sırasıyla [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--) ve [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--) özelliklerine atanacak önceden tanımlanmış değerleri içerir.

[**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) enumundaki önceden tanımlanmış değerler aşağıda listelenmiş ve açıklamalarıyla birlikte verilmiştir.

|**Yazdırma Yorumları Türleri**|**Açıklama**|
| :- | :- |
|PrintInPlace| Çalışma sayfasında görüntülenen yorumları yazdırmayı belirtir.
|PrintNoComments| Yorumları yazdırmamayı belirtir.
|PrintSheetEnd| Yorumları çalışma sayfasının sonunda yazdırmayı belirtir.

[**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype) enumundaki önceden tanımlanmış değerler aşağıda listelenmiş ve açıklamalarıyla birlikte verilmiştir.

|**Yazdırma Hataları Türleri**|**Açıklama**|
| :- | :- |
|PrintErrorsBlank| Hataları yazdırmamayı belirtir.
|PrintErrorsDash| Hataları "--" olarak yazdırmayı belirtir.
|PrintErrorsDisplayed| Hataları görüntülendiği gibi yazdırmayı belirtir.
|PrintErrorsNA| Hataları "#N/A" olarak yazdırmayı belirtir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Save the workbook.
workbook.save(path.join(dataDir, "OtherPrintOptions_out.xls"));
```

### **Sayfa Sırasını Belirleme**

[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) sınıfı, yazdırılacak birden fazla sayfayı sıralamak için kullanılan [**PageSetup.getOrder()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getOrder--) özelliği sağlar. Sayfaları sıralamanın iki olasılığı vardır.

- **Aşağıdan önce ardından:** herhangi bir sayfayı sağa yazdırmadan önce tüm sayfaları aşağıya yazdırır.
- **Ardından aşağıdan önce:** sayfaları aşağıya yazdırmadan önce soldan sağa doğru sayfaları yazdırır.

Aspose.Cells, tüm önceden tanımlanmış sıralama türlerini içeren [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) enumunu sağlar.

[**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype) enumunun önceden tanımlanmış değerleri aşağıda listelenmiştir.

|**Yazdırma Sıralama Türleri**|**Açıklama**|
| :- | :- |
|DownThenOver|Aşağıdan önce ardından sıralama temsil eder.
|OverThenDown|Ardından aşağıdan önce sıralama temsil eder.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook.
workbook.save(path.join(dataDir, "SetPageOrder_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
