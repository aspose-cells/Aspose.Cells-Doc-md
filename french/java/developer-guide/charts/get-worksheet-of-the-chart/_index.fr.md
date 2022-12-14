---
title: Obtenir la feuille de calcul du graphique
type: docs
weight: 80
url: /fr/java/get-worksheet-of-the-chart/
---
{{% alert color="primary" %}}

Parfois, vous souhaitez accéder à une feuille de calcul à partir de la référence d'un graphique. Aspose.Cells fournit le[**Graphique.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) propriété qui renvoie la référence de la feuille de calcul contenant le graphique.

{{% /alert %}}

## Exemple

 L'exemple suivant montre comment utiliser le[**Graphique.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) propriété. Le code imprime d'abord le nom de la feuille de calcul, puis accède au premier graphique de la feuille de calcul. Il imprime ensuite à nouveau le nom de la feuille de calcul, à l'aide de la[**Graphique.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)propriété.

### Java code pour accéder à la feuille de calcul du graphique

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetWorksheetOfChart-GetWorksheetOfChart.java" >}}

### Sortie de la console générée par l'exemple de code

Vous trouverez ci-dessous la sortie de la console à laquelle aboutit l'exemple de code. Comme vous pouvez le voir, il imprime le même nom de feuille de calcul les deux fois.

{{< highlight "java" >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
