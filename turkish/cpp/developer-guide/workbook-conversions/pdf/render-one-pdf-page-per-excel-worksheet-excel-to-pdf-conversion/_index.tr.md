---
title: Bir Excel Çalışma Sayfasını Bir PDF Sayfası Olarak Render Et  Excel den PDF ye Dönüştürme C++ ile
type: docs
weight: 100
url: /tr/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Aspose.Cells kullanarak, her çalışma sayfası için bir sayfa olacak şekilde Excel çalışma sayfalarını PDF formatına dönüştürün.
---

{{% alert color="primary" %}} 

Büyük Microsoft Excel dosyalarıyla çalışırken (örneğin, birçok sayfası olan ve her sayfasında 50 kolon ve 300 veya daha fazla satır verisi bulunan çalışma kitabı), PDF çıktısının her çalışma sayfası için bir sayfa gösterdiğinden emin olmak isteyebilirsiniz, sayfanın boyutu büyük farklılıklar gösterebilir. Bu durum, her sayfanın çok farklı sayfa boyutlarına sahip olmasına neden olur. Bu, Aspose.Cells for C++ kullanılarak gerçekleştirilebilir.

{{% /alert %}} 

Lütfen birden çok çalışsayfasına sahip bir Excel dosyasını PDF'ye dönüştüren aşağıdaki örnek kodu inceleyin.

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

    // Initialize a new Workbook and open an Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";
    Workbook workbook(inputFilePath);

    // Implement one page per worksheet option
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetOnePagePerSheet(true);

    // Save the PDF file
    U16String outputFile = srcDir + u"OutputFile.out.pdf";
    workbook.Save(outputFile, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

[PaginatedSaveOptions(PaginatedSaveOptions_Impl*)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) seçeneği **true** olarak ayarlandıysa, tüm sayfa içeriği tek bir PDF sayfasına render edilir.

{{% /alert %}} {{% alert color="primary" %}} 

Eğer elektronik tablonuz formüller içeriyorsa, PDF'ye dönüştürmeden hemen önce [Workbook::CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) metodunu çağırmanız en iyisidir. Bu, formüle bağlı değerlerin yeniden hesaplanmasını sağlar ve PDF'de doğru değerler gösterilir.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
