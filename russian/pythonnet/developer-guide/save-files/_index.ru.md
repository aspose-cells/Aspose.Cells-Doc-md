---
title: Различные способы сохранения файлов
linktitle: Сохранить файлы
type: docs
weight: 40
url: /ru/python-net/different-ways-to-save-files/
description: Aspose.Cells для Python via .NET может сохранять файлы в различные форматы. Сохранять файлы в PDF. Сохранять файлы в HTML. Сохранять файлы в DOCX. Сохранять файлы в PPTX. Сохранять файлы в JSON. Сохранять файлы в MHTML.
keywords: Aspose.Cells для Python via .NET сохраняет Excel в PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML и другие форматы с помощью C#, сохраняет или конвертирует рабочие книги в PDF, HTML, JSON, TXT, SQL в C#.
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET позволяет создавать и сохранять файлы. Эта статья объясняет различные способы сохранения файлов.

{{% /alert %}}

## **Различные способы сохранения файлов**

Aspose.Cells для Python via .NET предоставляет [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), которая представляет файл Microsoft Excel и содержит свойства и методы, необходимые для работы с файлами Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) предоставляет метод [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat), который используется для сохранения файлов Excel. Метод [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) имеет множество перегрузок, используемых для сохранения файлов различными способами.

Формат файла, в который файл сохраняется, определяется перечислением [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat)

|**Типы форматов файлов**|**Описание**|
| :- | :- |
|CSV|Представляет собой файл CSV|
|Excel97To2003|Представляет файл Excel 97 - 2003|
|Xlsx|Представляет файл Excel 2007 XLSX|
|Xlsm|Представляет файл Excel 2007 XLSM|
|Xltx|Представляет шаблон файла Excel 2007 XLTX|
|Xltm|Представляет макросов Excel 2007 XLTM|
|Xlsb|Представляет двоичный файл Excel 2007 XLSB|
|SpreadsheetML|Представляет файл XML электронной таблицы|
|TSV|Представляет собой файл значений, разделенных табуляцией|
|TabDelimited|Представляет файл текста с табуляцией|
|ODS|Представляет собой файл ODS|
|Html|Представляет файл(ы) HTML|
|MHtml|Представляет файл(ы) MHTML|
|Pdf|Представляет файл PDF|
|XPS|Представляет документ XPS|
|TIFF|Представляет файл формата Tagged Image File Format (TIFF)|

## **Как сохранить файл в разных форматах**

Для сохранения файлов в хранилище необходимо указать имя файла (с полным путем к хранилищу) и желаемый формат файла (из перечисления [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat)) при вызове метода [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) объекта [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SavingFiletoSomeLocation-1.py" >}}

## **Как сохранить книгу в Pdf**
Формат портативного документа (PDF) - это тип документа, созданный Adobe еще в 1990 годах. Цель этого формата файла заключалась во введении стандарта для представления документов и других справочных материалов в формате, независимом от прикладного программного обеспечения, аппаратного обеспечения и операционной системы. Формат файла PDF обладает полной способностью содержать информацию, такую как текст, изображения, гиперссылки, форм-поля, мультимедийные элементы, цифровые подписи, вложения, метаданные, геопространственные объекты и 3D-объекты, которые могут стать частью исходного документа.

Следующий код показывает, как сохранить рабочую книгу как файл PDF с помощью Aspose.Cells для Python via .NET:
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Save-As-Pdf.py" >}}

## **Как сохранить книгу в формате текста или CSV**

Иногда вам может потребоваться преобразовывать или сохранять рабочую книгу с несколькими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.) по умолчанию как Microsoft Excel, так и Aspose.Cells для Python via .NET сохраняют содержимое только активного листа.

В следующем примере кода объясняется, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может быть любым файлом электронных таблиц Microsoft Excel или OpenOffice (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством листов.

При выполнении кода он преобразует данные всех листов рабочей книги в формат TXT

Вы можете изменить тот же пример, чтобы сохранить файл в формате CSV. По умолчанию, [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator) — запятая, поэтому не указывайте разделитель при сохранении в формате CSV. Обратите внимание: если вы используете тестовую версию и даже если свойство [**TxtSaveOptions.export_all_sheets**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/export_all_sheets/) установлено в true, программа все равно экспортирует только один лист.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SaveWorkbookToTextCSVFormat-1.py" >}}

## **Как сохранить файл в текстовые файлы с пользовательским разделителем**

Текстовые файлы содержат данные электронных таблиц без форматирования. Файл представляет собой своего рода обычный текстовый файл, который может содержать некоторые настраиваемые разделители между его данными.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-OpeningTextFilewithCustomSeparator-1.py" >}}


## **Как сохранить файл Excel в файлы Html и Mht**
Aspose.Cells для Python via .NET может просто сохранять файл Excel, JSON, CSV или другие файлы, которые можно загрузить с помощью Aspose.Cells для Python via .NET, как .html и .mht файлы.
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-MHTML.py" >}}


## **Как сохранить файл Excel в форматы OpenOffice (ODS, SXC, FODS, OTS)**
Мы можем сохранить файлы в формате OpenOffice: ODS, SXC, FODS, OTS и т. д.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-ODS.py" >}}

## **Как сохранить файл Excel в формат JSON или XML**

JSON (JavaScript Object Notation) – это открытый стандартный файловый формат для обмена данными, который использует удобочитаемый текст для хранения и передачи данных. JSON-файлы сохраняются с расширением .json. JSON требует меньше форматирования и является хорошей альтернативой XML. JSON происходит из JavaScript, но является независимым от языка форматом данных. Создание и разбор JSON поддерживается многими современными языками программирования. application/json – это тип медиа-формат, используемый для JSON.

Aspose.Cells для Python via .NET поддерживает сохранение файлов в JSON или XML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-JSON.py" >}}


## **Продвинутые темы**
- [Настройка уровня сжатия книги Excel](/cells/ru/python-net/adjust-workbook-compression-level/)
- [Сохранить книгу в формате Strict Open XML Spreadsheet](/cells/ru/python-net/save-workbook-to-strict-open-xml-spreadsheet-format/)

{{< app/cells/assistant language="python-net" >}}
