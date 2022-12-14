---
title: Сохраняйте разделители для пустых строк при экспорте электронных таблиц в формат CSV
type: docs
weight: 110
url: /ru/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---
## **Сохраняйте разделители для пустых строк при экспорте электронных таблиц в формат CSV**

Aspose.Cells позволяет сохранять разделители строк при преобразовании электронных таблиц в формат CSV. Для этого Вы можете использовать**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**свойство**[TxtSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/TxtSaveOptions)**учебный класс.**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**является логическим свойством. Чтобы сохранить разделители для пустых строк при преобразовании файла Excel в CSV, установите**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**собственность на**истинный**.

Следующий пример кода загружает[исходный файл Excel](KeepSeparatorsForBlankRow.xlsx). Он устанавливает**[TxtSaveOptions.KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**собственность на**истинный** и сохраняет его как[KeepSeparatorsForBlankRow.out.csv](KeepSeparatorsForBlankRow.out.csv). На снимке экрана показано сравнение между исходным файлом Excel, выводом по умолчанию, созданным при преобразовании электронной таблицы в CSV, и выводом, созданным при настройке**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**к**истинный**.

![дело:изображение_альтернативный_текст](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-KeepSeparatorsForBlankRow-1.java" >}}
