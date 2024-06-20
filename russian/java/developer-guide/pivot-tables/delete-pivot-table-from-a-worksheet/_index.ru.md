---
title: Удалить сводную таблицу из листа
type: docs
weight: 50
url: /ru/java/delete-pivot-table-from-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет возможность удалить сводную таблицу с рабочего листа. Вы можете удалить сводную таблицу, используя объект сводной таблицы или позицию сводной таблицы. Пожалуйста, используйте метод [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) для удаления сводной таблицы, используя объект сводной таблицы и метод [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)) для удаления объекта сводной таблицы, используя его позицию в коллекции сводных таблиц.

{{% /alert %}}

## **Пример**

Приведенный ниже образец кода удаляет две сводные таблицы с рабочего листа. Сначала он удаляет сводную таблицу, используя метод [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)), а затем удаляет объект сводной таблицы, используя метод [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}
