---
title: Вставить сводную таблицу
linktitle: Сводные таблицы
type: docs
weight: 160
url: /ru/net/create-pivot-table/
description: Создание и форматирование сводных таблиц файлов электронных таблиц Excel.
---
## **Создать сводную таблицу**

Можно использовать Aspose.Cells для программного добавления сводных таблиц в электронные таблицы.

### **Объектная модель сводной таблицы**

Aspose.Cells предоставляет специальный набор классов в[**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) пространства имен, которые используются для создания сводных таблиц и управления ими. Эти классы используются для создания и установки[**сводная таблица**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)объекты, строительные блоки сводной таблицы. Объекты:

- [**сводное поле**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) представляет собой поле в[**сводная таблица**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) представляет собой совокупность всех[**сводное поле**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) объекты в[**сводная таблица**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**сводная таблица**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)представляет сводную таблицу на листе.
- [**сводная таблицаколлекция**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) представляет собой совокупность всех[**сводная таблица**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)объекты на рабочем листе.

### **Создание простой сводной таблицы с использованием Aspose.Cells**

1. Добавьте данные на лист с помощью[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) объекты[**путвалуе**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) метод.
 Эти данные будут использоваться в качестве источника данных сводной таблицы.
1.  Добавьте сводную таблицу на рабочий лист, вызвав метод[**сводные таблицы**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) коллекция[**Добавлять**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index)метод, который инкапсулирован в объект Worksheet.
1.  Доступ к новым[**сводная таблица**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) объект из[**сводные таблицы**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)коллекции путем передачи индекса сводной таблицы.
1.  Используйте любой из[**сводная таблица**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)объекты (описанные выше) для управления сводной таблицей.

После выполнения примера кода на рабочий лист добавляется сводная таблица.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

При назначении диапазона ячеек в качестве источника данных диапазон должен идти от левого верхнего угла к правому нижнему. Например, «A1:C3» допустимо, а «C3:A1» — нет.

{{% /alert %}}

## **Предварительные темы**
- [Функция консолидации](/cells/ru/net/consolidation-function/)
- [Пользовательская сортировка в сводной таблице](/cells/ru/net/custom-sorting-in-pivot-table/)
- [Настройка параметров глобализации для сводной таблицы](/cells/ru/net/customize-globalization-settings-for-pivot-table/)
- [Отключить ленты сводной таблицы](/cells/ru/net/disable-pivot-table-ribbons/)
- [Поиск и обновление вложенных или дочерних сводных таблиц родительской сводной таблицы](/cells/ru/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Форматирование сводной таблицы](/cells/ru/net/formatting-pivot-table/)
- [Получить источник данных внешнего подключения сводной таблицы](/cells/ru/net/get-external-connection-data-source-of-pivot-table/)
- [Получить дату обновления сводной таблицы и обновить информацию о том, кто](/cells/ru/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Группировать сводные поля в сводной таблице](/cells/ru/net/group-pivot-fields-in-the-pivot-table/)
- [Анализ сводных кэшированных записей при загрузке файла Excel](/cells/ru/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Сводная таблица и исходные данные](/cells/ru/net/pivot-table-and-source-data/)
- [Скрытие сводной таблицы и сортировка данных](/cells/ru/net/pivot-table-hide-and-sort-data/)
- [Обновить и рассчитать сводную таблицу с вычисляемыми элементами](/cells/ru/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Сохранить сводную таблицу в файле ODS](/cells/ru/net/save-pivot-table-in-ods-file/)
- [Параметр «Показать страницы фильтра отчета»](/cells/ru/net/show-report-filter-pages-option/)
- [Работа с форматами отображения данных DataField в сводной таблице](/cells/ru/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
