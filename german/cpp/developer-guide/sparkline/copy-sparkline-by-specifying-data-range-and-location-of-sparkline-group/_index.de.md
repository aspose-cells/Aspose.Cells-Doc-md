---
title: Kopieren Sie Sparkline durch Festlegen des Datenbereichs und des Standorts der Sparkline Gruppe mit C++
linktitle: Kopieren Sie Sparkline durch Festlegen des Datenbereichs und des Standorts
type: docs
weight: 300
url: /de/cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Erfahren Sie, wie Sie Sparklines durch Festlegen des Datenbereichs und des Standorts mit Aspose.Cells for C++ kopieren.
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Ihnen, eine Sparkline zu kopieren, indem Sie den Datenbereich und den Speicherort einer Sparkline-Gruppe angeben. Aspose.Cells unterstützt diese Funktion.

{{% /alert %}}

Um eine Sparkline in andere Zellen in Microsoft Excel zu kopieren:

1. Wählen Sie die Zelle aus, die die Sparkline enthält.
1. Wählen Sie **Daten bearbeiten** im **Sparkline**-Abschnitt des **Entwurfs**-Registers aus.
1. Wählen Sie **Gruppenposition & Daten bearbeiten** aus.
1. Geben Sie den Datenbereich und den Speicherort an.
1. Klicken Sie auf **OK**.

Aspose.Cells bietet die Methode `SparklineCollection.Add(dataRange, Zeile, Spalte)`, um den Datenbereich und den Standort einer Sparkline-Gruppe festzulegen. Der folgende Beispielcode lädt die Quellen-Excel-Datei, wie im obigen Screenshot gezeigt, greift auf die erste Sparkline-Gruppe zu und fügt Datenbereiche und Standorte in die Sparkline-Gruppe ein. Abschließend wird die Ausgabedatei auf die Festplatte geschrieben, die ebenfalls im obigen Screenshot zu sehen ist.

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

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first sparkline group
    SparklineGroup group = worksheet.GetSparklineGroups().Get(0);

    // Add Data Ranges and Locations inside this sparkline group
    group.GetSparklines().Add(u"D5:O5", 4, 15);
    group.GetSparklines().Add(u"D6:O6", 5, 15);
    group.GetSparklines().Add(u"D7:O7", 6, 15);
    group.GetSparklines().Add(u"D8:O8", 7, 15);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
