---
title: Imposta l'origine dati per il grafico
description: Scopri le varie origini dati supportate da Aspose.Cells for .NET. La nostra guida ti guiderà attraverso i diversi tipi di origini dati disponibili e ti mostrerà come connetterti e recuperare i dati da esse per popolare i tuoi fogli di lavoro.
keywords: Aspose.Cells for .NET, charting, data formatting, labels, colors, fonts, appearance, usability.
linktitle: Fonte di dati
type: docs
weight: 10
url: /it/net/data-formatting-in-charts/
---
Nei nostri argomenti precedenti abbiamo già fornito molti esempi per dimostrare come impostare un'origine dati per il grafico, ma in questo argomento forniremo maggiori dettagli sui tipi di dati che possono essere impostati per un grafico.

##  **Impostazione dei dati della mappa**

Esistono due tipi di dati da gestire mentre si lavora sui grafici utilizzando Aspose.Cells come segue:

- Dati del grafico.
- Dati di categoria.

###  **Dati del grafico**

 I dati del grafico sono i dati che utilizziamo come fonte di dati per costruire i nostri grafici. Possiamo aggiungere un intervallo di celle (contenenti i dati del grafico) chiamando il metodo[**SerieCollezione**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) dell'oggetto[**Aggiungere**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)metodo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

###  **Dati di categoria**

 I dati di categoria vengono utilizzati per l'etichettatura dei dati del grafico e possono essere aggiunti[**SerieCollezione**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) utilizzando il suo[**CategoriaDati**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)proprietà. Di seguito viene fornito un esempio completo per dimostrare l'utilizzo dei dati di grafici e categorie. Dopo aver eseguito il codice di esempio sopra, un istogramma verrà aggiunto al foglio di lavoro come mostrato di seguito.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

##  **Argomenti avanzati**
- [Modifica l'origine dati del grafico nel foglio di lavoro di destinazione durante la copia di righe o intervallo](/cells/it/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Crea grafici dinamici](/cells/it/net/create-dynamic-charts/)
- [Un modo semplice per impostare il grafico utilizzando il metodo Chart.SetChartDataRange](/cells/it/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Trova il tipo di valori X e Y dei punti nella serie di grafici](/cells/it/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
