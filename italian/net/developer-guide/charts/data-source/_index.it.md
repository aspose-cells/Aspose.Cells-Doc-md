---
title: Impostare l'origine dati per il grafico
linktitle: Fonte di dati
type: docs
weight: 10
url: /it/net/data-formatting-in-charts/
---
Nei nostri argomenti precedenti, abbiamo già fornito molti esempi per dimostrare come puoi impostare un'origine dati per il tuo grafico, ma in questo argomento forniremo maggiori dettagli sui tipi di dati che possono essere impostati per un grafico.

## **Impostazione dei dati del grafico**

Esistono due tipi di dati da gestire mentre si lavora sui grafici utilizzando Aspose.Cells come segue:

- Dati cartografici.
- Dati di categoria.

### **Dati del grafico**

 dati del grafico sono i dati che utilizziamo come origine dati per costruire i nostri grafici. Possiamo aggiungere un intervallo di celle (contenenti i dati del grafico) chiamando il metodo[**SerieCollezione**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) dell'oggetto[**Aggiungere**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)metodo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **Dati di categoria**

 I dati di categoria vengono utilizzati per l'etichettatura dei dati del grafico e possono essere aggiunti[**SerieCollezione**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) utilizzando il suo[**CategoriaDati**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)proprietà. Di seguito viene fornito un esempio completo per dimostrare l'uso dei dati di grafici e categorie. Dopo aver eseguito il codice di esempio precedente, un istogramma verrà aggiunto al foglio di lavoro come mostrato di seguito.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **Argomenti avanzati**
- [Cambia l'origine dati del grafico nel foglio di lavoro di destinazione durante la copia di righe o intervalli](/cells/it/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Crea grafici dinamici](/cells/it/net/create-dynamic-charts/)
- [Modo semplice per l'impostazione del grafico utilizzando il metodo Chart.SetChartDataRange](/cells/it/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Trova il tipo di valori X e Y dei punti nella serie di grafici](/cells/it/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
