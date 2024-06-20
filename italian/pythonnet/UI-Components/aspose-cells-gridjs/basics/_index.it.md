---
title: Aspetti di base di Aspose.Cells.GridJs
type: docs
weight: 250
url: /it/python-net/aspose-cells-gridjs/basics/
keywords: gridjs,python,edit,spreadsheet,view,viewer,editor,excel
---

## Concetti di base di GridJs

Aspose.Cells.GridJs è una libreria che consente agli utenti di sviluppare rapidamente e facilmente un'applicazione web multi-piattaforma per visualizzare o modificare file di fogli di calcolo. 

## Perché utilizzare Aspose.Cells.GridJs


- Consente agli utenti di creare, modificare, formattare, collaborare e condividere in modo sicuro i fogli di calcolo con aggiornamenti in tempo reale, supporto alle formule e ricchi strumenti di visualizzazione dei dati, simili alle tradizionali applicazioni desktop.
- Supporta l'input e la modifica dei dati, la formattazione, la navigazione nei fogli di calcolo, il calcolo delle formule, la manipolazione dei dati, i grafici e le visualizzazioni, l'importazione e l'esportazione, la sicurezza, i componenti aggiuntivi e la personalizzazione per i sviluppatori per adattare l'editor alle specifiche esigenze aziendali.

## Funzionalità


- Importa, visualizza e modifica i popolari formati di fogli di calcolo.
- Esporta i fogli di calcolo in vari formati di file supportati.
- Visualizza e gestisce i file di immagine, forma o grafico.
- Esegui personalizzazione del design e layout della griglia.
- Gestione di più fogli di lavoro.
- Creazione e calcolo delle formule di Excel®.

## Formati file supportati

https://docs.aspose.com/cells/python-net/supported-file-formats/

## Utilizzo generale

Di seguito i passaggi di base per sviluppare un'applicazione web di GridJs.

- Imposta la directory di archiviazione della cache con Config.set_file_cache_directory(`percorso di archiviazione`);
- Imposta la licenza con Config.set_license(`percorso della licenza`);
- Imposta l'URL del percorso dell'immagine con GridJsWorkbook.set_image_url_base(`percorso per visualizzare l'immagine`);
- Imposta un'azione di percorso per ottenere `json` dal file di foglio elettronico. È possibile utilizzare le API `GridJsWorkbook.ImportExcelFile` e `GridJsWorkbook.ExportToJson`, `GridJs` memorizzerà automaticamente il file del foglio elettronico nella cache.
- Imposta un'azione di percorso per ottenere `json` per l'operazione di aggiornamento. È possibile utilizzare l'API `GridJsWorkbook.UpdateCell`, `GridJs` effettuerà l'operazione di aggiornamento nella cache e restituirà il `json` aggiornato.
- Imposta un'azione di percorso per ottenere il file dalla cache, in questo modo è possibile ottenere il file zip delle immagini/forme o il file di foglio elettronico dalla cache.
- Imposta un'azione di percorso per scaricare il foglio elettronico. È possibile utilizzare l'API `GridJsWorkbook.SaveToCacheWithFileName`.

Di seguito è presentato un esempio di base per mostrare l'uso di Aspose.Cells.GridJs:

https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs_Python_Net 

Nell'esempio utilizziamo [gridjs-spreadsheet](https://www.npmjs.com/package/gridjs-spreadsheet) per il rendering della pagina lato client.

Se hai domande, requisiti o hai bisogno di aiuto, per favore fornisci un feedback al seguente sito web https://forum.aspose.com/c/cells/9
