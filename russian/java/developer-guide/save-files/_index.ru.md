---
title: Сохранение файлов Excel в CSV, PDF и другие форматы
linktitle: Сохранить файлы
type: docs
weight: 20
url: /ru/java/saving-excel-files-to-csv-pdf-and-other-formats/
---
{{% alert color="primary" %}}

**Aspose.Cells**позволяет разработчикам создавать файлы Excel с нуля, используя свой гибкий API. После создания файлов Excel вам также потребуется сохранить книгу (файл). Aspose.Cells предоставляет различные способы сохранения этих файлов. В этой теме мы обсудим все те возможные способы, которые могут быть приняты разработчиками для сохранения своих файлов.

{{% /alert %}}

## **Различные способы сохранения ваших файлов**

 Aspose.Cells API предоставляет класс с именем[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)который представляет файл Excel и предоставляет все необходимые свойства и методы, которые могут понадобиться разработчикам для работы с их файлами Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) класс предоставляет[**спасти**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)), который используется для сохранения файлов Excel.[**спасти**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) имеет множество перегрузок, которые используются для сохранения файлов Excel различными способами.

 Разработчики также могут указать формат файла, в котором должны быть сохранены их файлы. Файлы могут быть сохранены в нескольких форматах, таких как XLS, SpreadsheetML, CSV, с разделителями табуляции, значениями, разделенными табуляцией, TSV, XPS и многими другими. Эти форматы файлов задаются с помощью[**СохранитьФормат**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) перечисление.

[**СохранитьФормат**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)перечисление содержит множество предопределенных форматов файлов (которые могут быть выбраны вами) следующим образом:

|**Типы форматов файлов**|**Описание**|
|:- |:- |
|[**АВТО**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API пытается определить подходящий формат от расширения файла, указанного в первом параметре, до метода сохранения|
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|Представляет файл CSV|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Представляет файл Office Open XML SpreadsheetML.|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|Представляет файл XLSM на основе XML.|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Представляет файл шаблона Excel|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Представляет файл шаблона Excel с поддержкой макросов.|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Представляет файл Excel XLAM.|
|[**ТСВ**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|Представляет файл значений, разделенных табуляцией.|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|Представляет текстовый файл с разделителями табуляции|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|Представляет файл(ы) HTML|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|Представляет файл(ы) MHTML|
|[**ОРВ**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|Представляет файл электронной таблицы OpenDocument.|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Представляет файл XLS, который является форматом по умолчанию для версий Excel с 1997 по 2003 год.|
|[**SPREADSHET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|Представляет файл SpreadSheetML.|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Представляет двоичный файл Excel 2007 XLSB.|
|[**НЕИЗВЕСТНЫЙ**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|Представляет нераспознанный формат, не может быть сохранен.|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|Представляет PDF-документ|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|Представляет файл XML Paper Specification (XPS).|
|[**ТИФФ**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Представляет файл в формате Tagged Image File Format (TIFF).|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|Представляет файл масштабируемой векторной графики (SVG) на основе XML.|
|[**ДИФ**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|Представляет формат обмена данными.|
|[**НОМЕРА**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|Представляет файл чисел.|
|[**Уценка**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|Представляет уцененный документ.|
**Обычно существует два способа сохранения файлов Excel:**

1. **Сохранение файла в каком-либо месте**
1. **Сохранение файла в поток**

## **Сохранение файла в каком-либо месте**

 Если разработчикам необходимо сохранить свои файлы в каком-либо месте хранения, они могут просто указать имя файла (с указанием полного пути к нему) и желаемый формат файла (используя параметр[**СохранитьФормат**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) перечисление) при вызове[**спасти**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) метод[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)объект.

**Пример:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **Сохранение книги в текстовом формате или формате CSV**

Иногда вы хотите преобразовать или сохранить книгу с несколькими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.) по умолчанию как Microsoft Excel, так и Aspose.Cells сохраняют содержимое только активного рабочего листа.

В следующем примере кода показано, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может быть любым файлом электронной таблицы Microsoft Excel или OpenOffice (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством рабочих листов.

Когда код выполняется, он преобразует данные всех листов книги в формат TXT.

 Вы можете изменить тот же пример, чтобы сохранить файл в формате CSV. По умолчанию,[**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) является запятой, поэтому не указывайте разделитель при сохранении в формате CSV.

**Пример:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **Сохранение текстовых файлов с пользовательским разделителем**

Текстовые файлы содержат данные электронной таблицы без форматирования. Файл представляет собой обычный текстовый файл, который может иметь некоторые настраиваемые разделители между данными.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **Сохранение файла в поток**

 Если разработчикам необходимо сохранить свои файлы в**Ручей** то они должны создать**FileOutputStream** объект, а затем сохраните файл в этом**Ручей** объект, позвонив в[**спасти**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) метод[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)объект. Разработчики также могут указать желаемый формат файла (используя[**СохранитьФормат**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) перечисление) при вызове[**спасти**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) метод.

**Пример:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **Сохранение файла в другом формате**

### **XLS-файлы**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX-файлы**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDF-файлы**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **Установите параметр ContentCopyForAccessibility**

 С[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) класс, вы можете получить или установить PDF[**ДоступностьExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent) возможность контролировать доступ к содержимому в преобразованном PDF. Это означает, что он позволяет программному обеспечению для чтения с экрана использовать текст в файле PDF для чтения файла PDF. Вы можете отключить его, применив пароль для изменения разрешений и отменив выбор двух элементов на снимке экрана.[здесь](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **Экспорт пользовательских свойств в PDF**

С[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) class вы можете экспортировать пользовательские свойства исходной книги в PDF.[**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport)перечислитель предназначен для указания способа экспорта свойств. Эти свойства можно просмотреть в Adobe Acrobat Reader, щелкнув «Файл», а затем параметр «Свойства», как показано на следующем рисунке. Файл шаблона "sourceWithCustProps.xlsx" можно скачать[здесь](sourceWithCustProps.xlsx)для тестирования и вывода доступен PDF-файл "outSourceWithCustProps"[здесь](outSourceWithCustProps.pdf)для анализа.

![дело:изображение_альтернативный_текст](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Преобразование книги Excel в Markdown**

Aspose.Cells API обеспечивает поддержку экспорта электронных таблиц в формат Markdown. Чтобы экспортировать активный рабочий лист в Markdown, передайте[**СохранитьФормат.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)в качестве второго параметра[**Книга. Сохранить**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)) метод. Вы также можете использовать[**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions)класс, чтобы указать дополнительные параметры для экспорта рабочего листа в Markdown.

В следующем примере кода демонстрируется экспорт активного рабочего листа в Markdown с помощью[**СохранитьФормат.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)член перечисления. Пожалуйста, смотрите[выходной файл уценки](Book1.txt)сгенерированный кодом для справки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **Предварительные темы**
- [Настройка уровня сжатия книги](/cells/ru/java/adjust-workbook-compression-level/)
- [Преобразование рабочей книги в другие форматы](/cells/ru/java/converting-workbook-to-different-formats/)
- [Сохранить книгу в строгом формате электронной таблицы Open XML](/cells/ru/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Отслеживание процесса преобразования Excel в TIFF](/cells/ru/java/track-conversion-progress-of-excel-to-tiff/)
- [Отслеживание процесса преобразования документа](/cells/ru/java/track-document-conversion-progress/)
