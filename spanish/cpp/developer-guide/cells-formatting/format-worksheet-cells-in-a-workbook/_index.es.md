---
title: Formateo de celdas de hoja de cálculo en un libro con C++
linktitle: Formatear celdas de hoja de cálculo
description: Aspose.Cells es una biblioteca C++ para trabajar con archivos de hojas de cálculo. Soporta el formateo de celdas de las hojas de cálculo en libros, permitiendo a los usuarios personalizar la apariencia y estilo de las celdas. Este artículo introducirá cómo formatear celdas de hoja usando la biblioteca Aspose.Cells.
keywords: Aspose.Cells, Workbook, Worksheet, Cell, Formatting, Appearance, Style
type: docs
weight: 2000
url: /es/cpp/format-worksheet-cells-in-a-workbook/
---

{{% alert color="primary" %}}

Este artículo muestra cómo:

1. Usar estilos para formatear rápidamente los datos.
1. Formatear celdas en filas y columnas.
1. Usar bordes y colores para enfatizar los datos.
1. Aplicar formatos numéricos para enfatizar los datos.
1. Use fuentes y atributos para resaltar datos.
1. Formatee datos en un rango denominado.
1. Cambie la alineación y orientación de los datos.
1. Establezca la altura de fila y el ancho de columna.

El proyecto de ejemplo realiza todas estas tareas y proporciona a los desarrolladores una descripción detallada de cómo crear un libro, agregar datos y aplicar formato usando [Aspose.Cells](https://products.aspose.com/cells/cpp/).

{{% /alert %}}

## **Formato de datos**

El formato se utiliza para distinguir entre diferentes tipos de información y mostrar datos de manera clara.

Un formato representa un estilo y se define como un conjunto de características, como fuentes y tamaños de fuente, formatos de números, bordes de celdas, sombreado de celdas, sangría, alineación y orientación del texto. Los bordes proporcionan otras formas de resaltar información. Un borde es una línea dibujada alrededor de una celda o grupo de celdas.

Los formatos de números también hacen que los datos sean más significativos. Al aplicar diferentes formatos de números, puede cambiar la apariencia de los números sin cambiar el número que representa.

Aspose.Cells le permite dibujar bordes alrededor de celdas y rangos fácilmente. También le permite aplicar fuentes y sombrear celdas. El componente es lo suficientemente eficiente como para formatear una fila o columna completa, establecer alineaciones, envolver y rotar texto en celdas. Aspose.Cells también admite todos los formatos de números admitidos por Microsoft Excel.

Este artículo muestra cómo crear una aplicación de consola en Visual Studio que genere un informe de ventas anuales. El libro se crea desde cero, luego se insertan datos y se formatea la hoja de cálculo. Mostramos cómo crear una aplicación de consola sencilla que crea un libro de Excel (también puedes usar un archivo plantilla), inserta datos de ventas en la primera hoja, formatea los datos y guarda un archivo de Excel.

### **Proceso**

A continuación se detallan los pasos sobre cómo crear una hoja de cálculo y formatear diferentes celdas en diferentes filas y columnas de una hoja de trabajo.

1. Descargue e instale Aspose.Cells:
   1. [Descargar](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++.
   1. Instálelo en su equipo de desarrollo.
1. Cree un proyecto y agregue referencias:
   1. Inicie Visual Studio.
   1. Cree una nueva aplicación de consola.
   1. Agregue una referencia a Aspose.Cells, por ejemplo…\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Agrega el siguiente código al proyecto:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

void CreateReportData(Workbook& workbook);
void CreateCellsFormatting(Workbook& workbook);

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String inputFilePath = srcDir + u"FormatWorksheet.xls";

    Workbook workbook;

    workbook.ChangePalette(Color{ 155, 204, 255 }, 55);
    workbook.ChangePalette(Color{ 0, 51, 105 }, 54);
    workbook.ChangePalette(Color{ 250, 250, 200 }, 53);
    workbook.ChangePalette(Color{ 124, 199, 72 }, 52);

    CreateReportData(workbook);
    CreateCellsFormatting(workbook);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Sales Report");
    workbook.Save(outDir + u"FormatWorksheet_out.xls");

    Aspose::Cells::Cleanup();
}

void CreateReportData(Workbook& workbook)
{
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    cells.Get(u"B1").PutValue(u"Western Product Sales 2006");

    cells.Get(u"B2").PutValue(u"January");
    cells.Get(u"C2").PutValue(u"February");
    cells.Get(u"D2").PutValue(u"March");
    cells.Get(u"E2").PutValue(u"April");
    cells.Get(u"F2").PutValue(u"May");
    cells.Get(u"G2").PutValue(u"June");
    cells.Get(u"H2").PutValue(u"July");
    cells.Get(u"I2").PutValue(u"August");
    cells.Get(u"J2").PutValue(u"September");
    cells.Get(u"K2").PutValue(u"October");
    cells.Get(u"L2").PutValue(u"November");
    cells.Get(u"M2").PutValue(u"December");
    cells.Get(u"N2").PutValue(u"Total");

    cells.Get(u"A3").PutValue(u"Biscuits");
    cells.Get(u"A4").PutValue(u"Coffee");
    cells.Get(u"A5").PutValue(u"Tofu");
    cells.Get(u"A6").PutValue(u"Ikura");
    cells.Get(u"A7").PutValue(u"Choclade");
    cells.Get(u"A8").PutValue(u"Maxilaku");
    cells.Get(u"A9").PutValue(u"Scones");
    cells.Get(u"A10").PutValue(u"Sauce");
    cells.Get(u"A11").PutValue(u"Syrup");
    cells.Get(u"A12").PutValue(u"Spegesild");
    cells.Get(u"A13").PutValue(u"Filo Mix");
    cells.Get(u"A14").PutValue(u"Pears");
    cells.Get(u"A15").PutValue(u"Konbu");
    cells.Get(u"A16").PutValue(u"Kaviar");
    cells.Get(u"A17").PutValue(u"Zaanse");
    cells.Get(u"A18").PutValue(u"Cabrales");
    cells.Get(u"A19").PutValue(u"Gnocchi");
    cells.Get(u"A20").PutValue(u"Wimmers");
    cells.Get(u"A21").PutValue(u"Breads");
    cells.Get(u"A22").PutValue(u"Lager");
    cells.Get(u"A23").PutValue(u"Gravad");
    cells.Get(u"A24").PutValue(u"Telino");
    cells.Get(u"A25").PutValue(u"Pavlova");
    cells.Get(u"A26").PutValue(u"Total");

    cells.Get(u"B3").PutValue(5000);
    cells.Get(u"C3").PutValue(4500);
    cells.Get(u"D3").PutValue(6010);
    cells.Get(u"E3").PutValue(7230);
    cells.Get(u"F3").PutValue(5400);
    cells.Get(u"G3").PutValue(5030);
    cells.Get(u"H3").PutValue(3000);
    cells.Get(u"I3").PutValue(6000);
    cells.Get(u"J3").PutValue(9000);
    cells.Get(u"K3").PutValue(3300);
    cells.Get(u"L3").PutValue(2500);
    cells.Get(u"M3").PutValue(5510);

    cells.Get(u"B26").SetFormula(u"=SUM(B3:B25)");
    cells.Get(u"C26").SetFormula(u"=SUM(C3:C25)");
    cells.Get(u"D26").SetFormula(u"=SUM(D3:D25)");
    cells.Get(u"E26").SetFormula(u"=SUM(E3:E25)");
    cells.Get(u"F26").SetFormula(u"=SUM(F3:F25)");
    cells.Get(u"G26").SetFormula(u"=SUM(G3:G25)");
    cells.Get(u"H26").SetFormula(u"=SUM(H3:H25)");
    cells.Get(u"I26").SetFormula(u"=SUM(I3:I25)");
    cells.Get(u"J26").SetFormula(u"=SUM(J3:J25)");
    cells.Get(u"K26").SetFormula(u"=SUM(K3:K25)");
    cells.Get(u"L26").SetFormula(u"=SUM(L3:L25)");
    cells.Get(u"M26").SetFormula(u"=SUM(M3:M25)");

    cells.Get(u"N3").SetFormula(u"=SUM(B3:M3)");
    cells.Get(u"N4").SetFormula(u"=SUM(B4:M4)");
    cells.Get(u"N5").SetFormula(u"=SUM(B5:M5)");
    cells.Get(u"N6").SetFormula(u"=SUM(B6:M6)");
    cells.Get(u"N7").SetFormula(u"=SUM(B7:M7)");
    cells.Get(u"N8").SetFormula(u"=SUM(B8:M8)");
    cells.Get(u"N9").SetFormula(u"=SUM(B9:M9)");
    cells.Get(u"N10").SetFormula(u"=SUM(B10:M10)");
    cells.Get(u"N11").SetFormula(u"=SUM(B11:M11)");
    cells.Get(u"N12").SetFormula(u"=SUM(B12:M12)");
    cells.Get(u"N13").SetFormula(u"=SUM(B13:M13)");
    cells.Get(u"N14").SetFormula(u"=SUM(B14:M14)");
    cells.Get(u"N15").SetFormula(u"=SUM(B15:M15)");
    cells.Get(u"N16").SetFormula(u"=SUM(B16:M16)");
    cells.Get(u"N17").SetFormula(u"=SUM(B17:M17)");
    cells.Get(u"N18").SetFormula(u"=SUM(B18:M18)");
    cells.Get(u"N19").SetFormula(u"=SUM(B19:M19)");
    cells.Get(u"N20").SetFormula(u"=SUM(B20:M20)");
    cells.Get(u"N21").SetFormula(u"=SUM(B21:M21)");
    cells.Get(u"N22").SetFormula(u"=SUM(B22:M22)");
    cells.Get(u"N23").SetFormula(u"=SUM(B23:M23)");
    cells.Get(u"N24").SetFormula(u"=SUM(B24:M24)");
    cells.Get(u"N25").SetFormula(u"=SUM(B25:M25)");
    cells.Get(u"N26").SetFormula(u"=SUM(N3:N25)");
}

void CreateCellsFormatting(Workbook& workbook)
{
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    Style stl0 = workbook.CreateStyle();
    stl0.SetForegroundColor(Color{ 155, 204, 255 });
    stl0.SetPattern(BackgroundType::Solid);
    stl0.GetFont().SetName(u"Trebuchet MS");
    stl0.GetFont().SetSize(18);
    stl0.GetFont().SetColor(Color::Maroon());
    stl0.GetFont().SetIsBold(true);
    stl0.GetFont().SetIsItalic(true);

    StyleFlag flag;
    flag.SetCellShading(true);
    flag.SetFontName(true);
    flag.SetFontSize(true);
    flag.SetFontColor(true);
    flag.SetFontBold(true);
    flag.SetFontItalic(true);

    Row row = cells.GetRows().Get(0);
    row.ApplyStyle(stl0, flag);
    cells.SetRowHeight(0, 30);

    Style stl1 = workbook.CreateStyle();
    stl1.SetRotationAngle(45);
    stl1.SetForegroundColor(Color{ 0, 51, 105 });
    stl1.SetPattern(BackgroundType::Solid);
    stl1.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    stl1.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::White());
    stl1.SetHorizontalAlignment(TextAlignmentType::Center);
    stl1.SetVerticalAlignment(TextAlignmentType::Center);
    stl1.GetFont().SetName(u"Times New Roman");
    stl1.GetFont().SetSize(10);
    stl1.GetFont().SetColor(Color::White());
    stl1.GetFont().SetIsBold(true);

    flag = StyleFlag();
    flag.SetLeftBorder(true);
    flag.SetRotation(true);
    flag.SetCellShading(true);
    flag.SetHorizontalAlignment(true);
    flag.SetVerticalAlignment(true);
    flag.SetFontName(true);
    flag.SetFontSize(true);
    flag.SetFontColor(true);
    flag.SetFontBold(true);

    row = cells.GetRows().Get(1);
    row.ApplyStyle(stl1, flag);
    cells.SetRowHeight(1, 48);

    Style stl2 = workbook.CreateStyle();
    stl2.SetForegroundColor(Color{ 155, 204, 255 });
    stl2.SetPattern(BackgroundType::Solid);
    stl2.GetFont().SetName(u"Trebuchet MS");
    stl2.GetFont().SetColor(Color::Maroon());
    stl2.GetFont().SetSize(10);

    flag = StyleFlag();
    flag.SetCellShading(true);
    flag.SetFontName(true);
    flag.SetFontColor(true);
    flag.SetFontSize(true);

    Column col = cells.GetColumns().Get(0);
    col.ApplyStyle(stl2, flag);

    Style stl3 = workbook.CreateStyle();
    stl3.SetForegroundColor(Color{ 124, 199, 72 });
    stl3.SetPattern(BackgroundType::Solid);
    cells.Get(u"A2").SetStyle(stl3);

    Style stl4 = workbook.CreateStyle();
    stl4.GetFont().SetColor(Color{ 0, 51, 105 });
    stl4.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    stl4.GetBorders().Get(BorderType::BottomBorder).SetColor(Color{ 124, 199, 72 });
    stl4.SetForegroundColor(Color::White());
    stl4.SetPattern(BackgroundType::Solid);
    stl4.SetCustom(u"$#,##0.0");

    flag = StyleFlag();
    flag.SetFontColor(true);
    flag.SetCellShading(true);
    flag.SetNumberFormat(true);
    flag.SetBottomBorder(true);

    Style stl5 = workbook.CreateStyle();
    stl5.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    stl5.GetBorders().Get(BorderType::BottomBorder).SetColor(Color{ 124, 199, 72 });
    stl5.SetForegroundColor(Color{ 250, 250, 200 });
    stl5.SetPattern(BackgroundType::Solid);
    stl5.SetCustom(u"$#,##0.0");
    stl5.GetFont().SetColor(Color::Maroon());

    Range range = cells.CreateRange(u"B3", u"M25");
    range.SetName(u"MyRange");
    range.ApplyStyle(stl4, flag);

    for (int i = 0; i <= 22; i++)
    {
        for (int j = 0; j < 12; j++)
        {
            if (i % 2 == 0)
            {
                range.Get(i, j).SetStyle(stl5);
            }
        }
    }

    Style stl6 = workbook.CreateStyle();
    stl6.SetForegroundColor(Color{ 0, 51, 105 });
    stl6.SetPattern(BackgroundType::Solid);
    stl6.GetFont().SetName(u"Arial");
    stl6.GetFont().SetSize(10);
    stl6.GetFont().SetColor(Color::White());
    stl6.GetFont().SetIsBold(true);
    stl6.SetCustom(u"$#,##0.0");

    flag = StyleFlag();
    flag.SetCellShading(true);
    flag.SetFontName(true);
    flag.SetFontSize(true);
    flag.SetFontColor(true);
    flag.SetFontBold(true);
    flag.SetNumberFormat(true);

    row = cells.GetRows().Get(25);
    row.ApplyStyle(stl6, flag);

    for (int i = 2; i < 25; i++)
    {
        cells.Get(i, 13).SetStyle(stl6);
    }

    cells.SetColumnWidth(13, 9.33);
}
```
