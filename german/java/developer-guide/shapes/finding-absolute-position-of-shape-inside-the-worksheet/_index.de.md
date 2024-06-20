---
title: Ermittlung der absoluten Position einer Form innerhalb des Arbeitsblatts
type: docs
weight: 7000
url: /de/java/finding-absolute-position-of-shape-inside-the-worksheet/
description: Erfahren Sie, wie Sie die absolute Position einer Form im Arbeitsblatt über die Aspose.Cells for Java APIs ermitteln.
keywords: So ermitteln Sie die absolute Position einer Form in Java, erhalten Sie die absolute Position einer Form mit Java, ermitteln Sie die absolute Position einer Form im Arbeitsblatt via Java, Messen Sie die absolute Position einer Form mit Java.
---

{{% alert color="primary" %}}

Manchmal müssen Sie die absolute Position einer Form auf einem Arbeitsblatt kennen. Aspose.Cells bietet dazu die Eigenschaften [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) und [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner). Diese Eigenschaften geben die absolute Position einer Form in einem Arbeitsblatt in Pixel zurück.

{{% /alert %}}

## **Erklärung der Eigenschaften Shape.getLeftToCorner() und Shape.getTopToCorner()**

Dieser Screenshot erklärt, welche Entfernungen die Eigenschaften [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) und [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) messen.

**Wie man die absolute Position misst**

![todo:image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

Der folgende Beispielcode zeigt die absolute Position der ersten Form in einem Arbeitsblatt in Pixel. Der Code zeigt die folgende Ausgabe in der Konsole:

{{< highlight java >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
