---
title: Поиск и обновление вложенных или дочерних сводных таблиц родительской сводной таблицы
type: docs
weight: 50
url: /ru/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---
## **Возможные сценарии использования**

Иногда одна сводная таблица использует другую сводную таблицу в качестве источника данных, поэтому она называется дочерней сводной таблицей или вложенной сводной таблицей. Вы можете найти дочерние сводные таблицы родительской сводной таблицы, используя[**Сводная таблица.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren()) метод.

## **Поиск и обновление вложенных или дочерних сводных таблиц родительской сводной таблицы**

Следующий пример кода загружает[образец файла Excel](61767766.xlsx)который содержит три сводные таблицы. Две нижние сводные таблицы являются дочерними элементами приведенной выше сводной таблицы, как показано на этом снимке экрана. Код находит дочернюю сводную таблицу, используя[**Сводная таблица.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren()), а затем обновляет их один за другим.

![дело:изображение_альтернативный_текст](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}
