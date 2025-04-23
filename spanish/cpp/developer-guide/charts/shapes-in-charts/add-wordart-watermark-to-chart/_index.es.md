---
title: Agregar marca de agua WordArt a un gráfico con C++
description: Aprende cómo usar Aspose.Cells for C++ para agregar una marca de agua WordArt a un gráfico en Microsoft Excel. Nuestra guía demostrará cómo crear y posicionar una marca de agua WordArt para mejorar el atractivo visual y la singularidad de tu gráfico.
keywords: Aspose.Cells for C++, Marca de agua WordArt, Marca de agua del gráfico, Microsoft Excel, Atractivo visual, Singularidad del gráfico.
type: docs
weight: 50
url: /es/cpp/add-wordart-watermark-to-chart/
---

{{% alert color="primary" %}} 

Puede usar WordArt para agregar efectos especiales de texto a las hojas de cálculo. Por ejemplo, estirar un título, decorar texto, hacer que el texto se ajuste a una forma preestablecida o aplicar el texto afectado al área de trazado de un gráfico como marca de agua. El WordArt se convierte en un objeto que puede mover o posicionar en sus hojas de cálculo para agregar decoración.

El siguiente ejemplo muestra cómo agregar una forma de WordArt como marca de agua para el área de trazado del gráfico.

{{% /alert %}} 

El siguiente ejemplo muestra cómo agregar una forma de WordArt como marca de agua para el área de trazado de un gráfico existente.

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
