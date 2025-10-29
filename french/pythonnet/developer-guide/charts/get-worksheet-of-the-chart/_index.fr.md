---
title: Obtenir la feuille de calcul du graphique
description: Découvrez comment récupérer la feuille de calcul associée à un graphique Excel en utilisant Aspose.Cells pour Python via .NET. Notre guide vous montrera comment accéder à la feuille et effectuer des opérations pour manipuler les données sous jacentes du graphique.
keywords: Aspose.Cells pour Python via .NET, graphiques Excel, feuilles de calcul, manipulation de données, données sous jacentes, opérations.
type: docs
weight: 1000
url: /fr/python-net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Parfois, vous souhaitez accéder à une feuille de calcul à partir de la référence d'un graphique. Aspose.Cells pour Python via .NET fournit la propriété [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet) qui retourne la référence de la feuille contenant le graphique.

{{% /alert %}}

L'exemple suivant montre comment utiliser la propriété [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet). Le code imprime d'abord le nom de la feuille de calcul, puis accède au premier graphique sur la feuille de calcul. Il imprime ensuite à nouveau le nom de la feuille de calcul, en utilisant la propriété [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetWorksheetOfTheChart.py" >}}

Voici la sortie console que le code d'exemple produit. Comme vous pouvez le voir, il imprime le même nom de feuille de calcul à chaque fois.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
