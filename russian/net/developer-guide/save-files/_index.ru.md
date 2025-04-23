---
title: Различные способы сохранения файлов
linktitle: Сохранить файлы
type: docs
weight: 40
url: /ru/net/different-ways-to-save-files/
description: Aspose.Cells for .NET может сохранять файлы в различных форматах. Сохранить файлы в PDF. Сохранить файлы в HTML. Сохранить файлы в DOCX. Сохранить файлы в PPTX. Сохранить файлы в JSON. Сохранить файлы в MHTML.
keywords: Aspose.Cells Сохранить Excel в PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML и так далее с использованием C#, Сохранить или Преобразовать Рабочую книгу в PDF HTML JSON TXT SQL в C#.
---

{{% alert color="primary" %}}

Aspose.Cells делает возможным создание и сохранение файлов. В этой статье объясняются различные способы сохранения файлов.

{{% /alert %}}

## **Различные способы сохранения файлов**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel и обеспечивает необходимые свойства и методы для работы с файлами Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) предоставляет метод [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index), используемый для сохранения файлов Excel. Метод [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) имеет множество перегрузок, которые используются для сохранения файлов различными способами.

Формат файла, в который файл сохраняется, определяется перечислением [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)

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

Для сохранения файлов в хранилище необходимо указать имя файла (с полным путем к хранилищу) и желаемый формат файла (из перечисления [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)) при вызове метода [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) объекта [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **Как сохранить книгу в Pdf**
Формат портативного документа (PDF) - это тип документа, созданный Adobe еще в 1990 годах. Цель этого формата файла заключалась во введении стандарта для представления документов и других справочных материалов в формате, независимом от прикладного программного обеспечения, аппаратного обеспечения и операционной системы. Формат файла PDF обладает полной способностью содержать информацию, такую как текст, изображения, гиперссылки, форм-поля, мультимедийные элементы, цифровые подписи, вложения, метаданные, геопространственные объекты и 3D-объекты, которые могут стать частью исходного документа.

Следующие коды показывают, как сохранить книгу в формате PDF с помощью Aspose.Cells:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **Как сохранить книгу в формате текста или CSV**

Иногда вам может потребоваться конвертировать или сохранить книгу с несколькими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.) как Microsoft Excel, так и Aspose.Cells по умолчанию сохраняют только содержимое активного листа.

В следующем примере кода объясняется, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может быть любым файлом электронных таблиц Microsoft Excel или OpenOffice (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством листов.

При выполнении кода он преобразует данные всех листов рабочей книги в формат TXT

Вы можете изменить тот же пример, чтобы сохранить файл в формате CSV. По умолчанию, [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator) — запятая, поэтому не указывайте разделитель при сохранении в формате CSV. Обратите внимание: если вы используете тестовую версию и даже если свойство [**TxtSaveOptions.ExportAllSheets**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/exportallsheets/) установлено в true, программа все равно экспортирует только один лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Как сохранить файл в текстовые файлы с пользовательским разделителем**

Текстовые файлы содержат данные электронных таблиц без форматирования. Файл представляет собой своего рода обычный текстовый файл, который может содержать некоторые настраиваемые разделители между его данными.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **Как сохранить файл в поток**

Для сохранения файлов в поток создайте объект *MemoryStream* или *FileStream* и сохраните файл в этот объект потока, вызвав метод [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) объекта объекта [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index). Укажите желаемый формат файла, используя перечисление [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) при вызове метода [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **Как сохранить файл Excel в файлы Html и Mht**
Aspose.Cells просто может сохранить файл Excel, JSON, CSV или другие файлы, которые могут быть загружены Aspose.Cells, в файлы .html и .mht.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}


## **Как сохранить файл Excel в форматы OpenOffice (ODS, SXC, FODS, OTS)**
Мы можем сохранить файлы в формате OpenOffice: ODS, SXC, FODS, OTS и т. д.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **Как сохранить файл Excel в формат JSON или XML**

JSON (JavaScript Object Notation) – это открытый стандартный файловый формат для обмена данными, который использует удобочитаемый текст для хранения и передачи данных. JSON-файлы сохраняются с расширением .json. JSON требует меньше форматирования и является хорошей альтернативой XML. JSON происходит из JavaScript, но является независимым от языка форматом данных. Создание и разбор JSON поддерживается многими современными языками программирования. application/json – это тип медиа-формат, используемый для JSON.

Aspose.Cells поддерживает сохранение файлов в форматах JSON или XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **Продвинутые темы**
- [Настройка уровня сжатия книги Excel](/cells/ru/net/adjust-workbook-compression-level/)
- [Сохранить книгу в формате Strict Open XML Spreadsheet](/cells/ru/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Сохранение файла в объект ответа](/cells/ru/net/saving-file-to-response-object/)
{{< app/cells/assistant language="csharp" >}}
