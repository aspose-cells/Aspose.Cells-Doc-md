---
title: Formattazione dei dati nei grafici
linktitle: Origine dati
type: docs
weight: 50
url: /it/java/data-formatting-in-charts/
---

{{% alert color="primary" %}}

Nei nostri argomenti precedenti, abbiamo già fornito molti esempi per dimostrare come è possibile impostare una fonte dati per il tuo grafico ma in questo argomento forniremo più dettagli sui tipi di dati che possono essere impostati per un grafico.

{{% /alert %}}

## **Impostazione dei dati del grafico**

Ci sono due tipi di dati con cui lavorare mentre si lavora sui grafici utilizzando Aspose.Cells come segue:

- [Dati del grafico](/cells/it/java/data-formatting-in-charts/#chart-data).
- [Dati di categoria](/cells/it/java/data-formatting-in-charts/#category-data).

### **Dati del grafico**

I dati del grafico sono quei dati che utilizziamo come origine dati per costruire i nostri grafici. Possiamo aggiungere un intervallo di celle (contenenti dati del grafico) chiamando il metodo [**Add**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object)) dell'oggetto [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **Dati di categoria**

I dati di categoria vengono utilizzati per l'etichettatura dei dati del grafico e possono essere aggiunti a [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) utilizzando il suo metodo [**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**Grafico a colonne con dati del grafico e di categoria** 

![todo:image_alt_text](data-formatting-in-charts_1.png)

## **Argomenti avanzati**
- [Creazione di grafici dinamici](/cells/it/java/create-dynamic-charts/)
- [Modo facile per l'impostazione del grafico utilizzando il metodo Chart.setChartDataRange](/cells/it/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Trova il tipo di valori X e Y dei punti nella serie del grafico](/cells/it/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [Impostare il codice di formato dei valori della serie del grafico](/cells/it/java/set-the-values-format-code-of-chart-series/)
