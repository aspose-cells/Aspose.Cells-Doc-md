---
title: Преобразование рабочего листа в различные форматы изображений
type: docs
weight: 30
url: /ru/java/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}}

Aspose.Cells позволяет экспортировать рабочий лист из рабочей книги и преобразовывать его в различные форматы. В этой статье объясняется, как преобразовать рабочий лист в различные форматы.

{{% /alert %}}

## **Преобразование рабочего листа в изображение**

Иногда бывает полезно сохранить изображение рабочего листа. Изображения можно публиковать в Интернете, вставлять в другие документы (например, отчеты, написанные в Word Microsoft, или презентации PowerPoint).

Aspose.Cells обеспечивает экспорт изображения через**[SheetRender] (https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)** учебный класс. Этот класс представляет рабочий лист, который будет преобразован в изображение.**[SheetRender] (https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)** класс обеспечивает**[toImage()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream))**метод преобразования рабочего листа в файл изображения. Поддерживаются форматы BMP, PNG, JPEG, TIFF и EMF.

{{% alert color="primary" %}}

Aspose.Cells for Java также поддерживает преобразование в формат TIFF. Чтобы преобразовать рабочий лист в изображение TIFF, добавьте библиотеку JAI в путь к классам.

{{% /alert %}} {{% alert color="primary" %}}

В настоящее время преобразование рабочего листа в изображение API не поддерживает трехмерные пузырьковые диаграммы.

{{% /alert %}}

В приведенном ниже коде показано, как преобразовать рабочий лист в файле Excel Microsoft в файл PNG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Преобразование рабочего листа в SVG**

 SVG означает**Масштабируемая векторная графика**. SVG — это спецификация, основанная на стандартах XML для двумерной векторной графики. Это открытый стандарт, который разрабатывается Консорциумом World Wide Web (W3C) с 1999 года.

С момента выпуска v7.1.0,**Aspose.Cells for Java** может конвертировать рабочие листы в изображения SVG.

Чтобы использовать эту функцию, вам необходимо импортировать пространство имен com.aspose.cells в вашу программу или проект. Он имеет несколько полезных классов для рендеринга и печати, например,**[SheetRender] (https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**, **[ImageOrPrintOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**, **[WorkbookRender] (https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender)**, и другие.

**[com.aspose.cells.ImageOrPrintOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** class указывает, что рабочий лист будет сохранен в формате SVG.

**[SheetRender] (https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**класс принимает объект**[ImageOrPrintOptions] (https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** в качестве параметра, который задает формат сохранения в формате SVG.

В следующем фрагменте кода показано, как преобразовать рабочий лист в файле Excel в файл изображения SVG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Отобразить активный рабочий лист в рабочей книге**

Простой способ преобразовать активный рабочий лист в рабочую книгу — установить индекс активного листа, а затем сохранить рабочую книгу как SVG. Он отобразит активный лист в SVG. Следующий пример кода демонстрирует эту функцию:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## Статьи по Теме

- [Экспорт диаграммы в SVG с атрибутом viewBox](/cells/ru/java/export-chart-to-svg-with-viewbox-attribute/)
- [Экспорт рабочего листа или диаграммы в изображение с желаемой шириной и высотой](/cells/ru/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Преобразование рабочего листа в изображение и рабочего листа в изображение на странице](/cells/ru/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
