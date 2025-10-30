---
title: Sayfa Sayısını Sınırlandırma  C++ ile Excel den PDF ye Dönüştürme
linktitle: Sayfa Sayısını Sınırlandırma
type: docs
weight: 180
url: /tr/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Aspose.Cells kullanarak C++ ile Excel den PDF ye dönüşüm yaparken oluşturulan sayfa sayısını nasıl sınırlayacağınızı öğrenin.
---

{{% alert color="primary" %}}

Bazı durumlarda, bir aralığı PDF dosyasına dönüştürmek isteyebilirsiniz. Aspose.Cells, bir Excel elektronik tablosunun PDF dosya biçimine dönüştürülürken kaç sayfa oluşturulacağına sınır koyma yeteneğine sahiptir.

{{% /alert %}}

## **Oluşturulan Sayfa Sayısını Sınırlandırmak**

Aşağıdaki örnek, bir Microsoft Excel dosyasındaki (3 ve 4) sayfa aralığını PDF olarak nasıl oluşturacağını göstermektedir.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"TestBook.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Instantiate the PdfSaveOption
    PdfSaveOptions options;

    // Print only Page 3 and Page 4 in the output PDF
    // Starting page index (0-based index)
    options.SetPageIndex(3);
    // Number of pages to be printed
    options.SetPageCount(2);

    // Path of output PDF file
    U16String outputFilePath = srcDir + u"outPDF1.out.pdf";

    // Save the PDF file
    wb.Save(outputFilePath, options);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Eğer elektronik tablo formülleri içeriyorsa, PDF'ye dönüştürmeden önce[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) çağrılması en iyisidir. Bu işlem, formül bağımlı değerlerin yeniden hesaplanmasını sağlar ve çıktı dosyasında doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
