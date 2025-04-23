---
title: Удалить сводную таблицу из листа
type: docs
weight: 60
url: /ru/nodejs-cpp/delete-pivot-table-from-a-worksheet/
description: Код Aspose.Cells for Node.js via C++ для удаления сводной таблицы из рабочих листов Excel
keywords: Aspose.Cells for Node.js via C++ Excel, библиотека Excel Node.js, удаление сводной таблицы с листа, удаление сводной таблицы из Excel, как удалить сводную таблицу с помощью Aspose.Cells for Node.js via C++, удаление сводной таблицы, удаление сводной таблицы из Excel, удаляет сводную таблицу, Aspose.Cells for Node.js via C++ удаляет сводную таблицу, удалить сводную таблицу, удалить сводную таблицу, как удалить сводную таблицу
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ предоставляет функцию удаления сводной таблицы или ее отключения из рабочего листа. Можно удалить сводную таблицу с помощью объекта сводной таблицы или по ее позиции. Пожалуйста, используйте метод [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) для удаления сводной таблицы через объект сводной таблицы и метод [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-) для удаления объекта сводной таблицы по ее позиции в коллекции сводных таблиц.

{{% /alert %}}

## **Как удалить сводную таблицу из рабочего листа с помощью Aspose.Cells for Node.js via C++**

В следующем примере кода удаляются две сводные таблицы с листа. Сначала удаляется сводная таблица, используя метод [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-), а затем удаляется сводная таблица, используя метод [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.js" >}}
