---
title: Obtenir le texte de l'équation de la ligne de tendance du graphique
linktitle: Ligne de tendance
type: docs
weight: 90
url: /fr/java/get-equation-text-of-chart-trendline/
---
{{% alert color="primary" %}}

 Vous pouvez récupérer le texte de l'équation de la ligne de tendance du graphique en utilisant Aspose.Cells. Aspose.Cells fournit[**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) propriété qui renvoie le texte de l'équation de la courbe de tendance du graphique. Pour profiter de cette propriété, vous devrez d'abord appeler[**Graphique.calculer()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()) méthode.

{{% /alert %}}

## **Exemple**

 La capture d'écran suivante montre le graphique avec une ligne de tendance et son texte d'équation est affiché en rouge. Nous allons récupérer ce texte à l'aide de la[**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)propriété dans l'exemple de code suivant.

![tâche : image_autre_texte](get-equation-text-of-chart-trendline_1.png)

### Code Java pour obtenir le texte de l'équation de la courbe de tendance du graphique

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### Sortie générée par l'exemple de code

Il s'agit de la sortie console de l'exemple de code ci-dessus.

{{< highlight "java" >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
