---
title: Создание динамических графиков
description: Узнайте, как создавать динамические диаграммы в Aspose.Cells for .NET. Наше руководство покажет вам, как динамически обновлять данные диаграммы, серии и форматирование в соответствии с вашими потребностями, позволяя визуально представлять изменяющиеся данные в ваших листах.
keywords: Aspose.Cells for .NET, построение диаграмм, динамические диаграммы, данные, серии, форматирование, листы, обновление.
type: docs
weight: 240
url: /ru/net/create-dynamic-charts/
---

{{% alert color="primary" %}}

Динамические (или интерактивные) диаграммы обладают способностью изменяться при изменении объема данных. Другими словами, динамические диаграммы могут автоматически отражать изменения, когда меняется источник данных. Для вызова изменения источника данных можно использовать опцию фильтрации таблиц Excel или использовать элемент управления, такой как комбо-бокс или раскрывающийся список.

Эта статья демонстрирует использование Aspose.Cells for .NET API для создания динамических диаграмм с применением обоих вышеупомянутых подходов.

{{% /alert %}}

## **Использование таблиц Excel**

{{% alert color="primary" %}}

Таблицы Excel в перспективе Aspose.Cells называются ListObjects, поэтому мы будем использовать термин "ListObject" вместо "Таблица" для ясности. Пожалуйста, подробно ознакомьтесь с тем, как [создать ListObjects](/cells/ru/net/create-and-format-table/) с помощью Aspose.Cells for .NET API.

{{% /alert %}}

ListObjects предоставляет встроенную функциональность для сортировки и фильтрации данных после взаимодействия пользователя. Обе опции сортировки и фильтрации предоставляются через раскрывающиеся списки, которые автоматически добавляются в строку заголовка [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject). Благодаря этим функциям (сортировка и фильтрация) [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) кажется идеальным кандидатом для службы источника данных динамической диаграммы, потому что при изменении сортировки или фильтрации отображение данных на диаграмме будет изменено в соответствии с текущим состоянием [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

Чтобы сделать демонстрацию более понятной, мы создадим [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) с нуля и будем пошагово продвигаться вперед в соответствии с указанным ниже.

1. Создать пустой [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Получите доступ к [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) первого [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) в [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Вставить некоторые данные в ячейки.
1. Создайте [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) на основе вставленных данных.
1. Создайте [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) на основе диапазона данных [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Сохраните результат на диске.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

## **Использование динамических формул**

В случае, если вы не хотите использовать [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) в качестве источника данных для динамической диаграммы, другой вариант - использовать функции Excel (или формулы) для создания динамического диапазона данных и элемента управления (например, списка-комбобокс) для вызова изменения данных. В этом сценарии мы будем использовать функцию VLOOKUP для извлечения соответствующих значений на основе выбора списка-комбобокса. При изменении выбора функция VLOOKUP обновит значение ячейки. Если диапазон ячеек использует функцию VLOOKUP, весь диапазон может быть обновлен при взаимодействии пользователя, поэтому его можно использовать в качестве источника для динамической диаграммы.

Чтобы сделать демонстрацию понятной, мы создадим рабочую книгу с нуля и будем двигаться шаг за шагом, как описано ниже.

1. Создать пустой [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Получите доступ к [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) первого [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) в [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Вставьте данные в ячейки, создав именованный диапазон. Эти данные будут служить серией для динамической диаграммы.
1. Создайте [**ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) на основе созданного в предыдущем шаге именованного диапазона.
1. Вставьте еще данные в ячейки, которые будут служить источником для функции VLOOKUP.
1. Вставьте функцию VLOOKUP (соответствующими параметрами) в диапазон ячеек. Этот диапазон будет служить источником для динамической диаграммы.
1. Создайте [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) на основе созданного в предыдущем шаге диапазона.
1. Сохраните результат на диске.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
{{< app/cells/assistant language="csharp" >}}
