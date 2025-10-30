---
title: Imposta la sorgente dati per il grafico con Golang tramite C++
linktitle: Origine dati
type: docs
weight: 10
url: /it/go-cpp/data-formatting-in-charts/
description: Impara sui vari tipi di fonti di dati supportate da Aspose.Cells for C++. La nostra guida ti illustrerà i diversi tipi di fonti di dati disponibili e ti mostrerà come connetterti e recuperare dati da esse per compilare i tuoi fogli di lavoro.
keywords: Aspose.Cells for C++, grafici, formattazione dati, etichette, colori, caratteri, aspetto, usabilità.
---

Nei nostri argomenti precedenti, abbiamo già fornito molti esempi per dimostrare come puoi impostare una fonte di dati per il tuo grafico. In questo argomento, forniremo ulteriori dettagli sui tipi di dati che possono essere impostati per un grafico.

## **Impostazione dei dati del grafico**

Ci sono due tipi di dati con cui lavorare mentre si lavora sui grafici utilizzando Aspose.Cells come segue:

- Dati del grafico.
- Dati di categoria.

### **Dati del grafico**

I dati del grafico sono i dati che utilizziamo come origine dati per costruire i nostri grafici. Possiamo aggiungere un intervallo delle celle (contenenti dati del grafico) chiamando il metodo [**Add**](https://reference.aspose.com/cells/go-cpp/seriescollection/add/) dell'oggetto [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource.go" >}}
### **Dati di categoria**

I dati di categoria vengono utilizzati per l'etichettatura dei dati del grafico e possono essere aggiunti a [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/) utilizzando la sua proprietà [**GetCategoryData()**](https://reference.aspose.com/cells/go-cpp/seriescollection/getcategorydata/). Di seguito viene fornito un esempio completo per dimostrare l'uso dei dati del grafico e di categoria. Dopo l'esecuzione del codice di esempio sopra, verrà aggiunto un grafico a colonne al foglio di lavoro come mostrato di seguito.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource-1.go" >}}
## **Argomenti Avanzati**
- [Modifica dell'origine dei dati del grafico al foglio di lavoro di destinazione durante la copia delle righe o dell'intervallo](/cells/it/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Creazione di grafici dinamici](/cells/it/cpp/create-dynamic-charts/)
- [Modo semplice per l'impostazione del grafico utilizzando il metodo Chart.SetChartDataRange](/cells/it/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Trova il tipo di valori X e Y dei punti nella serie del grafico](/cells/it/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
