---
title: Excel teman och färger med C++
linktitle: Excel teman och färger
type: docs
weight: 100
url: /sv/cpp/excel-themes-and-colors/
description: C++ kod för att använda Excel färgschema med Aspose.Cells for C++ API
keywords: C++ för att skapa och tillämpa färgscheman, C++ programmatisk skapa ett anpassat färgschema, hur man programmatisk tillämpar ett anpassat färgschema, c++ hur man använder färgschema i excel
---

## **Hur man tillämpar och skapar färgschema i Excel**
Dokumentteman gör det enkelt att koordinera färger, teckensnitt och grafisk formateringseffekter för Excel-dokument och uppdatera dem snabbt. 
Teman ger en enhetlig look med namngivna stilar, grafiska effekter och andra objekt som används i en arbetsbok. Till exempel ser Accent1-stilen annorlunda ut i Office och Apex-temana. Ofta tillämpar du ett dokumenttema och ändrar det sedan efter hur du vill ha det.

### **Hur man tillämpar ett färgschema i Excel**
1. Öppna Excel och gå till fliken "Sidlayout" i Excel-ribbonen.
1. Klicka på knappen "Färger" i avsnittet "Teman".
<br>
<img src="color.png" width=70% />
1. Välj en färgpalett som matchar dina krav eller sväva över en schema för att se en förhandsgranskning i realtid.

### **Hur man skapar en anpassad färgpalett i Excel**
Du kan skapa din egen färguppsättning för att ge ditt dokument en fräsch, unik look eller följa din organisations varumärkesstandard.

1. Öppna Excel och gå till fliken "Sidlayout" i Excel-ribbonen.
1. Klicka på knappen "Färger" i avsnittet "Teman".
1. Klicka på knappen "Anpassa färger...".
<br>
<img src="color2.png" width=70% />

1. I dialogrutan "Skapa nya temafärger" kan du välja färger för varje element genom att klicka på färgnedtagningarna bredvid dem. Du kan välja färger från paletten eller definiera anpassade färger med hjälp av alternativet "Fler färger".
<br>
<img src="color3.png" width=70% />
1. Efter att ha valt alla önskade färger, ange ett namn för din anpassade färgpalett i fältet "Namn".

1. Klicka på knappen "Spara" för att spara din anpassade färgpalett. Din anpassade färgpalett kommer nu att finnas tillgänglig i rullgardinsmenyn "Färger" för framtida användning.

## **Hur man skapar och tillämpar färgpalett i Aspose.Cells**
Aspose.Cells ger funktioner för anpassning av teman och färger.

### **Hur man skapar anpassat färgtema i Aspose.Cells**
Om färgteman används i filen behöver vi inte modifiera varje cell individuellt, vi behöver bara ändra färgerna i temat.

Nedan följer ett exempel på hur man tillämpar anpassade teman med önskade färger. Vi använder en provmall manuellt skapad i Microsoft Excel 2007.

Följande exempel laddar en mall XLSX-fil, definierar färger för olika temafärgtyper, applicerar de anpassade färgerna och sparar excelfilen.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Define Color array (of 12 colors) for Theme
    Vector<Aspose::Cells::Color> carr(12);
    carr[0] = Color::AntiqueWhite(); // Background1
    carr[1] = Color::Brown();       // Text1
    carr[2] = Color::AliceBlue();   // Background2
    carr[3] = Color::Yellow();      // Text2
    carr[4] = Color::YellowGreen(); // Accent1
    carr[5] = Color::Red();         // Accent2
    carr[6] = Color::Pink();        // Accent3
    carr[7] = Color::Purple();      // Accent4
    carr[8] = Color::PaleGreen();   // Accent5
    carr[9] = Color::Orange();      // Accent6
    carr[10] = Color::Green();      // Hyperlink
    carr[11] = Color::Gray();       // Followed Hyperlink

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Instantiate a Workbook and open the template file
    Workbook workbook(inputFilePath);

    // Set the custom theme with specified colors
    workbook.CustomTheme(u"CustomeTheme1", carr);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Save as the excel file
    workbook.Save(outputFilePath);

    std::cout << "Custom theme applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Hur man tillämpar temafärger i Aspose.Cells**

Det följande exemplet applicerar en cells förgrund och fontfärger baserat på standardtema (av arbetsbok) färgtyper. Det sparar också excelfilen på disken.

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

    // Get cells collection in the first (default) worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Get the D3 cell
    Cell c = cells.Get(u"D3");

    // Get the style of the cell
    Style s = c.GetStyle();

    // Set foreground color for the cell from the default theme Accent2 color
    s.SetForegroundThemeColor(ThemeColor(ThemeColorType::Accent2, 0.5));

    // Set the pattern type
    s.SetPattern(BackgroundType::Solid);

    // Get the font for the style
    Font f = s.GetFont();

    // Set the theme color
    f.SetThemeColor(ThemeColor(ThemeColorType::Accent4, 0.1));

    // Apply style
    c.SetStyle(s);

    // Put a value
    c.PutValue(u"Testing1");

    // Save the excel file
    workbook.Save(outDir + u"output.out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Hur man får och ställer in temafärger i Aspose.Cells**
 Nedan följer några metoder och egenskaper som implementerar temafärger.

- [**Style.GetForegroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundthemecolor/): Används för att ställa in förgrundsfärgen.
- [**Style.GetBackgroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundthemecolor/): Används för att ställa in bakgrundsfärgen.
- [**Font.GetThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getthemecolor/): Används för att ställa in teckensnittsfärgen.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getthemecolor/): Används för att hämta ett tema i färg.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setthemecolor/): Används för att ställa in ett tema i färg.

Följande exempel visar hur man hämtar och ställer in tema färger.

Följande exempel använder en mall XLSX-fil, hämtar färgerna för olika temafärgtyper, ändrar färgerna och sparar Microsoft Excel-filen.

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
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Background1 theme color
    Color c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the color
    std::cout << "theme color Background1: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Get the Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the color
    std::cout << "theme color Accent2: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Background1 theme color
    workbook.SetThemeColor(ThemeColorType::Background1, Color::Red());

    // Get the updated Background1 theme color
    c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the updated color for confirmation
    std::cout << "theme color Background1 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Accent2 theme color
    workbook.SetThemeColor(ThemeColorType::Accent2, Color::Blue());

    // Get the updated Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the updated color for confirmation
    std::cout << "theme color Accent2 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Save the updated file
    workbook.Save(outputFilePath);

    std::cout << "Theme colors updated and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Fortsatta ämnen**
- [Extrahera temadata från Excel-fil](/cells/sv/cpp/extract-theme-data-from-excel-file/)
