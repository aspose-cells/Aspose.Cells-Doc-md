---
title: Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV
type: docs
weight: 100
url: /ru/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Удаление ведущих пустых строк и столбцов при экспорте таблиц в формат CSV с помощью Aspose.Cells для Python via .NET API.
keywords: Python Удаление ведущих пустых строк и столбцов при экспорте таблиц в формат CSV, Удаление ведущих пустых строк и столбцов при сохранении эксель в формат CSV в Python via NET, Python Удаление ведущих пустых строк и столбцов при экспорте Excel в формат CSV.
---

## **Возможные сценарии использования**

Иногда ваш файл Excel или CSV имеет ведущие пустые столбцы или строки. Например, рассмотрим эту строку

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Здесь первые три ячейки или столбца пусты. Когда вы открываете такой файл CSV в Microsoft Excel, то Microsoft Excel отбрасывает эти ведущие пустые строки и столбцы.

По умолчанию Aspose.Cells для Python via .NET не удаляет ведущие пустые столбцы и строки при сохранении, но если вы хотите удалить их, как это делает Microsoft Excel, то Aspose.Cells для Python via .NET предоставляет свойство [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/). Пожалуйста, установите его в **true**, и затем все ведущие пустые строки и столбцы будут удалены при сохранении.

{{% alert color="primary" %}}

До выпуска Aspose.Cells для Python via .NET 20.4 значение по умолчанию для [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) было **false**. С момента выпуска 20.4 значение по умолчанию для [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) - **true**.

{{% /alert %}}

## **Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV**

Приведенный ниже образец кода загружает [исходный файл Excel](sampleTrimBlankColumns.xlsx), в котором есть два ведущих пустых столбца. Сначала он сохраняет файл Excel в формате CSV без изменений, а затем устанавливает свойство [**TxtSaveOptions.trim_leading_blank_row_and_column**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/) в **true** и сохраняет его снова. Снимок экрана показывает [исходный файл Excel](sampleTrimBlankColumns.xlsx), [выходной файл CSV без обрезки](outputWithoutTrimBlankColumns.csv) и выходной файл CSV с обрезкой(outputTrimBlankColumns.csv).

![todo:image_alt_text](result.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
