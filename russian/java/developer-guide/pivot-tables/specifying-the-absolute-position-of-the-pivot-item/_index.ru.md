---
title: Указание абсолютного положения сводного элемента
type: docs
weight: 40
url: /ru/java/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

Иногда пользователю необходимо указать абсолютную позицию элементов сводки, Aspose.Cells API предоставляет несколько новых свойств и метод для выполнения этого требования пользователя.

-  Добавлен[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) свойство, которое можно использовать для указания индекса позиции во всех PivotItems независимо от родительского узла. Добавлен[**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) свойство, которое можно использовать для указания индекса позиции в PivotItems под тем же родительским узлом.
-  Добавлен[**PivotItem.move (целое число, логическое значение isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)для перемещения элемента вверх или вниз в зависимости от значения счетчика, где счетчик — это количество позиций для перемещения PivotItem вверх или вниз. Если значение счетчика меньше нуля, элемент будет перемещен вверх, а если значение счетчика больше нуля, PivotItem переместится вниз, параметр логического типа isSameParent, указывающий, должна ли операция перемещения выполняться в том же родительском узле или нет.
-  Устарело*PivotItem.move(целое число)* метод, поэтому предлагается использовать вновь добавленный метод[**PivotItem.move (целое число, логическое значение isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) вместо.

 Обратите внимание, необходимо позвонить[**сводная таблица.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) а также[**сводная таблица.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData() ) методы перед использованием[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) свойства и[**PivotItem.move (целое число, логическое значение isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) метод.

{{% /alert %}}

## Образец кода

Следующий пример кода создает сводную таблицу, а затем указывает позиции сводных элементов в том же родительском узле.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
