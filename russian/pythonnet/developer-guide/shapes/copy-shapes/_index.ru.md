---
title: Копирование форм между листами
linktitle: Копирование форм
type: docs
weight: 200
url: /ru/python-net/copy-shapes-between-worksheets/
description: В этой статье показано, как копировать фигуры между листами с помощью API Aspose.Cells для Python via .NET.
keywords: Библиотека для Excel на Python, Копирование Форм между Рабочими Листами на Python, как скопировать изображение с одного листа на другой на Python, как скопировать график с одного листа на другой на Python, как копировать управляемые элементы и другие объекты рисования с одного листа на другой на Python.
---

{{% alert color="primary" %}}

Иногда необходимо копировать элементы на листе, например изображения, графики и другие объекты рисунка, между рабочими листами. Aspose.Cells для Python via .NET поддерживает эту функцию. Графики, изображения и другие объекты могут быть скопированы с высоким уровнем точности.

В данной статье вы получите подробное понимание того, как копировать формы между рабочими листами.

{{% /alert %}}

## **Копирование изображения с одного листа в другой**

Чтобы скопировать изображение с одного рабочего листа на другой, используйте метод [**Worksheet.pictures.add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add/#int-int-io.RawIOBase-int-int), как показано в приведенном ниже образце кода.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.py" >}}

## **Копирование диаграммы из одного листа в другой**

Следующий код демонстрирует использование метода [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) для копирования диаграммы с одного листа на другой.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.py" >}}

## **Копирование элементов управления и других объектов рисования с одного листа на другой**

Чтобы скопировать элементы управления и другие объекты рисования, используйте метод [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int), как показано в примере ниже.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.py" >}}
