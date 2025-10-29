---
title: Преобразовать Excel в CSV, TSV и Txt
linktitle: Сохранить как CSV, TSV и Txt
type: docs
weight: 40
url: /ru/python-net/convert-excel-to-csv-tsv-and-txt/
description: Преобразовать Excel в CSV, TSV и Txt с помощью API Aspose.Cells для Python via .NET
keywords: Преобразовать Excel в CSV, TSV и Txt с помощью Python, Преобразовать Excel в CSV, TSV и Txt в Python via NET, Преобразовать рабочую книгу Excel в CSV, TSV и Txt с помощью Python
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET позволяет преобразовать файлы формата Excel, ods, json и другие в CSV, TSV и TXT

{{% /alert %}}

## **Сохранение рабочей книги в текстовом или CSV формате**

Иногда вам может потребоваться преобразовывать или сохранять рабочую книгу с несколькими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.) по умолчанию как Microsoft Excel, так и Aspose.Cells для Python via .NET сохраняют содержимое только активного листа.

В следующем примере кода объясняется, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может быть любым файлом электронных таблиц Microsoft Excel или OpenOffice (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством листов.

При выполнении кода он преобразует данные всех листов рабочей книги в формат TXT

Вы можете изменить предыдущий пример, чтобы сохранить файл в формат CSV. По умолчанию [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/) - запятая, поэтому не указывайте разделитель при сохранении в формате CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

## **Сохранение текстовых файлов с пользовательским разделителем**

Текстовые файлы содержат данные электронных таблиц без форматирования. Файл представляет собой своего рода обычный текстовый файл, который может содержать некоторые настраиваемые разделители между его данными.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


## **Продвинутые темы**
- [Сохранять разделители для пустых строк при экспорте таблиц в формат CSV](/cells/ru/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV](/cells/ru/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="python-net" >}}
