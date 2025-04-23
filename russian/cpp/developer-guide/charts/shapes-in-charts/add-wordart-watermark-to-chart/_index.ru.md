---
title: Добавьте водяной знак WordArt на график с помощью C++
description: Узнайте, как использовать Aspose.Cells for C++ для добавления водяного знака WordArt на график в Microsoft Excel. Наше руководство покажет, как создавать и позиционировать водяной знак WordArt для повышения визуальной привлекательности и уникальности вашего графика.
keywords: Aspose.Cells for C++, WordArt Watermark, Водяной знак графика, Microsoft Excel, Визуальная привлекательность, Уникальность графика.
type: docs
weight: 50
url: /ru/cpp/add-wordart-watermark-to-chart/
---

{{% alert color="primary" %}} 

Вы можете использовать WordArt для добавления специальных текстовых эффектов в электронные таблицы. Например, растянуть заголовок, украсить текст, сделать текст подходящим под предварительно заданную форму или применить к тексту эффект водяного знака к области построения диаграммы. WordArt становится объектом, который можно перемещать или располагать в электронных таблицах для добавления украшения.

В следующем примере показано, как добавить текст WordArt в качестве водяного знака для области построения диаграммы.

{{% /alert %}} 

В следующем примере показано, как добавить фигуру WordArt в качестве водяного знака для существующей зоны построения диаграммы.

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
