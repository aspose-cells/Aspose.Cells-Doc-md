---
title: Personalizzazione dei grafici
description: Impara come personalizzare i grafici in Aspose.Cells per Python via .NET. La nostra guida ti mostrerà come modificare i layout del grafico, aggiungere e formattare le serie di dati, regolare gli assi e applicare varie opzioni di formattazione per migliorare l aspetto e l usabilità dei tuoi grafici.
keywords: Aspose.Cells per Python via .NET, grafici, personalizzazione, layout, serie di dati, assi, formattazione, aspetto, usabilità.
type: docs
weight: 40
url: /it/python-net/customizing-charts/
---


## **Creazione di grafici personalizzati**

Finora, quando abbiamo discusso di grafici, abbiamo esaminato grafici standard che hanno le proprie impostazioni di formattazione standard. Definiamo solo la fonte dei dati, impostiamo alcune proprietà e il grafico viene creato con le impostazioni predefinite. Ma le API di Aspose.Cells per Python via .NET supportano anche la creazione di grafici personalizzati che consentono agli sviluppatori di creare grafici con le proprie impostazioni di formato.

Gli sviluppatori possono creare grafici personalizzati al momento dell'esecuzione utilizzando Aspose.Cells per Python via .NET.

Un grafico è composto da una serie di dati. Ogni serie di dati in Aspose.Cells per Python via .NET è rappresentata da un oggetto [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series) mentre l'oggetto [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) serve come raccolta di oggetti [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series). Quando si crea un grafico personalizzato, gli sviluppatori hanno la libertà di usare diversi tipi di grafici per diverse serie di dati (raccolti nell'oggetto [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)).

Il codice di esempio di seguito dimostra come creare grafici personalizzati. In questo esempio, utilizzeremo un grafico a colonne per la prima serie di dati e un grafico a linee per la seconda serie. Il risultato è che aggiungiamo un grafico a colonne, combinato con un grafico a linee, al foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateCustomChart-1.py" >}}

{{% alert color="primary" %}}

Attualmente Aspose.Cells per Python via .NET supporta solo grafici personalizzati che combinano grafici a torta, lineari, a colonne e impilati, ma in future versioni saranno supportati altri tipi di grafici.

{{% /alert %}}
