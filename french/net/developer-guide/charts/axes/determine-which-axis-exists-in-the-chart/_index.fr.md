---
title: Déterminer quel axe existe dans le graphique
type: docs
weight: 140
url: /fr/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

Parfois, l'utilisateur a besoin de savoir si un axe particulier existe dans le graphique. Par exemple, il veut savoir si un axe de valeur secondaire existe à l'intérieur du graphique ou non. Certains graphiques comme Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, etc. n'ont pas d'axe.

 Aspose.Cells fournit[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) méthode pour déterminer si le graphique a un axe particulier ou non.

{{% /alert %}}

 L'exemple de code suivant illustre l'utilisation de[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)pour déterminer si l'exemple de graphique a une catégorie primaire et secondaire et un axe des valeurs.

## Code C# pour déterminer quel axe existe dans le graphique

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Sortie de la console générée par l'exemple de code

La sortie de console du code a été montrée ci-dessous qui affiche vrai pour la catégorie primaire et l'axe des valeurs et faux pour la catégorie secondaire et l'axe des valeurs.

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
