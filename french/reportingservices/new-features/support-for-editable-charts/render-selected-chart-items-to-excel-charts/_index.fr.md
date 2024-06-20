---
title: Rendre les éléments sélectionnés du graphique sous forme de graphiques Excel
type: docs
weight: 30
url: /fr/reportingservices/render-selected-chart-items-to-excel-charts/
---

{{% alert color="primary" %}} 

Pour rendre uniquement certains graphiques dans un rapport sous forme de graphiques Excel :

1. Ouvrez le fichier **Aspose.Cells.ReportingServices.xml**.
1. Modifiez les paramètres de configuration du fichier **Aspose.Cells.ReportingServices.xml**.
1. Ajoutez les informations de configuration de rapport souhaitées.
1. Ajoutez les informations pour les éléments du graphique que vous ne voulez pas exporter en tant que graphiques modifiables. Ces éléments sont exportés sous forme d'images statiques.

Par exemple:

{{< highlight java >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**Un graphique exporté sous forme d'image** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_1.png)

**Un graphique exporté sous forme de graphique Excel modifiable** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
