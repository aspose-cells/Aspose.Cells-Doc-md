---
title: Resimler veya Grafikler içeren XLS Dosyasını C++ ile PDF ye dönüştürün
linktitle: İmaj veya Grafik İçeren XLS Dosyasını PDF ye Dönüştürme
type: docs
weight: 50
url: /tr/cpp/convert-xls-file-with-images-or-charts-to-pdf/
description: Aspose.Cells ile C++ kullanarak resim veya grafik içeren XLS dosyalarını PDF belgelerine dönüştürün.
---

{{% alert color="primary" %}} 

Aspose.Cells, resim ve grafik içeren XLS dosyalarını PDF belgesine dönüştürmeyi destekler. Aspose.Cells for C++ bağımsız olarak çalışan, bir hesap tablosunu PDF'ye dönüştüren bir araçtır: Aspose.PDF for C++ gerekmez. Bu işlem hafızada yapılabilir çünkü geçici veya ara XML dosyalarına bağlı değildir. Bu, büyük Excel dosyalarının, örneğin resimler, grafikler ve diğer çizim nesneleri içerenlerin hızlı ve verimli şekilde dönüştürülmesini sağlar.

{{% /alert %}} 
## **Örnek Kod**

```c++
#include <iostream>
#include <memory>
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

    // Path of input excel file
    U16String designerFile = srcDir + u"SampleInput.xls";

    // Path of output pdf file
    U16String pdfFile = outDir + u"Output.out.pdf";

    try
    {
        // Open the template excel file
        std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(designerFile);

        // Save the pdf file
        wb->Save(pdfFile, SaveFormat::Pdf);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}} 

Eğer hesap tablosu formüller içeriyorsa, PDF'ye dönmeden hemen önce [Calculate(CalculationData data)] metodunu çağırmak en iyisidir. Bu, formüle bağlı değerlerin yeniden hesaplanmasını sağlar ve PDF'de doğru değerlerin gösterilmesini sağlar.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
