---
title: Redimensionner la forme de l étiquette de données du graphique pour s adapter au texte
type: docs
weight: 190
url: /fr/java/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}

L'application Excel propose l'option **Redimensionner la forme pour ajuster le texte** pour les étiquettes de données du graphique afin d'augmenter la taille de la forme pour que le texte y rentre. Cette option peut être accédée sur l'interface Excel en sélectionnant l'une des étiquettes de données sur le graphique. Faites un clic droit et sélectionnez le menu **Format des étiquettes de données**. Sur l'onglet **Taille et propriétés**, développez **Alignement** pour révéler les propriétés associées, y compris l'option **Redimensionner la forme pour ajuster le texte**.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_1.png)

{{% /alert %}}

## **Redimensionner la forme de l'étiquette de données du graphique pour s'adapter au texte**

Afin de reproduire la fonctionnalité de redimensionnement des formes d'étiquette de données pour qu'elles s'adaptent au texte d'Excel, les API Aspose.Cells ont exposé la propriété de type booléen [**DataLabels.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText). Le morceau de code suivant montre le simple scénario d'utilisation de la propriété [**DataLabels.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText).

Le graphique ressemble comme suit avant d'exécuter le code.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResizeChartDataLabelShapeToFitText-ResizeChartDataLabelShapeToFitText.java" >}}

Le graphique ressemble comme suit après avoir exécuté le code.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_3.png)
{{< app/cells/assistant language="java" >}}
