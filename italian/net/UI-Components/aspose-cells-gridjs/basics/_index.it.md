---
title: Aspose.Cells.GridJs Nozioni di base
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/basics/
---
## Nozioni di base di GridJs

 Aspose.Cells.GridJs è una libreria standard .NET che consente agli utenti di sviluppare applicazioni Web per mostrare/modificare fogli di calcolo in modo rapido e semplice.

Aspose.Cells.GridJs supporta l'importazione dei formati di file di fogli di calcolo più diffusi (XLS, XLSX, XLSM, XLSB, CSV, SpreadsheetML, ODS).

Consente inoltre di esportare file Excel in PDF, HTML .etc. Di seguito sono riportati i passaggi del processo di base per sviluppare un'applicazione Web di GridJs.

- Implementa GridCacheForStream per scrivere la tua logica di business per l'archiviazione della cache.
- Imposta un'azione del controller per ottenere json dal file del foglio di calcolo. Puoi utilizzare le API GridJsWorkbook.ImportExcelFile e GridJsWorkbook.ExportToJson, GridJs memorizzerà automaticamente il file di diffusione nella cache.
- Imposta un'azione del controller per ottenere json per l'operazione di aggiornamento. Puoi utilizzare GridJsWorkbook.UpdateCell API, GridJs eseguirà l'operazione di aggiornamento nella cache e restituirà il json aggiornato.
- Imposta un'azione del controller per ottenere l'URL dei file di immagini/forme nel foglio di calcolo, GridJs comprimerà automaticamente tutte le immagini/forme nella cache. Userà GridCacheForStream.GetFileUrl API.
- Imposta un'azione del controller per ottenere il file nella cache, quindi possiamo ottenere il file zip delle immagini/forme o il file del foglio di calcolo nella cache. Userà GridCacheForStream.LoadStream API.
- Imposta un'azione del controller per scaricare il foglio di calcolo. Puoi utilizzare GridJsWorkbook.SaveToCacheWithFileName API.

 Di seguito una demo di base per mostrare l'utilizzo di Aspose.Cells.GridJs: https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs

In caso di domande, richieste o bisogno di aiuto, inviare un feedback al seguente sito Web https://forum.aspose.com/c/cells/9