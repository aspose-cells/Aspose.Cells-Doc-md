---
title: Verwendung eingebauter Stile mit C++
linktitle: Verwendung von integrierten Styles
type: docs
weight: 80
url: /de/cpp/using-built-in-styles/
description: C++ Code zur Nutzung der eingebauten Excel Stile mit der API Aspose.Cells for C++
keywords: c++ Nutzung eingebauter Excel Stile, c++ Programm zum programmatischen Anwenden von Stilen im Arbeitsbuch, Programm zur Anwendung von Stilen im Arbeitsbuch, c++ Anwendung eingebauter Stile in Excel, c++ Anwendung eingebauter Stile im Arbeitsbuch, c++ Code zum Anwenden eingebauter Stile im Arbeitsbuch, c++ Code zum Anwenden eingebauter Stile in Excel Arbeitsbuch
---

{{% alert color="primary" %}}

Aspose.Cells bietet eine umfangreiche Sammlung von wiederverwendbaren Stilen zur Formatierung einer Zelle in einem Tabellendokument. Wir können eingebaute Stile in unserer Arbeitsmappe verwenden und auch benutzerdefinierte Stile erstellen.

{{% /alert %}}

## **Wie man integrierte Styles verwendet**

Die Methode [**Workbook.CreateBuiltinStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/createbuiltinstyle/) und die Enumeration [**BuiltinStyleType**](https://reference.aspose.com/cells/cpp/aspose.cells/builtinstyletype/) machen es bequem, integrierte Stile zu verwenden. Hier ist eine Liste aller möglichen integrierten Stile:

- ZWANZIG_PROZENT_AKKENT_1
- ZWANZIG_PROZENT_BETONUNG_2
- ZWANZIG_PROZENT_BETONUNG_3
- ZWANZIG_PROZENT_BETONUNG_4
- ZWANZIG_PROZENT_BETONUNG_5
- ZWANZIG_PROZENT_BETONUNG_6
- VIERZIG_PROZENT_BETONUNG_1
- VIERZIG_PROZENT_BETONUNG_2
- VIERZIG_PROZENT_BETONUNG_3
- VIERZIG_PROZENT_BETONUNG_4
- VIERZIG_PROZENT_BETONUNG_5
- VIERZIG_PROZENT_BETONUNG_6
- SECHZIG_PROZENT_BETONUNG_1
- SECHZIG_PROZENT_BETONUNG_2
- SECHZIG_PROZENT_BETONUNG_3
- SECHZIG_PROZENT_BETONUNG_4
- SECHZIG_PROZENT_BETONUNG_5
- SECHZIG_PROZENT_BETONUNG_6
- BETONUNG_1
- BETONUNG_2
- BETONUNG_3
- BETONUNG_4
- BETONUNG_5
- BETONUNG_6
- SCHLECHT
- BERECHNUNG
- ZELLE_PRÜFEN
- KOMMA
- KOMMA_1
- WÄHRUNG
- WÄHRUNG_1
- ERKLÄRENDER_TEXT
- GUT
- ÜBERSCHRIFT_1
- ÜBERSCHRIFT_2
- ÜBERSCHRIFT_3
- ÜBERSCHRIFT_4
- HYPERLINK
- GEFOLGTEN_HYPERLINK
- EINGABE
- VERKNÜPFTE_ZELLE
- NEUTRAL
- NORMAL
- HINWEIS
- AUSGABE
- PROZENT
- TITEL
- GESAMT
- WARNTEXT
- REIHENEBENE
- SPALTENELEBENE

## C++ Code zur Nutzung eingebauter Stile

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output file paths
    U16String output1Path = srcDir + u"Output.xlsx";
    U16String output2Path = srcDir + u"Output.out.ods";

    // Create a new workbook
    Workbook workbook;

    // Create a built-in style of type Title
    Style style = workbook.CreateBuiltinStyle(BuiltinStyleType::Title);

    // Get the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Access cell A1 and set its value and style
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Aspose");
    cell.SetStyle(style);

    // Auto-fit the first column and row
    worksheet.AutoFitColumn(0);
    worksheet.AutoFitRow(0);

    // Save the workbook to the first output path
    workbook.Save(output1Path);
    std::cout << "File saved " << output1Path.ToUtf8() << std::endl;

    // Save the workbook to the second output path
    workbook.Save(output2Path);
    std::cout << "File saved " << output2Path.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
