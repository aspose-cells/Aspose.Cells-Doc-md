---
title: Déterminer quel axe existe dans le graphique
description: Découvrez comment déterminer quel axe existe dans un graphique créé à l'aide du Aspose.Cells for .NET. Notre guide vous aidera à comprendre comment identifier et accéder aux différents axes d'un graphique, y compris les axes de catégorie, de valeur et secondaires.
keywords: Aspose.Cells for .NET, chart, axis, existence, category, value, secondary.
type: docs
weight: 140
url: /fr/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

Parfois, l'utilisateur a besoin de savoir si un axe particulier existe dans le graphique. Par exemple, il veut savoir si un axe de valeur secondaire existe ou non à l'intérieur du graphique. Certains graphiques comme Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, etc. n'ont pas d'axe.

 Aspose.Cells fournit[**Chart.HasAxis (AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) méthode pour déterminer si le graphique a un axe particulier ou non.

{{% /alert %}}

 L'exemple de code suivant illustre l'utilisation de[**Chart.HasAxis (AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)pour déterminer si l'exemple de graphique comporte des catégories primaires et secondaires et un axe de valeurs.

##  Code C# pour déterminer quel axe existe dans le graphique

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Sortie de console générée par l'exemple de code

La sortie de console du code a été présentée ci-dessous et affiche vrai pour la catégorie principale et l'axe des valeurs et faux pour la catégorie secondaire et l'axe des valeurs.

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
