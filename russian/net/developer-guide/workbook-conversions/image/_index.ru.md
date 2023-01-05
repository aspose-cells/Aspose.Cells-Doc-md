---
title: Изображение
type: docs
weight: 300
url: /ru/net/convert-excel-to-image/
---
{{% alert color="primary" %}}

Aspose.Cells позволяет экспортировать рабочий лист из рабочей книги и преобразовывать его в различные форматы. В этой статье объясняется, как преобразовать рабочий лист в различные форматы.

{{% /alert %}}

## Преобразование книги в TIFF

 Файл Excel может содержать несколько листов с несколькими страницами.[Рабочая книгаВизуализация](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) позволяет конвертировать Excel в TIFF с несколькими страницами. Кроме того, вы можете управлять несколькими параметрами для TIFF, например[Сжатие](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [Глубина цвета](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth), Разрешение([Горизонтальное разрешение](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [Вертикальное разрешение](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

 В следующем фрагменте кода показано, как преобразовать Excel в TIFF с несколькими страницами.[исходный файл Excel](workbook-to-tiff-with-mulitiple-pages.xlsx) и[сгенерировано TIFF изображение](workbook-to-tiff-with-mulitiple-pages.tiff) прилагаются для справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **Преобразование рабочего листа в изображение**

Рабочие листы содержат данные, которые вы хотите проанализировать. Например, рабочий лист может содержать параметры, итоги, проценты, исключения и расчеты.

Как разработчику, вам может понадобиться представить рабочие листы в виде изображений. Например, вам может понадобиться использовать изображение рабочего листа в приложении или на веб-странице. Вы можете вставить изображение в документ Word Microsoft, файл PDF, презентацию PowerPoint или документ другого типа. Проще говоря, вы хотите, чтобы рабочий лист отображался как изображение, чтобы вы могли использовать его где-то еще.

Aspose.Cells поддерживает преобразование листов Excel в изображения. Чтобы использовать эту функцию, вам необходимо импортировать**[Aspose.Cells.Rendering](https://reference.aspose.com/cells/net/aspose.cells.rendering)** пространство имен для вашей программы или проекта. Он имеет несколько полезных классов для рендеринга и печати, например**[SheetRender] (https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)**, **[ImageOrPrintOptions] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, **[WorkbookRender] (https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)**, и другие.

**[SheetRender] (https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)** класс представляет рабочий лист для отображения в виде изображений. Он имеет перегруженный метод,**[ToImage] (https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)**который может преобразовать рабочий лист в файл(ы) изображения с различными атрибутами или параметрами. Он возвращает объект System.Drawing.Bitmap, и вы можете сохранить файл изображения на диск или в поток. Поддерживаются несколько форматов изображений, например BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

В следующем фрагменте кода показано, как преобразовать рабочий лист в файле Excel в файл изображения.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

В настоящее время API для преобразования рабочих листов в изображения не поддерживает трехмерные пузырьковые диаграммы.

{{% /alert %}}

## **Преобразование рабочего листа в SVG**

SVG означает Масштабируемая векторная графика. SVG — это спецификация, основанная на стандартах XML для двумерной векторной графики. Это открытый стандарт, который разрабатывается Консорциумом World Wide Web (W3C) с 1999 года.

Aspose.Cells for .NET смог преобразовать рабочие листы в изображение SVG, начиная с версии 7.1.0. В следующем фрагменте кода показано, как преобразовать рабочий лист в файле Excel в файл изображения SVG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **Предварительные темы**
- [Преобразование диаграммы Excel в изображение](/cells/ru/net/convert-an-excel-chart-to-image/)
- [Преобразование диаграммы в изображение в формате SVG](/cells/ru/net/converting-chart-to-image-in-svg-format/)
- [Экспорт диаграммы в SVG с атрибутом viewBox](/cells/ru/net/export-chart-to-svg-with-viewbox-attribute/)
- [Отслеживание процесса преобразования Excel в TIFF](/cells/ru/net/track-conversion-progress-of-excel-to-tiff/)
