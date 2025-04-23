---
title: Aggiornare i giorni conservando la cronologia dei log di revisione in un workbook condiviso con C++
linktitle: Aggiorna i giorni preservando la cronologia dei log di revisione in un libro di lavoro condiviso
type: docs
weight: 80
url: /it/cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Impara come aggiornare il numero di giorni per conservare la cronologia in un workbook condiviso usando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**

Quando condividi un workbook, ottieni un'opzione che dice ***Mantieni la cronologia delle modifiche per N giorni*** come mostrato nella seguente schermata. Puoi aggiornare il numero di giorni per conservare la cronologia usando Aspose.Cells con la proprietà [**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/cpp/aspose.cells.revisions/revisionlogcollection/getdayspreservinghistory/).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Aggiornare i giorni di conservazione della cronologia delle revisioni nel workbook condiviso**

Il seguente codice di esempio crea un workbook vuoto, quindi lo condivide e aggiorna i giorni di registro di revisione preservando la cronologia a 7 giorni, di solito 30 giorni. Consulta il [file Excel di output](60489773.xlsx) generato dal codice per un riferimento.

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Share the workbook
    wb.GetSettings().SetShared(true);

    // Update DaysPreservingHistory of RevisionLogs
    wb.GetWorksheets().GetRevisionLogs().SetDaysPreservingHistory(7);

    // Save the workbook
    wb.Save(u"outputShared_DaysPreservingHistory.xlsx");

    std::cout << "Workbook shared and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
