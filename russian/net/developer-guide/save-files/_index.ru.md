---
title: Различные способы сохранения файлов
linktitle: Сохранить файлы
type: docs
weight: 40
url: /ru/net/different-ways-to-save-files/
---
{{% alert color="primary" %}}

Aspose.Cells позволяет создавать и сохранять файлы. В этой статье объясняются различные способы сохранения файлов.

{{% /alert %}}

## **Различные способы сохранения файлов**

 Aspose.Cells обеспечивает**[Рабочая тетрадь] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** который представляет файл Excel Microsoft и предоставляет свойства и методы, необходимые для работы с файлами Excel.**[Рабочая тетрадь] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** класс обеспечивает**[Сохранить] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** метод, используемый для сохранения файлов Excel.**[Сохранить] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**Метод имеет множество перегрузок, которые используются для сохранения файлов разными способами.

 Формат файла, в котором сохраняется файл, определяется**[Сохранить формат] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)**перечисление

|**Типы форматов файлов**|**Описание**|
|:- |:- |
|CSV|Представляет файл CSV|
|Excel97To2003|Представляет файл Excel 97–2003.|
|XLSX|Представляет файл Excel 2007 XLSX.|
|XLSM|Представляет файл Excel 2007 XLSM.|
|XLTX|Представляет файл шаблона Excel 2007 XLTX.|
|XLTM|Представляет файл Excel 2007 с поддержкой макросов XLTM.|
|XLSB|Представляет двоичный файл Excel 2007 XLSB.|
|SpreadsheetML|Представляет XML-файл электронной таблицы.|
|TSV|Представляет файл значений, разделенных табуляцией.|
|TabDelimited|Представляет текстовый файл с разделителями табуляции|
|ODS|Представляет файл ODS|
|HTML|Представляет HTML файл(ы)|
|МХтмл|Представляет файл(ы) MHTML|
|PDF|Представляет файл PDF|
|XPS|Представляет документ XPS|
|TIFF|Представляет формат файла изображения с тегами (TIFF)|

## **Сохранение файла в разных форматах**

Чтобы сохранить файлы в месте хранения, укажите имя файла (вместе с путем хранения) и желаемый формат файла (из**[Сохранить формат] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)** перечисление) при вызове**[Рабочая тетрадь] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** объекты**[Сохранить] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**метод.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **Сохранение книги в формате PDF**
Portable Document Format (PDF) — это тип документа, созданный Adobe еще в 1990-х годах. Цель этого формата файла состояла в том, чтобы ввести стандарт для представления документов и других справочных материалов в формате, который не зависит от прикладного программного обеспечения, аппаратного обеспечения, а также операционной системы. Формат файла PDF имеет полную возможность содержать такую информацию, как текст, изображения, гиперссылки, поля форм, мультимедийные материалы, цифровые подписи, вложения, метаданные, геопространственные функции и трехмерные объекты, которые могут стать частью исходного документа.

Следующие коды показывают, как сохранить книгу в виде файла PDF с номером Aspose.Cells:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **Сохранение книги в текстовом формате или формате CSV**

Иногда вы хотите преобразовать или сохранить книгу с несколькими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.) по умолчанию как Microsoft Excel, так и Aspose.Cells сохраняют содержимое только активного рабочего листа.

В следующем примере кода показано, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может быть любым файлом электронной таблицы Microsoft Excel или OpenOffice (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством рабочих листов.

Когда код выполняется, он преобразует данные всех листов книги в формат TXT.

Вы можете изменить тот же пример, чтобы сохранить файл по адресу CSV. По умолчанию**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**является запятой, поэтому не указывайте разделитель при сохранении в формате CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Сохранение текстовых файлов с пользовательским разделителем**

Текстовые файлы содержат данные электронной таблицы без форматирования. Файл представляет собой обычный текстовый файл, который может иметь некоторые настраиваемые разделители между данными.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **Сохранение файла в поток**

 Чтобы сохранять файлы в поток, создайте*ПамятьПоток* или же*FileStream* объект и сохраните файл в этот объект потока, вызвав метод**[Рабочая тетрадь] (https://reference.aspose.com/cells/net/aspose.cells/workbook)** объекты**[Сохранить] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** метод. Укажите желаемый формат файла с помощью**[Сохранить формат] (https://reference.aspose.com/cells/net/aspose.cells/saveformat)** перечисление при вызове**[Сохранить] (https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**метод.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **Сохранение файлов в виде файлов Html и Mht**
Aspose.Cells может просто сохранить файл Excel JSON, CSV или другие файлы, которые могут быть загружены Aspose.Cells в виде файлов .html и .mht.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

## **Сохранение как OpenOffice (ODS, SXC, FODS, OTS)**
Мы можем сохранить файлы в формате открытого офиса: ODS, SXC, FODS, OTS и т. д.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **Сохранение файла Excel как JSON или XML**

JSON (обозначение объектов JavaScript) — это открытый стандартный формат файла для обмена данными, который использует удобочитаемый текст для хранения и передачи данных. JSON файлов хранятся с расширением .json. JSON требует меньше форматирования и является хорошей альтернативой XML. JSON является производным от JavaScript, но является независимым от языка форматом данных. Генерация и анализ JSON поддерживается многими современными языками программирования. application/json — тип носителя, используемый для JSON.

Aspose.Cells поддерживает сохранение файлов в JSON или XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **Предварительные темы**
- [Настройка уровня сжатия книги](/cells/ru/net/adjust-workbook-compression-level/)
- [Сохранить книгу в строгом формате электронной таблицы Open XML](/cells/ru/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Сохранение файла в объект ответа](/cells/ru/net/saving-file-to-response-object/)
