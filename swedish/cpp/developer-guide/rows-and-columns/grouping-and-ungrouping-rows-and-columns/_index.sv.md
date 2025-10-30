---
title: Gruppering och Uppringning av Rader och Kolumner med C++
linktitle: Gruppering och avgruppering av rader och kolumner
type: docs
weight: 50
url: /sv/cpp/grouping-and-ungrouping-rows-and-columns/
description: Lär dig hur man grupperar och avgrupperar rader och kolumner i Excel filer med Aspose.Cells och C++.
---

## **Introduktion**

I en Microsoft Excel-fil kan du skapa en översikt över data för att kunna visa och dölja detaljnivåer med en enda musklick.

Klicka på **Översiktssymbolerna**, 1,2,3, + och - för att snabbt visa endast de rader eller kolumner som ger sammanfattningar eller rubriker för avsnitt i ett kalkylblad, eller så kan du använda symbolerna för att se detaljer under en individuell sammanfattning eller rubrik som visas nedan i figuren:

|**Gruppering av rader och kolumner.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Grupperingshantering av rader och kolumner**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samling som representerar alla celler i kalkylbladet.

Samlingen [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) tillhandahåller flera metoder för att hantera rader eller kolumner i ett kalkylblad, några av dessa diskuteras nedan mer detaljerat.

### **Gruppering av rader och kolumner**

Det är möjligt att gruppera rader eller kolumner genom att anropa [**GroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/)- och [**GroupColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/)-metoderna i samlingen [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Båda metoderna tar följande parametrar:

- Första radens/kolumnens index, den första raden eller kolumnen i gruppen.
- Sista radens/kolumnens index, den sista raden eller kolumnen i gruppen.
- Är dold, en boolesk parameter som specificerar om rader/kolumner ska döljas efter gruppering eller inte.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Group first six rows (from 0 to 5) and make them hidden
    worksheet.GetCells().GroupRows(0, 5, true);

    // Group first three columns (from 0 to 2) and make them hidden
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns grouped successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Gruppinställningar**

Microsoft Excel tillåter att du konfigurerar gruppinställningar för att visa:

- Sammanfattande rader under detaljer.
- Sammanfattande kolumner till höger om detaljer.

Utvecklare kan konfigurera dessa gruppinställningar med hjälp av  [**GetOutline()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoutline/) egenskapen på  [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen.

### **Sammanfattande rader nedanför detalj**

Det är möjligt att kontrollera om sammanfattande rader ska visas under detaljer genom att ställa in klassens  [**GetSummaryRowBelow()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummaryrowbelow/) egenskap på **true** eller **false**.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Grouping first six rows and first three columns
    worksheet.GetCells().GroupRows(0, 5, true);
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Setting SummaryRowBelow property to false
    worksheet.GetOutline().SetSummaryRowBelow(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Sammanfattande kolumner till höger om detalj**

Utvecklare kan också styra visningen av sammanfattande kolumner till höger om detalj genom att ställa in  [**GetSummaryColumnRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummarycolumnright/) egenskapen på  [**Outline**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/) klassen till **true** eller **false**.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Grouping first six rows and first three columns
    worksheet.GetCells().GroupRows(0, 5, true);
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Set summary column to the right
    worksheet.GetOutline().SetSummaryColumnRight(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Avgruppering av rader och kolumner**

För att avgruppera eventuellt grupperade rader eller kolumner, anropa  [**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) vid. Båda metoderna tar två parametrar:

- Första radens/kolumnens index, den första raden/kolumnen att avgrupperas.
- Sista radens/kolumnens index, den sista raden/kolumnen att avgrupperas.

[**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) har en överbelastning som tar en boolesk tredje parameter. Om den ställs in på **true** tar den bort all grupperad information. Annars tas endast yttre gruppinformation bort.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Ungrouping first six rows (from 0 to 5)
    worksheet.GetCells().UngroupRows(0, 5);

    // Ungrouping first three columns (from 0 to 2)
    worksheet.GetCells().UngroupColumns(0, 2);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
