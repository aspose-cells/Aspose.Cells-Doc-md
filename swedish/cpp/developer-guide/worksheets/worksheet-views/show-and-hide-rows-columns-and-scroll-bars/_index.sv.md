---
title: Visa och Dölj Rader, Kolumner och Skrollfält med C++
linktitle: Visa och Dölj Rader, Kolumner och Skrollfält
type: docs
weight: 20
url: /sv/cpp/show-and-hide-rows-columns-and-scroll-bars/
description: Denna artikel demonstrerar hur man programmässigt visar och döljer Excel arkets rader och kolumner med C++ språket och Aspose.Cells API. Synligheten för skrollfält kan justeras, och flera rader och kolumner kan döljas.
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller sätt att kontrollera synligheten av rader, kolumner och skrollfält i ett kalkylblad.

{{% /alert %}}

## **Visa och göm rader och kolumner**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som tillåter utvecklare att komma åt varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-klassen. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samling som representerar alla celler i arbetsbladet. [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samlingen innehåller flera metoder för att hantera rader eller kolumner i ett arbetsblad. Några av dessa diskuteras nedan.

### **Visa Rader och Kolumner**

Utvecklare kan visa vilken dold rad eller kolumn som helst genom att anropa metoderna [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/) och [**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/) av [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samlingen respektive. Båda metoder tar två parametrar:

- **Rad- eller kolumnindex** - index för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.
- **Radhöjd eller kolumnbredd** - radhöjden eller kolumnbredden tilldelad till raden eller kolumnen efter att ha visats.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhiding the 3rd row and setting its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhiding the 2nd column and setting its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

När du gör en dold kolumn synlig, och du behöver återställa den till den tidigare tilldelade bredden eller till sin ursprungliga bredd, vänligen avdölj kolumnen med en negativ bredd. Till exempel: `worksheet->GetCells()->UnhideColumn(5, -1)`.

{{% /alert %}}

### **Dölj Rader och Kolumner**

Utvecklare kan dölja en rad eller kolumn genom att anropa metoderna [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/) och [**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/) av [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samlingen respektive. Båda metoder tar rad- och kolumnindex som parameter för att dölja den specifika raden eller kolumnen.

```cpp
#include <iostream>
#include <memory>
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Det är också möjligt att dölja en rad eller kolumn genom att ställa in radhöjden eller kolumnbredden till 0 respektive.

{{% /alert %}}

### **Dölj Flera Rader och Kolumner**

Utvecklare kan dölja flera rader eller kolumner samtidigt genom att anropa metoderna [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/) och [**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/) av [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samlingen respektive. Båda metoder tar startrad- eller startkolumnindex och antalet rader eller kolumner som ska döljas som parametrar.

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Visa och dölj bildrullningsfält**

Rullningslistor används för att navigera bland innehållet i en fil. Vanligtvis finns det två typer av rullningslistor:

- Vertikala bildrullningsfält
- Horisontella bildrullningsfält

Microsoft Excel tillhandahåller också horisontella och vertikala bildrullningsfält så att användare kan bläddra genom arbetsbladets innehåll. Med Aspose.Cells kan utvecklare kontrollera synligheten av båda typer av bildrullningsfält i Excelfiler.

### **Kontrollera Synligheten för Rullningslistor**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-klassen erbjuder ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten för skrollfält, använd [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-klassens [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) och [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) egenskaper. [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) och [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) är Boolean-egenskaper, vilket innebär att dessa egenskaper endast kan lagra **true** eller **false** värden.

#### **Gör bildrullningsfält synliga**

Gör rullningsfält synliga genom att ställa in [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) -klassens egenskaper [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) eller [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) till **true**.

#### **Dölja bildrullningsfält**

Dölj rullningsfält genom att ställa in egenskaperna [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) -klassens [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) eller [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) till **false**.

**Exempelkod**

Nedan finns ett komplett kodexempel som öppnar en Excel-fil, `book1.xls`, döljer båda skrollfälten och sedan sparar den modifierade filen som `output.xls`.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Hide the vertical scroll bar of the Excel file
    workbook.GetSettings().SetIsVScrollBarVisible(false);

    // Hide the horizontal scroll bar of the Excel file
    workbook.GetSettings().SetIsHScrollBarVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Scroll bars hidden successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
