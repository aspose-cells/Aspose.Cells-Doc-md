---
title: Указание абсолютного положения элемента сводной таблицы
type: docs
weight: 50
url: /ru/net/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Иногда пользователю необходимо указать абсолютное положение элементов сводной таблицы, для этого API Aspose.Cells предоставляет несколько новых свойств и метод.

- Добавлено свойство [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), которое можно использовать для указания индекса позиции во всех PivotItems независимо от родительского узла. Добавлено свойство [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode), которое можно использовать для указания индекса позиции в PivotItems под тем же родительским узлом.
- Добавлен метод [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) для перемещения элемента вверх или вниз на основе значения счетчика, где счетчик - количество позиций для перемещения элемента сводной таблицы вверх или вниз. Если значение счетчика меньше нуля, элемент будет перемещен вверх, а если значение счетчика больше нуля, элемент сводной таблицы переместится вниз, параметр типа Boolean isSameParent указывает на то, должна ли операция перемещения выполняться в одном и том же родительском узле или нет.
- Устарел метод *PivotItem.Move(int count)*, поэтому рекомендуется использовать вместо него только что добавленный метод [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move).

{{% /alert %}}

В следующем демонстрационном коде создается сводная таблица, после чего указываются позиции элементов сводной таблицы в том же родительском узле. Вы можете загрузить [исходный файл Excel](5112632.xlsx) и [выходной файл Excel](5112619.xlsx) для вашего справочника. Если вы откроете выходной файл Excel, вы увидите, что элемент сводной таблицы "4H12" находится в 0-й позиции в родителе "K11", а "DIF400" находится на 3-й позиции. Точно так же CA32 находится на позиции 1, а AAA3 на позиции 2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

Обратите внимание, что необходимо вызвать методы PivotTable.RefreshData и PivotTable.CalculateData перед использованием свойств [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) и метода [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move).

{{% /alert %}}
