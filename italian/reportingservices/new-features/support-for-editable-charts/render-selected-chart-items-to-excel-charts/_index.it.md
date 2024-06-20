---
title: Rendere gli elementi del grafico selezionato come grafici di Excel
type: docs
weight: 30
url: /it/reportingservices/render-selected-chart-items-to-excel-charts/
---

{{% alert color="primary" %}} 

Per rendere solo alcuni grafici di un report come grafici di Excel:

1. Aprire il file **Aspose.Cells.ReportingServices.xml**.
1. Modificare i parametri di configurazione del file **Aspose.Cells.ReportingServices.xml**.
1. Aggiungere le informazioni di configurazione del report desiderato.
1. Aggiungere le informazioni per gli elementi del grafico che non si desidera esportare come grafici modificabili. Questi elementi vengono esportati come immagini statiche.

Per esempio:

{{< highlight java >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**Un grafico esportato come un'immagine** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_1.png)

**Un grafico esportato come un grafico di Excel modificabile** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
