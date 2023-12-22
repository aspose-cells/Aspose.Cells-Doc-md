---
title: Trouver la position absolue de la forme dans la feuille de calcul
type: docs
weight: 7000
url: /fr/java/finding-absolute-position-of-shape-inside-the-worksheet/
description: Découvrez comment trouver la position absolue d'une forme dans la feuille de calcul via les API Aspose.Cells for Java.
keywords: How to Find Absolute Position of Shape in Java, Get Absolute Position of Shape using Java, Obtain Absolute Position of Shape inside the Worksheet via Java, Measure absolute position of Shape with Java.
---
{{% alert color="primary" %}}

 Parfois, vous avez besoin de connaître la position absolue d'une forme sur une feuille de calcul. Aspose.Cells fournit le[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) et[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) propriétés à cet effet. Ces propriétés renvoient la position absolue d'une forme dans une feuille de calcul en pixels.

{{% /alert %}}

##  **Explication des propriétés Shape.getLeftToCorner() et Shape.getTopToCorner()**

 Cette capture d'écran explique les distances[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) et[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)mesure des propriétés.

**Comment mesurer la position absolue**

![tâche : image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

L'exemple de code suivant affiche la position absolue de la première forme dans une feuille de calcul en pixels. Le code affiche le résultat suivant dans la console :

{{< highlight "java" >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
