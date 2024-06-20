---
title: Форматирование ячеек сводной таблицы
type: docs
weight: 20
url: /ru/python-java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

Иногда вы хотите форматировать ячейки сводной таблицы. Например, вы хотите применить цвет фона к ячейкам сводной таблицы. Aspose.Cells предоставляет два метода [**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)) и [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)), которые вы можете использовать для этой цели.

[**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)) применяет стиль ко всей сводной таблице, в то время как [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) применяет стиль к отдельной ячейке сводной таблицы.

{{% /alert %}}

В следующем образце кода форматируется вся сводная таблица с светло-голубым цветом, а затем форматируется вторая строка таблицы желтым цветом.

**Исходная сводная таблица перед выполнением кода**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**Выходная сводная таблица после выполнения кода**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
