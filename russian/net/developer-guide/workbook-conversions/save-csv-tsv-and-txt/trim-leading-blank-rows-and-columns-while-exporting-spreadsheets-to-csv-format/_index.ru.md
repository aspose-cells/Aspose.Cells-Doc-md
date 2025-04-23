---
title: Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV
type: docs
weight: 100
url: /ru/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **Возможные сценарии использования**

Иногда ваш файл Excel или CSV имеет ведущие пустые столбцы или строки. Например, рассмотрим эту строку

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Здесь первые три ячейки или столбца пусты. Когда вы открываете такой файл CSV в Microsoft Excel, то Microsoft Excel отбрасывает эти ведущие пустые строки и столбцы.

По умолчанию Aspose.Cells не отбрасывает ведущие пустые столбцы и строки при сохранении, но если вы хотите удалить их также, как это делает Microsoft Excel, то Aspose.Cells предоставляет свойство [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn). Пожалуйста, установите его в **true**, и затем все ведущие пустые строки и столбцы будут отброшены при сохранении.

{{% alert color="primary" %}}

До выпуска Aspose.Cells for .NET 20.4, значение по умолчанию для [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) было **false**. С момента выпуска 20.4 значение по умолчанию для [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) теперь **true**.

{{% /alert %}}

## **Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV**

Приведенный ниже образец кода загружает [исходный файл Excel](sampleTrimBlankColumns.xlsx), в котором есть два ведущих пустых столбца. Сначала он сохраняет файл Excel в формате CSV без изменений, а затем устанавливает свойство [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/trimleadingblankrowandcolumn) в **true** и сохраняет его снова. Снимок экрана показывает [исходный файл Excel](sampleTrimBlankColumns.xlsx), [выходной файл CSV без обрезки](outputWithoutTrimBlankColumns.csv) и выходной файл CSV с обрезкой(outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat.cs" >}}
{{< app/cells/assistant language="csharp" >}}
