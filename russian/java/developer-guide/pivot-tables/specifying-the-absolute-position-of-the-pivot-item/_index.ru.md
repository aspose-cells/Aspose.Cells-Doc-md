---
title: Указание абсолютной позиции элемента сводной таблицы
type: docs
weight: 40
url: /ru/java/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Иногда пользователю необходимо указать абсолютную позицию элементов сводной таблицы. В интерфейсе API Aspose.Cells предоставлено несколько новых свойств и метод для удовлетворения этого требования пользователя.

- Добавлено свойство [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), которое можно использовать для указания индекса позиции во всех PivotItems независимо от родительского узла. Добавлено свойство [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode), которое можно использовать для указания индекса позиции в PivotItems под тем же родительским узлом.
- Добавлен метод [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) для перемещения элемента вверх или вниз на основе значения счетчика, где счетчик - количество позиций для перемещения элемента вверх или вниз. Если значение счетчика меньше нуля, элемент будет перемещен вверх, а если значение счетчика больше нуля, PivotItem будет перемещен вниз, параметр типа Boolean isSameParent, который указывает, должна ли операция перемещения выполняться в том же родительском узле или нет.
- Устарел метод *PivotItem.move(int count)*, поэтому рекомендуется использовать вновь добавленный метод [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)).

Пожалуйста, обратите внимание, перед использованием методов [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) и свойств [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) и метода [**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--), необходимо вызвать методы [**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--).

{{% /alert %}}

## Образец кода

В следующем образце кода создается сводная таблица, а затем указываются позиции элементов сводной таблицы в том же родительском узле.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
