---
title: Сохранять разделители для пустых строк при экспорте таблиц в формат CSV
type: docs
weight: 110
url: /ru/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **Сохранять разделители для пустых строк при экспорте таблиц в формат CSV**

Aspose.Cells предоставляет возможность сохранять разделители строк при преобразовании электронных таблиц в формат CSV. Для этого можно использовать свойство [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) класса [**TxtSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TxtSaveOptions). [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) - это логическое свойство. Чтобы сохранить разделители для пустых строк при преобразовании файла Excel в CSV, установите свойство [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) в **true**.

Приведенный ниже образец кода загружает [исходный файл Excel](KeepSeparatorsForBlankRow.xlsx). Он устанавливает свойство [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) в **true** и сохраняет его в [KeepSeparatorsForBlankRow.out.csv](KeepSeparatorsForBlankRow.out.csv). На скриншоте показано сравнение между исходным файлом Excel, стандартным выводом, сгенерированным при преобразовании электронной таблицы в CSV, и выводом, сгенерированным при установке [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) в **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-KeepSeparatorsForBlankRow-1.java" >}}
