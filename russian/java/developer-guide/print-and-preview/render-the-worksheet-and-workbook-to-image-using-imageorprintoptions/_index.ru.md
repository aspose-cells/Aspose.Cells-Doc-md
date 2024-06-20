---
title: Отобразить Рабочий лист и Книгу в виде изображения с использованием параметров ImageOrPrintOptions
type: docs
weight: 220
url: /ru/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---

{{% alert color="primary" %}}

Этот документ предназначен для подробного понимания того, как преобразовать рабочий лист или книгу в файл изображения и применить различные параметры изображения и печати для изображения, такие как разрешение, сжатие TIFF, формат изображения и качество страницы.

{{% /alert %}}

## **Обзор**

Иногда вам может понадобиться представить ваши рабочие листы в виде изображения. Вам может потребоваться вставлять изображения в документ Word, файл PDF, презентацию PowerPoint или использовать их в другом сценарии. Просто говоря, вам нужен рабочий лист, отображенный как изображение, чтобы вы могли использовать его в другом месте. Aspose.Cells поддерживает конвертацию рабочих листов в файлы изображений. Также Aspose.Cells поддерживает установку различных параметров, таких как формат изображения, разрешение (вертикальное и горизонтальное), качество изображения и другие параметры изображения и печати.

API предоставляет несколько ценных классов, например, [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) и т. д.

Класс [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) обрабатывает задачу создания изображений для рабочего листа, в то время как класс [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) выполняет то же самое для книги. Оба упомянутых класса имеют несколько перегруженных версий метода *toImage*, которые могут непосредственно преобразовывать рабочий лист или книгу в файл(-ы) изображения с заданными желаемыми атрибутами или параметрами. Вы можете сохранить файл изображения на диск/поток. Поддерживается несколько форматов изображений, например BMP, PNG, GIFF, JPEG, TIFF, EMF и другие.

### **Преобразовать Рабочий лист в изображение**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **Опции конвертации**

Можно сохранить конкретные страницы в изображение. Следующий код преобразует первый и второй рабочие листы в книге в изображения JPG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

Или вы можете пройти по всей книге и отобразить каждый рабочий лист в отдельное изображение:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **Преобразовать Книгу в изображение:**

Для того чтобы отобразить всю книгу в формате изображения, вы можете использовать приведенный выше подход или просто использовать класс [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), который принимает экземпляр [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) а также объект [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Вы можете сохранить всю книгу в единичное изображение TIFF с несколькими кадрами или страницами:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## Связанные статьи

- [Преобразование листа в различные форматы изображения](/cells/ru/java/converting-worksheet-to-different-image-formats/)
- [Экспорт диаграммы в SVG с атрибутом viewBox](/cells/ru/java/export-chart-to-svg-with-viewbox-attribute/)
- [Экспорт листа или диаграммы в изображение с заданными шириной и высотой](/cells/ru/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Преобразование Рабочего листа в изображение и Рабочего листа в изображение по странице](/cells/ru/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
