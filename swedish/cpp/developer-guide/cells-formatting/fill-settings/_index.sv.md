---
title: Fyllningsinställningar med C++
linktitle: Fyllningsinställningar
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler. Det stöder inställning av fyllningsinställningar för celler, vilket gör det möjligt för användare att anpassa bakgrund och stil på cellerna. Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att ställa in cellfyllningsinställningar.
keywords: Aspose.Cells, Celler, Fyllningsinställningar, Bakgrund, Stil
type: docs
weight: 50
url: /sv/cpp/cells-fill-settings/
---

## **Färger och bakgrundsmönster**

Microsoft Excel kan ställa in förgrund (omridning) och bakgrundsfärger (fyllning) för celler och bakgrundsmönster.

Aspose.Cells stöder även dessa funktioner på ett flexibelt sätt. I det här avsnittet lär vi oss att använda dessa funktioner med hjälp av Aspose.Cells.

### **Inställning av färger och bakgrundsmönster**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innefattar en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-samling som tillåter åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

The [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) har [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) och [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) metoder som används för att hämta och sätta en cells formatering. Klassen [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) tillhandahåller egenskaper för att ange förgrund och bakgrundsfärger för cellerna. Aspose.Cells tillhandahåller en [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) uppräkning som innehåller en uppsättning fördefinierade typer av bakgrundsmönster som ges nedan.

|**Bakgrundsmönster**|**Beskrivning**|
| :- | :- |
|DiagonalCrosshatch|Representerar diagonalt kryssmönster|
|DiagonalStripe|Representerar diagonalt rutmönster|
|Gray6|Representerar 6,25% grått mönster|
|Gray12|Representerar 12,5% grått mönster|
|Gray25|Representerar 25% grått mönster|
|Gray50|Representerar 50% grått mönster|
|Gray75|Representerar 75% grått mönster|
|HorizontalStripe|Representerar horisontellt rutmönster|
|None|Representerar ingen bakgrund|
|ReverseDiagonalStripe|Representerar omvänd diagonalt rutmönster|
|Solid|Representerar enfärgat mönster|
|ThickDiagonalCrosshatch|Representerar tjockt diagonalt kryssmönster|
|ThinDiagonalCrosshatch|Representerar tunt diagonalt kryssmönster|
|ThinDiagonalStripe|Representerar tunt diagonalt rutmönster|
|ThinHorizontalCrosshatch|Representerar tunt horisontellt kryssmönster|
|ThinHorizontalStripe|Representerar tunt horisontellt rutmönster|
|ThinReverseDiagonalStripe|Representerar tunt omvänt diagonalt rutmönster|
|ThinVerticalStripe|Representerar tunt vertikalt rutmönster|
|VerticalStripe|Representerar vertikalt rutmönster|

I exemplet nedan är förgrundsfärgen för cellen A1 inställd men A2 är konfigurerad för att ha både förgrund och bakgrundsfärger med ett bakgrundsmönster med vertikal rand.

```c++
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

    // Adding a new worksheet to the Workbook object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Define a Style and get the A1 cell style
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    // Setting the foreground color to yellow
    style.SetForegroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A1 cell
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    // Get the A2 cell style
    style = worksheet.GetCells().Get(u"A2").GetStyle();

    // Setting the foreground color to blue
    style.SetForegroundColor(Color::Blue());

    // Setting the background color to yellow
    style.SetBackgroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A2 cell
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Viktigt att veta**

{{% alert color="primary" %}}

- För att ange en cells förgrund eller bakgrundsfärg, använd [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) objektets [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) eller [**GetBackgroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundcolor/) egenskaper. Båda egenskaperna kommer att ha effekt endast om [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) objektets [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) egenskap är konfigurerad.
- Egenskapen [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) sätter cellens skuggfärg.
  Egenskapen [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) anger typen av bakgrundsmönster som används för förgrund eller bakgrundsfärg. Aspose.Cells tillhandahåller en uppräkning, [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/). som innehåller en uppsättning fördefinierade typer av bakgrundsmönster.
- Om du väljer värdet *BackgroundType.None* från [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) uppräkningen, tillämpas inte förgrundsfärgen.
  Likaså tillämpas inte bakgrundsfärgen om du väljer värdena *BackgroundType.None* eller *BackgroundType.Solid*.
- Vid hämtning av cellens skugg-/fyllfärg, om [**Style.GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) är *BackgroundType.None*, kommer [**Style.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) att returnera *Color.Empty*.

{{% /alert %}}

### **Tillämpning av gradientfylleffekter**

För att applicera önskade gradientfylleffekter på cellen, använd [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) objektets [**SetTwoColorGradient**](https://reference.aspose.com/cells/cpp/aspose.cells/style/settwocolorgradient/) metod enligt behov.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::System;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(2, 1).PutValue(u"test");

    Cell cell = worksheet.GetCells().Get(u"B3");
    Style style = cell.GetStyle();
    style.SetIsGradient(true);
    style.SetTwoColorGradient(
        Color{ 0xFF, 0xFF, 0xFF, 0xFF },
        Color{ 0xFF, 0x4F, 0x81, 0xBD },
        GradientStyleType::Horizontal,
        1
    );

    style.GetFont().SetColor(Color::Red());
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    worksheet.GetCells().SetRowHeightPixel(2, 53);
    worksheet.GetCells().Merge(2, 1, 1, 2);

    workbook.Save(outDir + u"output.xlsx");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Färger och Palett**

En palett är antalet färger som är tillgängliga för att skapa en bild. Användningen av en standardiserad palett i en presentation gör att användaren kan skapa en enhetlig look. Varje Microsoft Excel (97-2003) fil har en palett med 56 färger som kan tillämpas på celler, teckensnitt, rutnät, grafiska objekt, fyllningar och linjer i en graf.

Med Aspose.Cells är det möjligt att inte bara använda palettens befintliga färger utan också anpassade färger. Innan du använder en anpassad färg, lägg till den först i paletten.

Detta ämne diskuterar hur man lägger till anpassade färger i paletten.

### **Lägga till Anpassade Färger i Paletten**

Aspose.Cells stöder Microsoft Excels 56-färgspalett. För att använda en anpassad färg som inte är definierad i paletten, lägg till färgen i paletten.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) tillhandahåller en [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/)-metod som tar följande parametrar för att lägga till en anpassad färg för att ändra paletten:

- Anpassad färg, den anpassade färgen som ska läggas till.
- Index, index för färgen i paletten som den anpassade färgen kommer att ersätta. Ska vara mellan 0-55.

Exemplet nedan lägger till en anpassad färg (Orchid) i paletten innan den tillämpas på en font.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid color is now in the palette
    std::cout << "Is Orchid in palette after change: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Paletten rymmer endast 56 färger. När du lägger till en anpassad färg i paletten ändras paletten och alla element i filen formaterade med den tidigare färgen ändras. Så, när du ändrar paletten, var mycket försiktig. Dessutom är detta begränsningen i XLS (Excel 97 - 2003) filformat endast då det inte finns någon sådan begränsning för XLSX eller andra avancerade MS Excel (2007/2010 eller 2013) filformat.

{{% /alert %}}
