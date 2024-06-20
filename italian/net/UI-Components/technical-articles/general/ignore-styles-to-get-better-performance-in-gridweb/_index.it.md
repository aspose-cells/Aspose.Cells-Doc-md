---
title: Ignora gli stili per ottenere migliori prestazioni in GridWeb
type: docs
weight: 1060
url: /it/net/aspose-cells-gridweb/ignorestylewithnodata
description: Questo articolo descrive come utilizzare IgnoreStyleWithNoData per ottenere migliori prestazioni in GridWeb.
keywords: GridWeb,performance
---

## **Possibili Scenari di Utilizzo**
Si prega di utilizzare la proprietà [GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata) per caricare meno righe/colonne richieste dal foglio di calcolo.

## **Migliorare le prestazioni durante il caricamento del foglio di calcolo**
Si prega di verificare il [file excel di esempio](largerowswithstyle.xlsx) 

Quando imposti IgnoreStyleWithNoData = true;

Come puoi vedere, mostra righe (fino a 15) e colonne (fino a L), non visualizzerà le ultime righe e colonne continue senza dati nelle celle. Di conseguenza, il tempo di caricamento sarà inferiore.

![foglio di lavoro con stile ignorato](ignorestyletrue.png)


Quando si imposta IgnoreStyleWithNoData = false; (il valore predefinito è false)

Come puoi vedere, mostra molte più righe (fino a 500) e colonne (fino a CZ)

Dalla riga 16 alla riga 500, alcune celle hanno impostato lo stile del bordo, tuttavia le celle non contengono dati.

Dalla colonna M alla colonna CZ, alcune celle hanno impostato lo stile del bordo, tuttavia le celle non contengono dati.

![foglio di lavoro senza stile ignorato](ignorestylefalse.png)



