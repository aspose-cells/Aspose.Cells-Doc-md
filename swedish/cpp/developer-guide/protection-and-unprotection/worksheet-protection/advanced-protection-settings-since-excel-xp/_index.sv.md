---
title: Avancerade säkerhetsinställningar sedan Excel XP med C++
linktitle: Avancerade skyddsinställningar sedan Excel XP
type: docs
weight: 30
url: /sv/cpp/advanced-protection-settings-since-excel-xp/
description: Lär dig hur man tillämpar avancerade säkerhetsinställningar i Excel filer med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Sedan utgåvan av Excel 2002 eller XP har Microsoft lagt till många avancerade skyddsinställningar.

{{% /alert %}}

## **Introduktion**

Dessa skyddsinställningar begränsar eller tillåter användare att:

- Ta bort rader eller kolumner.
- Redigera innehåll, objekt eller scenarier.
- Formatera celler, rader eller kolumner.
- Infoga rader, kolumner eller hyperlänkar.
- Välj låsta eller olåsta celler.
- Använd pivottabeller och mycket annat.

Aspose.Cells stöder alla avancerade skyddsinställningar som erbjuds av Excel XP eller senare versioner.

### **Avancerade skyddsinställningar med Excel XP och senare versioner**

För att visa de tillgängliga skyddsinställningarna i Excel XP:

1. Från **Verktyg**-menyn, välj **Skydda** följt av **Skydda kalkylblad**. En dialogruta kommer att visas.

För att visa de tillgängliga skyddsinställningarna i Excel 2016:

1. Från **Arkiv**-menyn, välj **Skydda arbetsbok** följt av **Skydda aktuellt kalkylblad**.
1. Välj **Skydda kalkylblad** i **Granska**-menyn.

Följ stegen ovan visar en dialogruta där du kan tillåta eller begränsa arbetsbladets funktioner eller tillämpa ett lösenord på arbetsbladet.

### **Avancerade skyddsinställningar med hjälp av Aspose.Cells**

Aspose.Cells stödjer alla avancerade skyddsinställningar.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-kollektion som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-klassen.

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-klassen ger egenskapen [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) som används för att tillämpa dessa avancerade skyddsinställningar. Egenskapen [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) är faktiskt ett objekt av [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/)-klassen som kapslar in flera booleska egenskaper för att inaktivera eller aktivera restriktioner.

Nedan finns en liten exempelapplikation. Den öppnar en Excel-fil och använder de flesta av de avancerade skyddsinställningarna som stöds av Excel XP och senare versioner.

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

    // Create workbook
    Workbook excel(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Restricting users to delete columns of the worksheet
    worksheet.GetProtection().SetAllowDeletingColumn(false);

    // Restricting users to delete row of the worksheet
    worksheet.GetProtection().SetAllowDeletingRow(false);

    // Restricting users to edit contents of the worksheet
    worksheet.GetProtection().SetAllowEditingContent(false);

    // Restricting users to edit objects of the worksheet
    worksheet.GetProtection().SetAllowEditingObject(false);

    // Restricting users to edit scenarios of the worksheet
    worksheet.GetProtection().SetAllowEditingScenario(false);

    // Restricting users to filter
    worksheet.GetProtection().SetAllowFiltering(false);

    // Allowing users to format cells of the worksheet
    worksheet.GetProtection().SetAllowFormattingCell(true);

    // Allowing users to format rows of the worksheet
    worksheet.GetProtection().SetAllowFormattingRow(true);

    // Allowing users to format columns of the worksheet
    worksheet.GetProtection().SetAllowFormattingColumn(true);

    // Allowing users to insert hyperlinks in the worksheet
    worksheet.GetProtection().SetAllowInsertingHyperlink(true);

    // Allowing users to insert rows in the worksheet
    worksheet.GetProtection().SetAllowInsertingRow(true);

    // Allowing users to select locked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingLockedCell(true);

    // Allowing users to select unlocked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingUnlockedCell(true);

    // Allowing users to sort
    worksheet.GetProtection().SetAllowSorting(true);

    // Allowing users to use pivot tables in the worksheet
    worksheet.GetProtection().SetAllowUsingPivotTable(true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();

    return 0;
}
```

{{% alert color="primary" %}}

Vänligen ring inte metoden [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) för klassen [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) när du använder egenskapen [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/). Spara också filen i Excel97Till2003 eller Xlsx-format eftersom de avancerade säkerhetsinställningarna endast stöds av Excel XP och senare versioner.

{{% /alert %}}

### **Cellåsningsproblem**

Om du vill begränsa användare från att redigera celler måste cellerna låsas innan några skyddsinställningar tillämpas. Annars kan cellerna redigeras även om arket är skyddat. I Microsoft Excel XP kan celler låsas genom följande dialog:

|**Dialogruta för att låsa celler i Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Det är också möjligt att låsa celler med Aspose.Cells API. Varje cell kan få [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) formatering som innehåller en Boolean-egenskap, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Sätt [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) egenskapen till **true** eller **false** för att låsa eller låsa upp cellen.

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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Lock the style of cell A1
    worksheet.GetCells().Get(u"A1").GetStyle().SetIsLocked(true);

    // Protect the sheet
    worksheet.Protect(ProtectionType::All);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
