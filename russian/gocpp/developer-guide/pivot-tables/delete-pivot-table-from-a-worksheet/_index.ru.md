---
title: Удаление сводной таблицы с листа с Golang через C++
linktitle: Удалить сводную таблицу
type: docs
weight: 60
url: /ru/go-cpp/delete-pivot-table-from-a-worksheet/
description: Код C++ для удаления сводной таблицы из листов Excel с помощью Aspose.Cells.
keywords: c++ удалить сводную таблицу из рабочего листа, c++ удалить сводную таблицу из Excel, как удалить сводную таблицу с помощью c++, удалить сводную таблицу с помощью c++, удалить сводную таблицу из Excel с помощью c++, c++ удалить сводную таблицу, c++ убрать сводную таблицу, убрать сводную таблицу, удалить сводную таблицу, как удалить сводную таблицу
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет функцию удаления сводной таблицы из листа. Вы можете удалить сводную таблицу, используя объект сводной таблицы или позицию сводной таблицы. Пожалуйста, используйте метод [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/) для удаления сводной таблицы с использованием объекта сводной таблицы, и метод [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) для удаления объекта сводной таблицы, используя его позицию в коллекции сводных таблиц.

{{% /alert %}}

Следующий пример кода удаляет две сводные таблицы из рабочего листа. Сначала он удаляет сводную таблицу с помощью метода [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/), затем — с помощью метода [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeletePivotTableFromAWorksheet.go" >}}
