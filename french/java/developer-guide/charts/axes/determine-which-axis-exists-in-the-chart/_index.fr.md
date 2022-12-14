---
title: Déterminer quel axe existe dans le graphique
type: docs
weight: 130
url: /fr/java/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

Parfois, l'utilisateur a besoin de savoir si un axe particulier existe dans le graphique. Par exemple, il veut savoir si un axe de valeur secondaire existe à l'intérieur du graphique ou non. Certains graphiques comme Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Donut, DonutExploded, etc. n'ont pas d'axe.

 Aspose.Cells fournit[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)) pour déterminer si le graphique a un axe particulier ou non.

{{% /alert %}}

## Déterminer quel axe existe dans le graphique

La capture d'écran suivante montre un graphique qui n'a que la catégorie principale et l'axe des valeurs. Il n'a pas de catégorie secondaire ni d'axe de valeur.

![tâche : image_autre_texte](determine-which-axis-exists-in-the-chart_1.png)

 L'exemple de code suivant illustre l'utilisation de[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)pour déterminer si l'exemple de graphique a une catégorie primaire et secondaire et un axe des valeurs. La sortie de console du code a été montrée ci-dessous qui affiche vrai pour la catégorie primaire et l'axe des valeurs et faux pour la catégorie secondaire et l'axe des valeurs.

### Code Java pour déterminer quel axe existe dans le graphique

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### Sortie de la console générée par l'exemple de code

Voici la sortie de la console de l'exemple de code ci-dessus.

{{< highlight "java" >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
