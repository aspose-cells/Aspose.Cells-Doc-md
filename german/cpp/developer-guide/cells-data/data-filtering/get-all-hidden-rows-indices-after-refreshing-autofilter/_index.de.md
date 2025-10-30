---
title: Alle versteckten Zeilen nach Aktualisierung des AutoFilter mit C++ indizieren.
linktitle: Alle versteckten Zeilenindizes nach dem Aktualisieren des Autofilters abrufen.
type: docs
weight: 320
url: /de/cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Erfahren Sie, wie Sie alle versteckten Zeilen nach der Aktualisierung des AutoFilters mithilfe der API Aspose.Cells for C++ ermitteln.
keywords: Erhalten Sie alle versteckten Zeilenindizes nach dem Aktualisieren des AutoFilters, Alle versteckten Zeilenindizes nach dem Aktualisieren des AutoFilters erhalten, Alle versteckten Zeilenindizes nach dem Aktualisieren des AutoFilters abrufen
---

## **Mögliche Verwendungsszenarien**

Wenn Sie den Autofilter auf Zellen des Arbeitsblattes anwenden, werden einige der Zeilen automatisch ausgeblendet. Es könnte jedoch sein, dass einige der Zeilen bereits manuell vom Excel-Endbenutzer ausgeblendet wurden und nicht vom Autofilter ausgeblendet sind. Daher ist es schwierig zu wissen, welche der Zeilen vom Autofilter ausgeblendet sind und welche manuell vom Excel-Endbenutzer ausgeblendet wurden. Aspose.Cells behandelt dieses Problem mit der Methode int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/refresh/). Diese Methode gibt die Zeilenindizes aller Zeilen zurück, die vom Autofilter ausgeblendet und nicht manuell vom Excel-Endbenutzer ausgeblendet wurden.

## **Alle versteckten Zeilenindizes nach Aktualisierung des AutoFilters abrufen**

Bitte sehen Sie sich den folgenden Beispielscode an, der die [Beispieldatei Excel](64716909.xlsx) lädt, die einige Zeilen enthält, die vom Excel-Endbenutzer manuell ausgeblendet wurden. Der Code wendet den Autofilter an und aktualisiert ihn mit der Methode int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/refresh/), die die Zeilenindizes aller ausgeblendeten Zeilen durch den Autofilter zurückgibt. Anschließend werden die Indizes der ausgeblendeten Zeilen zusammen mit Zellennamen und Werten auf der Konsole ausgegeben.

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + U16String(u"sampleGetAllHiddenRowsIndicesAfterRefreshingAutoFilter.xlsx");
    Workbook workbook(inputFilePath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    AutoFilter autoFilter = worksheet.GetAutoFilter();
    autoFilter.AddFilter(0, u"Orange");

    Vector<int32_t> rowIndices = autoFilter.Refresh(true);

    std::cout << "Printing Rows Indices, Cell Names and Values Hidden By AutoFilter." << std::endl;
    std::cout << "--------------------------" << std::endl;

    for (int32_t i = 0; i < rowIndices.GetLength(); i++)
    {
        int32_t r = rowIndices[i];
        Cell cell = worksheet.GetCells().Get(r, 0);
        std::cout << r << "\t" << cell.GetName().ToUtf8() << "\t" << cell.GetStringValue().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsolenausgabe**

{{< highlight java >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
