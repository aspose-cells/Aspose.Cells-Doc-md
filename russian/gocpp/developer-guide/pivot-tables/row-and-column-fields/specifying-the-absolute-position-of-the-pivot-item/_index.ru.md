---
title: Определение абсолютной позиции элемента свода с помощью Golang через C++
linktitle: Указание абсолютного положения элемента сводной таблицы
type: docs
weight: 50
url: /ru/go-cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Узнайте, как указать абсолютную позицию элементов сводной таблицы в C++ с помощью Aspose.Cells.
---

{{% alert color="primary" %}}

Иногда пользователи должны указывать абсолютную позицию элементов сводной таблицы. API Aspose.Cells ввело несколько новых свойств и метод для реализации этого требования.

- Добавлено свойство [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/), которое можно использовать для указания индекса позиции во всех PivotItems независимо от родительского узла. Добавлено свойство [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/), которое можно использовать для указания индекса позиции в PivotItems под тем же родительским узлом.
- Добавлен метод [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/) для перемещения элемента вверх или вниз на основе значения счетчика, где счетчик — это число позиций для перемещения PivotItem вверх или вниз. Если значение счетчика меньше нуля, элемент перемещается вверх, а если больше нуля — вниз. Параметр типа Boolean `isSameParent` указывает, нужно ли выполнять операцию в рамках одного и того же родительского узла.
- Устарел метод `PivotItem.Move(int count)`; рекомендуется использовать недавно добавленный метод [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/).

{{% /alert %}}

Следующий пример кода создает сводную таблицу и указывает позиции элементов сводной таблицы в одном родительском узле. Вы можете скачать исходный Excel-файл [source Excel](5112632.xlsx) и итоговый файл [output Excel](5112619.xlsx) для ознакомления. Открыв итоговый файл, вы увидите, что элемент "4H12" занимает 0-ю позицию в родительском элементе "K11", а "DIF400" — 3-ю позицию. Аналогично CA32 находится на позиции 1, а AAA3 — на позиции 2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingTheAbsolutePositionOfThePivotItem.go" >}}
{{% alert color="primary" %}}

Обратите внимание, что перед использованием свойств [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/), [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) и метода [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) необходимо вызвать методы `PivotTable.RefreshData` и `PivotTable.CalculateData`.

{{% /alert %}}
