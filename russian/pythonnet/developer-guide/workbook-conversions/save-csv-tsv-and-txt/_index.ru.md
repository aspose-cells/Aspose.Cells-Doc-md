---
title: Преобразование Excel в CSV,TSV и Txt
linktitle: Сохранить как CSV,TSV и Txt.
type: docs
weight: 40
url: /ru/python-net/convert-excel-to-csv-tsv-and-txt/
description: Преобразуйте Excel в CSV,TSV и Txt, используя Aspose.Cells for Python via .NET API.
keywords: Python Convert Excel to CSV,TSV and Txt, Convert Excel to CSV,TSV and Txt in Python via NET, Python Convert Workbook to CSV,TSV and Txt.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET позволяет конвертировать файлы Excel, ods, json и других форматов в CSV, TSV и TXT.

{{% /alert %}}

##  **Сохранение книги в текстовом формате или формате CSV**

Иногда вам нужно преобразовать или сохранить книгу с несколькими листами в текстовый формат. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.) по умолчанию Microsoft Excel и Aspose.Cells for Python via .NET сохраняют только содержимое активного листа.

В следующем примере кода объясняется, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может представлять собой любой файл электронной таблицы Excel или OpenOffice Microsoft (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством листов.

При выполнении кода он преобразует данные всех листов книги в формат TXT.

 Вы можете изменить тот же пример, чтобы сохранить файл по адресу CSV. По умолчанию:**[TxtSaveOptions.separator](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/)**является запятой, поэтому не указывайте разделитель при сохранении в формате CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

##  **Сохранение текстовых файлов с помощью специального разделителя**

Текстовые файлы содержат данные электронных таблиц без форматирования. Файл представляет собой своего рода обычный текстовый файл, который может иметь некоторые настраиваемые разделители между данными.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


##  **Предварительные темы**
- [Сохраняйте разделители для пустых строк при экспорте электронных таблиц в формат CSV.](/cells/ru/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Обрезайте начальные пустые строки и столбцы при экспорте электронных таблиц в формат CSV.](/cells/ru/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
