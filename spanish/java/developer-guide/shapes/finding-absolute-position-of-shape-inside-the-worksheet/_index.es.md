---
title: Encontrar la posición absoluta de la forma dentro de la hoja de trabajo
type: docs
weight: 7000
url: /es/java/finding-absolute-position-of-shape-inside-the-worksheet/
description: Aprenda a encontrar la posición absoluta de la forma dentro de la hoja de trabajo a través de las API Aspose.Cells for Java.
keywords: How to Find Absolute Position of Shape in Java, Get Absolute Position of Shape using Java, Obtain Absolute Position of Shape inside the Worksheet via Java, Measure absolute position of Shape with Java.
---
{{% alert color="primary" %}}

 A veces, es necesario conocer la posición absoluta de una forma en una hoja de trabajo. Aspose.Cells proporciona la[**Forma.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) y[**Forma.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) propiedades para este fin. Estas propiedades devuelven la posición absoluta de una forma en una hoja de trabajo en píxeles.

{{% /alert %}}

##  **Explicación de las propiedades Shape.getLeftToCorner() y Shape.getTopToCorner()**

 Esta captura de pantalla explica qué distancias[**Forma.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) y[**Forma.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)medida de propiedades.

**Cómo medir la posición absoluta**

![todo:image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

El siguiente código de muestra muestra la posición absoluta de la primera forma en una hoja de trabajo en píxeles. El código muestra el siguiente resultado en la consola:

{{< highlight "java" >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
