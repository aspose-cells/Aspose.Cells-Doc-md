---
title: Aspetti di base di Aspose.Cells.GridJs
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/basics/
keywords: GridJs
description: Questo articolo introduce i passaggi di base per configurare un applicazione web per GridJs.
---

## Concetti di base di GridJs

Aspose.Cells.GridJs è una libreria standard .NET che consente agli utenti di sviluppare rapidamente e facilmente applicazioni web per mostrare/modificare fogli di calcolo. 

Aspose.Cells.GridJs supporta l'importazione dei popolari formati di file di fogli di calcolo (XLS, XLSX, XLSM, XLSB, CSV, SpreadsheetML, ODS).

Consente inoltre di esportare file Excel in PDF, HTML, ecc. Di seguito sono riportati i passaggi di base per sviluppare un'applicazione web di GridJs.

- Implementa GridCacheForStream per scrivere la tua logica di business per la memorizzazione nella cache.
- Configurare un'azione del controller per ottenere JSON dal file di foglio di calcolo. È possibile utilizzare GridJsWorkbook.ImporExcelFile e le API GridJsWorkbook.ExportToJson, GridJs memorizzerà automaticamente il file di fogli di calcolo nella cache.
- Configura un'azione del controller per ottenere JSON per l'operazione di aggiornamento. È possibile utilizzare l'API GridJsWorkbook.UpdateCell, GridJs effettuerà l'operazione di aggiornamento nella cache e restituirà il JSON aggiornato.
- Configura un'azione del controller per ottenere l'URL dei file delle immagini/forme nel foglio di calcolo, GridJs ziperà automaticamente tutte le immagini/forme nella cache. Utilizzerà l'API GridCacheForStream.GetFileUrl.
- Configura un'azione del controller per ottenere il file nella cache, quindi è possibile ottenere il file zip delle immagini/forme o il file di foglio di calcolo nella cache. Utilizzerà l'API GridCacheForStream.LoadStream.
- Configura un'azione del controller per scaricare il foglio di calcolo. È possibile utilizzare l'API GridJsWorkbook.SaveToCacheWithFileName.

Di seguito è presente una demo di base per mostrare l'uso di Aspose.Cells.GridJs: https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs


Se hai domande, requisiti o hai bisogno di aiuto, per favore fornisci un feedback al seguente sito web https://forum.aspose.com/c/cells/9
