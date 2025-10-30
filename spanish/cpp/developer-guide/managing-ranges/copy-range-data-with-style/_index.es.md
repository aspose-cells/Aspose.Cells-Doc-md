---
title: Copiar datos del rango con estilo en C++
linktitle: Copiar Datos de Rango con Estilo
type: docs
weight: 610
url: /es/cpp/copy-range-data-with-style/
description: Copiar datos del rango incluyendo estilos de celdas en archivos de Excel usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

[Copiar solo datos del rango](/cells/es/cpp/copy-range-data-only/) explica cómo copiar datos de celdas entre rangos. Este artículo demuestra cómo copiar rangos de celdas preservando sus estilos de formato usando Aspose.Cells for C++.

{{% /alert %}}

Aspose.Cells proporciona clases y métodos para trabajar con rangos incluyendo [**CreateRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/), [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) y [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).

Este ejemplo demuestra cómo:

1. Crear un libro de trabajo
1. Poblar celdas con datos
1. Crear un [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)
1. Crear y configurar un objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)
1. Aplicar estilos al rango
1. Crear un segundo rango
1. Copiar datos formateados entre rangos

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

    for (int i = 0; i < 50; ++i)
    {
        for (int j = 0; j < 10; ++j)
        {
            cells.Get(i, j).PutValue((std::to_wstring(i) + L"," + std::to_wstring(j)).c_str());
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
    range2.Copy(range);

    U16String outputPath = outDir + u"CopyRange.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Range copied with formatting successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
