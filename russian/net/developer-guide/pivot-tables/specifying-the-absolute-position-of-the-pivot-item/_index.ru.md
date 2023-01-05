---
title: Указание абсолютного положения элемента сводки
type: docs
weight: 50
url: /ru/net/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

Иногда пользователю необходимо указать абсолютную позицию элементов сводки, Aspose.Cells API предоставил несколько новых свойств и метод для выполнения требований пользователя.

-  Добавлен[**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) свойство, которое можно использовать для указания индекса позиции во всех PivotItems независимо от родительского узла. Добавлен[**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) свойство, которое можно использовать для указания индекса позиции в PivotItems под тем же родительским узлом.
-  Добавлен[**PivotItem.Move (целое число, логическое значение isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)для перемещения элемента вверх или вниз в зависимости от значения счетчика, где счетчик — это номер позиции, на которую нужно переместить PivotItem вверх или вниз. Если значение счетчика меньше нуля, элемент будет перемещен вверх, а если значение счетчика больше нуля, PivotItem переместится вниз, логический параметр isSameParent указывает, должна ли операция перемещения выполняться в том же родительском узле. или не.
-  Устарело*PivotItem.Move(целое число)* метод, поэтому предлагается использовать недавно добавленный метод[**PivotItem.Move (целое число, логическое значение isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) вместо.

{{% /alert %}}

 Следующий пример кода создает сводную таблицу, а затем указывает позиции сводных элементов в том же родительском узле. Вы можете скачать[исходный файл Excel](5112632.xlsx) и[вывод Excel](5112619.xlsx) файлы для справки. Если вы откроете выходной файл Excel, вы увидите, что сводной элемент «4H12» находится на 0-й позиции в родительском «K11», а «DIF400» — на 3-й позиции. Точно так же CA32 находится в позиции 1, а AAA3 — в позиции 2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

Обратите внимание, перед использованием необходимо вызвать методы PivotTable.RefreshData и PivotTable.CalculateData.[**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) свойства и[**PivotItem.Move (целое число, логическое значение isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) метод.

{{% /alert %}}
