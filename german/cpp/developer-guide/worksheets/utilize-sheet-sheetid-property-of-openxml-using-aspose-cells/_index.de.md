---
title: Nutzen Sie Sheet.SheetId Eigenschaft von OpenXml mit C++
linktitle: Nutzen Sie Sheet.SheetId Eigenschaft von OpenXml
type: docs
weight: 200
url: /de/cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Dieser Artikel zeigt, wie man die Sheet.SheetId Eigenschaft von OpenXml mit der Excel Manipulations API oder Bibliothek in C++ programmatisch nutzt.
keywords: Sheet ID Eigenschaft von OpenXml in C++, Sheet ID Excel Arbeitsblatt in C++
---

## **Mögliche Verwendungsszenarien**

Die *Sheet.SheetId* -Eigenschaft befindet sich im *DocumentFormat.OpenXml.Spreadsheet* -Namespace und ist Teil von OpenXml. Sie können diese Eigenschaft und ihren Wert in *workbook.xml* wie im folgenden Screenshot gezeigt sehen. Aspose.Cells bietet die äquivalente Eigenschaft als [**Worksheet.GetTabId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettabid/).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Verwenden Sie die *Sheet.SheetId*-Eigenschaft von OpenXml mit Aspose.Cells**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](51740716.xlsx), liest ihre Tabellen- oder Registerkarten-ID, weist ihr dann eine neue Registerkarten-ID zu und speichert sie als [Ausgabe-Excel-Datei](51740717.xlsx). Bitte sehen Sie sich auch die Konsolenausgabe des untenstehenden Codes als Referenz an.

## **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load source Excel file
    Workbook wb(u"sampleSheetId.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Print its Sheet or Tab Id on console
    std::cout << "Sheet or Tab Id: " << ws.GetTabId() << std::endl;

    // Change Sheet or Tab Id
    ws.SetTabId(358);

    // Save the workbook
    wb.Save(u"outputSheetId.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Konsolenausgabe**

{{< highlight java >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
