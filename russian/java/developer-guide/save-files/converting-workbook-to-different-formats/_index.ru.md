---
title: Преобразование рабочей книги в другие форматы
type: docs
weight: 20
url: /ru/java/converting-workbook-to-different-formats/
---
{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование между многими форматами. Технически преобразование означает загрузку книги в одном формате файла и сохранение ее в другом.

{{% /alert %}}

## **Преобразование Excel в XPS**

Формат документа XPS состоит из структурированной XML-разметки, которая определяет макет документа и внешний вид каждой страницы, а также правила рендеринга для распространения, архивирования, рендеринга, обработки и печати документов.

Язык разметки для XPS — это подмножество XAML, которое позволяет включать элементы векторной графики в документы, используя XAML для разметки примитивов Windows Presentation Foundation (WPF). Используемые элементы описываются в терминах путей и других геометрических примитивов.

Файл XPS на самом деле представляет собой ZIP-архив в кодировке Unicode, использующий соглашения об открытой упаковке, содержащий файлы, составляющие документ. К ним относятся файл разметки XML для каждой страницы, текст, встроенные шрифты, растровые изображения, двумерная векторная графика, а также информация об управлении цифровыми правами. Содержимое файла XPS можно проверить, просто открыв его в приложении, поддерживающем файлы ZIP.

Начиная с Aspose.Cells 6.0.0, Microsoft поддерживается преобразование Excel в XPS.

### **Преобразование одного рабочего листа в XPS**

В следующем примере показано, как преобразовать один лист в файле Excel в формат XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **Экспорт всей книги в XPS**

В следующем примере показано, как преобразовать всю книгу в формат XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **Быстрое преобразование Excel в XPS**

В следующем примере показан простой способ прямого преобразования файла Excel в формат XPS.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **Преобразование Excel в файлы MHTML**

[MHTML](https://en.wikipedia.org/wiki/MHTML) сочетает обычный HTML с внешними ресурсами; то есть контент, который обычно связан, например изображения, анимация, аудио и т. Д., В один файл. Они используются для электронных писем с расширением файла .mht.

{{% alert color="primary" %}}

Aspose.Cells поддерживает чтение и запись файлов MHTML.

{{% /alert %}}

Преобразование электронной таблицы в MHTML — это быстрая операция, как показано ниже.

В приведенном ниже примере кода показано, как сохранить книгу в виде файла MHTML.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **Преобразование файлов Excel в HTML**

 API-интерфейсы Aspose.Cells обеспечивают поддержку экспорта электронных таблиц в формат HTML. Для этого Aspose.Cells использует**[HtmlSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**class, который позволяет разработчикам контролировать несколько аспектов выходного HTML.

В приведенном ниже коде показано, как использовать**[HtmlSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**класс для экспорта Microsoft файлов Excel в формат HTML без указания дополнительных параметров.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

 Вы можете добиться тех же результатов, передав**[SaveFormat.HTML](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)** к**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** метод.

{{% /alert %}}

### **Настройка параметров изображения для HTML**

 Начиная с 8.0.2, Aspose.Cells выставил**[ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)**для**[HtmlSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**class, который позволяет разработчикам указывать предпочтения изображения при сохранении электронных таблиц в формате HTML.

Настройки изображения, которые можно применить:

- **[ImageType](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType)**: Получает или задает тип изображения. Обратите внимание, что все фигуры, включая диаграммы, отображаются в виде изображений в выходном HTML-коде.
- **[Качество](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality)**: Получает или задает качество изображений от 0 до 100, если для параметра ImageFormat указано значение Jpeg.
- **[Вертикальное разрешение] (https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution)**: получает или задает разрешение изображения по вертикали в точках на дюйм.
- **[Горизонтальное разрешение] (https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution)**: получает или задает разрешение изображения по горизонтали в точках на дюйм.
- **[TiffCompression] (https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression)**: Получает или задает тип сжатия для изображений, если ImageFormat задан как Tiff.
- **[Прозрачный](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Прозрачный)**Указывает, должен ли фон изображения быть прозрачным, если ImageFormat указан как Png.

 В приведенном ниже коде показано, как использовать**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)** для указания различных предпочтений.

|**Представление электронной таблицы перед экспортом**|**Просмотр HTML после экспорта**|
|:- |:- |
|![Представление электронной таблицы перед экспортом](converting-workbook-to-different-formats_1.png)|![Просмотр HTML после экспорта](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **Преобразование Excel в файлы PDF**

Документы в формате PDF широко используются в качестве стандартного формата обмена документами между организациями, государственными секторами и отдельными лицами. Разработчиков программного обеспечения часто просят найти способ легко конвертировать Microsoft файлы Excel в документы PDF. Aspose.Cells поддерживает эти функции. В этой статье показано, как.

### **Преобразование Excel в PDF**

 Microsoft Преобразование Excel в PDF было введено в версии Aspose.Cells for Java 2.3.0. Начиная с этого выпуска, Aspose.Cells может[конвертировать электронные таблицы в PDF напрямую](#direct-conversion) (включая[PDF/А](#saving-excel-spreadsheets-to-pdfa-complied-files)), без другого продукта. Чтобы преобразовать электронные таблицы с более ранними версиями Aspose.Cells,[используйте Aspose.PDF для преобразования](#conversion-with-asposepdf-asposecells-prior-to-230).

 Aspose.Cell конвертирует электронные таблицы в PDF с высокой степенью точности и достоверности. Однако есть несколько[ограничения](/cells/ru/java/converting-workbook-to-different-formats/#conversion-attributes), перечисленные в конце этой статьи.

{{% alert color="primary" %}}

 Aspose.Cells for Java непосредственно записывает информацию о API и номере версии в выходных документах. Например, при преобразовании документа в PDF Aspose.Cells for Java заполняет**Заявление** поле со значением «Aspose.Cells» и**PDF-продюсер** поле со значением, например 'Aspose.Cells for Java v17.9'.

Обратите внимание, что вы не можете поручить Aspose.Cells for Java изменить или удалить эту информацию из выходных документов.

{{% /alert %}}

#### **Прямое преобразование**

Сохраните файл Excel непосредственно в PDF, используя**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** метод и предоставить**[SaveFormat.PDF] (https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)**член интерфейса. Прямое преобразование, подобное этому, является наиболее эффективным методом преобразования. Он не теряет данные или форматирование, но сохраняет выходной PDF-файл, похожий на входной файл Excel.

 Чтобы указать параметры безопасности при сохранении в PDF, используйте**[PdfSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **Расширенное преобразование**

Вы также можете выбрать использование**[PdfSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** класс для установки различных атрибутов для преобразования. Установка различных свойств**[PdfSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**class даст вам контроль над настройками печати, шрифта, безопасности и сжатия для результирующего файла PDF. Наиболее примечательным свойством является**[Соответствие](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**который позволяет сохранять файлы Excel в файлы PDF, совместимые с форматом PDF/A.

##### **Сохранение электронных таблиц Excel в файлы PDF/A Complied**

Приведенный ниже фрагмент кода демонстрирует использование**[PdfSaveOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** class для сохранения файлов Excel в формате PDF, совместимом с PDF/A.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Преобразование с Aspose.Pdf: Aspose.Cells До 2.3.0**

 Для версий Aspose.Cells до версии 2.3.0 вам необходимо использовать такой компонент, как[Aspose.PDF for Java](/pdf/java/) для преобразования электронных таблиц в файлы PDF. Aspose.Cells и Aspose.PDF работают вместе, чтобы преобразовать электронную таблицу в PDF через промежуточный шаг.

Чтобы преобразовать электронные таблицы в PDF с номерами Aspose.Cells и Aspose.PDF:

1.  Создать экземпляр объекта**[Рабочая тетрадь] (https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**class, вызвав его пустой конструктор.
1. Выполните желаемую работу в электронной таблице, используя Aspose.Cells API.
1. Позвоните**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))**метод сохранения таблицы:
1. Установите формат файла XML.
 1. Выберите Aspose_Pdf (заранее заданное значение) в интерфейсе FileFormatType. Это направляет метод сохранения для создания электронной таблицы в форме XML, совместимой со схемой Aspose.PDF, чтобы Aspose.PDF for Java мог затем создать документ PDF.
1. Когда файл XML будет создан, создайте объект класса Pdf в пакете aspose.pdf.
1. Вызовите метод bindXML класса Pdf и передайте имя выходного файла XML.
1. Вызовите метод сохранения класса Pdf, чтобы сгенерировать PDF-документ.

Описанные выше шаги реализованы ниже в примере.

{{% alert color="primary" %}}

 Если ваша электронная таблица содержит формулы, лучше всего вызвать**[Workbook.calculateFormula](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())** непосредственно перед преобразованием электронной таблицы в формат PDF. Это гарантирует, что значения, зависящие от формулы, будут пересчитаны, а в PDF-файле отобразятся правильные значения.

{{% /alert %}}

#### **Атрибуты конверсии**

Мы прилагаем все усилия, чтобы улучшить преобразование и другие аспекты Aspose.Cells с каждым выпуском. Преобразование Excel в PDF имеет несколько ограничений. Некоторые настройки формата, указанные в электронной таблице, могут быть потеряны, и не все объекты чертежа поддерживаются.

В таблице ниже перечислены все функции, которые полностью или частично поддерживаются при экспорте в PDF с помощью Aspose.Cells. Эта таблица не является окончательной и не охватывает все атрибуты электронной таблицы. Он также может определить те функции, которые могут не поддерживаться или частично поддерживаться для преобразования.

{{% alert color="primary" %}}

|**Элемент документа**|**Атрибут**|**Сеть поддерживается**|**Заметки**|
|:- |:- |:- |:- |
|Выравнивание||Да||
|Вращение||Частично|Поддерживает только 90 и -90.|
|Настройки фона||Да||
|Граница|Цвет|Да||
|Граница|Стиль линии|Да||
|Граница|Ширина линии|Да||
|Cell Данные||Да||
|Комментарии||Нет||
|Условное форматирование||Да||
|Свойства документа||Да||
|Объекты рисования||Да||
|Шрифт|Размер|Да||
|Шрифт|Цвет|Да||
|Шрифт|Стиль|Да||
|Шрифт|Подчеркнуть|Да||
|Шрифт|Последствия|Частично|Поддерживается только эффект зачеркивания|
|Картинки||Да||
|Гиперссылка||Да||
|Графики||Да||
|Объединено Cells||Да||
|Разрыв страницы||Да||
|Настройка страницы|Верхний/нижний колонтитул|Да||
|Настройка страницы|Поля|Да||
|Настройка страницы|Ориентация страницы|Да||
|Настройка страницы|Размер страницы|Да||
|Настройка страницы|Область печати|Да||
|Настройка страницы|Печать заголовков|Да||
|Настройка страницы|Масштабирование|Да||
|Высота строки/ширина столбца||Да||
{{% /alert %}}
