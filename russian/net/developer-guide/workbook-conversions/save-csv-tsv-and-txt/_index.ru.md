---
title: Преобразовать Excel в CSV, TSV и Txt
linktitle: Сохранить как CSV, TSV и Txt
type: docs
weight: 40
url: /ru/net/convert-excel-to-csv-tsv-and-txt/
---

{{% alert color="primary" %}}

Aspose.Cells позволяет конвертировать файлы в форматах Excel, ods, json и другие в CSV, TSV и TXT.

{{% /alert %}}

## **Сохранение рабочей книги в текстовом или CSV формате**

Иногда вам может потребоваться конвертировать или сохранить книгу с несколькими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.) как Microsoft Excel, так и Aspose.Cells по умолчанию сохраняют только содержимое активного листа.

В следующем примере кода объясняется, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может быть любым файлом электронных таблиц Microsoft Excel или OpenOffice (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством листов.

При выполнении кода он преобразует данные всех листов рабочей книги в формат TXT

Вы можете изменить предыдущий пример, чтобы сохранить файл в формат CSV. По умолчанию [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator) - запятая, поэтому не указывайте разделитель при сохранении в формате CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Сохранение текстовых файлов с пользовательским разделителем**

Текстовые файлы содержат данные электронных таблиц без форматирования. Файл представляет собой своего рода обычный текстовый файл, который может содержать некоторые настраиваемые разделители между его данными.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}


## **Продвинутые темы**
- [Сохранять разделители для пустых строк при экспорте таблиц в формат CSV](/cells/ru/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV](/cells/ru/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="csharp" >}}
