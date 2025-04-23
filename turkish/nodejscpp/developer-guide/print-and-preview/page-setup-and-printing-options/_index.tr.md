---  
title: Sayfa Ayarları ve Yazdırma Seçenekleri ile Node.js kullanımı  
linktitle: Sayfa Düzeni ve Yazdırma Seçenekleri  
type: docs  
weight: 60  
url: /tr/nodejs-cpp/page-setup-and-printing-options/  
---  

{{% alert color="primary" %}}  
Bazı durumlarda, geliştiriciler yazdırma sürecini kontrol etmek için sayfa düzeni ve yazdırma ayarlarını yapılandırmak isteyebilir. Sayfa düzeni ve yazdırma ayarları çeşitli seçenekler sunar ve Aspose.Cells tarafından tamamen desteklenir.  

Bu makale, Node.js üzerinde C++ kullanarak bir konsol uygulaması nasıl oluşturulacağını ve birkaç basit satır kod ile Aspose.Cells API kullanarak bir çalışma sayfası için sayfa ayarları ve yazdırma seçeneklerinin nasıl uygulanacağını gösterir.  
{{% /alert %}}  

## **Sayfa ve Yazdırma Ayarları İle Çalışma**  

Bu örnekte, Microsoft Excel’de bir çalışma kitabı oluşturduk ve Aspose.Cells kullanarak sayfa ayarları ve yazdırma seçenekleri ayarladık.  

### **Aspose.Cells Kullanarak Sayfa Düzeni Seçenekleri Ayarlama**  

Öncelikle Microsoft Excel'de basit bir çalışma sayfası oluşturun. Sonra ona sayfa düzeni seçenekleri uygulayın. Kodu yürüttüğünüzde, aşağıdaki ekran görüntüsünde görülen gibi Sayfa Düzeni seçeneklerini değiştirir.  

|**Çıktı dosyası.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|  

1. Microsoft Excel'de bazı veriler içeren bir çalışma sayfası oluşturun:  
   1. Microsoft Excel'de yeni bir çalışma kitabı açın.  
   1. Bazı veriler ekleyin.  
1. Sayfa düzeni seçeneklerini ayarlayın:  
   Ayarları dosyaya uygulayın. Yeni ayarların uygulanmadan önceki varsayılan seçeneklerin ekran görüntüsü aşağıda verilmiştir.  

|**Varsayılan sayfa düzeni seçenekleri.**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|  

1. Aspose.Cells'i indirin ve kurun:  
   1. [İndir](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++.  
   1. Geliştirme bilgisayarınıza kurun.  
      Kurulduğunda, tüm Aspose bileşenleri değerlendirme modunda çalışır. Değerlendirme modunun süresiz bir sınırlaması yoktur ve yalnızca üretilen belgelere filigran enjekte eder.  
1. Bir proje oluşturun:  
   1. Node.js ortamınızı başlatın.  
   1. Yeni bir konsol uygulaması oluşturun.  
      Bu örnek, bir Node.js konsol uygulaması gösterecek, ancak C++ bağlamlarını da kullanabilirsiniz.  
1. Referanslar ekleyin:  
   1. Bu örnek Aspose.Cells kullanır, bu bileşene projeye bir referans ekleyin. Örneğin:  
      …\Program Files\Aspose\Aspose.Cells\Bin\Node.js-Cpp\Aspose.Cells.node  
1. API'yi çağıran uygulamayı yazın:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "CustomerReport.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the orientation to Portrait
worksheet.getPageSetup().setOrientation(AsposeCells.PageOrientationType.Portrait);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Setting the paper size to A4
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Setting the print quality of the worksheet to 1200 dpi
worksheet.getPageSetup().setPrintQuality(1200);

// Setting the first page number of the worksheet pages
worksheet.getPageSetup().setFirstPageNumber(2);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_out.xlsx"));
```  

### **Yazdırma seçeneklerini ayarlama**  

Sayfa ayarı ayarları ayrıca kullanıcıların çalışma sayfalarının nasıl yazdırılacağını kontrol etmelerine olanak tanıyan birkaç yazdırma seçeneği (aynı zamanda sayfa seçenekleri de denir) sağlar. Kullanıcılara şunları yapma olanağı tanırlar:  

- Bir çalışma sayfasının belirli bir baskı alanını seçin.
- Başlıkları yazdırın.
- Izgaraları yazdırın.
- Satır/sütun başlıklarını yazdırın.
- Taslak kalitesine ulaşın.
- Yorumları yazdırın.
- Hücre hatalarını yazdırın.
- Sayfa sıralamasını tanımlayın.  

Aşağıdaki örnek yeni seçeneklerin uygulandığı dosyaya (Yukarıdaki örnekte oluşturulan PageSetup.xls) yazdırma seçeneklerini uygular. Aşağıdaki ekran görüntüsü, yeni seçenekler uygulanmadan önceki varsayılan yazdırma seçeneklerini gösterir.  

|**Giriş belgesi**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|  
Kodun çalıştırılması yazdırma seçeneklerini değiştirir.  

|**Çıktı dosyası**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageSetup.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

const pageSetup = worksheet.getPageSetup();

// Specifying the cells range (from A1 cell to E30 cell) of the print area
pageSetup.setPrintArea("A1:E30");

// Defining column numbers A & E as title columns
pageSetup.setPrintTitleColumns("$A:$E");

// Defining row numbers 1 as title rows
pageSetup.setPrintTitleRows("$1:$2");

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

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_Print_out.xlsx"));
```  

