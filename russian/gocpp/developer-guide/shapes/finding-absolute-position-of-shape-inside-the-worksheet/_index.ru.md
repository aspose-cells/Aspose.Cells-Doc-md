---
title: Поиск абсолютной позиции фигуры внутри листа с помощью Golang через C++
linktitle: Нахождение абсолютной позиции формы внутри Листа книги Excel
type: docs
weight: 8000
url: /ru/go-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Определение абсолютной позиции фигуры в листе с помощью Aspose.Cells на Golang через C++.
---

{{% alert color="primary" %}}

Иногда вам нужно знать абсолютное положение формы на листе. Aspose.Cells предоставляет свойства [**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/go-cpp/shape/getlefttocorner/) и [**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/) для этой цели. Эти свойства возвращают абсолютное положение формы внутри листа в пикселях.

{{% /alert %}}

Следующий образец кода отображает абсолютное положение первой формы на листе в пикселях. Образец кода отображает следующий вывод в консоли:

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindingAbsolutePositionOfShapeInsideTheWorksheet.go" >}}
