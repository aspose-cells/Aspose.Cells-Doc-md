---
title: Aggiorna i giorni preservando la cronologia dei log di revisione in un libro di lavoro condiviso
type: docs
weight: 80
url: /it/net/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Possibili Scenari di Utilizzo**

Quando condividi un workbook, ottieni un'opzione che dice ***Mantieni la cronologia delle modifiche per N giorni*** come mostrato nella seguente schermata. Puoi aggiornare il numero di giorni per conservare la cronologia usando Aspose.Cells con la proprietà [**WorksheetCollection.RevisionLogs.DaysPreservingHistory**](https://reference.aspose.com/cells/net/aspose.cells.revisions/revisionlogcollection/properties/dayspreservinghistory).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Aggiornare i giorni di conservazione della cronologia delle revisioni nel workbook condiviso**

Il seguente codice di esempio crea un workbook vuoto, quindi lo condivide e aggiorna i giorni di registro di revisione preservando la cronologia a 7 giorni, di solito 30 giorni. Consulta il [file Excel di output](60489773.xlsx) generato dal codice per un riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.cs" >}}
{{< app/cells/assistant language="csharp" >}}
