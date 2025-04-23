---
title: Преобразование книги в различные форматы
type: docs
weight: 20
url: /ru/java/converting-workbook-to-different-formats/
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает конвертацию между множеством форматов. Технически, конвертация означает загрузку книги в одном формате файла и сохранение ее в другом.

{{% /alert %}}

## **Преобразование Excel в XPS**

Формат документа XPS состоит из структурированной разметки XML, которая определяет макет документа и визуальное оформление каждой страницы, а также правила рендеринга для распределения, архивирования, рендеринга, обработки и печати документов.

Язык разметки для XPS является подмножеством XAML, что позволяет включать векторные графические элементы в документы, используя XAML для разметки примитивов Windows Presentation Foundation (WPF). Используемые элементы описываются в терминах путей и других геометрических примитивов.

Файл XPS на самом деле представляет собой Unicode ZIP-архив, использующий Открытые конвенции упаковки, содержащий файлы, составляющие документ. Сюда входят XML-файл разметки для каждой страницы, текст, встроенные шрифты, растровые изображения, 2D векторная графика, а также информация о цифровом управлении правами. Содержимое файла XPS можно изучить, просто открыв его в приложении, которое поддерживает файлы ZIP.

Начиная с Aspose.Cells 6.0.0, поддерживается преобразование Microsoft Excel в формат XPS.

### **Преобразование одного рабочего листа в формат XPS**

В следующем примере показано, как преобразовать один рабочий лист в файле Excel в формат XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **Экспорт всей книги в формат XPS**

В следующем примере показано, как преобразовать всю книгу в формат XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **Быстрое преобразование Excel в формат XPS**

В следующем примере показан простой способ прямого преобразования файла Excel в формат XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **Преобразование Excel в файлы MHTML**

[**MHTML**](https://en.wikipedia.org/wiki/MHTML) объединяет обычный HTML с внешними ресурсами, такими как изображения, анимации, аудио и т. д., в один файл. Они используются для электронной почты с расширением файла .mht.

{{% alert color="primary" %}}

Aspose.Cells поддерживает чтение и запись файлов MHTML.

{{% /alert %}}

Преобразование электронной таблицы в MHTML - быстрая операция, как показано ниже.

В приведенном ниже примере кода показано, как сохранить книгу в формате MHTML.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **Преобразование файлов Excel в HTML**

API Aspose.Cells поддерживает экспорт таблиц в формат HTML. Для этой цели Aspose.Cells использует класс [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions), который позволяет разработчикам контролировать несколько аспектов вывода HTML.

Приведенный ниже код демонстрирует использование класса [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions) для экспорта файлов Microsoft Excel в формат HTML без указания дополнительных параметров.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

Вы можете достичь тех же результатов, передав [**SaveFormat.HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML) методу [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-).

{{% /alert %}}

### **Настройка предпочтений изображения для HTML**

Начиная с версии 8.0.2, Aspose.Cells предоставляет [**ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) для класса [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions), что позволяет разработчикам указывать предпочтения по изображению при сохранении электронных таблиц в формат HTML.

Настройки изображений, которые можно применить, это:

- [**ImageType**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType): Получает или устанавливает тип изображения. Обратите внимание, что все формы, включая диаграммы, отображаются в виде изображений в выходном HTML.
- [**Quality**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality): Получает или устанавливает качество изображений от 0 до 100, когда указывается ImageFormat как Jpeg.
- [**VerticalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution): Получает или устанавливает вертикальное разрешение изображения в точках на дюйм.
- [**HorizontalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution): Получает или устанавливает горизонтальное разрешение изображения в точках на дюйм.
- [**TiffCompression**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression): Получает или устанавливает тип сжатия для изображений, когда ImageFormat указан как Tiff.
- [**Transparent**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent): Указывает, должен ли фон изображения быть прозрачным, когда ImageFormat указан как Png.

Приведенный ниже код демонстрирует, как использовать [**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) для указания различных предпочтений.

|**Просмотр электронной таблицы до экспорта**|**Просмотр HTML после экспорта**|
| :- | :- |
|![Просмотр электронной таблицы до экспорта](converting-workbook-to-different-formats_1.png)|![Просмотр HTML после экспорта](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **Преобразование Excel в файлы PDF**

Документы PDF широко используются в качестве стандартного формата обмена документами между организациями, секторами государственного управления и отдельными лицами. Часто разработчиков программного обеспечения просят создать способ легкого преобразования файлов Microsoft Excel в документы PDF. Aspose.Cells поддерживает эти функции. В данной статье показано, как это сделать.

### **Преобразование Excel в PDF**

Преобразование Microsoft Excel в PDF было представлено с версией Aspose.Cells for Java 2.3.0. С этого релиза Aspose.Cells может [преобразовывать электронные таблицы в PDF непосредственно](#direct-conversion) (включая [PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files)), без использования другого продукта. Для преобразования электронных таблиц с более старыми версиями Aspose.Cells, [используйте Aspose.PDF для преобразования](#conversion-with-asposepdf-asposecells-prior-to-230).

Aspose.Cells преобразует электронные таблицы в PDF с высокой точностью и достоверностью. Однако есть несколько [ограничений](/cells/ru/java/converting-workbook-to-different-formats/#conversion-attributes), перечисленных в конце этой статьи.

{{% alert color="primary" %}}

Aspose.Cells for Java напрямую записывает информацию о API и номере версии в выходные документы. Например, при рендеринге документа в PDF Aspose.Cells for Java заполняет поле **Application** значением 'Aspose.Cells' и поле **PDF Producer** значением, например, 'Aspose.Cells for Java v17.9'.

Обратите внимание, что нельзя указать Aspose.Cells for Java изменить или удалить эту информацию из выходных документов.

{{% /alert %}}

#### **Прямое преобразование**

Сохраните файл Excel непосредственно в PDF, используя метод [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-), и предоставьте член интерфейса [**SaveFormat.PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF). Прямое преобразование, таким образом, является наиболее эффективным методом преобразования. Оно не теряет данных или форматирование, но сохраняет PDF-файл выглядящим как исходный файл Excel.

Чтобы указать параметры безопасности при сохранении в PDF, используйте [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **Расширенное преобразование**

Вы также можете использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) для установки различных атрибутов для преобразования. Установка различных свойств класса [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) даст вам контроль над параметрами Печать, Шрифт, Безопасность и Сжатие для результирующего PDF-файла. Самое заметное свойство - это [**Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance), позволяющее сохранять файлы Excel в PDF/A-совместимые PDF-файлы.

##### **Сохранение электронных таблиц Excel в файлы PDF/A-совместимые**

Нижеприведенный фрагмент кода демонстрирует использование класса [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) для сохранения файлов Excel в PDF/A-совместимом формате PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Преобразование с помощью Aspose.Pdf: Aspose.Cells Перед 2.3.0**

Для версий Aspose.Cells до версии 2.3.0 вам нужно использовать компонент, например [Aspose.PDF для Java](/pdf/java/), чтобы преобразовать электронные таблицы в файлы PDF. Aspose.Cells и Aspose.PDF совместно работают для преобразования электронной таблицы в PDF с промежуточным этапом.

Для преобразования электронных таблиц в PDF с помощью Aspose.Cells и Aspose.PDF:

1. Создайте объект класса [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), вызвав его пустой конструктор.
1. Выполните необходимую работу с электронной таблицей, используя API Aspose.Cells.
1. Вызовите метод [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-) для сохранения электронной таблицы:
   1. Установите формат файла в формат XML.
   1. Выберите Aspose_Pdf (предопределенное значение) из интерфейса FileFormatType. Это направит метод сохранения на создание электронной таблицы в XML-форме, совместимой со схемой Aspose.PDF, чтобы затем Aspose.PDF для Java мог создать документ PDF.
1. Когда XML-файл будет создан, создайте объект класса Pdf в пакете aspose.pdf.
1. Вызовите метод bindXML класса Pdf и передайте название созданного XML-файла.
1. Вызовите метод save класса Pdf для создания документа PDF.

Вышеуказанные шаги реализованы ниже в примере.

{{% alert color="primary" %}}

Если ваша таблица содержит формулы, лучше всего вызвать метод [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) прямо перед отображением таблицы в формате PDF. Таким образом будет обеспечено пересчет значений, зависящих от формулы, и правильные значения будут отображены в PDF.

{{% /alert %}}

#### **Атрибуты преобразования**

Мы усердно работаем над улучшением преобразования и других аспектов Aspose.Cells с каждым релизом. Преобразование Excel в PDF имеет несколько ограничений. Некоторые настройки формата, указанные в электронной таблице, могут быть потеряны, и не все объекты рисования поддерживаются.

В таблице ниже перечислены все функции, которые полностью или частично поддерживаются при экспорте в PDF с помощью Aspose.Cells. Эта таблица не является окончательной и не охватывает все атрибуты электронной таблицы. Она также может идентифицировать те функции, которые могут не поддерживаться или быть частично поддерживаемыми для преобразования.

{{% alert color="primary" %}}

|**Элемент документа**|**Атрибут**|**Полностью поддерживается**|**Примечания**|
| :- | :- | :- | :- |
|Выравнивание| |Да| |
|Поворот| |Частично|Поддерживаются только 90 и -90.|
|Настройки фона| |Да| |
|Граница|Цвет|Да| |
|Граница|Стиль линии|Да| |
|Граница|Толщина линии|Да| |
|Данные ячейки| |Да| |
|Комментарии| |Нет| |
|Условное форматирование| |Да| |
|Свойства документа| |Да| |
|Объекты рисования| |Да| |
|Шрифт|Размер|Да| |
|Шрифт|Цвет|Да| |
|Шрифт|Стиль|Да| |
|Шрифт|Подчеркивание|Да| |
|Шрифт|Эффекты|Частично|Поддерживается только эффект зачеркивания|
|Изображения| |Да| |
|Гиперссылка| |Да| |
|Диаграммы| |Да| |
|Объединенные ячейки| |Да| |
|Разрыв страницы| |Да| |
|Настройка страницы|Верхний/нижний колонтитул|Да| |
|Настройка страницы|Поля|Да| |
|Настройка страницы|Ориентация страницы|Да| |
|Настройка страницы|Размер страницы|Да| |
|Настройка страницы|Область печати|Да| |
|Настройка страницы|Печатные заголовки|Да| |
|Настройка страницы|Масштабирование|Да| |
|Высота строки/Ширина столбца| |Да| |
{{% /alert %}}
{{< app/cells/assistant language="java" >}}
