---
title: Aggiorna i giorni mantenendo la cronologia dei log di revisione in un workbook condiviso con Golang via C++
linktitle: Aggiorna i giorni preservando la cronologia dei log di revisione in un libro di lavoro condiviso
type: docs
weight: 80
url: /it/go-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Impara come aggiornare il numero di giorni per la conservazione della cronologia in un workbook condiviso usando Aspose.Cells con Golang via C++.
---

## **Possibili Scenari di Utilizzo**

Quando condividi un workbook, ottieni un'opzione che dice ***Mantieni la cronologia delle modifiche per N giorni*** come mostrato nella seguente schermata. Puoi aggiornare il numero di giorni per conservare la cronologia usando Aspose.Cells con la proprietà [**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/go-cpp/revisionlogcollection/getdayspreservinghistory/).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Aggiornare i giorni di conservazione della cronologia delle revisioni nel workbook condiviso**

Il seguente codice di esempio crea un workbook vuoto, quindi lo condivide e aggiorna i giorni di registro di revisione preservando la cronologia a 7 giorni, di solito 30 giorni. Consulta il [file Excel di output](60489773.xlsx) generato dal codice per un riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.go" >}}
