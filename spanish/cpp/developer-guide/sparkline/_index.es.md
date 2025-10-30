---
title: Insertar Sparkline con C++
linktitle: Gráficos de Chispa
type: docs
weight: 160
url: /es/cpp/creating-sparklines/
description: Crear sparkline para Excel usando Aspose.Cells con C++.
---

## **Insertar un gráfico de chispa**
{{% alert color="primary" %}} 

Sparkline es un pequeño gráfico en una celda de la hoja de cálculo que proporciona una representación visual de los datos. Usa sparklines para mostrar tendencias en una serie de valores, como aumentos o disminuciones estacionales, ciclos económicos, o para resaltar valores máximos y mínimos. Posiciona un sparkline cerca de sus datos para mayor impacto. Hay tres tipos de Sparkline: Línea, Columna y Apilado.

{{% /alert %}} 

Es sencillo crear un gráfico de chispa con Aspose.Cells con los siguientes ejemplos de códigos:

```cpp
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

    // Create a new workbook
    Workbook book;
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Set values in cells
    sheet.GetCells().Get(u"A1").PutValue(5);
    sheet.GetCells().Get(u"B1").PutValue(2);
    sheet.GetCells().Get(u"C1").PutValue(1);
    sheet.GetCells().Get(u"D1").PutValue(3);

    // Define the CellArea
    CellArea ca;
    ca.StartColumn = 4;
    ca.EndColumn = 4;
    ca.StartRow = 0;
    ca.EndRow = 0;

    // Add a sparkline group
    int idx = sheet.GetSparklineGroups().Add(SparklineType::Line, sheet.GetName() + u"!A1:D1", false, ca);

    // Get the sparkline group
    SparklineGroup group = sheet.GetSparklineGroups().Get(idx);
    group.GetSparklines().Add(sheet.GetName() + u"!A1:D1", 0, 4);

    // Customize Sparklines
    // Create CellsColor
    CellsColor clr = book.CreateCellsColor();
    clr.SetColor(Color::Orange());
    group.SetSeriesColor(clr);

    // Set the high points to green and low points to red
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.GetHighPointColor().SetColor(Color::Green());
    group.GetLowPointColor().SetColor(Color::Red());

    // Set line weight
    group.SetLineWeight(1.0);

    // Optionally, apply a preset style
    // group.SetPresetStyle(SparklinePresetStyleType::Style10);

    // Save the workbook
    book.Save(outDir + u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Usar Gráficos de Chispa y Configuración de Formato 3D](/cells/es/cpp/using-sparklines-and-settings-3d-format/)
{{< app/cells/assistant language="cpp" >}}
