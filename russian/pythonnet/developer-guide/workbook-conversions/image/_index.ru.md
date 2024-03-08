---
title: Image
type: docs
weight: 300
url: /ru/python-net/convert-excel-to-image/
description: Преобразуйте диаграмму в Image, используя Aspose.Cells for Python via .NET API.
keywords: Python Convert Chart to Image, Export Chart to Image in Python via NET, Python Save Chart to Image.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET позволяет экспортировать лист из книги и конвертировать его в различные форматы. В этой статье объясняется, как преобразовать лист в другие форматы.

{{% /alert %}}

##  Преобразование книги в TIFF

 Файл Excel может содержать несколько листов с несколькими страницами.[Рабочая КнигаВизуализация](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) позволяет конвертировать Excel в TIFF с несколькими страницами. Кроме того, вы можете управлять несколькими параметрами для TIFF, например[Сжатие](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), [Глубина цвета](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/), Разрешение([Горизонтальное разрешение](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [Вертикальное разрешение](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

 В следующем фрагменте кода показано, как преобразовать Excel в TIFF с несколькими страницами.[исходный файл Excel](workbook-to-tiff-with-mulitiple-pages.xlsx) и[сгенерировано изображение TIFF](workbook-to-tiff-with-mulitiple-pages.tiff) прилагаются для справки.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

##  **Преобразование рабочего листа в Image**

Рабочие листы содержат данные, которые вы хотите проанализировать. Например, рабочий лист может содержать параметры, итоговые значения, проценты, исключения и вычисления.

Как разработчику вам может потребоваться представить рабочие листы в виде изображений. Например, вам может потребоваться использовать изображение листа в приложении или на веб-странице. Возможно, вы захотите вставить изображение в документ Word Microsoft, файл PDF, презентацию PowerPoint или документ другого типа. Проще говоря, вы хотите, чтобы рабочий лист отображался как изображение, чтобы вы могли использовать его где-нибудь еще.

Aspose.Cells for Python via .NET поддерживает преобразование листов Excel в изображения. Чтобы использовать эту функцию, вам необходимо импортировать**[aspose.cells.rendering](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/)**пространство имен в вашу программу или проект. Он имеет несколько ценных классов для рендеринга и печати, например *[ЛистРендеринг](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**, *[Параметры изображения или печати](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/)**, *[Рабочая КнигаВизуализация](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/)**, и другие.

**[SheetRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**Класс представляет собой рабочий лист для визуализации в виде изображений. У него есть перегруженный метод, *[изображать](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str)**, который может преобразовать рабочий лист в файл(ы) изображения с различными атрибутами или параметрами. Он возвращает объект System.Drawing.Bitmap, и вы можете сохранить файл изображения на диск или в поток. Поддерживается несколько форматов изображений, например BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

В следующем фрагменте кода показано, как преобразовать лист из файла Excel в файл изображения.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

В настоящее время программа API для преобразования листов в изображения не поддерживает пузырьковые 3D-диаграммы.

{{% /alert %}}

##  **Преобразование рабочего листа в SVG**

SVG означает масштабируемую векторную графику. SVG — это спецификация, основанная на стандартах XML для двумерной векторной графики. Это открытый стандарт, который разрабатывается Консорциумом Всемирной паутины (W3C) с 1999 года.

Aspose.Cells for Python via .NET может конвертировать рабочие листы в изображение SVG начиная с версии 7.1.0. В следующем фрагменте кода показано, как преобразовать лист из файла Excel в файл изображения SVG.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

##  **Предварительные темы**
- [Преобразование диаграммы Excel в Image](/cells/ru/python-net/convert-an-excel-chart-to-image/)
- [Преобразование диаграммы в Image в формате SVG](/cells/ru/python-net/converting-chart-to-image-in-svg-format/)
- [Экспортировать диаграмму в номер SVG с атрибутом viewBox.](/cells/ru/python-net/export-chart-to-svg-with-viewbox-attribute/)
