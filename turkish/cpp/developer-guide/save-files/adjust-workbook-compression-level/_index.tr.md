---
title: Workbook sıkıştırma seviyesini C++ ile ayarlama
linktitle: Çalışma Kitabı Sıkıştırma Seviyesini Ayarla
type: docs
weight: 180
url: /tr/cpp/adjust-workbook-compression-level/
description: Aspose.Cells for C++ kullanarak bir çalışma kitabının sıkıştırma seviyesini nasıl ayarlayacağınızı öğrenin, dosya boyutunu ve işlem süresini optimize edin.
---

## **Çalışma kitabının sıkıştırma seviyesini ayarlayın**

Geliştiriciler, daha büyük çalışma kitaplarıyla çalışırken çalışma kitabının sıkıştırma seviyesini ayarlayabilirler. Geliştiriciler, dosya boyutlarını işleme süresinin üzerine tercih edebilir veya tam tersini yapabilir. Aspose.Cells, çalışma kitabının sıkıştırma seviyesini ayarlamak için kullanabileceğiniz [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) numaralandırmasını sağlar. [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) numaralandırma aşağıdaki üyeleri sağlar.

- Seviye 1: En hızlı ama en az etkili sıkıştırma.
- Seviye 2: Seviye 1'den biraz daha yavaş, ancak daha iyi.
- Seviye 3: Seviye 2'den biraz daha yavaş, ama daha iyi.
- Seviye 4: Seviye 3'ten biraz daha yavaş, ama daha iyi.
- Seviye 5: Seviye 4'ten biraz daha yavaş, ancak daha iyi sıkıştırma ile.
- Seviye 6: Hız ve sıkıştırma verimliliği için iyi bir denge.
- Seviye 7: Oldukça iyi sıkıştırma!
- Seviye 8: Seviye 7'den daha iyi sıkıştırma!
- Seviye 9: En "iyi" sıkıştırma, en iyi, girdi veri akışının boyutunda en büyük azalma anlamına gelir. Bu aynı zamanda en yavaş sıkıştırmadır.

Aşağıdaki kod parçacığı, [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) numaralandırmasının kullanımını gösteriyor ve Düzey1, Düzey6 ve Düzey9 için dönüşüm süresini karşılaştırıyor. Oluşturulan dosyaların boyutlarını da karşılaştırabilirsiniz.

```cpp
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std::chrono;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"LargeSampleFile.xlsx");

    // Create XlsbSaveOptions object
    XlsbSaveOptions options;

    // Set compression level to 1 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level1);
    auto start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_1_out.xlsb", options);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 1 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 6 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level6);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_6_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 6 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 9 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level9);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_9_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 9 Elapsed Time: " << duration.count() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
