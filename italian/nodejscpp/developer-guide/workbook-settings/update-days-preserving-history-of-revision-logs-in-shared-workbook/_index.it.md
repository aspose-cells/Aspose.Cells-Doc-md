---  
title: Aggiornare i giorni preservando la cronologia delle revisioni in un workbook condiviso con Node.js tramite C++  
linktitle: Aggiorna i giorni preservando la cronologia dei log di revisione in un libro di lavoro condiviso  
type: docs  
weight: 80  
url: /it/nodejs-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/  
description: Impara come aggiornare i giorni per preservare la cronologia delle revisioni nei workbook condivisi usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**

Quando condividi un workbook, ricevi un'opzione chiamata ***Mantieni la cronologia delle modifiche per N giorni*** come mostrato nello screenshot seguente. Puoi aggiornare il numero di giorni per preservare la cronologia usando Aspose.Cells for Node.js via C++ con la proprietà [**WorksheetCollection.getDaysPreservingHistory()**](https://reference.aspose.com/cells/nodejs-cpp/revisionlogcollection/#getDaysPreservingHistory--).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Aggiornare i giorni di conservazione della cronologia delle revisioni nel workbook condiviso**

Il seguente codice di esempio crea un workbook vuoto, quindi lo condivide e aggiorna i giorni di registro di revisione preservando la cronologia a 7 giorni, di solito 30 giorni. Consulta il [file Excel di output](60489773.xlsx) generato dal codice per un riferimento.

## **Codice di Esempio**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Share the workbook
workbook.getSettings().setShared(true);

// Update DaysPreservingHistory of RevisionLogs
workbook.getWorksheets().getRevisionLogs().setDaysPreservingHistory(7);

// Save the workbook
workbook.save("outputShared_DaysPreservingHistory.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
