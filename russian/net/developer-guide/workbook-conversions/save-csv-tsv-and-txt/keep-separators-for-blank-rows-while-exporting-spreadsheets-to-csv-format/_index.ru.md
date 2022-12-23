---
title: Сохраняйте разделители для пустых строк при экспорте электронных таблиц в формат CSV
type: docs
weight: 160
url: /ru/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---
## **Сохраняйте разделители для пустых строк при экспорте электронных таблиц в формат CSV**

Aspose.Cells позволяет сохранять разделители строк при преобразовании электронных таблиц в формат CSV. Для этого Вы можете использовать**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)**собственностью**[TxtSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions)**учебный класс.**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)**является логическим свойством. Чтобы сохранить разделители для пустых строк при преобразовании файла Excel в CSV, установите**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)**собственность на**истинный**.

Следующий пример кода загружает[исходный файл Excel](84378743.xlsx). Он устанавливает**[TxtSaveOptions.KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)**собственность на**истинный** и сохраняет его как[вывод.csv](84378744.csv) . На снимке экрана показано сравнение между исходным файлом Excel, выводом по умолчанию, сгенерированным при преобразовании электронной таблицы в CSV, и выводом, сгенерированным при настройке**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)** к**истинный**.

![дело:изображение_альтернативный_текст](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-KeepSeparatorsForBlankRow-1.cs" >}}
