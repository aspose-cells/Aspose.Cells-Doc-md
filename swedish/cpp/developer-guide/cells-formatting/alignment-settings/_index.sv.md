---
title: Justeringsinställningar med C++
linktitle: Justeringsinställningar
description: I Aspose.Cells biblioteket kan du använda celljusteringsinställningar för att justera layouten och visningen av text. Genom att justera inställningar som horisontell justering, vertikal justering och textradbrytning har du mer kontroll över hur text flödar i celler. Detta dokument ger dig detaljerade steg och kodexempel för att snabbt lära dig hur du använder Aspose.Cells för celljusteringsinställningar.
keywords: Aspose.Cells, celljustering, horisontell justering, vertikal justering, textombrytning
type: docs
weight: 20
url: /sv/cpp/cells-alignment-settings/
---

## **Konfigurera justeringsinställningar**

### **Justeringsinställningar i Microsoft Excel**

Alla som har använt Microsoft Excel för att formatera celler kommer att vara bekanta med justeringsinställningarna i Microsoft Excel.

Som du kan se från figuren ovan, finns det olika typer av justeringsalternativ:

- Textjustering (horisontell & vertikal)
- Indrag.
- Orientering.
- Textkontroll.
- Textriktning.

Alla dessa justeringsinställningar stöds fullt ut av Aspose.Cells och diskuteras mer detaljerat nedan.

### **Justeringsinställningar i Aspose.Cells**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som tillåter åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen tillhandahåller en [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) samling. Varje objekt i [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) klassen.

Aspose.Cells tillhandahåller [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) och [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) metoder för klassen [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) som används för att få och ställa in en cells formatering. Klassen [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) tillhandahåller användbara egenskaper för att konfigurera justeringsinställningar.

Välj vilken som helst textjusteringstyp med hjälp av uppräkningen [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/). De fördefinierade textjusteringstyperna i uppräkningen [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/) är:

|**Textjusteringstyper**|**Beskrivning**|
| :- | :- |
|Bottom|Representerar bottenjustering av text|
|Center|Representerar mittenjustering av text|
|CenterAcross|Representerar mittenöverjustering av text|
|Distributed|Representerar fördelad textjustering|
|Fill|Representerar fyll textjustering|
|General|Representerar generell textjustering|
|Justify|Representerar rättfärdig textjustering|
|Left|Representerar vänsterjustering av text|
|Right|Representerar högerjustering av text|
|Top|Representerar toppjustering av text|
|JustifiedLow|Justerar texten med en justerad kashida-längd för arabisk text.|
|ThaiDistributed|Distribuerar thailändsk text särskilt, eftersom varje tecken behandlas som ett ord.|

{{% alert color="primary" %}}

Du kan också tillämpa inställningen för rättfärdigad distribution med hjälp av egenskapen [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/cpp/aspose.cells/style/isjustifydistributed/).

{{% /alert %}}

#### **Horisontell justering**

Använd [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) objektets [**GetHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gethorizontalalignment/) egenskap för att justera texten horisontellt.

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

    // Obtain the reference of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Set the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Vertikal justering**

Liknande horisontell justering, använd [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) objektets [**GetVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getverticalalignment/) egenskap för att justera texten vertikalt.

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

    // Create workbook
    Workbook workbook;

    // Clearing all the worksheets
    workbook.GetWorksheets().Clear();

    // Adding a new worksheet to the Excel object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Setting the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();

    // Setting the vertical alignment of the text in a cell
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Indrag**

Det är möjligt att ange indelningsnivån för texten i en cell med [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) objektets [**GetIndentLevel()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getindentlevel/) egenskap.

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
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the indentation level
    style.SetIndentLevel(2);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Orientering**

Ange orienteringen (rotationen) för texten i en cell med [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) objektets [**GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/) egenskap.

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
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the rotation angle of the text to 25 degrees
    style.SetRotationAngle(25);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook in Excel 97-2003 format
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Textkontroll**

I följande avsnitt diskuteras hur man kontrollerar text genom att ställa in textbrytning, krympa till passa och andra formateringsalternativ.

##### **Textindrag**

Att rada text i en cell gör det lättare att läsa: cellens höjd justeras för att passa all text istället för att klippa av den eller få den att rinna över i intilliggande celler. Ange textombrytning på eller av med [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) objektets [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) egenskap.

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

    // Create Workbook Object
    Workbook wb;

    // Open first Worksheet in the workbook
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Cells cell = ws.GetCells();

    // Increase the width of First Column Width
    cell.SetColumnWidth(0, 35);

    // Increase the height of first row
    cell.SetRowHeight(0, 36);

    // Add Text to the First Cell
    cell.Get(0, 0).PutValue(u"I am using the latest version of Aspose.Cells to test this functionality");

    // Make Cell's Text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    wb.Save(outDir + u"WrappingText_out.xlsx");

    std::cout << "Text wrapping applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Krympa passande**

Ett alternativ för att rada text i ett fält är att krympa textstorleken för att passa en cells dimensioner. Detta görs genom att ställa in [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) objektets [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) egenskap till **true**.

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
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set shrink to fit
    style.SetShrinkToFit(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Sammanfoga celler**

Liksom Microsoft Excel stöder Aspose.Cells att sammanfoga flera celler till en. Aspose.Cells tillhandahåller två tillvägagångssätt för denna uppgift. Ett sätt är att anropa [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) samlingen [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) metod. [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) metoden tar följande parametrar för att sammanfoga cellerna:

- Första rad: den första raden från vilken sammanfogningen ska börja.
- Första kolumn: den första kolumnen från vilken sammanfogningen ska börja.
- Antal rader: antalet rader att sammanfoga.
- Antal kolumner: antalet kolumner att sammanfoga.

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

Det andra sättet är att först anropa [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) samlingen [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) metod för att skapa en räckvidd av celler som ska sammanfogas. [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) metoden tar samma parametrar som [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) metoden som diskuterades ovan och returnerar ett [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) objekt. [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) objektet tillhandahåller också en [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) metod som sammanfogar den angivna räckvidden i [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) objektet.

##### **Textriktning**

Det är möjligt att ställa in läsordningen för text i celler. Läsordningen är den visuella ordningen där tecken, ord osv. visas. Till exempel är engelska ett vänster-till-höger-språk medan arabiska är ett höger-till-vänster-språk.

Läsordningen ställs in med [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) objektets [**GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gettextdirection/) egenskap. Aspose.Cells tillhandahåller fördefinierade textriktningstyper i [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/) uppräkning.

|**Textriktningstyper**|**Beskrivning**|
| :- | :- |
|Context| Läsordningen som är konsekvent med språket för det första inmatade tecknet
|LeftToRight|Vänster till höger-läsordning
|RightToLeft|Höger till vänster-läsordning

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"I am using the latest version of Aspose.Cells to test this functionality.");

    // Get the style of cell A1
    Style style = cell.GetStyle();

    // Set text direction to left-to-right
    style.SetTextDirection(TextDirectionType::LeftToRight);

    // Apply the modified style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(u"book1.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Fortsatta ämnen**
- [Ändra cellers justering och behåll befintlig formatering](/cells/sv/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Radbrytningar och textindrag](/cells/sv/cpp/line-breaks-and-text-wrapping/)
