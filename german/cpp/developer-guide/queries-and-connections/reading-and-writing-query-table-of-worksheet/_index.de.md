---
title: Lesen und Schreiben von Abfragtabelle im Arbeitsblatt mit C++
linktitle: Lesen und Schreiben von Abfrage Tabellen des Arbeitsblatts
type: docs
weight: 40
url: /de/cpp/reading-and-writing-query-table-of-worksheet/
description: Lernen, wie man Abfragtabellen in Excel Arbeitsblättern mit Aspose.Cells und C++ liest und schreibt.
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Sammlung `Worksheet.QueryTables`, die ein Objekt vom Typ `QueryTable` nach Index zurückgibt. Es hat die folgenden zwei Eigenschaften:

- `QueryTable.AdjustColumnWidth`
- `QueryTable.PreserveFormatting`

Dies sind beide boolesche Werte. Sie können sie in Microsoft Excel unter **Daten > Verbindungen > Eigenschaften** anzeigen.

{{% /alert %}}

## Lesen und Schreiben von Abfrage-Tabellen im Arbeitsblatt

Der folgende Beispielcode liest die erste `QueryTable` des ersten Arbeitsblatts und druckt dann beide Eigenschaften der `QueryTable`. Anschließend setzt er `QueryTable.PreserveFormatting` auf `true`.

Sie können die Quelldatei von Excel, die in diesem Code verwendet wird, und die Ausgabedatei, die von dem Code generiert wird, von den folgenden Links herunterladen.

- [Quelldatei](5115533.xlsx)
- [Ausgabedatei](5115537.xlsx)

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

    // Create workbook from source excel file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first Query Table
    QueryTable qt = worksheet.GetQueryTables().Get(0);

    // Print Query Table Data
    std::cout << "Adjust Column Width: " << qt.GetAdjustColumnWidth() << std::endl;
    std::cout << "Preserve Formatting: " << qt.GetPreserveFormatting() << std::endl;

    // Now set Preserve Formatting to true
    qt.SetPreserveFormatting(true);

    // Save the workbook
    workbook.Save(outDir + u"Output_out.xlsx");

    std::cout << "Query Table properties updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### Konsolenausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes:

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Abfrageergebnisbereich abrufen

Aspose.Cells bietet eine Option, die Adresse (d.h. Ergebnisbereich der Zellen) einer Abfragetable zu lesen. Der folgende Code demonstriert diese Funktion, indem er die Adresse des Ergebnisbereichs einer Abfragetable liest. Die Beispieldatei kann [hier](72417290.xlsx) heruntergeladen werden.

```cpp
#include <iostream>
#include <locale>
#include <codecvt>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::string convert_u16_to_string(const char16_t* data) {
    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    return converter.to_bytes(data);
}

int main()
{
    Aspose::Cells::Startup();

    Workbook wb(u"Query TXT.xlsx");
    std::cout << convert_u16_to_string(wb.GetWorksheets().Get(0).GetQueryTables().Get(0).GetResultRange().GetAddress().GetData()) << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
