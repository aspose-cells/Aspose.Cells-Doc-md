---
title: Recherche de la position absolue de la forme dans la feuille de calcul
type: docs
weight: 7000
url: /fr/java/finding-absolute-position-of-shape-inside-the-worksheet/
---
{{% alert color="primary" %}}

 Parfois, vous devez connaître la position absolue d'une forme sur une feuille de calcul. Aspose.Cells fournit le[**Forme.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) et[**Forme.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) propriétés à cet effet. Ces propriétés renvoient la position absolue d'une forme dans une feuille de calcul en pixels.

{{% /alert %}}

## **Explication des propriétés Shape.getLeftToCorner() et Shape.getTopToCorner()**

Cette capture d'écran explique à quelles distances[**Forme.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) et[**Forme.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)mesure des propriétés.

**Mesure de la position absolue**

![tâche : image_autre_texte](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

L'exemple de code suivant affiche la position absolue de la première forme dans une feuille de calcul en pixels. Le code affiche le résultat suivant dans la console :

{{< highlight "java" >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
