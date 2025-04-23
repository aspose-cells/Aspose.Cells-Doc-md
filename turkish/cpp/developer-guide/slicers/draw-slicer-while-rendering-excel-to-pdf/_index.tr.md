---
title: C++ ile Excel i PDF ye dönüştürürken Slicer çizimi yapma
linktitle: Excel i PDF ye dönüştürürken Dilimleyici Çizer
type: docs
weight: 60
url: /tr/cpp/draw-slicer-while-rendering-excel-to-pdf/
description: Aspose.Cells kullanarak, Slicer ayarlarıyla Excel i PDF ye dışa aktarın.
---

## **Excel dosyasına bir dilimleyici uygulanmışsa ve bu dilimleyicinin ayarlarını içeren bir Excel dosyasını PDF olarak dışa aktarmak istiyorsanız, Aspose.Cells bunu artık varsayılan olarak destekler. Sadece Excel dosyasını dilimleyici ile birlikte PDF olarak dışa aktarırsınız, oluşturulan PDF uygulanan dilimleyiciyi gösterecektir.**
Excel dosyasına Slicer uygulandıysa ve Slicer ayarlarıyla PDF'e dışa aktarılmak isteniyorsa, Aspose.Cells yeni sürümde bu özelliği desteklemektedir. Tek yapmanız gereken, Slicer içeren Excel dosyasını PDF olarak dışa aktarmak ve çıkan PDF'de slicer'ın görünmesini sağlamaktır.

Aşağıdaki örnek kod önceden var olan bir dilimleyici içeren [örnek Excel dosyasını](94044165.xlsx) yükler. Daha sonra, çalışma kitabını [çıkış PDF dosyası](94044166.pdf) olarak kaydeder. Aşağıdaki ekran görüntüsü kaynak Excel dosyasını ve oluşturulan PDF dosyasını karşılaştırır.

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

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
    U16String inputFilePath = srcDir + u"SampleSlicerChart.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"SampleSlicerChart.pdf";

    // Create workbook from the excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as a PDF file
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved as PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
