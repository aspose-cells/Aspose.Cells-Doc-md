---
title: Obtenir le texte d équation de la tendance du graphique
linktitle: Tendance du graphique
type: docs
weight: 90
url: /fr/java/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Vous pouvez récupérer le texte d'équation de la tendance du graphique en utilisant Aspose.Cells. Aspose.Cells fournit la propriété [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) qui retourne le texte d'équation de la tendance du graphique. Pour utiliser cette propriété, vous devrez d'abord appeler la méthode [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--).

{{% /alert %}}

## **Exemple**

La capture d'écran suivante montre le graphique avec une tendance et son texte d'équation est affiché en rouge. Nous récupérerons ce texte en utilisant la propriété [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) dans le code d'exemple suivant.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

### Code Java pour obtenir le texte de l'équation de la tendance du graphique

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### Sortie générée par le code d'exemple

Il s'agit de la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
