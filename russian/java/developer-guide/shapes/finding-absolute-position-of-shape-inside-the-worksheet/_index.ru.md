---
title: Нахождение абсолютной позиции формы внутри Листа книги Excel
type: docs
weight: 7000
url: /ru/java/finding-absolute-position-of-shape-inside-the-worksheet/
description: Узнайте, как найти абсолютную позицию формы внутри Листа книги Excel с помощью API Aspose.Cells for Java.
keywords: Как найти абсолютную позицию формы в Java, Получить абсолютную позицию формы с помощью Java, Получить абсолютную позицию формы внутри Листа книги Excel via Java, Измерить абсолютную позицию формы с помощью Java.
---

{{% alert color="primary" %}}

Иногда вам нужно знать абсолютную позицию формы на листе книги Excel. Aspose.Cells предоставляет свойства [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) и [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) для этой цели. Эти свойства возвращают абсолютную позицию формы на листе в пикселях.

{{% /alert %}}

## **Объяснение свойств Shape.getLeftToCorner() и Shape.getTopToCorner()**

Этот скриншот объясняет, какие расстояния измеряют свойства [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) и [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner).

**Как измерить абсолютную позицию**

![todo:image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

В следующем примере кода отображается абсолютная позиция первой формы на листе книги Excel в пикселях. Код отображает следующий вывод в консоли:

{{< highlight java >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
