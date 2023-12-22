---
title: Найдите и обновите вложенные или дочерние сводные таблицы родительской сводной таблицы.
type: docs
weight: 60
url: /ru/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Как найти и обновить вложенные или дочерние сводные таблицы родительской сводной таблицы с номерами Aspose.Cells for Python via .NET.
keywords: Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table.
---
##  **Возможные сценарии использования**

Иногда одна сводная таблица использует другую сводную таблицу в качестве источника данных, поэтому ее называют дочерней сводной таблицей или вложенной сводной таблицей. Вы можете найти дочерние сводные таблицы родительской сводной таблицы, используя команду[**Сводная таблица.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)метод.

##  **Найдите и обновите вложенные или дочерние сводные таблицы родительской сводной таблицы.**

 Следующий пример кода загружает[образец файла Excel](61767747.xlsx) который содержит три сводные таблицы. Две нижние сводные таблицы являются дочерними элементами приведенной выше сводной таблицы, как показано на этом снимке экрана. Код находит дочернюю сводную таблицу, используя метод[**Сводная таблица.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)метод, а затем обновляет их один за другим.

![задача: image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

##  **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}
