---
title: Colori di sezioni o settori personalizzati nel grafico a torta
type: docs
weight: 30
url: /it/java/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

Questo articolo spiega come aggiungere colori personalizzati alle fette/settori del grafico a torta. Per impostazione predefinita, i grafici a torta utilizzano il modello predefinito di Microsoft Excel. Per utilizzare altri colori, è possibile ridefinire i colori nella tabella.

{{% /alert %}}

Per impostare il colore personalizzato per le singole fette o settori di un grafico a torta:

1.  Accedi al[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) dell'oggetto[**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint).
1.  Assegna un colore a tua scelta usando il[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)metodo.

Questo articolo spiega anche come impostare:

- I dati di categoria di un grafico.
- Un titolo del grafico collegato a una cella.
- Le impostazioni del carattere del titolo del grafico.
- La posizione della leggenda.

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)non è specifico per i grafici a torta ma può essere utilizzato per tutti i tipi di grafici.

{{% /alert %}}

**Colori delle fette personalizzati nel grafico a torta**

![cose da fare:immagine_alt_testo](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
