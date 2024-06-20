---
title: Imposta la fonte dati per il grafico
description: Scopri le varie fonti dati supportate da Aspose.Cells for .NET. La nostra guida ti illustrerà i diversi tipi di fonti dati disponibili e ti mostrerà come connetterti e recuperare dati da esse per popolare i tuoi fogli di lavoro.
keywords: Aspose.Cells for .NET, creazione di grafici, formattazione dati, etichette, colori, caratteri, aspetto, usabilità.
linktitle: Fonte dati
type: docs
weight: 10
url: /it/net/data-formatting-in-charts/
---

Nei nostri argomenti precedenti, abbiamo già fornito molti esempi per dimostrare come è possibile impostare una fonte dati per il tuo grafico ma in questo argomento forniremo più dettagli sui tipi di dati che possono essere impostati per un grafico.

## **Impostazione dei dati del grafico**

Ci sono due tipi di dati con cui lavorare mentre si lavora sui grafici utilizzando Aspose.Cells come segue:

- Dati del grafico.
- Dati di categoria.

### **Dati del grafico**

I dati del grafico sono i dati che utilizziamo come origine dati per costruire i nostri grafici. Possiamo aggiungere un intervallo delle celle (contenenti dati del grafico) chiamando il metodo [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add) dell'oggetto [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **Dati di categoria**

I dati di categoria vengono utilizzati per l'etichettatura dei dati del grafico e possono essere aggiunti a [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) utilizzando la sua proprietà [**CategoryData**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata). Di seguito viene fornito un esempio completo per dimostrare l'uso dei dati del grafico e di categoria. Dopo l'esecuzione del codice di esempio sopra, verrà aggiunto un grafico a colonne al foglio di lavoro come mostrato di seguito.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **Argomenti avanzati**
- [Modifica dell'origine dei dati del grafico al foglio di lavoro di destinazione durante la copia delle righe o dell'intervallo](/cells/it/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Creazione di grafici dinamici](/cells/it/net/create-dynamic-charts/)
- [Modo semplice per l'impostazione del grafico utilizzando il metodo Chart.SetChartDataRange](/cells/it/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Trova il tipo di valori X e Y dei punti nella serie del grafico](/cells/it/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
