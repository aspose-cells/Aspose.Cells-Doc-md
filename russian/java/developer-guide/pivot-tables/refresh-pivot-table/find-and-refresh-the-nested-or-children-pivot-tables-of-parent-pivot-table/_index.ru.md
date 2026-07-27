---
title: Найти и обновить вложенные или дочерние сводные таблицы родительской сводной таблицы
type: docs
weight: 50
url: /ru/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **Возможные сценарии использования**

Иногда одна сводная таблица использует другую сводную таблицу в качестве источника данных, поэтому ее называют дочерней сводной таблицей или вложенной сводной таблицей. Вы можете найти дочерние сводные таблицы родительской сводной таблицы, используя метод [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--).

## **Найти и обновить вложенные или дочерние сводные таблицы родительской сводной таблицы**

Следующий образец кода загружает [образец файла Excel](61767766.xlsx), который содержит три сводные таблицы. Нижние две сводные таблицы являются дочерними элементами вышестоящей сводной таблицы, как показано на этом скриншоте. Код находит дочернюю сводную таблицу, используя метод [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--), а затем обновляет их по очереди.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}
{{< app/cells/assistant language="java" >}}
