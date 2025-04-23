---
title: Pivot Tabelle und Quelldaten mit C++
linktitle: Pivot Tabelle und Quelldaten
type: docs
weight: 30
url: /de/cpp/pivot-table-and-source-data/
description: Erfahren Sie, wie Sie eine Pivot Tabelle mit Aspose.Cells und C++ dynamisch ihre Quelldaten ändern.
---

## **Quelldaten der Pivot-Tabelle**

Es gibt Zeiten, in denen Sie Microsoft Excel-Berichte mit Pivot-Tabellen erstellen möchten, die Daten aus verschiedenen Datenquellen (wie einer Datenbank) enthalten, die zur Entwurfszeit nicht bekannt sind. Dieser Artikel stellt einen Ansatz zur Verfügung, um die Datenquelle einer Pivot-Tabelle dynamisch zu ändern.

### **Ändern der Datenquelle einer Pivot-Tabelle**

1. Erstellen einer neuen Designer-Vorlage.
   1. Erstellen Sie eine neue Designer-Vorlagendatei wie im folgenden Screenshot gezeigt.
   1. Definieren Sie dann einen benannten Bereich, **Datenquelle**, der sich auf diesen Zellenbereich bezieht.

      **Erstellen einer Designer-Vorlage & Definieren eines benannten Bereichs, Datenquelle** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Erstellen einer Pivot-Tabelle auf Basis dieses benannten Bereichs.
   1. Wählen Sie in Microsoft Excel **Daten**, dann **PivotTable** und **PivotChart-Bericht** aus.
   1. Erstellen Sie eine Pivot-Tabelle basierend auf dem im ersten Schritt erstellten benannten Bereich.

      **Erstellen einer Pivot-Tabelle basierend auf dem benannten Bereich, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. Ziehen Sie das entsprechende Feld in Zeile und Spalte der Pivot-Tabelle und erstellen Sie dann die resultierende Pivot-Tabelle wie im Screenshot unten.

   **Erstellen einer Pivot-Tabelle basierend auf einem entsprechenden Feld** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Klicken Sie mit der rechten Maustaste auf die Pivot-Tabelle und wählen Sie **Tabellenoptionen**.
   1. Aktivieren Sie **Beim Öffnen aktualisieren** in den **Dateneinstellungen**.

      **Festlegen der Pivot-Tabellenoptionen** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Nun können Sie diese Datei als Ihre Designer-Vorlagendatei speichern.

1. Neue Daten einfügen und die Quelldaten einer Pivot-Tabelle ändern.
   1. Sobald die Designer-Vorlage erstellt ist, verwenden Sie den folgenden Code, um die Quelldaten der Pivot-Tabelle zu ändern.

Die Ausführung des untenstehenden Beispielcodes ändert die Quelldaten der Pivot-Tabelle.

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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Populating new data to the worksheet cells
    worksheet.GetCells().Get(u"A9").PutValue(u"Golf");
    worksheet.GetCells().Get(u"B9").PutValue(u"Qtr4");
    worksheet.GetCells().Get(u"C9").PutValue(7000);

    // Changing named range "DataSource"
    Range range = worksheet.GetCells().CreateRange(0, 0, 9, 3);
    range.SetName(u"DataSource");

    // Saving the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File saved successfully!" << std::endl;

    return 0;
}
```
