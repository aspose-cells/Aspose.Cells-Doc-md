---
title: Вставить сводную таблицу
linktitle: Сводные таблицы
type: docs
weight: 160
url: /ru/python-net/create-pivot-table/
description: Создайте и отформатируйте сводную таблицу с помощью Aspose.Cells for Python via .NET.
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
---
##  **Создать сводную таблицу**

Можно использовать Aspose.Cells for Python via .NET для программного добавления сводных таблиц в электронные таблицы.

###  **Объектная модель сводной таблицы**

 Aspose.Cells for Python via .NET предоставляет специальный набор классов в[**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) пространство имен, которые используются для создания сводных таблиц и управления ими. Эти классы используются для создания и установки[**Сводная таблица**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)объекты, строительные блоки сводной таблицы. Объекты:

- [**Сводное поле**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) представляет поле в[**Сводная таблица**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) представляет собой совокупность всех[**Сводное поле**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) объекты в[**Сводная таблица**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**Сводная таблица**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)представляет сводную таблицу на листе.
- [**Коллекция сводной таблицы**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) представляет собой совокупность всех[**Сводная таблица**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)объекты на рабочем листе.

###  **Создание простой сводной таблицы с использованием Aspose.Cells**

1.  Добавьте данные на лист с помощью[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) объекты[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) метод.
 Эти данные будут использоваться в качестве источника данных сводной таблицы.
1.  Добавьте сводную таблицу на лист, вызвав метод[**Сводные таблицы**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) коллекция[**добавлять**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str)метод, который инкапсулирован в объект Worksheet.
1.  Доступ к новому[**Сводная таблица**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) объект из[**Сводные таблицы**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)коллекцию, передав индекс сводной таблицы.
1.  Используйте любой из[**Сводная таблица**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)объекты (описанные выше) для управления сводной таблицей.

После выполнения примера кода на лист добавляется сводная таблица.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}

При назначении диапазона ячеек в качестве источника данных диапазон должен идти сверху слева направо вниз. Например, «A1:C3» допустимо, а «C3:A1» — нет.

{{% /alert %}}

##  **Предварительные темы**
- [Функция консолидации](/cells/ru/python-net/consolidation-function/)
- [Пользовательская сортировка в сводной таблице](/cells/ru/python-net/custom-sorting-in-pivot-table/)
- [Настройка параметров глобализации для сводной таблицы](/cells/ru/python-net/customize-globalization-settings-for-pivot-table/)
- [Отключить ленты сводной таблицы](/cells/ru/python-net/disable-pivot-table-ribbons/)
- [Найдите и обновите вложенные или дочерние сводные таблицы родительской сводной таблицы.](/cells/ru/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Форматирование сводной таблицы](/cells/ru/python-net/formatting-pivot-table/)
- [Получить источник данных внешнего соединения сводной таблицы](/cells/ru/python-net/get-external-connection-data-source-of-pivot-table/)
- [Получить дату обновления сводной таблицы и обновить информацию о том, кто](/cells/ru/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Группировка сводных полей в сводной таблице](/cells/ru/python-net/group-pivot-fields-in-the-pivot-table/)
- [Анализ сводных кэшированных записей при загрузке файла Excel](/cells/ru/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Сводная таблица и исходные данные](/cells/ru/python-net/pivot-table-and-source-data/)
- [Сводная таблица: скрытие и сортировка данных](/cells/ru/python-net/pivot-table-hide-and-sort-data/)
- [Обновить и вычислить сводную таблицу с вычисляемыми элементами](/cells/ru/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Сохранить сводную таблицу в файле ODS.](/cells/ru/python-net/save-pivot-table-in-ods-file/)
- [Опция «Показать страницы фильтра отчета»](/cells/ru/python-net/show-report-filter-pages-option/)
- [Работа с форматами отображения данных DataField в сводной таблице](/cells/ru/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
