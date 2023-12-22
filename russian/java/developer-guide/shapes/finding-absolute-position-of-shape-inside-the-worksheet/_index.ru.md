---
title: Поиск абсолютного положения фигуры внутри листа
type: docs
weight: 7000
url: /ru/java/finding-absolute-position-of-shape-inside-the-worksheet/
description: Узнайте, как найти абсолютное положение фигуры внутри листа с помощью API Aspose.Cells for Java.
keywords: How to Find Absolute Position of Shape in Java, Get Absolute Position of Shape using Java, Obtain Absolute Position of Shape inside the Worksheet via Java, Measure absolute position of Shape with Java.
---
{{% alert color="primary" %}}

 Иногда вам нужно знать абсолютное положение фигуры на листе. Aspose.Cells обеспечивает[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) и[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) свойства для этой цели. Эти свойства возвращают абсолютное положение фигуры на листе в пикселях.

{{% /alert %}}

##  **Объяснение свойств Shape.getLeftToCorner() и Shape.getTopToCorner()**

 Этот скриншот объясняет, на каких расстояниях[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) и[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)мера свойств.

**Как измерить абсолютное положение**

![задача: image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

В следующем примере кода отображается абсолютное положение первой фигуры на листе в пикселях. Код отображает следующий вывод в консоли:

{{< highlight "java" >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
