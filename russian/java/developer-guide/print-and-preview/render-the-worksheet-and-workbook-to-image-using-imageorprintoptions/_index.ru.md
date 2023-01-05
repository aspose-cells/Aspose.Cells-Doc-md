---
title: Визуализация рабочего листа и рабочей книги в изображение с помощью ImageOrPrintOptions
type: docs
weight: 220
url: /ru/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---
{{% alert color="primary" %}}

Этот документ предназначен для подробного понимания того, как преобразовать рабочий лист или рабочую книгу в файл изображения и применить к изображению различные параметры изображения и печати, такие параметры, как разрешение, сжатие TIFF, формат изображения и качество страницы.

{{% /alert %}}

## **Обзор**

Иногда вам может потребоваться представить свои рабочие листы в виде графического представления. Вам необходимо представить изображения рабочего листа в ваших приложениях или на веб-страницах. Вам может понадобиться вставить изображения в документ Word, файл PDF, презентацию PowerPoint или использовать их в каком-либо другом сценарии. Просто вы хотите, чтобы рабочий лист отображался как изображение, чтобы вы могли использовать его в другом месте. Aspose.Cells поддерживает преобразование рабочих листов в файлах Excel в изображения. Кроме того, Aspose.Cells поддерживает настройку различных параметров, таких как формат изображения, разрешение (как по вертикали, так и по горизонтали), качество изображения и другие параметры изображения и печати.

API предоставляет несколько ценных классов, например,[**Листрендеринг**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**Имажеорпринтоптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**Рабочая книгаВизуализация**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), и т.д.

[**Листрендеринг**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) класс обрабатывает задачу рендеринга изображений для рабочего листа, тогда как класс[**Рабочая книгаВизуализация**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)делает то же самое для рабочей книги. Оба вышеупомянутых класса имеют несколько перегруженных версий*изображать*метод, который может напрямую преобразовывать лист или книгу в файлы изображений, указанные с нужными атрибутами или параметрами. Вы можете сохранить файл изображения на диск/поток. Поддерживается несколько форматов изображений, например BMP, PNG, GIFF, JPEG, TIFF, EMF и так далее.

### **Преобразовать рабочий лист в изображение**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **Параметры преобразования**

Можно сохранить определенные страницы в изображение. Следующий код преобразует первый и второй листы книги в изображения JPG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

Или вы можете циклически просматривать книгу и отображать каждый лист в ней в отдельное изображение:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **Преобразование книги в изображение:**

 Чтобы преобразовать полную книгу в формат изображения, вы можете либо использовать описанный выше подход, либо просто использовать[**Рабочая книгаВизуализация**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) класс, который принимает экземпляр[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) а также объект[**Имажеорпринтоптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

{{% alert color="primary" %}}

[**Рабочая книгаВизуализация**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) class может сохранить книгу только в формате TIFF.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## Статьи по Теме

- [Преобразование рабочего листа в различные форматы изображений](/cells/ru/java/converting-worksheet-to-different-image-formats/)
- [Экспорт диаграммы в SVG с атрибутом viewBox](/cells/ru/java/export-chart-to-svg-with-viewbox-attribute/)
- [Экспорт рабочего листа или диаграммы в изображение с желаемой шириной и высотой](/cells/ru/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Преобразование рабочего листа в изображение и рабочего листа в изображение на странице](/cells/ru/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
