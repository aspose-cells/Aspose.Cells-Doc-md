---
title: Auto Anpassa rader och kolumner med C++
linktitle: Automatisk anpassning av rader och kolumner
type: docs
weight: 20
url: /sv/cpp/autofit-rows-and-columns/
description: Den här artikeln visar hur du auto anpassar rader, kolumner, rader i sammanslagna celler och rader i ett cellområde med hjälp av API Aspose.Cells for C++.
keywords: Autostorlek för rader, autostorlek för kolumner, autostorlek för rad i en cellintervall, autostorlek för rader i sammanslagna celler
---

{{% alert color="primary" %}}

Microsoft Excel tillåter användare att automatiskt anpassa bredd och höjd på celler efter deras innehåll. Den här funktionen är också tillgänglig via Aspose.Cells, så att utvecklare kan automatisk anpassa dimensionerna på en cell vid körning.

{{% /alert %}}

## **Autostorlek**

Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) samling som ger tillgång till varje kalkblad i en Excel-fil. Ett kalkblad representeras av [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen erbjuder ett brett utbud av metoder för att hantera ett kalkblad. Den här artikeln tittar på att använda [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen för att autofitta rader eller kolumner.

### **AutoFit Row - Enkelt**

Det enklaste sättet att auto-anpassa bredd och höjd på en rad är att anropa [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-klassens [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/)-metod. [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/)-metoden tar ett radindex (på raden som ska ändras storlek på) som parameter.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fit the 2nd row (index 1) of the worksheet
    worksheet.AutoFitRow(1);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Hur man Autofitrad i ett område av celler**

En rad består av många kolumner. Aspose.Cells tillåter utvecklare att autofit-a en rad baserat på innehållet i ett cellområde inom raden genom att anropa en överlagrad version av [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/)-metoden. Den tar följande parametrar:

- **Radindex**, index för raden som ska autofit.
- **Första kolumnindex**, index för radens första kolumn.
- **Sista kolumnindex**, index för radens sista kolumn.

[**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/)-metoden kontrollerar innehållet i alla kolumner i raden och autofitar sedan raden.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fitting the 3rd row of the worksheet
    worksheet.AutoFitRow(1, 0, 5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Hur man Autofittar kolumn i ett område av celler**

En kolumn består av många rader. Det är möjligt att automatiskt anpassa en kolumn baserat på innehållet i ett område av celler i kolumnen genom att anropa en överbelastad version av [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) metoden som tar följande parametrar:

- **Kolumnindex**, index för kolumnen som ska autofit.
- **Första radindex**, index för kolumnens första rad.
- **Sista radindex**, index för kolumnens sista rad.

[**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/)-metoden kontrollerar innehållet i alla rader i kolumnen och autofitar sedan kolumnen.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fit the 5th column (index 4) from row 4 to 6
    worksheet.AutoFitColumn(4, 4, 6);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Hur man Autofittar rader för sammanfogade celler**

Med Aspose.Cells är det möjligt att autofit-rader även för celler som har blivit sammanslagna med hjälp av [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) API. [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) klassen tillhandahåller egenskapen [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/) som kan användas för att autofitta rader för sammanslagna celler. [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/) accepterar [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitmergedcellstype/) enumeration, som har följande medlemmar:

- Ingen: Ignorera sammanslagna celler.
- FörstaLinjen: Utökar endast höjden på den första raden.
- SistaLinjen: Utökar endast höjden på den sista raden.
- VarjeRad: Utökar endast höjden på varje rad.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook wb;

    // Get the first (default) worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Create a range A1:B1
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 2);

    // Merge the cells
    range.Merge();

    // Insert value to the merged cell A1
    worksheet.GetCells().Get(0, 0).SetValue(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

    // Create a style object
    Style style = worksheet.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style.SetIsTextWrapped(true);

    // Apply the style to the cell
    worksheet.GetCells().Get(0, 0).SetStyle(style);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options;

    // Set auto-fit for merged cells
    options.SetAutoFitMergedCellsType(AutoFitMergedCellsType::EachLine);

    // Autofit rows in the sheet (including the merged cells)
    worksheet.AutoFitRows(options);

    // Save the Excel file
    wb.Save(outDir + u"AutofitRowsforMergedCells.xlsx");

    std::cout << "Autofit rows for merged cells completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Du kan också försöka använda de överbelastade versionerna av [**AutoFitRows**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrows/) och [**AutoFitColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumns/) metoder som tar ett område av rader/kolumner och en instans av [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) för att auto-anpassa de valda raderna/kolumnerna med din önskade [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) i åtanke.

Signaturerna för dessa metoder är som följer:

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) options)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) options)

{{% /alert %}}

## **Viktigt att veta**

{{% alert color="primary" %}}

Om en cell är sammanslagen kommer AutoFit-metoderna inte att tillämpas, vilket är samma beteende som i Microsoft Excel. Du kan kringgå detta genom att använda Auto Filter API. Dessutom, om texten i en cell är ombryten kommer inte [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) metoden att tillämpas heller. En annan sak att veta är att *AutoFit* metoder är tidskrävande. Därför bör du anropa dessa metoder så sällan som möjligt för att säkerställa effektiviteten i din applikation.

{{% /alert %}}

## **Avancerade ämnen**
- [Automatisk justering av rader för sammanfogade celler](/cells/sv/cpp/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="cpp" >}}
