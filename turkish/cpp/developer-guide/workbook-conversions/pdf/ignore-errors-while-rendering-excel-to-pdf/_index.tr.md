---
title: C++ ile Excel i PDF ye dönüştürürken Hataları Yoksay
linktitle: Excel i PDF olarak dönüştürürken Hataları Yoksay
type: docs
weight: 80
url: /tr/cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Aspose.Cells for C++ kullanarak Excel den PDF ye dönüştürürken hataları nasıl yoksayacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

Bazen Excel dosyanızı PDF'ye dönüştürürken hatalar veya istisnalar oluşur ve dönüşüm işlemi sona erer. Bu hataları yoksaymak için [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) özelliğini kullanabilirsiniz. Bu şekilde, dönüşüm işlemi herhangi bir hata veya istisna fırlatmadan sorunsuz tamamlanacaktır ancak veri kaybı olabilir. Bu nedenle, veri kaybı sizin için kritik değilse bu özelliği kullanın.

## **Excel'den PDF'e Dönüştürme Sırasında Hataları Yoksay**

Aşağıdaki kod, [örnek Excel dosyasını](55541778.xlsx) yükler, ancak bu örnek Excel dosyası hatalıdır ve [dönüşüm sırasında bir hata](55541779.pdf) oluşur 17.11'de, ancak [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) özelliğini kullandığımız için hata fırlatmaz. Ancak, bu ekran görüntüsünde gösterildiği gibi bir *yuvarlak kırmızı ok şekli* kaybolur.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Örnek Kod**

```c++
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
    U16String inputFilePath = srcDir + u"sampleErrorExcel2Pdf.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"outputErrorExcel2Pdf.pdf";

    // Load the Sample Workbook that throws Error on Excel2Pdf conversion
    Workbook wb(inputFilePath);

    // Specify Pdf Save Options - Ignore Error
    PdfSaveOptions opts;
    opts.SetIgnoreError(true);

    // Save the Workbook in Pdf with Pdf Save Options
    wb.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully with error ignored!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
