---
title: Преобразование электронной таблицы в различные форматы изображений
type: docs
weight: 30
url: /ru/java/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells позволяет экспортировать лист из книги Excel и преобразовать его в различные форматы. В этой статье объясняется, как преобразовать лист в различные форматы.

{{% /alert %}}

## **Преобразование Рабочего листа в изображение**

Иногда бывает полезно сохранить изображение листа. Изображения можно делить онлайн, вставлять в другие документы (например, отчёты в Microsoft Word или презентации PowerPoint).

Aspose.Cells предоставляет экспорт изображений через класс [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender). Этот класс представляет лист, который будет отображен в виде изображения. Класс [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) предоставляет метод [**toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)) для преобразования листа в файл изображения. Поддерживаются форматы BMP, PNG, JPEG, TIFF и EMF.

{{% alert color="primary" %}}

Aspose.Cells for Java также поддерживает преобразование в формат TIFF. Для преобразования листа в изображение TIFF добавьте библиотеку JAI в свой classpath.

{{% /alert %}} {{% alert color="primary" %}}

В настоящее время API преобразования листа в изображение не поддерживает трехмерные пузырьковые диаграммы.

{{% /alert %}}

Ниже приведен код, показывающий, как преобразовать лист в файле Microsoft Excel в файл PNG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Преобразование Рабочего листа в SVG**

SVG означает **Масштабируемая векторная графика**. SVG - это спецификация на основе стандартов XML для двумерной векторной графики. Это открытый стандарт, который разрабатывается Консорциумом Всемирной паутины (W3C) с 1999 года.

С момента выпуска v7.1.0 **Aspose.Cells for Java** может преобразовывать листы в изображения SVG.

Для использования этой функции вам нужно импортировать пространство имен com.aspose.cells в свою программу или проект. В нем есть несколько ценных классов для отображения и печати, например, [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender) и другие.

Класс [**com.aspose.cells.ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) указывает, что лист будет сохранен в формате SVG.

Класс [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) принимает объект [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) в качестве параметра, который устанавливает формат сохранения в формат SVG.

Ниже приведен фрагмент кода, показывающий, как преобразовать лист в файле Excel в файл изображения SVG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Отображение активного листа в книге**

Простой способ преобразовать активный лист в книге - установить индекс активного листа, а затем сохранить книгу как SVG. Это отобразит активный лист в SVG. Ниже приведен образец кода, демонстрирующий эту функцию:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## Связанные статьи

- [Экспорт диаграммы в SVG с атрибутом viewBox](/cells/ru/java/export-chart-to-svg-with-viewbox-attribute/)
- [Экспорт листа или диаграммы в изображение с заданными шириной и высотой](/cells/ru/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Преобразование Рабочего листа в изображение и Рабочего листа в изображение по странице](/cells/ru/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
