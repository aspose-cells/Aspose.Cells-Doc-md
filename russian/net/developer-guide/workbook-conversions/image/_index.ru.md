---
title: Изображение
type: docs
weight: 300
url: /ru/net/convert-excel-to-image/
---


{{% alert color="primary" %}}

Aspose.Cells позволяет экспортировать лист из книги Excel и преобразовать его в различные форматы. В этой статье объясняется, как преобразовать лист в различные форматы.

{{% /alert %}}

## Преобразование книги в TIFF

Файл Excel может содержать несколько листов с несколькими страницами. [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) позволяет преобразовывать Excel в TIFF с несколькими страницами. Также можно контролировать несколько опций для TIFF, такие как [Сжатие](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [Глубина цвета](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth), Разрешение ([Горизонтальное разрешение](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [Вертикальное разрешение](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

В следующем фрагменте кода показано, как конвертировать Excel в TIFF с несколькими страницами. [Исходный файл Excel](workbook-to-tiff-with-mulitiple-pages.xlsx) и [созданное изображение TIFF](workbook-to-tiff-with-mulitiple-pages.tiff) приложены для вашего справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **Преобразование Рабочего листа в изображение**

Рабочие листы содержат данные, которые вы хотите проанализировать. Например, рабочий лист может содержать параметры, итоги, проценты, исключения и вычисления.

Как разработчик вам может понадобиться представить рабочие листы в виде изображений. Например, вам может потребоваться использовать изображение рабочего листа в приложении или на веб-странице. Вам может понадобиться вставить изображение в документ Microsoft Word, файл PDF, презентацию PowerPoint или в другой тип документа. Просто говоря, вам нужно, чтобы рабочий лист был отображен в виде изображения, чтобы вы могли его использовать в другом месте.

Aspose.Cells поддерживает преобразование листов Excel в изображения. Для использования этой функции вам нужно импортировать пространство имен [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) в свою программу или проект. Оно имеет несколько ценных классов для рендеринга и печати, например [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) и другие.

Класс [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) представляет лист, который нужно преобразовать в изображения. Он имеет перегруженный метод [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index), который может конвертировать лист в файл(ы) изображения с различными атрибутами или опциями. Он возвращает объект System.Drawing.Bitmap и вы можете сохранить файл изображения на диск или поток. Поддерживаются несколько форматов изображений, таких как BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Ниже приведен фрагмент кода, демонстрирующий, как преобразовать рабочий лист в Excel-файле в файл изображения.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

В настоящее время API для преобразования листов в изображения не поддерживает 3D-графики в виде пузырьков.

{{% /alert %}}

## **Преобразование Рабочего листа в SVG**

SVG означает масштабируемую векторную графику. SVG является спецификацией на основе стандартов XML для двумерной векторной графики. Это открытый стандарт, над разработкой которого работает Консорциум Всемирной паутины (W3C) с 1999 года.

С версии 7.1.0 Aspose.Cells for .NET смог конвертировать рабочие листы в изображения SVG. В следующем фрагменте кода показано, как конвертировать рабочий лист в файл изображения SVG из файла Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **Продвинутые темы**
- [Конвертировать диаграмму Excel в изображение](/cells/ru/net/convert-an-excel-chart-to-image/)
- [Преобразование диаграммы в изображение в формате SVG](/cells/ru/net/converting-chart-to-image-in-svg-format/)
- [Экспорт диаграммы в SVG с атрибутом viewBox](/cells/ru/net/export-chart-to-svg-with-viewbox-attribute/)
- [Отслеживание процесса преобразования Excel в TIFF](/cells/ru/net/track-conversion-progress-of-excel-to-tiff/)
{{< app/cells/assistant language="csharp" >}}
