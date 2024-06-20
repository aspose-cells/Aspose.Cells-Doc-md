---
title: Trouver la position absolue de la forme dans la feuille de calcul
type: docs
weight: 7000
url: /fr/java/finding-absolute-position-of-shape-inside-the-worksheet/
description: Apprenez à trouver la position absolue de la forme à l intérieur de la feuille de calcul grâce aux API Aspose.Cells for Java.
keywords: Comment trouver la position absolue d une forme en Java, obtenir la position absolue d une forme en utilisant Java, obtenir la position absolue d une forme à l intérieur de la feuille de calcul via Java, mesurer la position absolue d une forme avec Java.
---

{{% alert color="primary" %}}

Parfois, vous avez besoin de connaître la position absolue d'une forme sur une feuille de calcul. Aspose.Cells fournit les propriétés [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) et [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) à cet effet. Ces propriétés renvoient la position absolue d'une forme dans une feuille de calcul en pixels.

{{% /alert %}}

## **Explication des propriétés Shape.getLeftToCorner() et Shape.getTopToCorner()**

Cette capture d'écran explique quelles distances mesurent les propriétés [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) et [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner).

**Comment mesurer la position absolue**

![todo:image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

Le code d'exemple suivant affiche la position absolue de la première forme dans une feuille de calcul en pixels. Le code affiche la sortie suivante dans la console :

{{< highlight java >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
