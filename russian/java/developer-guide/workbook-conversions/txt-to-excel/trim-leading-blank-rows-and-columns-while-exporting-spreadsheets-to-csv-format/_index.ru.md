---
title: Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV
type: docs
weight: 50
url: /ru/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
---

## **Возможные сценарии использования**

Иногда ваш файл Excel или CSV имеет ведущие пустые столбцы или строки. Например, рассмотрим эту строку

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Здесь первые три ячейки или столбца пусты. Когда вы открываете такой файл CSV в Microsoft Excel, то Microsoft Excel отбрасывает эти ведущие пустые строки и столбцы.

По умолчанию Aspose.Cells не отбрасывает ведущие пустые столбцы и строки при сохранении, но если вы хотите удалить их также, как это делает Microsoft Excel, то Aspose.Cells предоставляет свойство [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn). Пожалуйста, установите его в **true**, и затем все ведущие пустые строки и столбцы будут отброшены при сохранении.

{{% alert color="primary" %}}

До выпуска Aspose.Cells for Java 20.4 значение по умолчанию для [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) было **false**. Начиная с релиза 20.4, значение по умолчанию для [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) — **true.**

{{% /alert %}}

## **Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV**

Приведенный ниже примерный код загружает исходный файл Excel, в котором есть два ведущих пустых столбца. Сначала он сохраняет файл Excel в формате CSV без каких-либо изменений, а затем устанавливает свойство [**TxtSaveOptions.TrimLeadingBlankRowAndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#TrimLeadingBlankRowAndColumn) в **true** и сохраняет его снова. На скриншоте показаны [исходный файл Excel](sampleTrimBlankColumns.xlsx), [выходной файл CSV без обрезки](outputWithoutTrimBlankColumns.csv), и [выходной файл CSV с обрезкой](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVFormat-TrimBlankRowsAndColsWhileExportingSpreadsheetsToCSVForm.Java" >}}
{{< app/cells/assistant language="java" >}}
