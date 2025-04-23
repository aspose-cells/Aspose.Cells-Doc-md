---
title: Sök data med ursprungliga värden med C++
linktitle: Sök data med hjälp av ursprungliga värden
type: docs
weight: 380
url: /sv/cpp/search-data-using-original-values/
description: Lär dig hur du söker data med ursprungliga värden via API et Aspose.Cells for C++.
keywords: Sök data med ursprungliga värden, Hitta data med ursprungliga värden, Sök data efter ursprungliga värden, Hitta data enligt ursprungliga värden
---

{{% alert color="primary" %}}

Ibland är värdet på datan dolt eftersom det är formaterat på något sätt. Till exempel, anta att cell D4 har formeln = Sum(A1:A2) och dess värde är 20, men det är formaterat som ---, då är värdet 20 dolt och kan inte hittas med hjälp av Microsoft Excels sökalternativ. Du kan dock hitta det med Aspose.Cells genom att använda [**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/)

{{% /alert %}}

Följande exempelkod illustrerar ovanstående. Den hittar cell D4 som inte kan hittas med Microsoft Excels sökalternativ men Aspose.Cells kan hitta den med hjälp av [**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/). Läs kommentarerna i koden för mer information.

## C++ kod för att söka data med originalvärden

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

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add 10 in cell A1 and A2
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(10);

    // Add Sum formula in cell D4 but customize it as ---
    Cell cell = worksheet.GetCells().Get(u"D4");

    Style style = cell.GetStyle();
    style.SetCustom(u"---", true);
    cell.SetStyle(style);

    // The result of formula will be 20 but 20 will not be visible because the cell is formatted as ---
    cell.SetFormula(u"=Sum(A1:A2)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Create find options, we will search 20 using original values otherwise 20 will never be found because it is formatted as ---
    FindOptions options;
    options.SetLookInType(LookInType::OriginalValues);
    options.SetLookAtType(LookAtType::EntireContent);

    Cell foundCell;
    int32_t obj = 20;

    // Find 20 which is Sum(A1:A2) and formatted as ---
    foundCell = worksheet.GetCells().Find(obj, foundCell, options);

    // Print the found cell
    std::cout << foundCell.ToString().ToUtf8() << std::endl;

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## Konsolutdata som genereras av exempelkoden

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
