---
title: Formeln mit C++ berechnen
linktitle: Berechnung von Formeln
description: Dieser Artikel zeigt, wie die Aspose.Cells Bibliothek verwendet werden kann, um Formeln in Microsoft Excel mit C++ zu berechnen. Durch Laden einer bestehenden Excel Datei oder Erstellen einer neuen Excel Datei können die Methoden von Aspose.Cells zur Berechnung der Formel und zum Erhalt des Ergebnisses genutzt werden. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, Formeln, Berechnungen, Direkte Formelberechnung, Formeln wiederholt berechnen, Formeln hinzufügen.
type: docs
weight: 125
url: /de/cpp/calculate-formulas/
---

## **Hinzufügen von Formeln & Berechnen von Ergebnissen**

Aspose.Cells verfügt über eine eingebaute Formelrechnungs-Engine. Es kann nicht nur Formeln, die aus Designer-Vorlagen importiert wurden, neu berechnen, sondern auch die Ergebnisse von Formeln, die zur Laufzeit hinzugefügt wurden, berechnen.

Aspose.Cells unterstützt die meisten Formeln oder Funktionen, die Teil von Microsoft Excel sind (Lesen Sie [eine Liste der von der Rechenmaschine unterstützten Funktionen](/cells/de/cpp/supported-formula-functions/)). Diese Funktionen können über die APIs oder Designer-Tabellen verwendet werden. Aspose.Cells unterstützt eine große Vielfalt an mathematischen, String-, Boolean-, Datums-/Uhrzeit-, Statistik-, Datenbank-, Lookup- und Referenzformeln.

Verwenden Sie die [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/)-Eigenschaft oder [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/)-Methoden der [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse, um eine Formel in eine Zelle einzufügen. Beim Anwenden einer Formel beginnt der String immer mit einem Gleichheitszeichen (=), so wie Sie es beim Erstellen einer Formel in Microsoft Excel tun, und verwenden Sie ein Komma (,) zur Trennung der Funktionsparameter.

Um die Ergebnisse von Formeln zu berechnen, kann der Benutzer die [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)-Methode der [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-Klasse aufrufen, die alle in einer Excel-Datei eingebetteten Formeln verarbeitet. Alternativ kann der Benutzer die [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/)-Methode der [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse aufrufen, die alle in einem Blatt eingebetteten Formeln verarbeitet. Oder der Benutzer kann auch die [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/)-Methode der [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse aufrufen, die die Formel einer einzelnen Zelle verarbeitet:

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add values to cells
    worksheet.GetCells().Get(u"A1").PutValue(1);
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(3);

    // Add a SUM formula to cell A4
    worksheet.GetCells().Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Calculate the results of formulas
    workbook.CalculateFormula();

    // Get the calculated value of cell A4
    U16String value = worksheet.GetCells().Get(u"A4").GetStringValue();

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Wichtiges zu Formeln**

{{% alert color="primary" %}}

Die **GetFormula**-Eigenschaft und die **SetFormula(...)**-Methoden der [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse arbeiten anders als die **Calculate**-Methoden der [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) und [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klassen. Die **GetFormula**-Eigenschaft und die **SetFormula(...)**-Methoden fügen die Formel einfach einer Zelle hinzu, berechnen aber das Ergebnis zur Laufzeit nicht. Um das Ergebnis der Formeln zu erhalten, rufen Sie bitte die **Calculate**-Methoden auf.

{{% /alert %}}

## **Direkte Berechnung von Formeln**

Aspose.Cells verfügt über einen eingebetteten Formelberechnungsmotor. Neben der Berechnung von Formeln, die aus einer Designerdatei importiert wurden, kann Aspose.Cells auch Formelergebnisse direkt berechnen.

Manchmal müssen Sie Formelergebnisse direkt berechnen, ohne sie in ein Arbeitsblatt einzufügen. Die Werte der in der Formel verwendeten Zellen sind bereits in einem Arbeitsblatt vorhanden, und alles, was Sie brauchen, ist, das Ergebnis dieser Werte basierend auf einer Microsoft-Excel-Formel zu finden, ohne die Formel ins Arbeitsblatt einzufügen.

Sie können die APIs der Aspose.Cells-Formelberechnung engine für [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bis [**calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) nutzen, um die Ergebnisse solcher Formeln zu ermitteln, ohne sie ins Arbeitsblatt einzufügen:

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

    // Create a workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put 20 in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.PutValue(20);

    // Put 30 in cell A2
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.PutValue(30);

    // Calculate the Sum of A1 and A2
    Aspose::Cells::Object results = worksheet.CalculateFormula(u"=Sum(A1:A2)");

    // Print the output
    std::cout << "Value of A1: " << cellA1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Value of A2: " << cellA2.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Result of Sum(A1:A2): " << results.ToString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

Der obige Code erzeugt die folgende Ausgabe:
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Wie man Formeln wiederholt berechnet**

Wenn sich viele Formeln im Arbeitsbuch befinden und der Benutzer sie wiederholt berechnen muss, wobei nur ein kleiner Teil geändert wird, kann es für die Leistung hilfreich sein, die Formelberechnungskette zu aktivieren: [**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/getenablecalculationchain/).

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the template workbook
    Workbook workbook(srcDir + u"book1.xls");

    // Print the time before formula calculation
    auto start = std::chrono::system_clock::now();
    std::time_t start_time = std::chrono::system_clock::to_time_t(start);
    std::cout << "Start time: " << std::ctime(&start_time);

    // Set the CreateCalcChain as true
    workbook.GetSettings().GetFormulaSettings().SetEnableCalculationChain(true);

    // Calculate the workbook formulas
    workbook.CalculateFormula();

    // Print the time after formula calculation
    auto end = std::chrono::system_clock::now();
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);
    std::cout << "End time: " << std::ctime(&end_time);

    // Change the value of one cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"newvalue");

    // Re-calculate those formulas which depend on cell A1
    workbook.CalculateFormula();

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Wichtig zu wissen**

{{% alert color="primary" %}}

Standardmäßig ist die Berechnungskette deaktiviert. Da das Erstellen der Kette zusätzliche Zeit benötigt, kann die erste Berechnung der Formeln ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)) mehr CPU- und Speicherkapazität beanspruchen im Vergleich zur Berechnung ohne Kette. Falls der Benutzer Formeln nicht wiederholt berechnen muss, ist das Standardverhalten (direktes Berechnen der Formel ohne Kette) die bessere Option.

{{% /alert %}}

## **Fortgeschrittene Themen**
- [Zellen zur Microsoft Excel-Formelüberwachung hinzufügen](/cells/de/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Berechnung der IFNA-Funktion mit Aspose.Cells](/cells/de/cpp/calculating-ifna-function-using-aspose-cells/)
- [Berechnung der Arrayformel von Datenblättern](/cells/de/cpp/calculation-of-array-formula-of-data-tables/)
- [Berechnung der Excel 2016 MINIFS- und MAXIFS-Funktionen](/cells/de/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Vermindern der Berechnungszeit der Cell.Calculate-Methode](/cells/de/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Direkte Berechnung einer benutzerdefinierten Funktion ohne Eintragung in ein Arbeitsblatt](/cells/de/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementieren eines benutzerdefinierten Berechnungsmotors zur Erweiterung des Standard-Berechnungsmotors von Aspose.Cells](/cells/de/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Rückgabe eines Bereichs von Werten unter Verwendung von AbstractCalculationEngine](/cells/de/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Festlegen des Formelberechnungsmodus des Arbeitsbuchs](/cells/de/cpp/setting-formula-calculation-mode-of-workbook/)
- [Verwendung der FormulaText-Funktion in Aspose.Cells](/cells/de/cpp/using-formulatext-function-in-aspose-cells/)
{{< app/cells/assistant language="cpp" >}}
