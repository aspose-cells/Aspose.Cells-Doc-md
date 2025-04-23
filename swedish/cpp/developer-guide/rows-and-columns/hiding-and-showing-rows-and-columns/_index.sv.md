---
title: Dölj och visa rader och kolumner med C++
linktitle: Dölja och visa rader och kolumner
type: docs
weight: 60
url: /sv/cpp/hiding-and-showing-rows-and-columns/
description: Lär dig hur du döljer och visar rader och kolumner i Excel filer programmässigt med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Ibland kan det vara meningsfullt att dölja vissa rader eller kolumner i ett kalkylblad och visa dem senare. Microsoft Excel erbjuder denna funktion, och det gör även Aspose.Cells.

{{% /alert %}}

## **Kontrollera synligheten av rader och kolumner**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) som gör det möjligt för utvecklare att komma åt varje arbetsblad i Excel-filen. Ett arbetsblad representeras av  [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen.  [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen tillhandahåller en  [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samling som representerar alla celler i arbetsbladet.  [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingen tillhandahåller flera metoder för hantering av rader eller kolumner i ett arbetsblad. Några av dessa diskuteras nedan.

### **Dölja rader och kolumner**

Utvecklare kan dölja en rad eller kolumn genom att anropa  [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/) och  [**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/) metoderna i respektive samling. Båda metoderna tar rad- och kolumnindex som parameter för att gömma den specifika raden eller kolumnen.

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

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully. File saved to: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Det är också möjligt att dölja en rad eller kolumn genom att ställa in radhöjden eller kolumnbredden till 0 respektive.

{{% /alert %}}

### **Visa rader och kolumner**

Utvecklare kan visa vilken som helst dold rad eller kolumn genom att anropa  [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/) och [**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/) orden samling respektive metoder. Båda metoderna tar två parametrar:

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhide the 3rd row and set its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhide the 2nd column and set its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File modified and saved successfully!" << std::endl;

    return 0;
}
```

{{% alert color="primary" %}}

När du visar en dold kolumn igen, om du behöver återställa den till dess tidigare tilldelade bredd eller till dess ursprungliga bredd, vänligen avmarkera kolumnen med negativ bredd. Till exempel: `worksheet.Cells.UnhideColumn(5, -1)`

{{% /alert %}}

### **Dölja flera rader och kolumner**

Utvecklare kan dölja flera rader eller kolumner samtidigt genom att anropa  [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/) och [**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/) orden i respektive samling. Båda metoderna tar startindex för rad eller kolumn och antalet rader eller kolumner som ska döljas som parametrar.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet (zero-based index)
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet (zero-based index)
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Det är också möjligt att använda  {1} klassens  {2} och {3} metoder för att göra flera rader och kolumner synliga.

{{% /alert %}}
