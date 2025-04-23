---
title: Visa och göm rutnätslinjer och rubriker för rader och kolumner med C++
linktitle: Visa och dölj rutnät och radkolumnhuvuden
type: docs
weight: 30
url: /sv/cpp/show-and-hide-gridlines-and-row-column-headers/
description: Denna artikel ger exempel kod för att använda C++ API eller bibliotek för att programmatiskt gömma eller visa rutnätslinjer, rad och kolumnrubriker i ett Excel arbetsblad.
---

{{% alert color="primary" %}}

Aspose.Cells stödjer döljning och visning av kalkylbladets rutnät som är synliga som standard. Den ger också kontroll över synligheten av radkolumnhuvuden på kalkylbladet.

{{% /alert %}}

## **Visa och dölj rutnät**

Alla Excel-kalkylblad har rutnät som standard. De hjälper till att avgränsa celler så att det är lätt att ange data i specifika celler. Rutnät gör det möjligt för oss att se ett kalkylblad som en samling av celler, där varje cell är lätt identifierbar.

### **Kontrollera synligheten av rutnäten**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som låter utvecklare komma åt varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) erbjuder ett brett utbud av egenskaper och metoder för att hantera ett arbetsblad. För att styra synligheten av rutnätslinjer, använd [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) egenskap. [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) är en Boolean-egenskap, vilket innebär att den bara kan lagra ett **true** eller **false** värde.

#### **Gör rutnätslinjer synliga**

Gör rutnätslinjerna synliga genom att sätta [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassens [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) egenskap till **true**.

#### **Gömmer rutnätslinjer**

Göm rutnätslinjer genom att sätta [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassens [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) egenskap till **false**.

Ett fullständigt exempel ges nedan som visar användningen av [**IsGridlinesVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isgridlinesvisible/) egenskapen genom att öppna en excel-fil (book1.xls), gömma rutnätslinjer på det första arbetsbladet och spara den modifierade filen som output.xls.

```cpp
#include <iostream>
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

    // Hide the grid lines of the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Grid lines hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Visa och dölj radkolumnhuvuden**

Alla kalkylblad i en Excel-fil består av celler som är ordnade i rader och kolumner. Alla rader och kolumner har unika värden som används för att identifiera dem och individuella celler. Till exempel har rader nummer - 1, 2, 3, 4, osv.- och kolumner är ordnade alfabetiskt - A, B, C, D, osv. Rad- och kolumnvärdena visas i huvudena. Med Aspose.Cells kan utvecklare kontrollera synligheten av dessa rad- och kolumnhuvuden.

### **Kontrollera synligheten av arbetsbladen**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) innehåller en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som låter utvecklare komma åt varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) erbjuder ett brett utbud av egenskaper och metoder för att hantera ett arbetsblad. För att styra synligheten av rader och kolumnrubriker, använd [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) egenskap. [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) är en Boolean-egenskap, vilket innebär att den bara kan lagra ett **true** eller **false** värde.

#### **Göra rad-/kolumnrubriker synliga**

Gör rad- och kolumnrubriker synliga genom att sätta [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) egenskap till **true**.

#### **Gömma rad-/kolumnrubriker**

Dölj rad- och kolumnetiketter genom att ställa in [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassens [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/) egenskap till **false**.

Ett komplett exempel ges nedan som visar hur man använder [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isrowcolumnheadersvisible/)-egenskapen genom att öppna en Excel-fil (book1.xls), dölja rad- och kolumnetiketter på det första bladet och spara den modifierade filen som output.xls.

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

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the headers of rows and columns
    worksheet.SetIsRowColumnHeadersVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Headers hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Det är också möjligt att använda metoderna [**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/) och [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) av [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-klassen för att göra flera rader och kolumner synliga.

{{% /alert %}}
