---
title: Удалять ведущие пустые строки и столбцы при экспорте таблиц в формат CSV с помощью Golang через C++
linktitle: Обрезать ведущие пустые строки и столбцы
type: docs
weight: 100
url: /ru/go-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Узнайте, как обрезать ведущие пустые строки и столбцы при экспорте таблиц в CSV с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Иногда ваш файл Excel или CSV содержит ведущие пустые столбцы или строки. Например, рассмотрим следующую строку:

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Здесь первые три ячейки или столбца пусты. Когда вы открываете такой файл CSV в Microsoft Excel, то Microsoft Excel отбрасывает эти ведущие пустые строки и столбцы.

По умолчанию Aspose.Cells не отбрасывает ведущие пустые столбцы и строки при сохранении, но если вы хотите удалить их также, как это делает Microsoft Excel, то Aspose.Cells предоставляет свойство [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/). Пожалуйста, установите его в **true**, и затем все ведущие пустые строки и столбцы будут отброшены при сохранении.

{{% alert color="primary" %}}

Перед выпуском Aspose.Cells for C++ 20.4 значение по умолчанию для [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) было **false**. С выпуском 20.4 значение по умолчанию для [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) — **true**.

{{% /alert %}}

## **Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV**

Приведенный ниже образец кода загружает [исходный файл Excel](sampleTrimBlankColumns.xlsx), в котором есть два ведущих пустых столбца. Сначала он сохраняет файл Excel в формате CSV без изменений, а затем устанавливает свойство [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) в **true** и сохраняет его снова. Снимок экрана показывает [исходный файл Excel](sampleTrimBlankColumns.xlsx), [выходной файл CSV без обрезки](outputWithoutTrimBlankColumns.csv) и выходной файл CSV с обрезкой(outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCsvFormat.go" >}}
