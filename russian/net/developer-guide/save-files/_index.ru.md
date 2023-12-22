---
title: Различные способы сохранения файлов
linktitle: Сохранить файлы
type: docs
weight: 40
url: /ru/net/different-ways-to-save-files/
description: Aspose.Cells for .NET умеет сохранять файлы в разные форматы. Сохраните файлы на номер PDF. Сохраните файлы на номер HTML. Сохраните файлы на номер DOCX. Сохраните файлы на номер PPTX. Сохраните файлы на номер JSON. Сохраните файлы на номер MHTML.
keywords: Aspose.Cells Save Excel to PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML and so on using C#, Save or Convert Workbook to PDF HTML JSON TXT SQL in C#.
---
{{% alert color="primary" %}}

Aspose.Cells позволяет создавать и сохранять файлы. В этой статье объясняются различные способы сохранения файлов.

{{% /alert %}}

##  **Различные способы сохранения файлов**

 Aspose.Cells обеспечивает**[Рабочая книга](https://reference.aspose.com/cells/net/aspose.cells/workbook)** который представляет файл Excel Microsoft и предоставляет свойства и методы, необходимые для работы с файлами Excel.**[Рабочая книга](https://reference.aspose.com/cells/net/aspose.cells/workbook)** класс обеспечивает**[Сохранить](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** метод, используемый для сохранения файлов Excel.**[Сохранить](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**Метод имеет множество перегрузок, которые используются для сохранения файлов разными способами.

 Формат файла, в котором сохраняется файл, определяется**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**перечисление

|**Типы форматов файлов**|**Описание**|
| :- | :- |
|CSV|Представляет файл CSV.|
|Excel97To2003|Представляет файл Excel 97–2003.|
|XLSX|Представляет файл Excel 2007 XLSX.|
|XLSM|Представляет файл Excel 2007 XLSM.|
|XLTX|Представляет файл шаблона Excel 2007 XLTX.|
|XLTM|Представляет файл XLTM Excel 2007 с поддержкой макросов.|
|XLSB|Представляет двоичный файл Excel 2007 XLSB.|
|SpreadsheetML|Представляет XML-файл электронной таблицы.|
|TSV|Представляет файл значений, разделенных табуляцией.|
|TabDelimited|Представляет текстовый файл с разделителями табуляции.|
|ODS|Представляет файл ODS.|
|HTML|Представляет HTML файл(ов)|
|МХтмл|Представляет файл(ы) MHTML.|
|PDF|Представляет файл PDF.|
|XPS|Представляет документ XPS.|
|TIFF|Представляет формат файла изображения с тегами (TIFF).|

##  **Как сохранить файл в разных форматах**

Чтобы сохранить файлы в место хранения, укажите имя файла (вместе с путем к хранилищу) и желаемый формат файла (из**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** перечисление) при вызове**[Рабочая книга](https://reference.aspose.com/cells/net/aspose.cells/workbook)** объекты**[Сохранить](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**метод.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

##  **Как сохранить книгу в PDF**
Формат переносимого документа (PDF) — это тип документа, созданный Adobe еще в 1990-х годах. Целью этого формата файла было введение стандарта для представления документов и других справочных материалов в формате, независимом от прикладного программного обеспечения, оборудования, а также операционной системы. Формат файла PDF имеет полную возможность содержать такую информацию, как текст, изображения, гиперссылки, поля формы, мультимедийные материалы, цифровые подписи, вложения, метаданные, геопространственные функции и трехмерные объекты, которые могут стать частью исходного документа.

Следующие коды показывают, как сохранить книгу в формате PDF с номером Aspose.Cells:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

##  **Как сохранить книгу в текстовом формате или в формате CSV**

Иногда вам нужно преобразовать или сохранить книгу с несколькими листами в текстовый формат. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.) по умолчанию Microsoft Excel и Aspose.Cells сохраняют только содержимое активного листа.

В следующем примере кода объясняется, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может представлять собой любой файл электронной таблицы Excel или OpenOffice Microsoft (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством листов.

При выполнении кода он преобразует данные всех листов книги в формат TXT.

 Вы можете изменить тот же пример, чтобы сохранить файл по адресу CSV. По умолчанию:**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**является запятой, поэтому не указывайте разделитель при сохранении в формате CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

##  **Как сохранить файл в текстовые файлы с помощью специального разделителя**

Текстовые файлы содержат данные электронных таблиц без форматирования. Файл представляет собой своего рода обычный текстовый файл, который может иметь некоторые настраиваемые разделители между данными.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

##  **Как сохранить файл в поток**

 Чтобы сохранить файлы в поток, создайте*Памятьпоток* или*Файловый поток*объект и сохраните файл в этом объекте потока, вызвав метод**[Рабочая книга](https://reference.aspose.com/cells/net/aspose.cells/workbook)** объекты**[Сохранить](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** метод. Укажите желаемый формат файла с помощью**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** перечисление при вызове**[Сохранить](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**метод.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

##  **Как сохранить файл Excel в файлы Html и Mht**
Aspose.Cells может просто сохранить файл Excel, JSON, CSV или другие файлы, которые Aspose.Cells может загрузить в виде файлов .html и .mht.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

##  **Как сохранить файл Excel в OpenOffice (ODS, SXC, FODS, OTS)**
Мы можем сохранить файлы в формате Open Office: ODS, SXC, FODS, OTS и т. д.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

##  **Как сохранить файл Excel в формате JSON или XML**

JSON (нотация объектов JavaScript) — это открытый стандартный формат файла для обмена данными, в котором для хранения и передачи данных используется удобочитаемый текст. Файлы JSON хранятся с расширением .json. JSON требует меньше форматирования и является хорошей альтернативой XML. JSON получен из JavaScript, но является независимым от языка форматом данных. Генерация и анализ JSON поддерживается многими современными языками программирования. application/json — это тип носителя, используемый для JSON.

Aspose.Cells поддерживает сохранение файлов в формате JSON или XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


##  **Предварительные темы**
- [Настройка уровня сжатия книги](/cells/ru/net/adjust-workbook-compression-level/)
- [Сохранение книги в строгом формате электронной таблицы Open XML](/cells/ru/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Сохранение файла в объекте ответа](/cells/ru/net/saving-file-to-response-object/)
