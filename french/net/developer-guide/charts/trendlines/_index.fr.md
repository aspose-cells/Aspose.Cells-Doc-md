---
title: Obtenir le texte de l'équation de la ligne de tendance du graphique
linktitle: Lignes de tendance
type: docs
weight: 110
url: /fr/net/get-equation-text-of-chart-trendline/
---
{{% alert color="primary" %}}

 Vous pouvez récupérer le texte de l'équation de la ligne de tendance du graphique en utilisant Aspose.Cells. Aspose.Cells fournit[**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text) propriété qui renvoie le texte de l'équation de la courbe de tendance du graphique. Pour profiter de cette propriété, vous devrez d'abord appeler[**Graphique.Calculer()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/calculate) méthode.

{{% /alert %}}

 La capture d'écran suivante montre le graphique avec une ligne de tendance et son texte d'équation est affiché en rouge. Nous allons récupérer ce texte à l'aide de la[**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text)propriété dans l'exemple de code suivant.

![tâche : image_autre_texte](get-equation-text-of-chart-trendline_1.png)

## C# code pour obtenir le texte de l'équation de la courbe de tendance du graphique

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetEquationTextOfChartTrendLine-1.cs" >}}

## Sortie générée par l'exemple de code

Il s'agit de la sortie console de l'exemple de code ci-dessus.

{{< highlight "java" >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
