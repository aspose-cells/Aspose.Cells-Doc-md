---
title: Нахождение абсолютной позиции формы внутри Листа книги Excel
type: docs
weight: 8000
url: /ru/net/finding-absolute-position-of-shape-inside-the-worksheet/
---

{{% alert color="primary" %}}

Иногда вам нужно знать абсолютное положение формы на листе. Aspose.Cells предоставляет свойства [**Shape.LeftToCorner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lefttocorner) и [**Shape.TopToCorner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/toptocorner) для этой цели. Эти свойства возвращают абсолютное положение формы внутри листа в пикселях.

{{% /alert %}}

Следующий образец кода отображает абсолютное положение первой формы на листе в пикселях. Образец кода отображает следующий вывод в консоли:

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-AbsolutePositionOfShapeInsideWorksheet-1.cs" >}}
