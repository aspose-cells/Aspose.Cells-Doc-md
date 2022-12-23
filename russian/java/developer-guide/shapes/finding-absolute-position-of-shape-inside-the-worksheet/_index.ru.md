---
title: Нахождение абсолютного положения формы внутри рабочего листа
type: docs
weight: 7000
url: /ru/java/finding-absolute-position-of-shape-inside-the-worksheet/
---
{{% alert color="primary" %}}

 Иногда вам нужно знать абсолютное положение фигуры на листе. Aspose.Cells обеспечивает[**Форма.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) и[**Форма.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) свойств для этой цели. Эти свойства возвращают абсолютное положение фигуры на листе в пикселях.

{{% /alert %}}

## **Объяснение свойств Shape.getLeftToCorner() и Shape.getTopToCorner()**

На этом снимке экрана показано, на каком расстоянии[**Форма.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) и[**Форма.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)мера свойств.

**Измерение абсолютного положения**

![дело:изображение_альтернативный_текст](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

В следующем примере кода отображается абсолютное положение первой фигуры на листе в пикселях. Код отображает следующий вывод в консоли:

{{< highlight "java" >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
