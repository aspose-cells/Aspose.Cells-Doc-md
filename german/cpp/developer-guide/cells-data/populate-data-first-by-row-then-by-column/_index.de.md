---
title: Daten zuerst zeilenweise und dann spaltenweise mit C++ eintragen
linktitle: Füllen Sie zuerst die Daten nach Zeile und dann nach Spalte aus
type: docs
weight: 1000
url: /de/cpp/populate-data-first-by-row-then-by-column/
description: Lernen Sie, wie man Daten zuerst zeilenweise und dann spaltenweise über die API Aspose.Cells for C++ einträgt.
keywords: Zuerst Daten zuerst nach Zeile und dann nach Spalte einfügen, Daten zuerst nach Zeile und dann nach Spalte einsetzen, Daten zuerst nach Zeile und dann nach Spalte hinzufügen, Hochleistungsdateneinfügung, Hochleistungsdatenhinzufügung
---

{{% alert color="primary" %}} 

Das Ausfüllen einer Tabelle mit Daten zuerst nach Zeile und dann nach Spalte verbessert die Gesamtperformance.

{{% /alert %}} 

Das Einsetzen von Daten in die Folge A1, B1, A2, B2 ist schneller als A1, A2, B1, B2. Wenn es viele Zellen in einem Arbeitsblatt gibt und Sie die zweite Sequenz befolgen, das heißt, Sie füllen die Daten Zeile für Zeile ein, kann dieser Tipp das Programm wesentlich schneller machen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook workbook;

    // Populate Data into Cells
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();
    cells.Get(u"A1").PutValue(U"data1");
    cells.Get(u"B1").PutValue(U"data2");
    cells.Get(u"A2").PutValue(U"data3");
    cells.Get(u"B2").PutValue(U"data4");

    // Save workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
