---
title: Копирование форм между листами
linktitle: Копирование форм
type: docs
weight: 200
url: /ru/net/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

Иногда вам может понадобиться скопировать элементы на рабочем листе, например, изображения, диаграммы и другие объекты рисования, между рабочими листами. Aspose.Cells поддерживает эту функцию. Диаграммы, изображения и другие объекты могут быть скопированы с высочайшей точностью.

В данной статье вы получите подробное понимание того, как копировать формы между рабочими листами.

{{% /alert %}}

## **Копирование изображения с одного листа в другой**

Чтобы скопировать изображение с одного рабочего листа на другой, используйте метод [**Worksheet.Pictures.Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index), как показано в приведенном ниже образце кода.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.cs" >}}

## **Копирование диаграммы из одного листа в другой**

Следующий код демонстрирует использование метода [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) для копирования диаграммы с одного листа на другой.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.cs" >}}

## **Копирование элементов управления и других объектов рисования с одного листа на другой**

Чтобы скопировать элементы управления и другие объекты рисования, используйте метод [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy), как показано в примере ниже.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.cs" >}}
{{< app/cells/assistant language="csharp" >}}
