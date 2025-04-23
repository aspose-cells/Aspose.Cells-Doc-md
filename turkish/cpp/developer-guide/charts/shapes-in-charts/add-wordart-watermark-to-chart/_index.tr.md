---
title: Chart a WordArt Su İşareti Eklemek için C++ kullanın
description: Microsoft Excel de bir grafiğe WordArt su işareti eklemek için Aspose.Cells for C++ nasıl kullanılır öğrenin. Rehberimiz, WordArt su işareti oluşturma ve konumlandırma adımlarını gösterecek, görsel çekiciliği ve grafiğinizin benzersizliğini artıracaktır.
keywords: Aspose.Cells for C++, WordArt Su İşareti, Grafik Su İşareti, Microsoft Excel, Görsel Çekicilik, Grafik Benzersizliği.
type: docs
weight: 50
url: /tr/cpp/add-wordart-watermark-to-chart/
---

{{% alert color="primary" %}} 

WordArt'ı elektronik tablolara özel metin efektleri eklemek için kullanabilirsiniz. Örneğin, başlığı uzatabilir, metni süsleyebilir, metni önceden belirlenmiş bir şekle sığdırabilir veya etkilenen metni bir grafik çizim alanına bir filigran olarak uygulayabilirsiniz. WordArt, elektronik tablolarınızda hareket ettirebileceğiniz veya konumlandırabileceğiniz bir nesne haline gelirken dekorasyon eklemek için.

Aşağıdaki örnek, bir WordArt şeklinin grafik çizim alanı için bir filigran olarak nasıl ekleneceğini göstermektedir.

{{% /alert %}} 

Aşağıdaki örnek, varolan bir grafik çizim alanı için bir WordArt şeklinin filigran olarak nasıl ekleneceğini göstermektedir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the existing excel file.
    Workbook workbook(srcDir + u"sample.xlsx");

    // Get the chart in the first worksheet.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Add a WordArt watermark (shape) to the chart's plot area.
    Shape wordart = chart.GetShapes().AddTextEffectInChart(MsoPresetTextEffect::TextEffect2,
        u"CONFIDENTIAL", u"Arial Black", 66, false, false, 1200, 500, 2000, 3000);

    // Get the shape's fill format.
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the transparency.
    wordArtFormat.SetTransparency(0.9);

    // Get the line format.
    LineFormat lineFormat = wordart.GetLine();

    // Set Line format to invisible.
    lineFormat.SetWeight(0.0);

    // Save the excel file.
    workbook.Save(outputDir + u"output_out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
