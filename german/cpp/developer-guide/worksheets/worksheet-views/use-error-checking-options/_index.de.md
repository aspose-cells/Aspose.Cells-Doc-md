---
title: Verwenden Sie Fehlerüberprüfung Optionen mit C++
linktitle: Verwenden von Fehlerüberprüfungsoptionen
type: docs
weight: 140
url: /de/cpp/use-error-checking-options/
description: In diesem Artikel finden Sie Beispielcode, der die Fehlerüberprüfung von Excel Arbeitsblättern programmatisch nutzt, z.B. Nummern, die als Text gespeichert sind, mit der C++ API oder Bibliothek.
keywords: Legen Sie die Nummer in Excel als Text mit C++ fest, Fehlerüberprüfung der Excel Optionen C++
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Benutzern, Fehlerprüfoptionen und -regeln zu definieren. Benutzer sehen oft Fehlerprüfungen beim Erstellen von Formeln, ein kleines Dreieck in der oberen rechten Ecke einer Zelle markiert, wenn ein Problem mit einer Zelle vorliegt. Excel bietet Informationen, die den Benutzern helfen, häufige Probleme zu korrigieren.

{{% /alert %}}

## **Arten von Fehlern**

Fehler, die bedeuten, dass die Formel kein Ergebnis zurückgeben kann - wie beispielsweise die Division durch Null - erfordern sofortige Aufmerksamkeit, und ein Fehlerwert wird in der Zelle angezeigt. Durch Klicken auf das grüne Dreieck wird ein Ausrufezeichen angezeigt, und ein Klick darauf öffnet eine Liste von Optionen.

Der Fehler kann mithilfe der Optionen behoben oder ignoriert werden. Das Ignorieren eines Fehlers bedeutet, dass dieser bei weiteren Fehlerprüfungen nicht mehr angezeigt wird.

Aspose.Cells bietet Optionen zur Fehlerprüfung. Die Klasse [**ErrorCheckOption**](https://reference.aspose.com/cells/cpp/aspose.cells/errorcheckoption/) verwaltet verschiedene Arten von Fehlerprüfungen, wie beispielsweise Zahlen, die als Text gespeichert sind, Formelberechnungsfehler und Validierungsfehler. Verwenden Sie die Aufzählung [**ErrorCheckType**](https://reference.aspose.com/cells/cpp/aspose.cells/errorchecktype/), um die gewünschte Fehlerprüfung festzulegen.

## **Als Text gespeicherte Zahlen**

Gelegentlich werden Zahlen formatiert und in Zellen als Text gespeichert. Dies kann Probleme bei Berechnungen verursachen oder irreführende Sortierreihenfolgen erzeugen. Zahlen, die als Text formatiert sind, sind in der Zelle linksbündig anstelle von rechtsbündig. Wenn eine Formel, die eine mathematische Operation mit Zellen durchführen sollte, kein Ergebnis zurückgibt, überprüfen Sie die Ausrichtung in den Zellen, auf die sich die Formel bezieht - einige oder alle diese Zellen könnten als Text formatierte Zahlen sein.

Sie können die Fehlerprüfungsoptionen verwenden, um Zahlen, die als Text gespeichert sind, schnell in echte Zahlen umzuwandeln. In Microsoft Excel 2003:

1. Klicken Sie im Menü **Extras** auf **Optionen**.
1. Wählen Sie den Tab Fehlerüberprüfung aus.
   Die Option **Als Text gespeicherte Zahl** ist standardmäßig aktiviert.
1. Deaktivieren Sie es.

Der folgende Beispielcode zeigt, wie Sie die Option zur Fehlerprüfung von als Text gespeicherten Zahlen für ein Arbeitsblatt in der Vorlage XLS-Datei mithilfe der Aspose.Cells-APIs deaktivieren.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a workbook and open the template spreadsheet
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Instantiate the error checking options
    ErrorCheckOptionCollection opts = sheet.GetErrorCheckOptions();

    // Add a new error check option
    int index = opts.Add();
    ErrorCheckOption opt = opts.Get(index);

    // Disable the numbers stored as text option
    opt.SetErrorCheck(ErrorCheckType::NumberStoredAsText, false);

    // Set the range
    CellArea area = CellArea::CreateCellArea(0, 0, 1000, 50);
    opt.AddRange(area);

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_test.out.xlsx";

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Error check options applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
