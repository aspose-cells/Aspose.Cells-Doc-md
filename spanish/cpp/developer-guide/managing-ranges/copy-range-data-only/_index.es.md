---
title: Copiar solo los datos del rango con C++
linktitle: Copiar Solo Datos de Rango
type: docs
weight: 600
url: /es/cpp/copy-range-data-only/
description: Aprende cómo copiar solo los datos del rango sin formateo usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A veces, necesitas copiar datos de un rango de celdas a otro, copiando solo los datos, no el formato. Aspose.Cells ofrece esta función.

Este artículo proporciona un código de ejemplo que utiliza Aspose.Cells para copiar un rango de datos.

{{% /alert %}}

Este ejemplo muestra cómo:

1. Crear un libro de trabajo.
1. Agregar datos a las celdas en la primera hoja de cálculo.
1. Crear un [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/).
1. Crea un objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) con atributos de formato especificados.
1. Aplica el formato de estilo al rango.
1. Crear otro rango de celdas.
1. Copiar datos del primer rango a este segundo rango.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    for (int i = 0; i < 50; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            std::wstring value = std::to_wstring(i) + L"," + std::to_wstring(j);
            cells.Get(i, j).PutValue(U16String(reinterpret_cast<const char16_t*>(value.c_str())));
        }
    }

    Range range = cells.CreateRange(u"A1", u"D3");
    Style style = workbook.CreateStyle();

    style.GetFont().SetName(u"Calibri");
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);

    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Blue());
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Blue());
    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Blue());
    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Blue());

    StyleFlag flag1;
    flag1.SetFontName(true);
    flag1.SetCellShading(true);
    flag1.SetBorders(true);

    range.ApplyStyle(style, flag1);

    Range range2 = cells.CreateRange(u"C10", u"F12");
    range2.CopyData(range);

    U16String outputPath = outDir + u"CopyRangeData.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Range data copied and styled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
