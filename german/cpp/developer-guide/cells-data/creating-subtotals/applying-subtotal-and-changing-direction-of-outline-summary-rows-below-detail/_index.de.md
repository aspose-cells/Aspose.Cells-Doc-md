---
title: Anwenden von Subtotal und Ändern der Richtung der Gliederungszusammenfassung unter Detail mit C++
linktitle: Anwendung von Zwischensumme und Änderung der Richtung der Zusammenfassungszeilen unterhalb der Details
type: docs
weight: 100
url: /de/cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Erfahren Sie, wie Sie Subtotal anwenden und die Richtung der Gliederungszusammenfassung unter Detail mit der API Aspose.Cells for C++ ändern.
keywords: Zwischensumme anwenden, Zwischensumme hinzufügen, Richtung der Zusammenfassungszeilen unterhalb des Details ändern, Richtung der Zusammenfassungszeilen rechts neben dem Detail ändern, Zwischensumme erstellen und Richtung der Zusammenfassungszeilen unterhalb des Details ändern
---

{{% alert color="primary" %}}

Dieser Artikel erklärt, wie man Subtotal auf Daten anwendet und die Richtung der Gliederungszusammenfassung unter Detail ändert.

Sie können Subtotal auf Daten anwenden mit der Methode [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/subtotal/). Es nimmt folgende Parameter entgegen:

- **CellArea** - Der Bereich, auf den die Zwischensumme angewendet werden soll
- **GroupBy** - Das Feld, nach dem gruppiert werden soll, als nullbasierter Ganzzahlenoffset
- **Funktion** - Die Zwischensummenfunktion
- **TotalList** - Ein Array von nullbasierten Feldoffsets, die die Felder angeben, zu denen die Zwischensummen hinzugefügt werden
- **Replace** - Gibt an, ob die aktuellen Zwischensummen ersetzt werden sollen
- **PageBreaks** - Gibt an, ob zwischen den Gruppen Seitenumbrüche eingefügt werden sollen
- **SummaryBelowData** - Gibt an, ob die Zusammenfassung unter den Daten hinzugefügt werden soll.

Außerdem können Sie die Richtung der Gliederungszeilen **Zusammenfassung unter Details** mit der folgenden Eigenschaft `Worksheet.Outline.SummaryRowBelow` steuern. Diese Einstellung können Sie in Microsoft Excel im Menü **Daten > Gliederung > Einstellungen** öffnen.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Bilder von Quell- und Ausgabedateien

Der folgende Screenshot zeigt die verwendete Excel-Quelldatei im untenstehenden Beispielcode, die einige Daten in den Spalten A und B enthält.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

Der folgende Screenshot zeigt die von dem Beispielcode generierte Ausgabedatei in Excel. Wie Sie sehen können, wurde eine Zwischensumme für den Bereich A2:B11 angewendet und die Richtung der Zusammenfassung ist unterhalb der Detailinformationen.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## C++-Code zum Anwenden von Subtotal und Ändern der Richtung der Gliederungszusammenfassung

Hier ist der Beispielcode, um das oben gezeigte Ergebnis zu erzielen.

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
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the Cells collection in the first worksheet
    Cells cells = worksheet.GetCells();

    // Create a cellarea i.e.., A2:B11
    CellArea ca = CellArea::CreateCellArea(u"A2", u"B11");

    // Apply subtotal, the consolidation function is Sum and it will applied to Second column (B) in the list
    cells.Subtotal(ca, 0, ConsolidationFunction::Sum, { 1 }, true, false, true);

    // Set the direction of outline summary
    worksheet.GetOutline().SetSummaryRowBelow(true);

    // Save the excel file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Subtotal applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
