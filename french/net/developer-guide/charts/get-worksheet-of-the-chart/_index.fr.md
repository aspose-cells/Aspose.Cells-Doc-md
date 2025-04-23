---
title: Obtenir la feuille de calcul du graphique
description: Apprenez à récupérer la feuille de calcul associée à un graphique Excel en utilisant Aspose.Cells for .NET. Notre guide vous montrera comment accéder à la feuille de calcul et effectuer des opérations dessus pour manipuler les données sous jacentes du graphique.
keywords: Aspose.Cells for .NET, graphiques Excel, feuilles de calcul, manipulation des données, données sous jacentes, opérations.
type: docs
weight: 1000
url: /fr/net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Parfois, vous voulez accéder à une feuille de calcul à partir d'une référence à un graphique. Aspose.Cells fournit la propriété [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet) qui renvoie la référence de la feuille de calcul contenant le graphique.

{{% /alert %}}

L'exemple suivant montre comment utiliser la propriété [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet). Le code imprime d'abord le nom de la feuille de calcul, puis accède au premier graphique sur la feuille de calcul. Il imprime ensuite à nouveau le nom de la feuille de calcul, en utilisant la propriété [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetWorksheetOfTheChart-GetWorksheetOfTheChart.cs" >}}

Voici la sortie console que le code d'exemple produit. Comme vous pouvez le voir, il imprime le même nom de feuille de calcul à chaque fois.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
