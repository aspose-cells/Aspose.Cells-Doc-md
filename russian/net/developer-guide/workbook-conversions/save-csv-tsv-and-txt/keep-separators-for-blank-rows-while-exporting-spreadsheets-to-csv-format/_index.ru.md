---
title: Сохранять разделители для пустых строк при экспорте таблиц в формат CSV
type: docs
weight: 160
url: /ru/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **Сохранять разделители для пустых строк при экспорте таблиц в формат CSV**

Aspose.Cells предоставляет возможность сохранять разделители строк при преобразовании электронных таблиц в формат CSV. Для этого можно использовать свойство [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) класса [**TxtSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions). [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) - это логическое свойство. Чтобы сохранить разделители для пустых строк при преобразовании файла Excel в CSV, установите свойство [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) в **true**.

Приведенный ниже образец кода загружает [исходный файл Excel](84378743.xlsx). Устанавливает свойство [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) в **true** и сохраняет его в [output.csv](84378744.csv). Снимок экрана показывает сравнение между исходным файлом Excel, выходным файлом, сгенерированным по умолчанию при преобразовании электронной таблицы в CSV и выходным файлом, сгенерированным при установке [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) в **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-KeepSeparatorsForBlankRow-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
