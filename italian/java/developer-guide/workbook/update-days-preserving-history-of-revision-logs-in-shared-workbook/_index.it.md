---
title: Aggiorna i giorni preservando la cronologia dei log di revisione in un libro di lavoro condiviso
type: docs
weight: 90
url: /it/java/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Possibili Scenari di Utilizzo**

Quando condividi un workbook, hai l'opzione che dice ***Mantieni la cronologia delle modifiche per N giorni*** come mostrato nella seguente schermata. Puoi aggiornare il numero di giorni per conservare la cronologia usando Aspose.Cells con la proprietà [**WorksheetCollection.RevisionLogs.DaysPreservingHistory**](https://reference.aspose.com/cells/java/com.aspose.cells/revisionlogcollection#DaysPreservingHistory).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Aggiornare i giorni di conservazione della cronologia delle revisioni nel workbook condiviso**

Il seguente codice di esempio crea un workbook vuoto, lo condivide e aggiorna i giorni di conservazione della cronologia delle revisioni a 7 giorni anziché 30 giorni. Si prega di vedere il [file Excel di output](60489784.xlsx) generato dal codice per un riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.java" >}}
