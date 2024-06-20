---
title: Сохранение файлов Excel в CSV, PDF и другие форматы
linktitle: Сохранить файлы
type: docs
weight: 20
url: /ru/java/saving-excel-files-to-csv-pdf-and-other-formats/
---

{{% alert color="primary" %}}

**Aspose.Cells** позволяет разработчикам создавать файлы Excel с нуля с использованием его гибкого API. После создания файлов Excel вам также потребуется сохранить свою книгу (файл). Aspose.Cells предоставляет различные способы для сохранения этих файлов. В этой теме мы обсудим все возможные способы, которые могут быть использованы разработчиками для сохранения их файлов.

{{% /alert %}}

## **Различные способы сохранения ваших файлов**

Aspose.Cells API предоставляет класс с именем [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), который представляет собой файл Excel и предоставляет все необходимые свойства и методы, которые могут понадобиться разработчикам для работы с их файлами Excel. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) предоставляет метод [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)), который используется для сохранения файлов Excel. Метод [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) имеет множество вариантов перегрузки, которые используются для сохранения файлов Excel различными способами.

Разработчики также могут указать формат файла, в котором должны быть сохранены их файлы. Файлы могут быть сохранены в нескольких форматах, таких как XLS, SpreadsheetML, CSV, разделенные табуляциями, TSV, XPS и многие другие. Эти форматы файлов указываются с использованием перечисления [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat).

Перечисление [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) содержит множество предопределенных форматов файлов (которые могут быть выбраны вами) следующим образом:

|**Типы форматов файлов**|**Описание**|
| :- | :- |
|[**AUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API пытается определить соответствующий формат по указанному расширению файла в первом параметре метода сохранения|
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|Представляет собой файл CSV|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Представляет файл формата Office Open XML SpreadsheetML|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|Представляет файл формата на основе XML XLSM|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Представляет файл шаблона Excel|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Представляет файл шаблона с поддержкой макросов Excel|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Представляет файл Excel XLAM|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|Представляет файл значений, разделенных табуляцией|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|Представляет файл с текстом, разделенным табуляцией|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|Представляет файл(ы) HTML|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|Представляет файл(ы) MHTML|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|Представляет файл таблицы OpenDocument|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Представляет файл XLS, который является форматом по умолчанию для ревизий Excel 1997 по 2003 годы|
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|Представляет файл SpreadSheetML|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Представляет двоичный файл Excel 2007 XLSB|
|[**UNKNOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|Представляет нераспознанный формат, не может быть сохранен.|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|Представляет документ PDF|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|Представляет файл формата XML Paper Specification (XPS)|
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Представляет файл формата Tagged Image File Format (TIFF)|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|Представляет файл формата XML-based Scalable Vector Graphics (SVG)|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|Представляет формат обмена данными.|
|[**NUMBERS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|Представляет файл чисел.|
|[**MARKDOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|Представляет документ в формате markdown.|
**Обычно существуют два способа сохранения файлов Excel следующим образом:**

1. **Сохранение файла в выбранное место**
1. **Сохранение файла в поток**

## **Сохранение файла в указанное местоположение**

Если разработчикам нужно сохранить их файлы в каком-либо месте хранения, то они могут просто указать имя файла (с полным путем к хранению) и желаемый формат файла (используя перечисление [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)) при вызове метода [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) объекта [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook).

**Пример:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **Сохранение рабочей книги в текстовом или CSV формате**

Иногда вам нужно преобразовать или сохранить книгу с несколькими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.), по умолчанию как Microsoft Excel, так и Aspose.Cells сохраняют содержимое только активного листа.

В следующем примере кода объясняется, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может быть любым файлом электронных таблиц Microsoft Excel или OpenOffice (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством листов.

При выполнении кода конвертируются данные всех листов книги в формат TXT.

Вы можете изменить тот же пример, чтобы сохранить свой файл в CSV. По умолчанию, [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) это запятая, поэтому не указывайте разделитель при сохранении в формат CSV.

**Пример:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **Сохранение текстовых файлов с пользовательским разделителем**

Текстовые файлы содержат данные электронных таблиц без форматирования. Файл представляет собой своего рода обычный текстовый файл, который может содержать некоторые настраиваемые разделители между его данными.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **Сохранение файла в поток**

Если разработчикам нужно сохранить их файлы в **поток**, то они должны создать объект **FileOutputStream** и затем сохранить файл в этот **поток**, вызвав метод [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) объекта [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Разработчики также могут указать желаемый формат файла (используя перечисление [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)) при вызове метода [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)).

**Пример:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **Сохранение файла в другом формате**

### **XLS Файлы**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX Файлы**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDF Файлы**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **Установите опцию ContentCopyForAccessibility**

С помощью класса [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) вы можете получить или установить опцию PDF [**AccessibilityExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent), чтобы контролировать доступ к содержимому в преобразованном PDF. Это позволяет программному обеспечению для работы со скринридерами использовать текст внутри PDF-файла для чтения PDF-файла. Вы можете отключить это, применив пароль для изменения разрешений и сняв выбор двух элементов на скриншоте [здесь](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **Экспорт пользовательских свойств в PDF**

С помощью класса [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) вы можете экспортировать пользовательские свойства из исходной книги в PDF. Для указания способа экспорта предоставляется перечисление [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport). Эти свойства можно просмотреть в Adobe Acrobat Reader, нажав на пункт File, а затем свойства, как показано на следующем изображении. Файл-шаблон "sourceWithCustProps.xlsx" можно скачать [здесь](sourceWithCustProps.xlsx) для тестирования, а выходной PDF-файл "outSourceWithCustProps" доступен [здесь](outSourceWithCustProps.pdf) для анализа.

![todo:image_alt_text](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Преобразование электронной таблицы Excel в Markdown**

API Aspose.Cells поддерживает экспорт электронных таблиц в формат Markdown. Чтобы экспортировать активный лист в формат Markdown, передайте [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN) вторым параметром метода [**Workbook.Save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)). Вы также можете использовать класс [**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions), чтобы указать дополнительные настройки для экспорта листа в Markdown.

Приведен пример кода, демонстрирующий экспорт активного листа в формат Markdown с использованием члена перечисления [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN). Пожалуйста, ознакомьтесь с [выходным файлом Markdown](Book1.txt), сгенерированным кодом для справки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **Продвинутые темы**
- [Настройка уровня сжатия книги Excel](/cells/ru/java/adjust-workbook-compression-level/)
- [Преобразование книги в различные форматы](/cells/ru/java/converting-workbook-to-different-formats/)
- [Сохранить книгу в формате Strict Open XML Spreadsheet](/cells/ru/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Отслеживание процесса преобразования Excel в TIFF](/cells/ru/java/track-conversion-progress-of-excel-to-tiff/)
- [Отслеживание прогресса конвертации документов](/cells/ru/java/track-document-conversion-progress/)
