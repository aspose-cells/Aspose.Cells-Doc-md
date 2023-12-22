---
title: Obtenir la feuille de calcul du graphique
description: Découvrez comment récupérer la feuille de calcul associée à un graphique Excel en utilisant le Aspose.Cells for .NET. Notre guide vous montrera comment accéder à la feuille de calcul et y effectuer des opérations pour manipuler les données sous-jacentes du graphique.
keywords: Aspose.Cells for .NET, Excel charts, worksheets, data manipulation, underlying data, operations.
type: docs
weight: 1000
url: /fr/net/get-worksheet-of-the-chart/
---
{{% alert color="primary" %}}

 Parfois, vous souhaitez accéder à une feuille de calcul à partir de la référence d'un graphique. Aspose.Cells fournit le[**Graphique.Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet) propriété qui renvoie la référence de la feuille de calcul contenant le graphique.

{{% /alert %}}

 L'exemple suivant montre comment utiliser le[**Graphique.Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet) propriété. Le code imprime d'abord le nom de la feuille de calcul, puis accède au premier graphique de la feuille de calcul. Il imprime ensuite à nouveau le nom de la feuille de calcul, en utilisant le[**Graphique.Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet)propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetWorksheetOfTheChart-GetWorksheetOfTheChart.cs" >}}

Vous trouverez ci-dessous la sortie de la console résultant de l'exemple de code. Comme vous pouvez le voir, il imprime le même nom de feuille de calcul les deux fois.

{{< highlight "java" >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
