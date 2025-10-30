---
title: Resampling eklenmiş Resimler  C++ ile Excel den PDF ye Dönüştürme
linktitle: Eklenen Resimleri Yeniden Örnekleme  Excel den PDF ye Dönütürme
type: docs
weight: 150
url: /tr/cpp/resampling-added-images-excel-to-pdf-conversion/
description: Aspose.Cells ile C++ kullanarak eklenen resimleri yeniden örnekleyerek PDF boyutunu küçültmeyi öğrenin.
---

{{% alert color="primary" %}}

Birçok resmi içeren büyük Microsoft Excel dosyaları ile çalışırken, çıktı PDF dosyasının boyutunu küçültmek ve genel dönüşüm performansını iyileştirmek için eklenen resimleri yeniden örneklemek gerekebilir. Aspose.Cells, eklenen resimleri yeniden örnekleme ve çıktı PDF dosya boyutunu küçültme konusunda destek sağlar.

{{% /alert %}}

Aşağıdaki örnek kod, Aspose.Cells API'sını kullanarak görevi nasıl gerçekleştirebileceğinizi açıklamaktadır. Örnek, dosyadaki resimleri sıkıştırarak Microsoft Excel dosyasını PDF dosyasına dönüştürmektedir.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Initialize a new Workbook and open an Excel file
    U16String inputPath = srcDir + u"input.xlsx";
    Workbook workbook(inputPath);

    // Instantiate the PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set Image Resample properties
    pdfSaveOptions.SetImageResample(300, 70);

    // Save the PDF file
    U16String outputPath = outDir + u"OutputFile_out_pdf.pdf";
    workbook.Save(outputPath, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

[**SetImageResample**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setimageresample/) seçeneğini kullanarak çıktı PDF dosyasının boyutunu en aza indirir, ancak görüntü kalitesini biraz etkileyebilir.

{{% /alert %}} 

{{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}
