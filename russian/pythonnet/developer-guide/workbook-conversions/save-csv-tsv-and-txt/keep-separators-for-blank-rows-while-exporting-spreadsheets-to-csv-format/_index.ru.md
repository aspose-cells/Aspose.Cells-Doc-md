---
title: Сохранять разделители для пустых строк при экспорте таблиц в формат CSV
type: docs
weight: 160
url: /ru/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Сохранение разделителей для пустых строк при экспорте таблиц в формат CSV с использованием Aspose.Cells для Python via .NET API.
keywords: Python Сохранение разделителей для пустых строк при экспорте таблиц в формат CSV, Сохранение разделителей для пустых строк при сохранении эксель в формат CSV в Python via NET, Python Сохранение разделителей для пустых строк при экспорте Excel в формат CSV.
---

## **Сохранять разделители для пустых строк при экспорте таблиц в формат CSV**

Aspose.Cells для Python via .NET позволяет сохранять разделители строк при преобразовании электронных таблиц в формат CSV. Для этого можно использовать свойство [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) класса [**TxtSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/). [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) является логическим свойством. Чтобы сохранить разделители для пустых строк при преобразовании файла Excel в CSV, установите свойство [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) в **true**.

Приведенный ниже образец кода загружает [исходный файл Excel](84378743.xlsx). Устанавливает свойство [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) в **true** и сохраняет его в [output.csv](84378744.csv). Снимок экрана показывает сравнение между исходным файлом Excel, выходным файлом, сгенерированным по умолчанию при преобразовании электронной таблицы в CSV и выходным файлом, сгенерированным при установке [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) в **true**.

![todo:image_alt_text](result.jpg)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-KeepSeparatorsForBlankRow-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
