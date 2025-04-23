---
title: C++ ile Spreadsheets Dönüştürürken WordArt için Gradyan Doldurma Render Et
linktitle: Hücre Dizelerini HTML ye Dönüştürürken WordArt için Gradient Doldurmayı Oluşturma
type: docs
weight: 90
url: /tr/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: Spreadsheets’leri HTML’ye dönüştürürken WordArt için gradyan doldurma render etmeyi öğrenin.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells 17.1'den önce, Aspose.Cells Excel dosyası HTML formatına dönüştürüldüğünde word art'ın gradient doldurudğunu oluşturmazdı. Aspose.Cells 17.1'in piyasaya sürülmesinden bu yana, word art gradient doldurma desteklenmektedir. Aşağıdaki ekran görüntüsü, excel dosyasının Aspose.Cells 17.1 ile ve eski sürüm ile dönüştürülmesinin gradient doldurmadaki etkisini karşılaştırıyor.

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)
## **Hücre Dizelerini HTML'ye dönüştürürken word art için gradient doldurmayı oluştur.**
Aşağıdaki örnek kod, [kaynak excel dosyasını](22774111.xlsx) [çıktı HTML formatına](22774109.zip) dönüştürür. Kaynak excel dosyası yukarıdaki ekran görüntüsünde gösterilen gibi gradient doldurulu word art nesnelerini içerir.
## **Örnek Kod**
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sourceGradientFill.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save workbook to HTML format
    workbook.Save(outDir + u"out_sourceGradientFill.html");

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
