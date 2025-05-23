---
title: Найти и обновить вложенные или дочерние сводные таблицы родительской сводной таблицы
type: docs
weight: 60
url: /ru/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **Возможные сценарии использования**

Иногда одна сводная таблица использует другую сводную таблицу в качестве источника данных, поэтому ее называют дочерней сводной таблицей или вложенной сводной таблицей. Вы можете найти дочерние сводные таблицы родительской сводной таблицы, используя метод [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren).

## **Найти и обновить вложенные или дочерние сводные таблицы родительской сводной таблицы**

В следующем примере кода загружается [образец файла Excel](61767747.xlsx), который содержит три сводные таблицы. Нижние две сводные таблицы являются детьми вышеприведенной сводной таблицы, как показано на этом скриншоте. Код находит дочернюю сводную таблицу с помощью метода [**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren), а затем поочередно обновляет их.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.cs" >}}
{{< app/cells/assistant language="csharp" >}}
