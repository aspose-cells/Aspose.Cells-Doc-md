---
title: Формат сводной таблицы Cells
type: docs
weight: 20
url: /ru/java/format-pivot-table-cells/
---
{{% alert color="primary" %}}

 Иногда вам нужно отформатировать ячейки сводной таблицы. Например, вы хотите применить цвет фона к ячейкам сводной таблицы. Aspose.Cells предоставляет два метода[**Сводная таблица.formatAll()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#formatAll(com.aspose.cells.Style) ) а также[**Сводная таблица.формат()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#format(int,%20int,%20com.aspose.cells.Style)), который вы можете использовать для этой цели.

[**Сводная таблица.formatAll()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#formatAll(com.aspose.cells.Style) ) применяет стиль ко всей сводной таблице, а[**Сводная таблица.формат()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#format(int,%20int,%20com.aspose.cells.Style)) применяет стиль к одной ячейке сводной таблицы.

{{% /alert %}}

Следующий пример кода форматирует всю сводную таблицу светло-голубым цветом, а затем форматирует вторую строку таблицы желтым цветом.

**Входная сводная таблица перед выполнением кода**

![дело:изображение_альтернативный_текст](format-pivot-table-cells_1.png)

**Выходная сводная таблица после выполнения кода**

![дело:изображение_альтернативный_текст](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FormatPivotTableCells-FormatPivotTableCells.java" >}}
