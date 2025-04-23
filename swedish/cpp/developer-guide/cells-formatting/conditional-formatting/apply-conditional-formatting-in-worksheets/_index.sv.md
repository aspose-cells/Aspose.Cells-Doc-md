---
title: Tillämpa villkorsformatering i arbetsblad med C++
linktitle: Tillämpa villkorsformatering
description: Hur man använder Aspose.Cells biblioteket i C++ för att tillämpa villkorsformatering i arbetsblad. Genom att justera dessa kriterier får du mer kontroll över hur cellerna ser ut och visas.
keywords: Aspose.Cells, Villkorsformatering, C++, Arbetsblad, Formatering
type: docs
weight: 130
url: /sv/cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Den här artikeln syftar till att ge en detaljerad förståelse för hur man lägger till villkorlig formatering till en rad celler i ett arbetsblad.

Villkorlig formatering är en avancerad funktion i Microsoft Excel som gör det möjligt att tillämpa format på en rad celler och ha den formateringen ändras beroende på cellens värde eller värdet på en formel. Till exempel kan bakgrunden för en cell vara röd för att markera ett negativt värde eller textfärgen kan vara grön för ett positivt värde. När cellens värde uppfyller formatvillkoret tillämpas formatet. Om cellens värde inte uppfyller formatvillkoret används cellens standardformatering.

Det är möjligt att tillämpa villkorlig formatering med Microsoft Office Automation men det har sina nackdelar. Det finns flera skäl och problem involverade: till exempel säkerhet, stabilitet, skalbarhet och hastighet. Det främsta skälet till att hitta en annan lösning är att Microsoft själva starkt avråder från Office Automation för programvarulösningar.

Den här artikeln visar hur du skapar en konsolapplikation, lägger till villkorlig formatering på celler med några få enklaste kodrader med hjälp av Aspose.Cells API.

{{% /alert %}}

## **Använda Aspose.Cells för att tillämpa villkorlig formatering baserat på cellvärde**

1. **Ladda ner och installera Aspose.Cells**.
   1. Ladda ner Aspose.Cells for C++.
1. Installera det på din utvecklingsdator.
   Alla Aspose-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar endast vattenstämplar i producerade dokument.
1. **Skapa ett projekt**.
   Starta ditt C++-utvecklingsmiljö och skapa ett nytt konsolprogram.
1. **Lägg till referenser**.
   Lägg till en referens till Aspose.Cells i ditt projekt, till exempel en referens till ….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. **Tillämpa villkorlig formatering baserat på cellvärde**.
   Nedan är koden som används för att utföra uppgiften. Den tillämpar villkorlig formatering på en cell.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the FormatConditionCollection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(0, 0, 0, 0);

    // Add the cell area to the format condition collection
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Sets the background color
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

När den ovan nämnda koden körs, tillämpas villkorlig formatering på cell "A1" i det första arket i utdatafilen (output.xls). Den villkorsstyrda formateringen som tillämpas på A1 beror på cellens värde. Om cellens värde i A1 är mellan 50 och 100 är bakgrundsfärgen röd på grund av den tillämpade villkorliga formateringen.

## **Använd Aspose.Cells för att tillämpa villkorlig formatering baserat på formel**

1. **Tillämpa villkorsformatering beroende på formel (Kodexempel)**
   Nedan är koden för att utföra uppgiften. Den tillämpar villkorlig formatering på B3.

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

    // Create workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the conditional formatting collection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(2, 1, 2, 1);

    // Add the area to the conditional formatting
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::Expression);

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Set the formula for the condition
    fc.SetFormula1(u"=IF(SUM(B1:B2)>100,TRUE,FALSE)");

    // Set the background color
    Style style = fc.GetStyle();
    style.SetBackgroundColor(Color::Red());
    fc.SetStyle(style);

    // Set the formula for cell B3
    sheet.GetCells().Get(u"B3").SetFormula(u"=SUM(B1:B2)");

    // Set the value for cell C4
    sheet.GetCells().Get(u"C4").PutValue(u"If Sum of B1:B2 is greater than 100, B3 will have RED background");

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

När den ovan nämnda koden körs, tillämpas villkorlig formatering på cell "B3" i det första arket i utdatafilen (output.xls). Den tillämpade villkorsstyrda formateringen beror på formeln som beräknar värdet av "B3" som summan av B1 & B2.
