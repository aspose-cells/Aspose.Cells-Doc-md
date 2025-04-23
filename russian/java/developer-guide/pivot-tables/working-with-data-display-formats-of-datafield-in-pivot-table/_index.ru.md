---
title: Работа с форматами отображения данных DataField в сводной таблице
type: docs
weight: 150
url: /ru/java/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает все форматы отображения данных DataField.

{{% /alert %}}

## **Опция отображения форматов "Ранжировать от меньшего к большему" и "Ранжировать от большего к меньшему"**

Aspose.Cells позволяет установить опцию отображения формата для поля сводной таблицы. Для этого API предоставляет свойство [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat). Чтобы отранжировать от большего к меньшему, можно установить свойство [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) в [**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfielddatadisplayformat#RANK-LARGEST-TO-SMALLEST). В следующем фрагменте кода показано установление опций отображения формата.

Образцы и выходные файлы можно загрузить отсюда для тестирования образца кода:

[Исходный файл Excel](PivotTableSample.xlsx)

[Исправленный файл Excel](PivotTableDataDisplayFormatRanking_out.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-PivotTableDataDisplayFormatRanking-1.java" >}}
{{< app/cells/assistant language="java" >}}
