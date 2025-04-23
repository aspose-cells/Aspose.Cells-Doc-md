---
title: Преобразование листа в изображение и Лист в изображение по странице
type: docs
weight: 210
url: /ru/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Этот документ предназначен для предоставления разработчикам подробного понимания того, как преобразовать лист в файл изображения и лист с несколькими страницами в файл изображения на страницу.

Иногда вам может понадобиться представить листы в виде изображений, например, чтобы использовать их в приложениях или веб-страницах. Может понадобиться вставить изображения в документ Word, файл PDF, презентацию PowerPoint или использовать их в другом сценарии. Просто говоря, вы хотите отобразить лист в виде изображения. API Aspose.Cells поддерживает преобразование листов в файлах Microsoft Excel в изображения. Кроме того, Aspose.Cells поддерживает преобразование книги в несколько файлов изображений, по одному файлу на страницу.

{{% /alert %}}

## **Использование Aspose.Cells для преобразования листа в файл изображения**

Эта статья показывает, как использовать API Aspose.Cells for Java для преобразования рабочего листа в изображение. API предоставляет несколько ценных классов, таких как [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) и так далее. Класс [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) представляет рабочий лист для отображения изображений рабочего листа и имеет перегруженный метод [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage-int-java.io.OutputStream-), который может преобразовывать рабочий лист в изображения напрямую с установленными атрибутами или параметрами.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **Результат**

После выполнения вышеуказанного кода лист с именем Sheet1 будет преобразован в изображение с именем SheetImage.jpg.

**Выходной JPG**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Использование Aspose.Cells для преобразования листа в изображение по страницам**

В этом примере показано, как использовать Aspose.Cells для преобразования листа из шаблонной книги, которая содержит несколько страниц, в один файл изображения на каждой странице.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **Результат**

После выполнения вышеуказанного кода лист с именем Sheet1 будет преобразован в два изображения (по одному на страницу) Sheet 1 Page 1.Tiff и Sheet 1 Page 2.Tiff.

**Сгенерированный файл изображения (Sheet 1 Page 1.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**Сгенерированный файл изображения (Sheet 1 Page 2.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

Эта статья показывает, как преобразовать лист в файл изображения и преобразовать листы с несколькими страницами в несколько файлов изображений (по одному на страницу) с помощью Aspose.Cells. Aspose.Cells предлагает больше гибкости, чем другие компоненты, и обеспечивает выдающуюся скорость, эффективность и надежность. Результаты показывают, что Aspose.Cells получил преимущества благодаря годам исследований, разработки и тщательной настройки.

{{% /alert %}}

## Связанные статьи

- [Преобразование листа в различные форматы изображения](/cells/ru/java/converting-worksheet-to-different-image-formats/)
- [Экспорт листа или диаграммы в изображение с заданными шириной и высотой](/cells/ru/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
{{< app/cells/assistant language="java" >}}
