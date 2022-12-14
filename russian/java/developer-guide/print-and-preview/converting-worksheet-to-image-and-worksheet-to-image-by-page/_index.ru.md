---
title: Преобразование рабочего листа в изображение и рабочего листа в изображение на странице
type: docs
weight: 210
url: /ru/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

Этот документ предназначен для предоставления разработчикам подробного понимания того, как преобразовать рабочий лист в файл изображения и рабочий лист с несколькими страницами в файл изображения на странице.

Иногда вам может понадобиться представить рабочие листы в виде изображений, например, чтобы использовать их в приложениях или на веб-страницах. Вам может понадобиться вставить изображения в документ Word, файл PDF, презентацию PowerPoint или использовать их в каком-либо другом сценарии. Просто вы хотите отобразить рабочий лист как изображение. Aspose.Cells API-интерфейсы поддерживают преобразование рабочих листов в Microsoft файлах Excel в изображения. Кроме того, Aspose.Cells поддерживает преобразование книги в несколько файлов изображений, по одному на страницу.

{{% /alert %}}

## **Использование Aspose.Cells для преобразования рабочего листа в файл изображения**

В этой статье показано, как использовать Aspose.Cells for Java API для преобразования рабочего листа в изображение. API предоставляет несколько ценных классов, таких как[**Листрендеринг**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**Имажеорпринтоптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**Рабочая книгаВизуализация**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) , и так далее.[**Листрендеринг**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) класс представляет рабочий лист для рендеринга изображений для рабочего листа и имеет перегруженный[**изображать**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)), который может напрямую преобразовывать рабочий лист в файлы изображений с любым набором атрибутов или параметров.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **Результат**

После выполнения приведенного выше кода рабочий лист с именем Sheet1 преобразуется в файл изображения SheetImage.jpg.

**Выходной JPG**

![дело:изображение_альтернативный_текст](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Использование Aspose.Cells для преобразования рабочего листа в файл изображения по страницам**

В этом примере показано, как использовать Aspose.Cells для преобразования рабочего листа из шаблона рабочей книги с несколькими страницами в один файл изображения на странице.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **Результат**

После выполнения приведенного выше кода рабочий лист с именем Sheet1 преобразуется в два файла изображений (по одному на страницу): Sheet 1 Page 1.Tiff и Sheet 1 Page 2.Tiff.

**Сгенерированный файл изображения (Лист 1 Страница 1.Tiff)**

![дело:изображение_альтернативный_текст](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**Сгенерированный файл изображения (Лист 1 Страница 2.Tiff)**

![дело:изображение_альтернативный_текст](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

В этой статье показано, как преобразовать рабочий лист в файл изображения и преобразовать рабочие листы с несколькими страницами в несколько файлов изображений (по одному на страницу) с помощью Aspose.Cells. Aspose.Cells предлагает большую гибкость, чем другие компоненты, и обеспечивает выдающуюся скорость, эффективность и надежность. Результаты показывают, что Aspose.Cells извлек выгоду из многолетних исследований, проектирования и тщательной настройки.

{{% /alert %}}

## Статьи по Теме

- [Преобразование рабочего листа в различные форматы изображений](/cells/ru/java/converting-worksheet-to-different-image-formats/)
- [Экспорт рабочего листа или диаграммы в изображение с желаемой шириной и высотой](/cells/ru/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
