---
title: Erhalten des Cell Objekts anhand des DisplayName des PivotField im PivotTable mit C++
linktitle: Erhalten des Cell Objekts anhand des DisplayName des PivotField im PivotTable
type: docs
weight: 70
url: /de/cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Erfahren Sie, wie Sie das Cell Objekt anhand des Anzeigenamens eines Pivot Felds abrufen und Formatierungen mithilfe von Aspose.Cells for C++ anwenden.
---

{{% alert color="primary" %}}

Aspose.Cells bietet die [**PivotTable::GetCellByDisplayName()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getcellbydisplayname/)-Methode, mit der Sie auf das Cell-Objekt anhand des Anzeigenamens eines Pivot-Felds zugreifen können. Diese Methode ist nützlich, wenn Sie die Überschrift Ihres Pivot-Felds hervorheben oder formatieren möchten. Dieser Artikel erklärt, wie man das Cell-Objekt anhand des Anzeigenamens eines Datenfelds abruft und anschließend formatiert.

{{% /alert %}}

## **Erhalten des Cell-Objekts anhand des DisplayName des PivotField im PivotTable**

Der folgende Code greift auf die erste Pivot-Tabelle des Arbeitsblatts zu und ruft dann die Zelle anhand des DisplayName des zweiten Datenfelds der Pivot-Tabelle ab. Anschließend ändert er die Füllfarbe und die Schriftfarbe der Zelle auf Hellblau bzw. Schwarz. Nachstehend sind Screenshots, die zeigen, wie die Pivot-Tabelle vor und nach der Ausführung des Codes aussieht.

|**Pivot-Tabelle - Vorher**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"source.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    Cell cell = pivotTable.GetCellByDisplayName(pivotTable.GetDataFields().Get(0).GetDisplayName());

    Style style = cell.GetStyle();
    style.SetForegroundColor(Color::LightBlue());
    style.GetFont().SetColor(Color::Black());

    pivotTable.Format(cell.GetRow(), cell.GetColumn(), style);
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Pivot table formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

|**Pivot-Tabelle - Nachher**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
{{< app/cells/assistant language="cpp" >}}
