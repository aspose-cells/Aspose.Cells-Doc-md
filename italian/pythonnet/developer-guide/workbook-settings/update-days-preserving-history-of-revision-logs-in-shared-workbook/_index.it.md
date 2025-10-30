---
title: Aggiorna i giorni preservando la cronologia dei log di revisione in un libro di lavoro condiviso
type: docs
weight: 80
url: /it/python-net/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Possibili Scenari di Utilizzo**

Quando condividi un workbook, ottieni un'opzione chiamata ***Mantieni la cronologia delle modifiche per N giorni*** come mostrato nella schermata seguente. Puoi aggiornare il numero di giorni per conservare la cronologia usando Aspose.Cells for Python via .NET con la proprietà [**WorksheetCollection.revision_logs.days_preserving_history**](https://reference.aspose.com/cells/python-net/aspose.cells.revisions/revisionlogcollection/days_preserving_history).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Aggiornare i giorni di conservazione della cronologia delle revisioni nel workbook condiviso**

Il seguente codice di esempio crea un workbook vuoto, quindi lo condivide e aggiorna i giorni di registro di revisione preservando la cronologia a 7 giorni, di solito 30 giorni. Consulta il [file Excel di output](60489773.xlsx) generato dal codice per un riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
