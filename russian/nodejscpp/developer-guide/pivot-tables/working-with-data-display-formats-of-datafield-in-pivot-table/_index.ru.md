---
title: Работа с форматами отображения данных DataField в сводной таблице
type: docs
weight: 140
url: /ru/nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ поддерживает все форматы отображения данных DataField.

{{% /alert %}}

## **Опция отображения форматов "Ранжировать от меньшего к большему" и "Ранжировать от большего к меньшему"**

ASpose.Cells предоставляет возможность устанавливать опцию формата отображения для сводных полей. Для этого API предоставляет свойство [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-). Чтобы выполнить ранжирование от наибольшего к наименьшему, вы можете установить свойство [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-) в [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/nodejs-cpp/pivotfielddatadisplayformat/). Нижеприведенный фрагмент кода демонстрирует установку опций формата отображения.

Образцы и выходные файлы можно загрузить отсюда для тестирования образца кода:

[Исходный файл Excel](101089332.xlsx)

[Файл Excel с результатом](101089333.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTableDataDisplayFormatRanking-1.js" >}}

