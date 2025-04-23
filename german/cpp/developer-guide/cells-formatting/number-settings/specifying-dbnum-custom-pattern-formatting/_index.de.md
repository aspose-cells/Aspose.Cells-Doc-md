---
title: Spezifizierung des DBNum Benutzerdefinierten Pattern Formats mit C++
linktitle: Benutzerdefinierte Musterformatierung für DBNum festlegen
description: Aspose.Cells ist eine C++ Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien, die das Formatieren von Daten und Zahlen mit benutzerdefinierten Mustern unterstützt. Dieser Artikel zeigt, wie man die Bibliothek Aspose.Cells verwendet, um das dbnum benutzerdefinierte Formatmuster anzugeben, sodass Benutzer mehr Kontrolle über die Anzeige der Zahlen haben.
keywords: Aspose.Cells, C++ Bibliothek, elektronische Tabelle, benutzerdefiniertes Formatmuster, Formatierung, dbnum , Steuerung der Anzeige
type: docs
weight: 110
url: /de/cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells unterstützt die *DBNum*-benutzerdefinierte Musterformatierung. Wenn beispielsweise der Zellwert 123 ist und die benutzerdefinierte Formatierung als [DBNum2][$-804]General festgelegt wird, wird er wie 壹佰贰拾叁 angezeigt. Sie können die benutzerdefinierte Formatierung der Zelle mit [**Cell.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)-Methode und [**Style.Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/)-Eigenschaft festlegen.

## **Beispielcode**

Das folgende Beispiel zeigt, wie man die *DBNum*-benutzerdefinierte Musterformatierung festlegt. Bitte überprüfen Sie das [AusgabepDF](43352081.pdf) für weitere Unterstützung.

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
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1 and put value 123
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(123);

    // Access cell style
    Style st = cell.GetStyle();

    // Specifying DBNum custom pattern formatting
    st.SetCustom(u"[DBNum2][$-804]General", true);

    // Set the cell style
    cell.SetStyle(st);

    // Set the first column width
    ws.GetCells().SetColumnWidth(0, 30);

    // Save the workbook in output pdf format
    wb.Save(outDir + u"outputDBNumCustomFormatting.pdf", SaveFormat::Pdf);

    std::cout << "DBNum custom formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
