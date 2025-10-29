---
title: Работа с форматами отображения данных DataField в сводной таблице с помощью Golang через C++
linktitle: Работа с форматами отображения данных поля данных в сводной таблице
type: docs
weight: 140
url: /ru/go-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Узнайте, как работать с форматами отображения данных поля данных в сводной таблице с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает все форматы отображения данных DataField.

{{% /alert %}}

## **Опция отображения "Ранг по возрастанию" и "Ранг по убыванию"**

Aspose.Cells предоставляет возможность установить опцию формата отображения для полей сводной таблицы. Для этого API предоставляет свойство [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/). Для ранжирования от большего к меньшему установите свойство [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/) в [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/). Ниже приведен пример кода установки опций формата отображения.

Образцы и выходные файлы можно загрузить отсюда для тестирования образца кода:

[Исходный файл Excel](101089332.xlsx)

[Файл Excel с результатом](101089333.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithDataDisplayFormatsOfDatafieldInPivotTable.go" >}}
