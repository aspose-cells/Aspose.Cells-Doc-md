---
title: CSV Datei mit Formeln laden oder importieren mit C++
linktitle: Laden oder Importieren von CSV Dateien mit Formeln
type: docs
weight: 350
url: /de/cpp/load-or-import-csv-file-with-formulas/
description: Lade oder importiere eine CSV Datei mit Formeln unter Verwendung von Aspose.Cells mit C++.
---

{{% alert color="primary" %}} 

CSV-Dateien enthalten meist Textdaten und enthalten typischerweise keine Formeln. Es gibt jedoch Fälle, in denen CSV-Dateien Formeln enthalten können. Solche CSV-Dateien sollten geladen werden, indem die [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/gethasformula/) auf **true** gesetzt wird. Sobald diese Eigenschaft auf **true** gesetzt ist, behandelt Aspose.Cells Formeln nicht als einfachen Text. Sie werden als Formeln behandelt, und die Aspose.Cells-Formelberechnung wird sie wie üblich verarbeiten.

{{% /alert %}} 

Das folgende Beispiel zeigt, wie du eine CSV-Datei mit Formeln laden und importieren kannst. Du kannst jede CSV-Datei verwenden. Zur Veranschaulichung verwenden wir die [einfache CSV-Datei](5115034.csv), die folgende Daten enthält. Wie du siehst, enthält sie eine Formel.

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    //For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    //Create TxtLoadOptions with specified settings
    TxtLoadOptions opts;
    opts.SetSeparator(u','); // Set the separator to a comma
    opts.SetHasFormula(true); // Indicate that the CSV may have formulas

    // Load the CSV file into a Workbook object
    Workbook workbook(srcDir + u"sample.csv", opts);

    // You can also import the CSV file starting from cell D4 (indices 3,3)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().ImportCSV(srcDir + u"sample.csv", opts, 3, 3);

    // Save the workbook in Xlsx format
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "CSV file loaded and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Der Code lädt zuerst die CSV-Datei, importiert sie erneut bei Zelle D4. Schließlich speichert er das Arbeitsbuch im XLSX-Format. Die [Ausgabedatei XLSX](5115052.xlsx) sieht folgendermaßen aus. Wie du siehst, enthalten die Zellen C3 und F4 Formeln und deren Ergebnis ist 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
{{< app/cells/assistant language="cpp" >}}
