---
title: Ottieni l oggetto cella tramite DisplayName di PivotField di PivotTable con C++
linktitle: Ottieni l oggetto cella tramite DisplayName di PivotField di PivotTable
type: docs
weight: 70
url: /it/cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Impara come recuperare l oggetto cella tramite il nome visualizzato di un campo pivot e applicare formattazione usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells fornisce il metodo [**PivotTable::GetCellByDisplayName()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getcellbydisplayname/), che puoi usare per accedere all'oggetto cella tramite il nome visualizzato di un campo pivot. Questo metodo è utile quando si desidera evidenziare o formattare l'intestazione del campo pivot. Questo articolo spiega come recuperare l'oggetto cella tramite il nome visualizzato di un campo dati e poi applicare formattazioni.

{{% /alert %}}

## **Ottieni l'oggetto cella tramite DisplayName di PivotField di PivotTable**

 Il codice seguente accede alla prima tabella pivot del foglio di lavoro e successivamente recupera la cella tramite il nome visualizzato del secondo campo dati della tabella pivot. Poi cambia il colore di riempimento e di testo della cella rispettivamente in azzurro chiaro e nero. Di seguito sono riportati screenshot che mostrano come appare la tabella pivot prima e dopo l'esecuzione del codice.

|**Tabella Pivot - Prima**|
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

|**Tabella Pivot - Dopo**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
