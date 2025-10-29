---
title: Obtenir le texte d équation de la tendance du graphique
description: Découvrez comment utiliser Aspose.Cells pour Python via .NET pour récupérer le texte de l’équation d’une ligne de tendance dans un graphique créé dans Microsoft Excel. Notre guide montrera comment accéder et extraire l’équation d’une ligne de tendance pour une analyse ou une présentation ultérieure.
keywords: Aspose.Cells pour Python via .NET, Ligne de tendance du graphique, Texte de l’équation, Microsoft Excel, Analyse de données, Affichage.
linktitle: Trendlines
type: docs
weight: 110
url: /fr/python-net/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Vous pouvez récupérer le texte de l’équation de la ligne de tendance du graphique en utilisant Aspose.Cells pour Python via .NET. Aspose.Cells pour Python via .NET fournit une propriété qui retourne le texte de l’équation de la ligne de tendance du graphique. Pour utiliser cette propriété, vous devrez d’abord appeler la méthode [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate).

{{% /alert %}}

La capture d'écran suivante montre le graphique avec une tendance et son texte d'équation est affiché en rouge. Nous récupérerons ce texte en utilisant la propriété [**Trendline.data_labels.text**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/datalabels/text) dans le code d'exemple suivant.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Code C# pour obtenir le texte d'équation de la tendance du graphique

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetEquationTextOfChartTrendLine-1.py" >}}

## Sortie générée par le code d'exemple

Il s'agit de la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
