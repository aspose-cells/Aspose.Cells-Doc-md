---
title: Obtenir le texte de l équation de la ligne de tendance du graphique avec Golang via C++
linktitle: Trendlines
description: Apprenez comment utiliser Aspose.Cells for C++ pour récupérer le texte de l’équation d’une ligne de tendance dans un graphique créé dans Microsoft Excel. Notre guide montrera comment accéder à cette équation et l’extraire pour une analyse ou une affichage ultérieur.
keywords: Aspose.Cells for C++, Ligne de tendance du graphique, Texte de l’équation, Microsoft Excel, Analyse de données, Affichage.
type: docs
weight: 110
url: /fr/go-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Vous pouvez récupérer le texte d'équation de la tendance du graphique en utilisant Aspose.Cells. Aspose.Cells fournit la propriété [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/) qui retourne le texte d'équation de la tendance du graphique. Pour utiliser cette propriété, vous devrez d'abord appeler la méthode [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/).

{{% /alert %}}

La capture d'écran suivante montre le graphique avec une ligne de tendance et son texte d'équation en rouge. Nous allons récupérer ce texte en utilisant la propriété [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/) dans l'exemple de code ci-dessous.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Code C++ pour obtenir le texte de l’équation de la ligne de tendance du graphique

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Trendlines.go" >}}
## Sortie générée par le code d'exemple

Il s'agit de la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
