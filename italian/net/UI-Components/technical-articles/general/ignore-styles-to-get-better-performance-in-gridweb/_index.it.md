---
title: Ignora gli stili per ottenere prestazioni migliori in GridWeb
type: docs
weight: 1060
url: /it/net/aspose-cells-gridweb/ignorestylewithnodata
description: Questo articolo descrive come usare IgnoreStyleWithNoData per ottenere prestazioni migliori per la libreria Aspose.Cells.GridWeb.
keywords: performance
---
## **Possibili scenari di utilizzo**
 Si prega di utilizzare[GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata)proprietà per caricare meno righe/colonne richieste dalla cartella di lavoro.
 
## **Ottieni prestazioni migliori durante il caricamento della cartella di lavoro**
 Si prega di controllare[file excel di esempio](largerowswithstyle.xlsx) 

Quando impostato IgnoreStyleWithNoData = true;

Come puoi vedere, mostra righe (a 15) e colonne (a L), non visualizzerà le ultime righe e colonne continue senza dati nelle celle. Pertanto, il tempo di caricamento sarà inferiore.

![cartella di lavoro con stile ignora](ignorestyletrue.png)


Quando impostato IgnoreStyleWithNoData = false; (il valore predefinito è false)

Come puoi vedere, mostra molte più righe (fino a 500) e colonne (fino a CZ)

Dalla riga 16 alla riga 500, alcune celle hanno impostato lo stile boder, tuttavia le celle non contengono dati.

Dalla colonna M alla colonna CZ, alcune celle hanno impostato lo stile boder, tuttavia le celle non contengono dati.

![cartella di lavoro senza ignorare lo stile](ignorestylefalse.png)
 
 
 