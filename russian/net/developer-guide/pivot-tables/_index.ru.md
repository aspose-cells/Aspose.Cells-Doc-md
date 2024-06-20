---
title: Вставка сводной таблицы
linktitle: Сводные таблицы
type: docs
weight: 160
url: /ru/net/create-pivot-table/
description: Создание и форматирование сводных таблиц файла электронной таблицы Excel.
---

## **Создать сводную таблицу**

Возможно использовать Aspose.Cells для добавления сводных таблиц в электронные таблицы программно.

### **Модель объекта сводной таблицы**

Aspose.Cells предоставляет специальный набор классов в пространстве имен [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot), которые используются для создания и управления сводными таблицами. Эти классы используются для создания и установки объектов [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable), строительных блоков сводной таблицы. Объекты представляют собой:

- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) представляет поле в [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) представляет собой коллекцию всех объектов [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) в [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) представляет собой сводную таблицу на листе.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) представляет собой коллекцию всех объектов [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) на листе.

### **Создание простой сводной таблицы с использованием Aspose.Cells**

1. Добавьте данные на лист с использованием метода [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) объекта [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).
   Эти данные будут использоваться в качестве источника данных сводной таблицы.
1. Добавьте сводную таблицу на лист, вызвав метод [**add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) коллекции [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection), который инкапсулирован в объекте Лист.
1. Получите доступ к новому объекту [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) из коллекции [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection), передав индекс сводной таблицы.
1. Используйте любые из объектов [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) (описанных выше), чтобы управлять сводной таблицей.

После выполнения примера кода сводная таблица добавляется на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

При назначении диапазона ячеек в качестве источника данных диапазон должен проходить сверху вниз. Например, "A1:C3" допустим, но "C3:A1" - нет.

{{% /alert %}}

## **Продвинутые темы**
- [Функция консолидации](/cells/ru/net/consolidation-function/)
- [Пользовательская сортировка в сводной таблице](/cells/ru/net/custom-sorting-in-pivot-table/)
- [Настройка глобализации для сводной таблицы](/cells/ru/net/customize-globalization-settings-for-pivot-table/)
- [Отключение лент сводной таблицы](/cells/ru/net/disable-pivot-table-ribbons/)
- [Найти и обновить вложенные или дочерние сводные таблицы родительской сводной таблицы](/cells/ru/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Форматирование сводной таблицы](/cells/ru/net/formatting-pivot-table/)
- [Получить внешний источник подключения сводной таблицы](/cells/ru/net/get-external-connection-data-source-of-pivot-table/)
- [Получить дату обновления и информацию об обновлении сводной таблицы](/cells/ru/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Группировка полей сводной таблицы](/cells/ru/net/group-pivot-fields-in-the-pivot-table/)
- [Анализ кэшированных записей сводной таблицы при загрузке файла Excel](/cells/ru/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Сводная таблица и исходные данные](/cells/ru/net/pivot-table-and-source-data/)
- [Скрытие и сортировка данных в сводной таблице](/cells/ru/net/pivot-table-hide-and-sort-data/)
- [Обновление и вычисление сводной таблицы с вычисляемыми элементами](/cells/ru/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Сохранение сводной таблицы в файле ODS](/cells/ru/net/save-pivot-table-in-ods-file/)
- [Опция отображения страниц фильтров отчета](/cells/ru/net/show-report-filter-pages-option/)
- [Работа с форматами отображения данных DataField в сводной таблице](/cells/ru/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
