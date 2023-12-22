---
title: Создание динамических диаграмм
description: Узнайте, как создавать динамические диаграммы по телефону Aspose.Cells for .NET. Наше руководство покажет вам, как динамически обновлять данные, ряды и форматирование диаграмм в соответствии с вашими требованиями, что позволяет визуально представлять изменяющиеся данные на ваших листах.
keywords: Aspose.Cells for .NET, charting, dynamic charts, data, series, formatting, worksheets, updating.
type: docs
weight: 240
url: /ru/net/create-dynamic-charts/
---
{{% alert color="primary" %}}

Динамические (или интерактивные) диаграммы могут меняться при изменении объема данных. Другими словами, динамические диаграммы могут автоматически отражать изменения при изменении источника данных. Чтобы инициировать изменение источника данных, можно использовать опцию фильтрации таблиц Excel или использовать такой элемент управления, как ComboBox или раскрывающийся список.

В этой статье показано использование API-интерфейсов Aspose.Cells for .NET для создания динамических диаграмм с использованием обоих вышеупомянутых подходов.

{{% /alert %}}

##  **Использование таблиц Excel**

{{% alert color="primary" %}}

 Таблицы Excel в перспективе Aspose.Cells называются ListObjects, поэтому для ясности мы будем использовать термин «ListObject» вместо «Table». Пожалуйста, прочитайте подробно о том, как[создать объекты списка](/cells/ru/net/create-and-format-table/)с Aspose.Cells for .NET API.

{{% /alert %}}

 ListObjects предоставляет встроенные функции для сортировки и фильтрации данных при взаимодействии с пользователем. Параметры сортировки и фильтрации предоставляются через раскрывающиеся списки, которые автоматически добавляются в строку заголовка[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) . Благодаря этим функциям (сортировка и фильтрация)[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) кажется идеальным кандидатом на роль источника данных для динамической диаграммы, поскольку при изменении сортировки или фильтрации представление данных на диаграмме будет изменено, чтобы отразить текущее состояние диаграммы.[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).

 Чтобы демонстрация была простой для понимания, мы создадим[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)с нуля и двигаться вперед шаг за шагом, как описано ниже.

1.  Создайте пустой[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Доступ к[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) из первых[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) в[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Вставьте некоторые данные в ячейки.
1.  Создавать[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)на основе вставленных данных.
1.  Создавать[**Диаграмма**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) на основе диапазона данных[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject).
1. Сохраните результат на диск.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreateDynamicCharts-CreateDynamicCharts.cs" >}}

##  **Использование динамических формул**

В случае, если вы не желаете использовать[**СписокОбъект**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)В качестве источника данных для динамической диаграммы другой вариант — использовать функции Excel (или формулы) для создания динамического диапазона данных и элемент управления (например, ComboBox) для запуска изменения данных. В этом сценарии мы будем использовать функцию ВПР для получения соответствующих значений на основе выбора ComboBox. При изменении выбора функция ВПР обновит значение ячейки. Если диапазон ячеек использует функцию ВПР, весь диапазон может быть обновлен при взаимодействии с пользователем, поэтому его можно использовать в качестве источника для динамической диаграммы.

Чтобы демонстрация была простой для понимания, мы создадим рабочую тетрадь с нуля и будем двигаться вперед шаг за шагом, как описано ниже.

1.  Создайте пустой[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1.  Доступ к[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) из первых[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) в[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Вставьте некоторые данные в ячейки, создав именованный диапазон. Эти данные будут служить в качестве серии для динамической диаграммы.
1.  Создавать[**Поле со списком**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox)на основе именованного диапазона, созданного на предыдущем шаге.
1. Вставьте в ячейки еще несколько данных, которые будут служить источником для функции ВПР.
1. Вставьте функцию ВПР (с соответствующими параметрами) в диапазон ячеек. Этот диапазон будет служить источником для динамической диаграммы.
1.  Создавать[**Диаграмма**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)на основе диапазона, созданного на предыдущем шаге.
1. Сохраните результат на диск.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-UsingDynamicFormula-CreateDynamicChartsUsingDynamicFormula.cs" >}}
