---
title: Найти и обновить вложенные или дочерние сводные таблицы родительской сводной таблицы
type: docs
weight: 60
url: /ru/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Как найти и обновить вложенные или дочерние сводные таблицы родительской сводной таблицы с помощью Aspose.Cells для Python via .NET.
keywords: Aspose.Cells для Python Excel, библиотека Excel Python, Найти и обновить вложенные или дочерние сводные таблицы родительской сводной таблицы с использованием Aspose.Cells для библиотеки Excel Python.
---

## **Возможные сценарии использования**

Иногда одна сводная таблица использует другую сводную таблицу в качестве источника данных, поэтому ее называют дочерней сводной таблицей или вложенной сводной таблицей. Вы можете найти дочерние сводные таблицы родительской сводной таблицы, используя метод [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#).

## **Как найти и обновить вложенные или дочерние сводные таблицы родительской сводной таблицы**

В следующем примере кода загружается [образец файла Excel](61767747.xlsx), который содержит три сводные таблицы. Нижние две сводные таблицы являются детьми вышеприведенной сводной таблицы, как показано на этом скриншоте. Код находит дочернюю сводную таблицу с помощью метода [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#), а затем поочередно обновляет их.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}
