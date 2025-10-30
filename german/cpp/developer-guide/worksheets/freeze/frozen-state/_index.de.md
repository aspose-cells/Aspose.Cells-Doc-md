--- 
title: Wie man den eingefrorenen Zustand ohne Excel mit C++ überprüft 
linktitle: Einfrierungsstatus 
type: docs 
weight: 190 
url: /de/cpp/how-to-check-frozen-state-of-excel-worksheet 
description: In diesem Artikel lernen Sie, wie man den eingefrorenen Zustand eines Excel Arbeitsblatts programmatisch mit C++ und der Aspose.Cells API überprüft. 
--- 

## **Einführung** 

In diesem Artikel lernen wir, wie man den eingefrorenen Zustand eines Excel-Arbeitsblatts programmatisch überprüft. Wir können einfach feststellen, ob das Arbeitsblatt eingefroren oder gesplittet ist, in MS Excel. Gibt es eine Möglichkeit, mit C++ zu erkennen, ob es eingefroren oder gesplittet ist? Das geht mit Aspose.Cells for C++. 

## **Sind Fensterscheiben eingefroren?** 
Mit Aspose.Cells for C++ können wir überprüfen, ob das Fenster eingefroren ist und wie viele Zeilen und Spalten gesperrt sind. 

Bitte verwenden Sie die Eigenschaft [**GetPaneState()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getpanestate/), um den Zustand der Fensterbereiche zu überprüfen und die gesperrten Zeilen und Spalten mit der Methode [**Worksheet::GetFreezedPanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getfreezedpanes/) abzurufen. 
1. Arbeitsmappe erstellen, um die Datei zu öffnen. 
2. Überprüfen Sie, ob das Arbeitsblatt eingefroren ist. 
3. Die gesperrten Zeilen und Spalten abrufen. 

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create the workbook from the specified file
    Workbook workbook(u"Frozen.xlsx");

    // Get the first worksheet from the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Check whether the worksheet is frozen
    if (sheet.GetPaneState() == PaneStateType::Frozen || sheet.GetPaneState() == PaneStateType::FrozenSplit)
    {
        int32_t row = 0, column = 0;
        int32_t rows = 0, columns = 0;

        // Get the locked rows and columns
        sheet.GetFreezedPanes(row, column, rows, columns);

        // Output the details if needed (just for demonstration)
        std::cout << "Frozen panes at Row: " << row << ", Column: " << column << ", Total Frozen Rows: " 
                  << rows << ", Total Frozen Columns: " << columns << std::endl;
    }

    Aspose::Cells::Cleanup();
}
``` 

{{< app/cells/assistant language="cpp" >}}
