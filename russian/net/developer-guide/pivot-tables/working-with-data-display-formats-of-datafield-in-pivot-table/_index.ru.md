---
title: Работа с форматами отображения данных DataField в сводной таблице
type: docs
weight: 140
url: /ru/net/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает все форматы отображения данных DataField.

{{% /alert %}}

## **Опция отображения форматов "Ранжировать от меньшего к большему" и "Ранжировать от большего к меньшему"**

ASpose.Cells предоставляет возможность устанавливать опцию формата отображения для сводных полей. Для этого API предоставляет свойство [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/properties/datadisplayformat). Чтобы выполнить ранжирование от наибольшего к наименьшему, вы можете установить свойство [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/properties/datadisplayformat) в [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfielddatadisplayformat). Нижеприведенный фрагмент кода демонстрирует установку опций формата отображения.

Образцы и выходные файлы можно загрузить отсюда для тестирования образца кода:

[Исходный файл Excel](101089332.xlsx)

[Файл Excel с результатом](101089333.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTables-PivotTableDataDisplayFormatRanking-1.cs" >}}
