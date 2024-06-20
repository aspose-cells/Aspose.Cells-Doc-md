---
title: Personalizzazione dei grafici
description: Scopri come personalizzare i grafici in Aspose.Cells for .NET. La nostra guida ti mostrerà come modificare i layout dei grafici, aggiungere e formattare le serie di dati, regolare gli assi e applicare varie opzioni di formattazione per migliorare l aspetto e l usabilità dei tuoi grafici.
keywords: Aspose.Cells for .NET, grafici, personalizzazione, layout, serie di dati, assi, formattazione, aspetto, usabilità.
type: docs
weight: 40
url: /it/net/customizing-charts/
---

{{% alert color="primary" %}}

## **Creazione di grafici personalizzati**

Finora, quando abbiamo discusso dei grafici, abbiamo guardato i grafici standard che hanno le loro impostazioni standard di formattazione. Abbiamo solo definito la fonte dati, impostato alcune proprietà e il grafico è stato creato con le sue impostazioni di formato predefinite. Ma le API di Aspose.Cells supportano anche la creazione di grafici personalizzati che permette agli sviluppatori di creare grafici con le proprie impostazioni di formato.

Gli sviluppatori possono creare grafici personalizzati in fase di esecuzione utilizzando Aspose.Cells.

Un grafico è composto da una serie di dati. Ogni serie di dati in Aspose.Cells è rappresentata da un oggetto [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series), mentre un oggetto [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) funge da collezione di oggetti [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series). Creando un grafico personalizzato, gli sviluppatori hanno la libertà di utilizzare diversi tipi di grafici per diverse serie di dati (raccolte nell'oggetto [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)).

Il codice di esempio di seguito dimostra come creare grafici personalizzati. In questo esempio, utilizzeremo un grafico a colonne per la prima serie di dati e un grafico a linee per la seconda serie. Il risultato è che aggiungiamo un grafico a colonne, combinato con un grafico a linee, al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

Attualmente Aspose.Cells supporta solo grafici personalizzati che combinano grafici a torta, a linee, a colonne e a pila di colonne, ma altri grafici saranno supportati in future versioni.

{{% /alert %}}
