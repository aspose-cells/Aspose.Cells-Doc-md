---
title: Déterminez quel axe existe dans le graphique
type: docs
weight: 130
url: /fr/java/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Parfois, l'utilisateur a besoin de savoir si un axe particulier existe dans le graphique. Par exemple, il veut savoir si un axe de valeur secondaire existe à l'intérieur du graphique ou non. Certains graphiques comme Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, etc. n'ont pas d'axe.

Aspose.Cells fournit [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis-int-boolean-) méthode pour déterminer si le graphique a un axe particulier ou non.

{{% /alert %}}

## Déterminez quel axe existe dans le graphique

La capture d'écran ci-dessous montre un graphique qui a uniquement l'axe de catégorie et de valeur principaux. Il n'a pas d'axe de catégorie et de valeur secondaires.

![todo:image_alt_text](determine-which-axis-exists-in-the-chart_1.png)

Le code d'exemple suivant démontre l'utilisation de [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis-int-boolean-) pour déterminer si le graphique d'exemple possède des axes de catégorie et de valeur principaux et secondaires. La sortie de la console du code est affichée ci-dessous, affichant vrai pour l'axe de catégorie principal et de valeur, et faux pour l'axe de catégorie et de valeur secondaires.

### Code Java pour déterminer quels axes existent dans le graphique

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### Sortie de la console générée par le code d'exemple

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
