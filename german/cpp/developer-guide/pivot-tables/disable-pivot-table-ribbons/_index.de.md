---
title: Pivot Tabellen Bänder mit C++ deaktivieren
linktitle: Pivot Tabellen Ribbons deaktivieren
type: docs
weight: 90
url: /de/cpp/disable-pivot-table-ribbons/
description: Lernen Sie, wie Sie die Bänder in Pivot Tabellen in Excel Dateien mit Aspose.Cells for C++ deaktivieren.
---

{{% alert color="primary" %}}

Berichte auf Basis von Pivot-Tabellen sind nützlich, aber anfällig für Fehler, wenn die Zielbenutzer kein detailliertes Excel-Wissen haben, um diese Berichte zu konfigurieren. In solchen Fällen möchten Organisationen die Benutzer daran hindern, Änderungen an Pivot-Tabellenberichten vorzunehmen. Funktionen wie zusätzliche Filter, Slicer, Felder oder die Änderung der Reihenfolge im Bericht sind meistens nicht für jeden Benutzer geeignet. Andererseits sollen diese Benutzer den Bericht aktualisieren und vorhandene Filter oder Slicer verwenden können. Aspose.Cells bietet Entwicklern die Möglichkeit, Benutzer beim Ändern dieser Berichte zu beschränken. Dafür stellt Excel eine Funktion zum Deaktivieren des Pivot-Tabellen-Bandes bereit, die auch von Aspose.Cells unterstützt wird. Entwickler können das Band mit den Steuerelementen zur Bearbeitung dieser Berichte deaktivieren.

{{% /alert %}}

## **Pivot-Tabelle-Ribbon mit PivotTable.EnableWizard deaktivieren**

Das folgende Beispiel demonstriert diese Funktion, indem es auf eine Pivot-Tabelle in einem Blatt zugreift und dann [**GetEnableWizard()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getenablewizard/) auf **false** setzt. Eine Beispiel-Pivot-Tabellendatei kann von [diesem Link](pivot_table_test.xlsx) heruntergeladen werden.

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
    U16String inputFilePath = srcDir + u"pivot_table_test.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Access the pivot table in the first sheet
    PivotTable pt = wb.GetWorksheets().Get(0).GetPivotTables().Get(0);

    // Disable ribbon for this pivot table
    pt.SetEnableWizard(false);

    // Save output file
    wb.Save(outputFilePath);

    std::cout << "Pivot table ribbon disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
