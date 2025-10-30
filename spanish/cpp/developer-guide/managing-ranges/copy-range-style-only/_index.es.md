---
title: Copiar solo el estilo del rango en C++
linktitle: Copiar solo estilo de rango
type: docs
weight: 620
url: /es/cpp/copy-range-style-only/
description: Aprende cómo copiar solo el estilo de un rango en Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

[Copiar solo datos del rango](/cells/es/cpp/copy-range-data-only/) y [Copiar datos del rango con estilo](/cells/es/cpp/copy-range-data-with-style/) explican cómo copiar datos de un rango a otro por sí solo o completo con formato. También es posible copiar solo el formato. Este artículo muestra cómo.

{{% /alert %}} 

Este ejemplo crea un libro de trabajo, lo llena con datos y copia solo el estilo de un rango.

1. Crear un rango.
1. Crea un objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) con atributos de formato especificados.
1. Aplica el formato de estilo al rango.
1. Crear un segundo rango de celdas.
1. Copiar el formato del primer rango al segundo rango.

```c++
#include <iostream>
#include <string>
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

    Range range2 = cells.CreateRange(u"C10", u"E13");
    range2.CopyStyle(range);

    U16String outputPath = outDir + u"copyrangestyle.out.xls";
    workbook.Save(outputPath);

    std::cout << "Range style copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
