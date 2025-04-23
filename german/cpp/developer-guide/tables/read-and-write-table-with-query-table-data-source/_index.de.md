---
title: Lesen und Schreiben von Tabellen mit Query Table Datenquelle mit C++
linktitle: Tabelle mit Abfrage Tabellendatenquelle lesen und schreiben
type: docs
weight: 30
url: /de/cpp/read-and-write-table-with-query-table-data-source/
description: Lernen Sie, wie man Tabellen mit QueryTable als Datenquelle liest und schreibt mit Aspose.Cells for C++.
---

## **Tabelle mit Abfrage-Tabellendatenquelle lesen und schreiben**
Mit Aspose.Cells können Sie eine Tabelle lesen und schreiben, die eine QueryTable als Datenquelle hat. Diese Unterstützung besteht auch für XLS-Dateien. Das folgende Code-Snippet demonstriert das Lesen und Schreiben einer solchen Tabelle, indem die Tabelle zuerst gelesen und dann modifiziert wird, um die Summezeile hinzuzufügen.

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

    // Load workbook object
    Workbook workbook(srcDir + u"SampleTableWithQueryTable.xls");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first ListObject (Table) in the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Check the data source type if it is query table
    if (table.GetDataSourceType() == TableDataSourceType::QueryTable)
    {
        table.SetShowTotals(true);
    }

    // Save the file
    workbook.Save(outDir + u"SampleTableWithQueryTable_out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

Die Quell- und Ausgabedateien im Excel-Format sind zur Referenz beigefügt.

[Quelldatei](96928091.xls)

[Ausgabedatei](96928092.xls)
