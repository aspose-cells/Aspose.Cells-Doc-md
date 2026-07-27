---
title: Работа с форматами отображения данных DataField в сводной таблице
type: docs
weight: 140
url: /ru/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Как работать с форматами отображения данных поля данных в сводной таблице с помощью Aspose.Cells для Python via .NET.
keywords: Aspose.Cells для Python Excel, библиотека Excel Python, Работа с форматами отображения данных поля данных в сводной таблице.
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET поддерживает все форматы отображения данных поля данных.

{{% /alert %}}

## **Как установить опцию отображения формата "Ранжирование от меньшего к большему" и "Ранжирование от большего к меньшему"**

Aspose.Cells для Python via .NET предоставляет возможность установить опцию отображения формата для полей сводных таблиц. Для этого API предоставляет свойство [**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/). Чтобы ранжировать от большего к меньшему, вы можете установить свойство [**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/) в [**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfielddatadisplayformat/). Приведенный ниже фрагмент кода демонстрирует установку опций отображения формата.

Образцы и выходные файлы можно загрузить отсюда для тестирования образца кода:

[Исходный файл Excel](101089332.xlsx)

[Файл Excel с результатом](101089333.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTableDataDisplayFormatRanking-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
