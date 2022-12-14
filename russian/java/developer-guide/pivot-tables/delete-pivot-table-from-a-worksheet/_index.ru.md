---
title: Удалить сводную таблицу с рабочего листа
type: docs
weight: 50
url: /ru/java/delete-pivot-table-from-a-worksheet/
---
{{% alert color="primary" %}}

 Aspose.Cells предоставляет функцию удаления или удаления сводной таблицы из рабочего листа. Вы можете удалить сводную таблицу, используя объект сводной таблицы или позицию сводной таблицы. Пожалуйста, используйте[**Рабочий лист.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable) ) метод удаления сводной таблицы с помощью объекта сводной таблицы и[**Рабочий лист.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)для удаления объекта сводной таблицы, используя его положение в коллекции сводных таблиц.

{{% /alert %}}

## **Пример**

 Следующий пример кода удаляет две сводные таблицы с листа. Во-первых, он удаляет сводную таблицу, используя[**Рабочий лист.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)), а затем удаляет сводную таблицу, используя[**Рабочий лист.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)) метод

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}
