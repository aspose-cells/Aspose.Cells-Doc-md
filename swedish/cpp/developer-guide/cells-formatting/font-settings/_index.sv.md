---
title: Teckensnittinställningar med C++
linktitle: Fontinställningar
type: docs
weight: 30
url: /sv/cpp/cells-font-settings/
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler. Det stöder inställning av teckensnitt för celler, vilket gör det möjligt för användare att anpassa stil och egenskaper för teckensnitt. Denna artikel visar hur man använder Aspose.Cells biblioteket för att ställa in teckensnitt i celler.
keywords: Aspose.Cells, Cells, Fontinställningar, Stilar, Egenskaper
---

{{% alert color="primary" %}}

Utseendet och känslan av en text kan styras genom att ändra teckensnittsinställningar. Teckensnittsinställningarna kan inkludera namn, stil, storlek, färg och andra effekter för teckensnitt. Precis som Microsoft Excel stöder Aspose.Cells konfiguration av teckensnitt i cellerna.

{{% /alert %}}

## **Konfigurera fontinställningar**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-samling som möjliggör åtkomst till varje kalkylblad i en Excelfil. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller en [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-samling. Varje objekt i [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells tillhandahåller klassens [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) metoder [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) och [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) som används för att hämta och ställa in cellens formateringsstil. Klassen [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) tillhandahåller egenskaper för att konfigurera fontinställningar.

### **Ange fontnamn**

Utvecklare kan tillämpa vilken font som helst på text inuti en cell genom att använda [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) objektets [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) egenskap.

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font name to "Times New Roman"
    style.GetFont().SetName(u"Times New Roman");

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Ange fontstil till Fetstil**

Utvecklare kan göra texten fet genom att ställa in objektets [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) egenskap [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) till **true**.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font weight to bold
    style.GetFont().SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Inställning av fontstorlek**

Ställ in fontstorlek med objektets [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) egenskap [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font size to 14
    style.GetFont().SetSize(14);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Sätt Typsnittsfärg**

 Använd [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) objektets [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) egenskap för att ställa in teckensnittfärgen. Välj vilken färg som helst från Color-enum (del av C++-ramverket) och tilldela den till [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) egenskapen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font color to blue
    style.GetFont().SetColor(Color::Blue());

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```

### **Inställning av font underlinjetyp**

Använd objektets [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) egenskap [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) för att understryka text. Aspose.Cells erbjuder olika fördefinierade teckenstilunderstrykningstyper i [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/)-utseendet.

|**Font Underline Types**|**Beskrivning**|
| :- | :- |
|Accounting|Enkel redovisningsunderstrykning|
|Double|Dubbel understrykning|
|DoubleAccounting|Dubbel redovisningsunderstrykning|
|None|Ingen understrykning|
|Single|Enkel understrykning|

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font to be underlined
    style.GetFont().SetUnderline(FontUnderlineType::Single);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Inställning för överstruken effekt**

Tillämpa överstrykning genom att ställa in objektets [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) egenskap [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) till **true**.

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

    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Hello Aspose!");

    Style style = cell.GetStyle();
    style.GetFont().SetIsStrikeout(true);
    cell.SetStyle(style);

    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Inställning av understreckningseffekt**

Tillämpa understreckning genom att ställa in objektets [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) egenskap [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) till **true**.

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set subscript effect
    style.GetFont().SetIsSubscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Inställning av överstruken effekt på font**

Utvecklare kan applicera överstruken effekt på fonten genom att ställa in [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) egenskapen för objektet [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) till **true**.

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set superscript effect
    style.GetFont().SetIsSuperscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Fortsatta ämnen**
- [Applicera Superscript- och Subscript-effekter på typsnitt](/cells/sv/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Få en lista över typsnitt som används i en kalkylblad eller arbetsbok](/cells/sv/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
{{< app/cells/assistant language="cpp" >}}
