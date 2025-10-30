---
title: Formel automatisch in Tabellen oder Listenobjekt propagieren, während Sie beim Eingeben neuer Zeilen Daten hinzufügen, mit C++
linktitle: Tabellenformel festlegen
type: docs
weight: 260
url: /de/cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Erfahren Sie, wie Sie Formeln in Tabellen oder Listenobjekten automatisch beim Hinzufügen neuer Daten propagieren, mit Aspose.Cells for C++.
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie, dass eine Formel in Ihrem Tabellen- oder Listenobjekt automatisch auf neue Zeilen übertragen wird, während Sie neue Daten eingeben. Dies ist das Standardverhalten von Microsoft Excel. Um dieselbe Funktionalität mit Aspose.Cells zu erreichen, verwenden Sie die [ListColumn::GetFormula](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listcolumn/getformula/) Methode.

## **Formel in Tabelle oder List-Objekt automatisch propagieren, während neue Zeilen eingegeben werden**
Der folgende Beispielcode erstellt eine Tabelle oder Listenobjekt so, dass die Formel in Spalte B automatisch auf neue Zeilen übertragen wird, wenn Sie neue Daten eingeben. Bitte überprüfen Sie die [Ausgabedatei] (5115469.xlsx), die mit diesem Code generiert wurde. Wenn Sie eine beliebige Zahl in Zelle A3 eingeben, werden Sie sehen, dass die Formel in Zelle B2 automatisch nach B3 propagiert wird.

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

    // Create workbook object
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add column headings in cell A1 and B1
    sheet.GetCells().Get(0, 0).PutValue(u"Column A");
    sheet.GetCells().Get(0, 1).PutValue(u"Column B");

    // Add list object, set its name and style
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(0, 0, 1, sheet.GetCells().GetMaxColumn(), true));
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium2);
    listObject.SetDisplayName(u"Table");

    // Set the formula of second column so that it propagates to new rows automatically while entering data
    listObject.GetListColumns().Get(1).SetFormula(u"=[Column A] + 1");

    // Save the workbook in xlsx format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
