---
title: Поиск и обновление вложенных или дочерних сводных таблиц родительской сводной таблицы с Golang через C++
linktitle: Найти и обновить вложенные или дочерние сводные таблицы
type: docs
weight: 60
url: /ru/go-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Научитесь находить и обновлять вложенные или дочерние сводные таблицы родительской сводной таблицы с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Иногда одна сводная таблица использует другую сводную таблицу в качестве источника данных, поэтому ее называют дочерней сводной таблицей или вложенной сводной таблицей. Вы можете найти дочерние сводные таблицы родительской сводной таблицы, используя метод [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/go-cpp/pivottable/getchildren/).

## **Найти и обновить вложенные или дочерние сводные таблицы родительской сводной таблицы**

В следующем примере кода загружается [образец файла Excel](61767747.xlsx), который содержит три сводные таблицы. Нижние две сводные таблицы являются детьми вышеприведенной сводной таблицы, как показано на этом скриншоте. Код находит дочернюю сводную таблицу с помощью метода [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/go-cpp/pivottable/getchildren/), а затем поочередно обновляет их.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindAndRefreshTheNestedOrChildrenPivotTablesOfParentPivotTable.go" >}}
