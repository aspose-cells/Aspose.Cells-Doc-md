---
title: Обрезать начальные пустые строки и столбцы при экспорте электронных таблиц в формат CSV
type: docs
weight: 50
url: /ru/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---
## **Возможные сценарии использования**

Иногда в вашем файле Excel или CSV есть ведущие пустые столбцы или строки. Например, рассмотрим эту строку

{{< highlight "java" >}}

 ,,,data1,data2

{{< /highlight >}}

Здесь первые три ячейки или столбца пусты. Когда вы открываете такой CSV-файл в Microsoft Excel, Microsoft Excel отбрасывает эти начальные пустые строки и столбцы.

 По умолчанию Aspose.Cells не отбрасывает начальные пустые столбцы и строки при сохранении, но если вы хотите удалить их так же, как Microsoft Excel, тогда Aspose.Cells предоставляет**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)** имущество. Пожалуйста, установите его на**истинный**а затем все ведущие пустые строки и столбцы будут удалены при сохранении.

{{% alert color="primary" %}}

 До выпуска Aspose.Cells for .NET 20.4 значение по умолчанию**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)** был**ЛОЖЬ** . Начиная с версии 20.4 значение по умолчанию**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)** является**истинный.**

{{% /alert %}}

## **Обрезать начальные пустые строки и столбцы при экспорте электронных таблиц в формат CSV**

Следующий пример кода загружает исходный файл Excel с двумя ведущими пустыми столбцами. Сначала он сохраняет файл excel в формате CSV без каких-либо изменений, а затем устанавливает**[TxtSaveOptions.TrimLeadingBlankRowAndColumn](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn)** собственность на**истинный** и снова сохраняет. На скриншоте показано[исходный файл excel](sampleTrimBlankColumns.xlsx), [вывод файла CSV без обрезки](outputWithoutTrimBlankColumns.csv), и[выходной файл CSV с обрезкой](outputTrimBlankColumns.csv).

![дело:изображение_альтернативный_текст](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
