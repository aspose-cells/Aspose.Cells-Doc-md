---
title: Преобразование Excel в CSV, TSV и Txt
linktitle: Сохранить как CSV, TSV и Txt
type: docs
weight: 40
url: /ru/net/convert-excel-to-csv-tsv-and-txt/
---
{{% alert color="primary" %}}

Aspose.Cells позволяет конвертировать файлы excel, ods, json и других форматов в CSV, TSV и TXT.

{{% /alert %}}

## **Сохранение книги в текстовом формате или формате CSV**

Иногда вы хотите преобразовать или сохранить книгу с несколькими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.) по умолчанию как Microsoft Excel, так и Aspose.Cells сохраняют содержимое только активного рабочего листа.

В следующем примере кода показано, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может быть любым файлом электронной таблицы Microsoft Excel или OpenOffice (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством рабочих листов.

Когда код выполняется, он преобразует данные всех листов книги в формат TXT.

 Вы можете изменить тот же пример, чтобы сохранить файл в формате CSV. По умолчанию,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**является запятой, поэтому не указывайте разделитель при сохранении в формате CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Сохранение текстовых файлов с пользовательским разделителем**

Текстовые файлы содержат данные электронной таблицы без форматирования. Файл представляет собой обычный текстовый файл, который может иметь некоторые настраиваемые разделители между данными.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}


## **Предварительные темы**
- [Сохраняйте разделители для пустых строк при экспорте электронных таблиц в формат CSV](/cells/ru/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Обрезать начальные пустые строки и столбцы при экспорте электронных таблиц в формат CSV](/cells/ru/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
