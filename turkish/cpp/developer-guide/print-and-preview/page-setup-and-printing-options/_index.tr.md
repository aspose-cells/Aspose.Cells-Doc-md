---
title: C++ ile Sayfa Ayarları ve Yazdırma Seçenekleri
linktitle: Sayfa Düzeni ve Yazdırma Seçenekleri
type: docs
weight: 60
url: /tr/cpp/page-setup-and-printing-options/
description: Aspose.Cells kullanarak sayfa ayarlarını ve yazdırma ayarlarını yapılandırın.
---

{{% alert color="primary" %}}

Bazı durumlarda, geliştiriciler yazdırma sürecini kontrol etmek için sayfa düzeni ve yazdırma ayarlarını yapılandırmak isteyebilir. Sayfa düzeni ve yazdırma ayarları çeşitli seçenekler sunar ve Aspose.Cells tarafından tamamen desteklenir.

Bu makale, Visual Studio'da nasıl bir komut satırı uygulaması oluşturulacağını ve Aspose.Cells API'sini kullanarak birkaç basit satır kodla bir çalışma sayfasına sayfa ayarları ve yazdırma seçenekleri uygulayacağınızı gösterir.

{{% /alert %}}

## **Sayfa ve Yazdırma Ayarları İle Çalışma**

Bu örnekte, Microsoft Excel'de bir çalışma kitabı oluşturduk ve Aspose.Cells kullanarak sayfa düzeni ve yazdırma seçeneklerini ayarladık.

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
   1. [İndir](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++.
   1. Geliştirme bilgisayarınıza kurun.
      Kurulduğunda, tüm Aspose bileşenleri değerlendirme modunda çalışır. Değerlendirme modunun süresiz bir sınırlaması yoktur ve yalnızca üretilen belgelere filigran enjekte eder.
1. Bir proje oluşturun:
   1. Visual Studio'yu başlatın.
   1. Yeni bir konsol uygulaması oluşturun.
      Bu örnek, bir C++ komut satırı uygulaması gösterecektir.
1. Referanslar ekleyin:
   1. Bu örnek Aspose.Cells kullanır, bu bileşene projeye bir referans ekleyin. Örneğin:
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. API'yi çağıran uygulamayı yazın:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"CustomerReport.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting the orientation to Portrait
    worksheet.GetPageSetup().SetOrientation(PageOrientationType::Portrait);

    // Setting the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Setting the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Setting the paper size to A4
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Setting the print quality of the worksheet to 1200 dpi
    worksheet.GetPageSetup().SetPrintQuality(1200);

    // Setting the first page number of the worksheet pages
    worksheet.GetPageSetup().SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
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

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"PageSetup.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_Print_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get PageSetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specifying the cells range (from A1 cell to E30 cell) of the print area
    pageSetup.SetPrintArea(u"A1:E30");

    // Defining column numbers A & E as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$E");

    // Defining row numbers 1 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Allowing to print gridlines
    pageSetup.SetPrintGridlines(true);

    // Allowing to print row/column headings
    pageSetup.SetPrintHeadings(true);

    // Allowing to print worksheet in black & white mode
    pageSetup.SetBlackAndWhite(true);

    // Allowing to print comments as displayed on worksheet
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);

    // Allowing to print worksheet with draft quality
    pageSetup.SetPrintDraft(true);

    // Allowing to print cell errors as N/A
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);

    // Setting the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
