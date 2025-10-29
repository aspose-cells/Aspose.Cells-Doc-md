---
title: Нахождение абсолютной позиции формы внутри Листа книги Excel
type: docs
weight: 8000
url: /ru/python-net/finding-absolute-position-of-shape-inside-the-worksheet/
description: В данной статье показано, как найти абсолютную позицию фигуры внутри рабочего листа через API Aspose.Cells для Python via .NET.
keywords: Библиотека для Excel на Python, как найти абсолютную позицию фигуры внутри рабочего листа на Python.
---

{{% alert color="primary" %}}

Иногда необходимо определить абсолютную позицию фигуры на листе. Aspose.Cells для Python via .NET предоставляет свойства [**Shape.left_to_corner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/left_to_corner) и [**Shape.top_to_corner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/top_to_corner) для этой цели. Эти свойства возвращают абсолютную позицию фигуры внутри листа в пикселях.

{{% /alert %}}

Следующий образец кода отображает абсолютное положение первой формы на листе в пикселях. Образец кода отображает следующий вывод в консоли:

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-AbsolutePositionOfShapeInsideWorksheet-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
