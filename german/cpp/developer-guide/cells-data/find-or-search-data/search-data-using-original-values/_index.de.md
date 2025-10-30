---
title: Daten mit Originalwerten suchen mit C++
linktitle: Daten mithilfe der Originalwerte suchen
type: docs
weight: 380
url: /de/cpp/search-data-using-original-values/
description: Erfahren Sie, wie Sie Daten mit Originalwerten mithilfe der API Aspose.Cells for C++ durchsuchen.
keywords: Daten mithilfe der Originalwerte suchen, Daten mithilfe der Originalwerte finden, Daten mithilfe der Originalwerte nach Werten suchen, Daten mithilfe der Originalwerte nach Werten finden
---

{{% alert color="primary" %}}

Manchmal wird der Wert der Daten verborgen, weil er auf irgendeine Weise formatiert ist. Zum Beispiel hat die Zelle D4 die Formel =Summe(A1:A2) und ihr Wert ist 20, aber sie ist als --- formatiert, dann ist der Wert 20 verborgen und kann nicht mit den Suchoptionen von Microsoft Excel gefunden werden. Sie können ihn jedoch mit Aspose.Cells unter Verwendung von [**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/) finden.

{{% /alert %}}

Der folgende Beispielcode verdeutlicht den obigen Punkt. Er findet die Zelle D4, die mit den Suchoptionen von Microsoft Excel nicht gefunden werden kann, aber Aspose.Cells kann sie mithilfe von [**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/) finden. Bitte lesen Sie die Kommentare im Code für weitere Informationen.

## C++ Code zum Suchen von Daten mit Originalwerten

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

## Von dem Beispielcode generierte Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
