---
title: Указание абсолютного положения элемента сводной таблицы
type: docs
weight: 50
url: /ru/nodejs-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Иногда пользователю необходимо указать абсолютное положение элементов сводной таблицы, API Aspose.Cells for Node.js via C++ внедрил несколько новых свойств и метод для реализации этой потребности.

- Добавлено свойство [**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-), которое можно использовать для указания индекса позиции во всех PivotItems независимо от родительского узла. Добавлено свойство [**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-), которое можно использовать для указания индекса позиции в PivotItems под тем же родительским узлом.
- Добавлен метод [**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-) для перемещения элемента вверх или вниз на основе значения счетчика, где счетчик - количество позиций для перемещения элемента сводной таблицы вверх или вниз. Если значение счетчика меньше нуля, элемент будет перемещен вверх, а если значение счетчика больше нуля, элемент сводной таблицы переместится вниз, параметр типа Boolean isSameParent указывает на то, должна ли операция перемещения выполняться в одном и том же родительском узле или нет.
- Устарел метод *PivotItem.move(int count)*, поэтому рекомендуется использовать недавно добавленный метод [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-).

{{% /alert %}}

В следующем демонстрационном коде создается сводная таблица, после чего указываются позиции элементов сводной таблицы в том же родительском узле. Вы можете загрузить [исходный файл Excel](5112632.xlsx) и [выходной файл Excel](5112619.xlsx) для вашего справочника. Если вы откроете выходной файл Excel, вы увидите, что элемент сводной таблицы "4H12" находится в 0-й позиции в родителе "K11", а "DIF400" находится на 3-й позиции. Точно так же CA32 находится на позиции 1, а AAA3 на позиции 2.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyAbsolutePositionOfPivotItem.js" >}}

{{% alert color="primary" %}}

Обратите внимание, что необходимо вызвать методы PivotTable.RefreshData и PivotTable.CalculateData перед использованием свойств [**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-), [**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-) и метода [**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-).

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
