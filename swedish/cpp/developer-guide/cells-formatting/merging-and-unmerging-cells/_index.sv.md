---
title: Merging och upplösning av celler med C++
linktitle: Sammanfoga och dela upp celler
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler, som stöder sammanslagning och upplösning av celler. Denna artikel introducerar hur man slår samman och upplöser celler med Aspose.Cells biblioteket och hur man anpassar den sammanslagna cellens stil.
keywords: Aspose.Cells, C++ bibliotek, kalkylblad, slå samman celler, upplösa celler, stilinställningar, anpassade stilar
type: docs
weight: 190
url: /sv/cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells stöder den här funktionen och kan också sammanslå celler i ett kalkylblad. Du kan också dela upp eller splittra de sammanslagna cellerna. En sammanslagen cells cellreferens är referensen för den översta vänstra cellen i det ursprungliga markerade området.

{{% /alert %}} 

## **Introduktion**
Du vill inte alltid ha samma antal celler i varje rad eller kolumn. Till exempel kan du vilja lägga en titel i en cell som spänner över flera kolumner. Eller om du skapar en faktura kan du vilja ha färre kolumner för den totala summan. För att göra en cell från två eller flera celler, sammanslag dem. Microsoft Excel låter användare välja filer och sammanfoga dem för att strukturera kalkylbladet på önskat sätt.

{{% alert color="primary" %}} 

Observera att när celler sammanslås behålls endast data i de översta vänstra cellerna. Om det finns data i de andra cellerna i området raderas denna data.
Formatering är också baserad på referenscellen så att när du sammanslår celler tillämpas formateringsinställningarna för den översta vänstra cellen i området på den sammanslagna cellen. När cellen splittas behåller de nya cellerna sina ursprungliga formateringsinställningar.

{{% /alert %}} 

## **Sammanslagning av celler i ett kalkylblad**
### **Sammanslagning av celler i Microsoft Excel**
Följande steg beskriver hur man sammanslår celler i kalkylbladet med hjälp av MS Excel.

1. Kopiera den data du vill ha till den övre vänstra cellen inom området.
1. Välj cellerna du vill sammanfoga.
1. För att sammanfoga celler i en rad eller kolumn och centrera cellinnehållet klickar du på ikonen **Sammanfoga och centrerat** på verktygsfältet **Formatering**.

### **Sammanslagning av celler med Aspose.Cells**
`Aspose::Cells::Cells`-klassen har några användbara metoder för denna uppgift. Till exempel slår metoden `Merge()` samman cellerna till en enskild cell inom ett specificerat område.

Följande exempel visar hur man slår samman celler (C6:E7) i en arbetsbok.

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

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Avfussning (delning) av sammanslagna celler**
### **Använda Microsoft Excel**
Följande steg beskriver hur man delar sammanslagna celler med hjälp av Microsoft Excel.

1. Välj den sammanslagna cellen.
   När cellerna har kombinerats väljs **Slå samman och centrera** på **Formateringsverktygsfältet**.
1. Klicka på **Slå samman och centrera** på **Formateringsverktygsfältet**.

### **Använda Aspose.Cells**
 Klassen `Aspose::Cells::Cells` har en metod som heter `UnMerge()` som delar upp cellerna till deras ursprungliga tillstånd. Metoden upplöser cellerna med hjälp av cellreferensen i det sammanslagna cellområdet.

Följande exempel visar hur man delar de sammanslagna cellerna (C6). Exemplet använder filen som skapades i det föregående exemplet och delar de sammanslagna cellerna.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"mergingcells.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"unmergingcells.out.xls";

    // Create a Workbook and open the excel file
    Workbook wbk(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Get the Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Unmerge the cells
    cells.UnMerge(5, 2, 2, 3);

    // Save the file
    wbk.Save(outputFilePath);

    std::cout << "Cells unmerged successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Fortsatta ämnen**
- [Identifiera sammanslagna celler i ett kalkylblad](/cells/sv/cpp/detect-merged-cells-in-a-worksheet/)
