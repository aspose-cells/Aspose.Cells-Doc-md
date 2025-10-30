---
title: Timeline mit C++ einfügen
linktitle: Zeitachsen
type: docs
weight: 170
url: /de/cpp/create-timeline/
description: Erfahren Sie, wie Sie mit Aspose.Cells in C++ eine Zeitleiste erstellen.
---

## **Mögliche Verwendungsszenarien**

Anstatt Filter anzupassen, um Daten anzuzeigen, können Sie eine PivotTable-Zeitleiste verwenden - eine dynamische Filteroption, mit der Sie einfach nach Datum/Uhrzeit filtern und mit einem Schieberegler in den Zeitraum hineinzoomen können. Microsoft Excel ermöglicht es Ihnen, eine Zeitleiste zu erstellen, indem Sie eine Pivot-Tabelle auswählen und dann auf *Einfügen > Zeitleiste* klicken. Aspose.Cells ermöglicht ebenfalls die Erstellung einer Zeitleiste mit der [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.timelines/timelinecollection/add/) Methode.

## **Erstellen Sie eine Zeitleiste für eine Pivottabelle**

Bitte sehen Sie sich den folgenden Beispielcode an. Er lädt die [Beispiel-Excel-Datei](input.xlsx), die die Pivottabelle enthält. Dann erstellt er die Zeitleiste basierend auf dem ersten Basis-Pivottabellenfeld. Schließlich speichert er die Arbeitsmappe im [Ausgabe-XLSX](output.xlsx)-Format. Der folgende Screenshot zeigt die von Aspose.Cells in der Ausgabe-Excel-Datei erstellte Zeitleiste.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing pivot table
    U16String inputFilePath = u"input.xlsx";
    Workbook wb(inputFilePath);

    // Access second worksheet (index 1)
    Worksheet sheet = wb.GetWorksheets().Get(1);

    // Access first pivot table inside the worksheet
    PivotTable pivot = sheet.GetPivotTables().Get(0);

    // Add timeline relating to pivot table
    int index = sheet.GetTimelines().Add(pivot, 15, 1, u"Ship Date");

    // Access the newly added timeline from timeline collection
    Timeline timeline = sheet.GetTimelines().Get(index);

    // Save the modified workbook
    U16String outputFilePath = u"output.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Timeline added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
