---
title: Удалить сводную таблицу из листа
type: docs
weight: 60
url: /ru/net/delete-pivot-table-from-a-worksheet/
description: C# код для удаления сводной таблицы из листов Excel
keywords: C# удалить сводную таблицу из листа, c# удалить сводную таблицу из excel, как удалить сводную таблицу с c#, удалить сводную таблицу с c#, удалить сводную таблицу из excel с c#, c# удалить сводную таблицу, c# удалить сводную таблицу, удалить сводную таблицу, удалить сводную таблицу, как удалить сводную таблицу
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет функцию удаления сводной таблицы из листа. Вы можете удалить сводную таблицу, используя объект сводной таблицы или позицию сводной таблицы. Пожалуйста, используйте метод [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) для удаления сводной таблицы с использованием объекта сводной таблицы, и метод [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) для удаления объекта сводной таблицы, используя его позицию в коллекции сводных таблиц.

{{% /alert %}}

В следующем примере кода удаляются две сводные таблицы с листа. Сначала удаляется сводная таблица, используя метод [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove), а затем удаляется сводная таблица, используя метод [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}
