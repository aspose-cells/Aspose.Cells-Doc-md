---
title: Excel 2016 MINIFS ve MAXIFS fonksiyonlarının C++ ile hesaplanması
description: Bu makale, Aspose.Cells kütüphanesini kullanarak Microsoft Excel 2016 da MINIFS ve MAXIFS fonksiyonlarının nasıl hesaplanacağını anlatır. C++ ile.
keywords: Aspose.Cells, Excel, 2016, MINIFS işlevi, MAXIFS işlevi, hesaplama
type: docs
weight: 300
url: /tr/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Olası Kullanım Senaryoları**
Microsoft Excel 2016, MINIFS ve MAXIFS fonksiyonlarını destekler. Bu fonksiyonlar, Excel 2013 veya önceki sürümlerde desteklenmemektedir. Aspose.Cells bu fonksiyonların hesaplamasını da destekler. Aşağıdaki ekran görüntüsü, bu fonksiyonların kullanımını gösterir. Bu ekran görüntüsü içindeki kırmızı yorumları okuyarak fonksiyonların nasıl çalıştığını öğrenebilirsiniz.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Excel 2016 MINIFS ve MAXIFS işlevlerinin hesaplanması**
Aşağıdaki örnek kod, [örnek Excel dosyasını](5115149.xlsx) yükler ve [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) metodunu çağırarak Aspose.Cells kullanılarak formül hesaplaması yapar ve ardından sonuçları [çıkış PDF'sine](5115154.pdf) kaydeder.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source workbook containing MINIFS and MAXIFS functions
    Workbook workbook(srcDir + u"sampleMINIFSAndMAXIFS.xlsx");

    // Perform Aspose.Cells formula calculation
    workbook.CalculateFormula();

    // Save the calculations result in pdf format
    PdfSaveOptions options;
    options.SetOnePagePerSheet(true);
    workbook.Save(outDir + u"outputMINIFSAndMAXIFS.pdf", options);

    std::cout << "PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
