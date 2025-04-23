---
title: Gemeinsame Formel mit C++ festlegen
linktitle: Einstellung gemeinsamer Formel
type: docs
weight: 10
url: /de/cpp/setting-shared-formula/
description: Erfahren Sie, wie Sie gemeinsam genutzte Formeln in Excel Arbeitsblättern mit Aspose.Cells und C++ festlegen.
---

{{% alert color="primary" %}}

Wenn Sie eine Funktion in einem Arbeitsblatt hinzufügen möchten, die Berechnungen durchführt, erklärt dieser Artikel, wie Sie dies mit Aspose.Cells erreichen.

{{% /alert %}}

## Gemeinsame Formel mit Aspose.Cells festlegen

Angenommen, Sie haben ein Arbeitsblatt mit Daten im Format, das wie das folgende Beispieldatenblatt aussieht.

|**Eingabedatei mit einer Spalte Daten**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Sie möchten eine Funktion in B2 hinzufügen, die die Umsatzsteuer für die erste Datensatzreihe berechnet. Die Steuer beträgt **9%**. Die Formel zur Berechnung der Umsatzsteuer lautet: **"=A2*0,09"**. In diesem Artikel wird erläutert, wie diese Formel mit Aspose.Cells angewendet wird.

Mit Aspose.Cells können Sie eine Formel mit der Eigenschaft [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/) angeben. Es gibt zwei Optionen, um Formeln zu den anderen Zellen (B3, B4, B5 usw.) in der Spalte hinzuzufügen.

Entweder tun Sie das, was Sie für die erste Zelle gemacht haben, indem Sie die Formel effektiv für jede Zelle festlegen und die Zellreferenz entsprechend aktualisieren (A3*0.09, A4*0.09, A5*0.09 und so weiter). Dies erfordert, dass die Zellreferenzen für jede Zeile aktualisiert werden. Es erfordert auch, dass Aspose.Cells jede Formel einzeln parst, was bei großen Tabellen und komplexen Formeln zeitaufwendig sein kann. Es fügt auch zusätzliche Zeilen Code hinzu, obwohl Schleifen sie etwas reduzieren können.

Ein anderer Ansatz ist die Verwendung einer **gemeinsamen Formel**. Mit einer gemeinsamen Formel werden die Formeln automatisch für die Zellbezüge in jeder Zeile aktualisiert, sodass die Steuer ordnungsgemäß berechnet wird. Die Methode [**SetSharedFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setsharedformula/) ist effizienter als die erste Methode.

Das folgende Beispiel zeigt, wie es verwendet wird.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Instantiate a Workbook from existing file
    Workbook workbook(inputFilePath);

    // Get the cells collection in the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Apply the shared formula in the range i.e.., B2:B14
    cells.Get(u"B2").SetSharedFormula(u"=A2*0.09", 13, 1);

    // Save the excel file
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Shared formula applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
