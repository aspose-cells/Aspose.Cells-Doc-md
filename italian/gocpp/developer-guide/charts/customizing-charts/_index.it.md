---
title: Personalizzazione dei grafici con Golang tramite C++
linktitle: Personalizzazione dei grafici
description: Impara come personalizzare grafici in Aspose.Cells for C++. La nostra guida ti mostrerà come modificare il layout del grafico, aggiungere e formattare le serie di dati, regolare gli assi e applicare varie opzioni di formattazione per migliorare l aspetto e l usabilità dei tuoi grafici.
keywords: Aspose.Cells for C++, grafici, personalizzazione, layout, serie di dati, assi, formattazione, aspetto, usabilità.
type: docs
weight: 40
url: /it/go-cpp/customizing-charts/
---


## **Creazione di grafici personalizzati**

Finora, quando abbiamo parlato di grafici, abbiamo esaminato grafici standard con le loro impostazioni di formattazione standard. Definiamo solo la fonte dei dati, impostiamo alcune proprietà e il grafico viene creato con le sue impostazioni di formato predefinite. Ma le API di Aspose.Cells supportano anche la creazione di grafici personalizzati che permettono agli sviluppatori di creare grafici con le proprie impostazioni di formato.

Gli sviluppatori possono creare grafici personalizzati in fase di esecuzione utilizzando Aspose.Cells.

Un grafico è composto da una serie di dati. Ogni serie di dati in Aspose.Cells è rappresentata da un oggetto [**Series**](https://reference.aspose.com/cells/go-cpp/series/), mentre un oggetto [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) funge da collezione di oggetti [**Series**](https://reference.aspose.com/cells/go-cpp/series/). Creando un grafico personalizzato, gli sviluppatori hanno la libertà di utilizzare diversi tipi di grafici per diverse serie di dati (raccolte nell'oggetto [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)).

Il codice di esempio di seguito dimostra come creare grafici personalizzati. In questo esempio, utilizzeremo un grafico a colonne per la prima serie di dati e un grafico a linee per la seconda serie. Il risultato è che aggiungiamo un grafico a colonne, combinato con un grafico a linee, al foglio di lavoro.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizingCharts.go" >}}
{{% alert color="primary" %}}

Attualmente, Aspose.Cells supporta solo grafici personalizzati che combinano grafici a torta, linee, colonne e colonne impilate, ma altri grafici saranno supportati in future versioni.

{{% /alert %}}
