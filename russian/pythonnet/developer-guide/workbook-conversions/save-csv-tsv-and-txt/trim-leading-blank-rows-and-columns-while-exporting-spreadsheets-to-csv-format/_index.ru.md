---
title: Обрезайте начальные пустые строки и столбцы при экспорте электронных таблиц в формат CSV.
type: docs
weight: 100
url: /ru/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Обрежьте начальные пустые строки и столбцы при экспорте электронных таблиц в формат CSV, используя Aspose.Cells for Python via .NET API.
keywords: Python Trim Leading Blank Rows and Columns while exporting spreadsheets to CSV format, Trim Leading Blank Rows and Columns while saving excel to CSV format in Python via NET, Python Trim Leading Blank Rows and Columns exporting excel to CSV format.
---
##  **Возможные сценарии использования**

Иногда в вашем файле Excel или CSV есть пустые столбцы или строки. Например, рассмотрим эту строку

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

Здесь первые три ячейки или столбца пусты. Когда вы открываете такой файл CSV в Microsoft Excel, Excel Microsoft отбрасывает эти начальные пустые строки и столбцы.

 По умолчанию Aspose.Cells for Python via .NET не отбрасывает начальные пустые столбцы и строки при сохранении, но если вы хотите удалить их так же, как это делает Microsoft Excel, тогда Aspose.Cells for Python via .NET предоставляет**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** свойство. Пожалуйста, установите его на**истинный**и тогда все ведущие пустые строки и столбцы будут отброшены при сохранении.

{{% alert color="primary" %}}

 До выпуска Aspose.Cells for Python via .NET 20.4 значение по умолчанию**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)**был**ЛОЖЬ**. Начиная с версии 20.4, значение по умолчанию **[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** является**истинный.**

{{% /alert %}}

##  **Обрезайте начальные пустые строки и столбцы при экспорте электронных таблиц в формат CSV.**

 Следующий пример кода загружает[исходный файл Excel](sampleTrimBlankColumns.xlsx) который имеет два ведущих пустых столбца. Сначала он сохраняет файл Excel в формате CSV без каких-либо изменений, а затем устанавливает**[TxtSaveOptions.trim_leading_blank_row_and_column](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/trim_leading_blank_row_and_column/)** собственность**истинный** и сохраняет его снова. На скриншоте показано[исходный файл Excel](sampleTrimBlankColumns.xlsx), [вывести файл CSV без обрезки](outputWithoutTrimBlankColumns.csv)и[вывод CSV файл с обрезкой](outputTrimBlankColumns.csv).

![задача: image_alt_text](result.png)

##  **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-TrimLeadingBlankRowsAndColumns.py" >}}
