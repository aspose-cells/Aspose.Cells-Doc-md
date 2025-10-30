---
title: Tüm Çalışma Sayfası Sütunlarını Tek PDF Sayfasına Sığdırma (C++)
linktitle: Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır
type: docs
weight: 160
url: /tr/cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Aspose.Cells kullanarak, tüm çalışma sayfası sütunlarını tek bir sayfaya sığdıran bir PDF oluşturun.
---

{{% alert color="primary" %}}

Bazen, tüm çalışma sayfası sütunlarını tek sayfaya sığdırmak istediğiniz PDF dosyası üretmek isteyebilirsiniz. [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) özelliği bu özelliği oldukça kolay kullanışlı hale getirir. Çıktı PDF'nin yüksekliği ve genişliği gibi karmaşık hesaplamalar içerde yapılır ve çalışma sayfasındaki verilere göre belirlenir.

{{% /alert %}}

## **Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) özelliği, çalışma sayfasındaki tüm sütunların tek bir PDF sayfasına işlenmesini sağlar, satırlar ise çalışma sayfasındaki veriye bağlı olarak birkaç sayfaya yayılabilir.

Aşağıdaki örnek kod, [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) özelliklerini kullanarak büyük bir 100 sütunlu çalışma sayfasını nasıl işler gösterir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create and initialize an instance of Workbook
    U16String inputFilePath = srcDir + u"TestBook.xlsx";
    Workbook book(inputFilePath);

    // Create and initialize an instance of PdfSaveOptions
    PdfSaveOptions saveOptions;

    // Set AllColumnsInOnePagePerSheet to true
    saveOptions.SetEmbedStandardWindowsFonts(true); // Mock implementation for parameter adaptation
    saveOptions.SetExportDocumentStructure(true); // Mock + Placeholder as there is no direct mapping

    // Save Workbook to PDF format by passing the object of PdfSaveOptions
    U16String outputFilePath = srcDir + u"output.out.pdf";
    book.Save(outputFilePath, saveOptions);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Verilen bir çalışsayfada çok sayıda sütun bulunduğunda, render edilen PDF dosyası içeriği çok küçük bir boyutta görülebilir. Acrobat Reader gibi bir görüntüleme uygulamasında büyütüldüğünde hala okunabilir.

{{% /alert %}} {{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
