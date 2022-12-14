---
title: Renderizza gli elementi del grafico selezionati nei grafici di Excel
type: docs
weight: 30
url: /it/reportingservices/render-selected-chart-items-to-excel-charts/
---
{{% alert color="primary" %}} 

Per eseguire il rendering solo di alcuni grafici in un report in grafici Excel:

1. Apri il**Aspose.Cells.ReportingServices.xml** file.
1.  Modificare i parametri di configurazione del**Aspose.Cells.ReportingServices.xml** file.
1. Aggiungere le informazioni di configurazione del report desiderate.
1. Aggiungere le informazioni per gli elementi del grafico che non si desidera esportare come grafici modificabili. Questi elementi vengono esportati come immagini statiche.

Per esempio:

{{< highlight "java" >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**Un grafico esportato come immagine** 

![cose da fare:immagine_alt_testo](render-selected-chart-items-to-excel-charts_1.png)

**Un grafico esportato come grafico Excel modificabile** 

![cose da fare:immagine_alt_testo](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
