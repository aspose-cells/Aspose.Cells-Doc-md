---
title: Personalizzazione dei grafici
description: Scopri come personalizzare i grafici al numero Aspose.Cells for .NET. La nostra guida ti mostrerà come modificare i layout dei grafici, aggiungere e formattare serie di dati, regolare gli assi e applicare varie opzioni di formattazione per migliorare l'aspetto e l'usabilità dei tuoi grafici.
keywords: Aspose.Cells for .NET, charting, customization, layouts, data series, axes, formatting, appearance, usability.
type: docs
weight: 40
url: /it/net/customizing-charts/
---
{{% alert color="primary" %}}

##  **Creazione di grafici personalizzati**

Finora, quando abbiamo parlato dei grafici, abbiamo esaminato i grafici standard che hanno le loro impostazioni di formattazione standard. Definiamo solo l'origine dati, impostiamo alcune proprietà e il grafico viene creato con le impostazioni di formato predefinite. Ma le API Aspose.Cells supportano anche la creazione di grafici personalizzati che consentono agli sviluppatori di creare grafici con le proprie impostazioni di formato.

Gli sviluppatori possono creare grafici personalizzati in fase di esecuzione utilizzando Aspose.Cells.

 Un grafico è composto da una serie di dati. Ciascuna serie di dati in Aspose.Cells è rappresentata da a[**Serie**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) oggetto mentre[**SerieCollezione**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) L'oggetto funge da raccolta di[**Serie**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)oggetti. Quando creano un grafico personalizzato, gli sviluppatori hanno la libertà di utilizzare diversi tipi di grafici per diverse serie di dati (raccolti nel file[**SerieCollezione**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)oggetto).

Il codice di esempio seguente mostra come creare grafici personalizzati. In questo esempio utilizzeremo un grafico a colonne per la prima serie di dati e un grafico a linee per la seconda serie. Il risultato è che aggiungiamo un grafico a colonne, combinato con un grafico a linee, al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

Attualmente Aspose.Cells supporta solo grafici personalizzati che combinano grafici a torta, a linee, a colonne e in pila, ma nelle versioni future saranno supportati più grafici.

{{% /alert %}}
