---
title: Berechnung der Array Formel von Datentabellen mit C++
linktitle: Berechnung der Array Formel von DatenTabellen
description: So verwenden Sie die Aspose.Cells Bibliothek, um Array Formeln für eine Datentabelle in Microsoft Excel mit C++ zu berechnen. Durch das Laden einer bestehenden Excel Datei oder das Erstellen einer neuen Excel Datei können wir die von Aspose.Cells bereitgestellte Methode verwenden, um die Array Formel der Datentabelle zu berechnen und das Ergebnis zu erhalten. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, Datentabellen, Array Formeln, Berechnungen, C++
type: docs
weight: 70
url: /de/cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Sie können in Microsoft Excel über Daten > Was-wäre-wenn-Analyse > Datentabelle... eine Datentabelle erstellen. Aspose.Cells ermöglicht es Ihnen jetzt, die Array-Formel einer Datentabelle zu berechnen. Bitte verwenden Sie [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) wie normal, um jegliche Art von Formeln zu berechnen.

{{% /alert %}}

Im folgenden Beispiellcode haben wir die [Quellexceldatei](5115535.xlsx) verwendet. Wenn Sie den Wert von Zelle B1 auf 100 ändern, werden die Werte der Datentabelle, die mit Gelb gefüllt sind, wie in den folgenden Bildern gezeigt, zu 120. Der Beispiellcode generiert die [Ausgabepdf](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Hier ist der Beispiellcode, der verwendet wurde, um das [Ausgabepdf](5115538.pdf) von der [Quellexceldatei](5115535.xlsx) zu generieren. Bitte lesen Sie die Kommentare für weitere Informationen.

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
    U16String inputFilePath = srcDir + u"DataTable.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
    worksheet.GetCells().Get(u"B1").PutValue(100);

    // Calculate formula, now it also calculates Data Table array formula
    workbook.CalculateFormula();

    // Save the workbook in pdf format
    workbook.Save(outDir + u"output_out.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
