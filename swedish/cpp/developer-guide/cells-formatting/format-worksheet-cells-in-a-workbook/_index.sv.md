---
title: Formatera arbetsbladsceller i en arbetsbok med C++
linktitle: Formatera arbetsbladsceller
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler. Det stöder formatering av arbetsbladsceller i arbetsboken, vilket ger användare möjlighet att anpassa cellernas utseende och stil. Denna artikel visar hur man formaterar arbetsbladsceller med Aspose.Cells biblioteket.
keywords: Aspose.Cells, Workbook, Worksheet, Cell, Formatting, Appearance, Style
type: docs
weight: 2000
url: /sv/cpp/format-worksheet-cells-in-a-workbook/
---

{{% alert color="primary" %}}

Den här artikeln visar hur du:

1. Använd stilar för att snabbt formatera data.
1. Formatera celler i rader och kolumner.
1. Använd gränser och färger för att betona data.
1. Tillämpa nummerformat för att betona data.
1. Använd typsnitt och attribut för att markera data.
1. Formatera data i en namngiven omfattning.
1. Ändra datajustering och orientering.
1. Ställ in radhöjd och kolumnbredd.

Exempelprojektet utför alla dessa uppgifter och ger utvecklare en detaljerad beskrivning av hur man skapar en arbetsbok, lägger till data och tillämpar formatering med [Aspose.Cells](https://products.aspose.com/cells/cpp/).

{{% /alert %}}

## **Dataformatering**

Formatering används för att skilja mellan olika typer av information och för att tydligt visa data.

Ett format representerar en stil och är definierat som en uppsättning egenskaper, såsom typsnitt och typsnittstorlekar, nummerformat, cellgränser, cellskuggning, indragning, justering och textorientering. Gränser ger ytterligare sätt att markera information. En gräns är en linje som dras runt en cell eller en grupp av celler.

Nummerformat gör också data mer meningsfull. Genom att tillämpa olika nummerformat kan du ändra utseendet på nummer utan att ändra numret bakom utseendet.

Aspose.Cells ger dig möjlighet att dra ramar runt celler och områden på ett enkelt sätt. Det låter dig också applicera fonter och skugga celler. Komponenten är tillräckligt effektiv så att du kan formatera en hel rad eller kolumn, ställa in justeringar, radbrytningar och rotera text i celler. Aspose.Cells stöder dessutom alla nummerformat som stöds av Microsoft Excel.

 Denna artikel visar hur man skapar en konsolapplikation i Visual Studio som genererar en årlig försäljningsrapport. Arbetsboken skapas från början, därefter infogas data och arket formateras. Vi visar hur man skapar en enkel konsolapplikation som skapar en Excel-arbetsbok (du kan även använda en mallfil), infogar försäljningsdata i det första arket, formaterar data och sparar en Excel-fil.

### **Process**

Nedan är stegen för hur man skapar en kalkylblad och formaterar olika celler i olika rader och kolumner i ett kalkylblad.

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++.
   1. Installera det på din utvecklingsdator.
1. Skapa ett projekt och lägg till referenser:
   1. Starta Visual Studio.
   1. Skapa en ny konsolapplikation.
   1. Lägg till en referens till Aspose.Cells, till exempel ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Lägg till följande kod i projektet:

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
