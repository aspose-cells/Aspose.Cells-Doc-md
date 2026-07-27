---
title: Найти и обновить вложенные или дочерние сводные таблицы родительской сводной таблицы
type: docs
weight: 60
url: /ru/nodejs-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Как находить и обновлять вложенные или дочерние сводные таблицы по отношению к родительской с помощью Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells для Node.js Excel, библиотека Excel Node.js, Найти и обновить вложенные или дочерние сводные таблицы родительской сводной таблицы с помощью Aspose.Cells для Node.js Excel Library.
---

## **Возможные сценарии использования**

Иногда одна сводная таблица использует другую сводную таблицу в качестве источника данных, поэтому ее называют дочерней сводной таблицей или вложенной сводной таблицей. Вы можете найти дочерние сводные таблицы родительской сводной таблицы, используя метод [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--).

## **Как найти и обновить вложенные или дочерние сводные таблицы родительской сводной таблицы**

В следующем примере кода загружается [образец файла Excel](61767747.xlsx), который содержит три сводные таблицы. Нижние две сводные таблицы являются детьми вышеприведенной сводной таблицы, как показано на этом скриншоте. Код находит дочернюю сводную таблицу с помощью метода [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--), а затем поочередно обновляет их.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
