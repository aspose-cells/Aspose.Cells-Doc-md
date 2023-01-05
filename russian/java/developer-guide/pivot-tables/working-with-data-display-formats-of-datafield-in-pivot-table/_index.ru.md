---
title: Работа с форматами отображения данных DataField в сводной таблице
type: docs
weight: 150
url: /ru/java/working-with-data-display-formats-of-datafield-in-pivot-table/
---
{{% alert color="primary" %}}

Aspose.Cells поддерживает все форматы отображения данных DataField.

{{% /alert %}}

## **Параметр формата отображения «Рейтинг от наименьшего к наибольшему» и «Рейтинг от наибольшего к наименьшему».**

Aspose.Cells предоставляет возможность установить параметр формата отображения для сводных полей. Для этого API предоставляет[**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) имущество. Для ранжирования от наибольшего к наименьшему вы можете установить[**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat)собственность на[**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfielddatadisplayformat#RANK_LARGEST_TO_SMALLEST). Следующий фрагмент кода демонстрирует настройку параметров формата отображения.

Образцы исходных и выходных файлов можно загрузить отсюда для тестирования примера кода:

[Исходный файл Excel](PivotTableSample.xlsx)

[Выходной файл Excel](PivotTableDataDisplayFormatRanking_out.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-PivotTableDataDisplayFormatRanking-1.java" >}}
