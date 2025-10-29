---
title: Сохранять разделители для пустых строк при экспорте таблиц в формат CSV с помощью Golang через C++
linktitle: Сохранять разделители для пустых строк при экспорте таблиц в формат CSV
type: docs
weight: 160
url: /ru/go-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Узнайте, как сохранять разделители для пустых строк при экспорте таблиц в формат CSV с помощью Aspose.Cells и Golang через C++.
---

## **Сохранять разделители для пустых строк при экспорте таблиц в формат CSV**

Aspose.Cells позволяет сохранять разделители строк при преобразовании таблиц в CSV. Для этого используйте свойство [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) класса [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/). [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) — булево свойство. Чтобы сохранять разделители для пустых строк при преобразовании файла Excel в CSV, установите свойство [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) в **true**.

Следующий пример загружает [исходный файл Excel](84378743.xlsx). Он устанавливает свойство [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) в **true** и сохраняет файл как [output.csv](84378744.csv). Скриншот показывает сравнение исходного файла Excel, стандартного вывода при преобразовании в CSV и итогового результата, созданного при установке [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) в **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-KeepSeparatorsForBlankRowsWhileExportingSpreadsheetsToCsvFormat.go" >}}
