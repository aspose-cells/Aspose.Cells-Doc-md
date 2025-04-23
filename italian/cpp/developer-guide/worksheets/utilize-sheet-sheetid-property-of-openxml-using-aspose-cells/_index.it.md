---
title: Utilizza la proprietà Sheet.SheetId di OpenXml con C++
linktitle: Utilizza la proprietà Sheet.SheetId di OpenXml
type: docs
weight: 200
url: /it/cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Questo articolo mostra come utilizzare la proprietà Sheet.SheetId di OpenXml tramite l API o la libreria C++ per la manipolazione di Excel.
keywords: proprietà sheet id di openxml c++, sheet id worksheet excel c++
---

## **Possibili Scenari di Utilizzo**

La proprietà *Sheet.SheetId* si trova all'interno dello spazio dei nomi *DocumentFormat.OpenXml.Spreadsheet* ed è parte di OpenXml. È possibile vedere questa proprietà e il relativo valore all'interno di *workbook.xml* come mostrato nello screenshot seguente. Aspose.Cells fornisce la proprietà equivalente come [**Worksheet.GetTabId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettabid/).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Utilizza la proprietà Sheet.SheetId di OpenXml utilizzando Aspose.Cells**

Il codice di esempio seguente carica il [file Excel di esempio](51740716.xlsx), legge il suo ID della scheda o tabulato, quindi ne assegna un nuovo ID della scheda e lo salva come [file Excel di output](51740717.xlsx). Si prega di vedere anche l'output della console del codice sottostante per un riferimento.

## **Codice di Esempio**

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

## **Output della console**

{{< highlight java >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
