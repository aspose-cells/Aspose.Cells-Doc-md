---
title: Формат сводной таблицы Cells
type: docs
weight: 20
url: /ru/python-java/format-pivot-table-cells/
---
{{% alert color="primary" %}}

 Иногда вам нужно отформатировать ячейки сводной таблицы. Например, вы хотите применить цвет фона к ячейкам сводной таблицы. Aspose.Cells предоставляет два метода[**Сводная таблица.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style) ) а также[**Сводная таблица.формат()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)), который вы можете использовать для этой цели.

[**Сводная таблица.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style) ) применяет стиль ко всей сводной таблице, а[**Сводная таблица.формат()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) применяет стиль к одной ячейке сводной таблицы.

{{% /alert %}}

Следующий пример кода форматирует всю сводную таблицу светло-голубым цветом, а затем форматирует вторую строку таблицы желтым цветом.

**Входная сводная таблица перед выполнением кода**

![дело:изображение_альтернативный_текст](format-pivot-table-cells_1.png)

**Выходная сводная таблица после выполнения кода**

![дело:изображение_альтернативный_текст](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
