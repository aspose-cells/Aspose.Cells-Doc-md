---
title: Encontrar la posición absoluta de la forma dentro de la hoja de cálculo
type: docs
weight: 7000
url: /es/java/finding-absolute-position-of-shape-inside-the-worksheet/
description: Aprenda a encontrar la posición absoluta de una forma dentro de la hoja de cálculo a través de las API Aspose.Cells for Java.
keywords: Cómo encontrar la posición absoluta de una forma en Java, obtener la posición absoluta de una forma usando Java, obtener la posición absoluta de una forma dentro de la hoja de cálculo via Java, medir la posición absoluta de una forma con Java.
---

{{% alert color="primary" %}}

A veces, es necesario conocer la posición absoluta de una forma en una hoja de cálculo. Aspose.Cells proporciona las propiedades [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) y [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) para este propósito. Estas propiedades devuelven la posición absoluta de una forma en una hoja de cálculo en píxeles.

{{% /alert %}}

## **Explicación de las propiedades Shape.getLeftToCorner() y Shape.getTopToCorner()**

Esta captura de pantalla explica qué distancias miden las propiedades [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) y [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner).

**Cómo medir la posición absoluta**

![todo:image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

El siguiente código de ejemplo muestra la posición absoluta de la primera forma en una hoja de cálculo en píxeles. El código muestra la siguiente salida en la consola:

{{< highlight java >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
