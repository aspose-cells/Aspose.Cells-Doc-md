---
title: İşyerleri İçinde ve İşyerleri Arasında Sayfaları Kopyala ve Taşı ile C++
linktitle: Sayfaları Kopyalayın ve Taşıyın
type: docs
weight: 80
url: /tr/cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Excel çalışma kitapları içinde ve arasında çalışma sayfalarını nasıl kopyalayacağınızı ve taşıyacağınızı Aspose.Cells for C++ kullanarak öğrenin.
---

{{% alert color="primary" %}}

Bazen, ortak biçimlendirme ve veri girişine sahip birden çok sayfaya ihtiyacınız olur. Örneğin, üç aylık bütçelerle çalışıyorsanız, aynı sütun başlıkları, satır başlıkları ve formülleri içeren çalışma sayfaları olan bir çalışma kitabı oluşturmak isteyebilirsiniz. Bunu yapmanın bir yolu vardır: bir sayfa oluşturmak ve sonra onu birden çok kez kopyalamak.

Aspose.Cells, çalışma kitapları arasında veya içinde çalışma sayfalarını kopyalama veya taşımayı destekler. Veri, biçimlendirme, tablolar, matrisler, grafikler, resimler ve diğer nesnelerin yanı sıra sayfalar en yüksek hassasiyetle kopyalanır.

{{% /alert %}}

## **Çalışma Sayfalarını Kopyalama ve Taşıma**

### **Bir Çalışma Sayfasını Bir Çalışma Kitabı İçinde Kopyalama**

Başlangıç adımları tüm örnekler için aynıdır:

1. Microsoft Excel’de bazı verilerle iki çalışma kitabı oluşturun. Bu örnekte, Microsoft Excel’de iki yeni çalışma kitabı oluşturduk ve çalışma sayfalarına bazı veriler girdik:
   - FirstWorkbook.xlsx (3 çalışma sayfası)
   - SecondWorkbook.xlsx (1 çalışma sayfası)

1. Aspose.Cells'i indirin ve kurun:
   1. [Aspose.Cells for C++ indir](https://downloads.aspose.com/cells/cpp)
   1. Geliştirme bilgisayarınıza kurun

1. Bir proje oluşturun:
   1. Tercih ettiğiniz IDE’de yeni bir C++ projesi oluşturun

1. Referanslar ekleyin:
   1. Aspose.Cells for C++ kütüphanesini projenize ekleyin

1. Bir çalışma kitabı içindeki çalışsayfayı kopyalama
   İlk örnek, İlkÇalışmaKitabı.xlsx içindeki ilk çalışsayfayı (Kopya) kopyalar.

Kod çalıştırıldığında, Kopya adlı çalışsayfa, İlkÇalışmaKitabı.xlsx içinde Last Sheet adıyla kopyalanır.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from input file
    Workbook excelWorkbook1(srcDir + u"FirstWorkbook.xlsx");

    // Get worksheet collection reference
    WorksheetCollection worksheets = excelWorkbook1.GetWorksheets();

    // Copy third worksheet (index 2) within the workbook
    worksheets.AddCopy(worksheets.Get(2).GetName());

    // Save modified workbook
    excelWorkbook1.Save(outDir + u"FirstWorkbookCopied_out.xlsx");

    std::cout << "Worksheet copied successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Bir Çalışma Kitabı içinde bir Çalışsayfayı Taşıma**

Aşağıdaki kod, bir çalışma kitabı içindeki bir çalışsayfayı bir konumdan başka bir konuma taşımanın nasıl yapıldığını gösterir. Kod çalıştırıldığında, İlkÇalışmaKitabı.xlsx içindeki İndex 1'de Move olarak adlandırılan çalışsayfa, İndex 2'ye taşınır.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create input and output file paths
    U16String inputFilePath = srcDir + u"FirstWorkbook.xlsx";
    U16String outputFilePath = outDir + u"FirstWorkbookMoved_out.xlsx";

    // Load source workbook
    Workbook excelWorkbook2(inputFilePath);

    // Access worksheet collection and move target sheet
    WorksheetCollection sheets = excelWorkbook2.GetWorksheets();
    sheets.Get(u"Move").MoveTo(2);

    // Save modified workbook
    excelWorkbook2.Save(outputFilePath);

    std::cout << "Worksheet moved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Çalışma Kitapları Arasında Bir Çalışma Sayfası Kopylama**

Kodu çalıştırmak, Copy adlı çalışma sayfasını SecondWorkbook.xlsx’e kopyalar ve adı Sheet2 olur.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open source workbooks
    Workbook excelWorkbook3(srcDir + u"FirstWorkbook.xlsx");
    Workbook excelWorkbook4(srcDir + u"SecondWorkbook.xlsx");

    // Access worksheets collection from second workbook
    WorksheetCollection sheets4 = excelWorkbook4.GetWorksheets();

    // Add new worksheet to destination workbook
    sheets4.Add();

    // Copy specified worksheet from source to destination
    Worksheet sourceSheet = excelWorkbook3.GetWorksheets().Get(u"Copy");
    sheets4.Get(1).Copy(sourceSheet);

    // Save modified workbook
    excelWorkbook4.Save(outDir + u"CopyWorksheetsBetweenWorkbooks_out.xlsx");

    std::cout << "Worksheets copied successfully between workbooks." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Çalışma Kitapları Arasında Bir Çalışma Sayfası Taşıma**

Kod çalıştırıldığında, İlkÇalışmaKitabı.xlsx içindeki Move adlı çalışsayfa, İkinciÇalışmaKitabı.xlsx içine Sheet3 adıyla taşınır.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open first workbook
    Workbook excelWorkbook5(srcDir + u"FirstWorkbook.xlsx");

    // Open second workbook and add new worksheet
    Workbook excelWorkbook6(srcDir + u"SecondWorkbook.xlsx");
    excelWorkbook6.GetWorksheets().Add();

    // Copy third worksheet from first workbook to third position in second workbook
    WorksheetCollection sheets5 = excelWorkbook5.GetWorksheets();
    WorksheetCollection sheets6 = excelWorkbook6.GetWorksheets();
    sheets6.Get(2).Copy(sheets5.Get(2));

    // Remove copied worksheet from source workbook
    sheets5.RemoveAt(2);

    // Save modified workbooks
    excelWorkbook5.Save(outDir + u"FirstWorkbookWithMove_out.xlsx");
    excelWorkbook6.Save(outDir + u"SecondWorkbookWithMove_out.xlsx");

    std::cout << "Worksheets moved successfully between workbooks." << std::endl;

    Aspose::Cells::Cleanup();
}
```
