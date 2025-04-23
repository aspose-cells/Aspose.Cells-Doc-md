---
title: Obtenir la feuille de calcul du graphique
type: docs
weight: 80
url: /fr/java/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Parfois, vous voulez accéder à une feuille de calcul à partir d'une référence à un graphique. Aspose.Cells fournit la propriété [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) qui renvoie la référence de la feuille de calcul contenant le graphique.

{{% /alert %}}

## Exemple

L'exemple suivant montre comment utiliser la propriété [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet). Le code imprime d'abord le nom de la feuille de calcul, puis accède au premier graphique sur la feuille de calcul. Il imprime ensuite à nouveau le nom de la feuille de calcul, en utilisant la propriété [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet).

### Code Java pour accéder à la feuille de calcul du graphique

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetWorksheetOfChart-GetWorksheetOfChart.java" >}}

### Sortie de la console générée par le code d'exemple

Ci-dessous la sortie console résultant du code d'exemple. Comme vous pouvez le voir, il imprime le même nom de feuille de calcul à chaque fois.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
