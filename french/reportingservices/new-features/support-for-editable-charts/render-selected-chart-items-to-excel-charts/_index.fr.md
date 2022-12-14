---
title: Rendre les éléments de graphique sélectionnés en graphiques Excel
type: docs
weight: 30
url: /fr/reportingservices/render-selected-chart-items-to-excel-charts/
---
{{% alert color="primary" %}} 

Pour afficher uniquement certains graphiques d'un rapport sous forme de graphiques Excel :

1. Ouvrez le**Aspose.Cells.ReportingServices.xml** dossier.
1.  Modifier les paramètres de configuration du**Aspose.Cells.ReportingServices.xml** dossier.
1. Ajoutez les informations de configuration de rapport souhaitées.
1. Ajoutez les informations pour les éléments de graphique que vous ne souhaitez pas exporter en tant que graphiques modifiables. Ces éléments sont exportés sous forme d'images statiques.

Par exemple:

{{< highlight "java" >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**Un graphique exporté sous forme d'image** 

![tâche : image_autre_texte](render-selected-chart-items-to-excel-charts_1.png)

**Un graphique exporté sous forme de graphique Excel modifiable** 

![tâche : image_autre_texte](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
