---
title: Obtenir la feuille de calcul du graphique avec Golang via C++
linktitle: Obtenir la feuille de calcul du graphique
description: Découvrez comment récupérer la feuille associée à un graphique Excel à l aide de Aspose.Cells for C++. Notre guide vous montrera comment accéder à la feuille et y effectuer des opérations pour manipuler les données sous jacentes du graphique.
keywords: Aspose.Cells for C++, graphiques Excel, feuilles de calcul, manipulation de données, données sous jacentes, opérations.
type: docs
weight: 1000
url: /fr/go-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Parfois, vous souhaitez accéder à une feuille de calcul à partir d'une référence de graphique. Aspose.Cells fournit la méthode [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/) qui retourne la référence de la feuille contenant le graphique.

{{% /alert %}}

L'exemple suivant montre comment utiliser la méthode [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/). Le code affiche d'abord le nom de la feuille, puis accède au premier graphique de la feuille. Ensuite, il affiche à nouveau le nom de la feuille en utilisant la méthode [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWorksheetOfTheChart.go" >}}
Voici la sortie console que le code d'exemple produit. Comme vous pouvez le voir, il imprime le même nom de feuille de calcul à chaque fois.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
