---
title: Redimensionner la forme de l'étiquette de données du graphique pour l'adapter au texte
type: docs
weight: 190
url: /fr/java/resize-chart-s-data-label-shape-to-fit-text/
---
{{% alert color="primary" %}}

 L'application Excel fournit le**Redimensionner la forme pour l'adapter au texte** option pour les DataLabels du graphique afin d'augmenter la taille de la forme afin que le texte tienne à l'intérieur de celle-ci. Cette option est accessible sur l'interface Excel en sélectionnant l'une des étiquettes de données sur le graphique. Faites un clic droit et sélectionnez**Formater les étiquettes de données** menu. Sur**Taille et propriétés** onglet, développez**Alignement** pour révéler les propriétés associées, y compris les**Redimensionner la forme pour corriger le texte** option.

![tâche : image_autre_texte](resize-chart-s-data-label-shape-to-fit-text_1.png)

{{% /alert %}}

## **Redimensionner la forme de l'étiquette de données du graphique pour l'adapter au texte**

 Afin d'imiter la fonctionnalité d'Excel consistant à redimensionner les formes d'étiquettes de données pour les adapter au texte, les API Aspose.Cells ont exposé le type booléen[**DataLabels.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText)propriété. Le morceau de code suivant montre le scénario d'utilisation simple de[**DataLabels.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText)propriété.

Le graphique se présente comme suit avant d'exécuter le code.

![tâche : image_autre_texte](resize-chart-s-data-label-shape-to-fit-text_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResizeChartDataLabelShapeToFitText-ResizeChartDataLabelShapeToFitText.java" >}}

Le graphique se présente comme suit après l'exécution du code.

![tâche : image_autre_texte](resize-chart-s-data-label-shape-to-fit-text_3.png)
