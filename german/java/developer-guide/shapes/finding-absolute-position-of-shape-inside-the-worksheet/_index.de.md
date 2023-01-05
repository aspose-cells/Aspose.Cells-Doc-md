---
title: Finden der absoluten Position der Form innerhalb des Arbeitsblatts
type: docs
weight: 7000
url: /de/java/finding-absolute-position-of-shape-inside-the-worksheet/
---
{{% alert color="primary" %}}

 Manchmal müssen Sie die absolute Position einer Form auf einem Arbeitsblatt kennen. Aspose.Cells bietet die[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) und[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) Eigenschaften für diesen Zweck. Diese Eigenschaften geben die absolute Position einer Form in einem Arbeitsblatt in Pixel zurück.

{{% /alert %}}

## **Erläuterung der Eigenschaften Shape.getLeftToCorner() und Shape.getTopToCorner()**

Dieser Screenshot erklärt, welche Entfernungen die[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) und[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)Eigenschaften messen.

**Absolutposition messen**

![todo: Bild_alt_Text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

Der folgende Beispielcode zeigt die absolute Position der ersten Form in einem Arbeitsblatt in Pixel an. Der Code zeigt die folgende Ausgabe in der Konsole an:

{{< highlight "java" >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
