---
title: Изображение
type: docs
weight: 300
url: /ru/python-net/convert-excel-to-image/
description: Конвертировать график в изображение с помощью Aspose.Cells для Python via .NET API.
keywords: Python Конвертировать график в изображение, Экспортировать график в изображение в Python via NET, Python Сохранить график в изображение.
---


{{% alert color="primary" %}}

Aspose.Cells для Python via .NET позволяет экспортировать рабочий лист из книги и конвертировать его в различные форматы. В этой статье объясняется, как сконвертировать рабочий лист в различные форматы.

{{% /alert %}}

## Преобразование книги в TIFF

Файл Excel может содержать несколько листов с несколькими страницами. [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) позволяет вам конвертировать Excel в TIFF с несколькими страницами. Также вы можете управлять несколькими параметрами для TIFF, такими как [Сжатие](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), [Глубина цвета](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/), Разрешение ([Горизонтальное разрешение](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [Вертикальное разрешение](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

В следующем фрагменте кода показано, как конвертировать Excel в TIFF с несколькими страницами. [Исходный файл Excel](workbook-to-tiff-with-mulitiple-pages.xlsx) и [созданное изображение TIFF](workbook-to-tiff-with-mulitiple-pages.tiff) приложены для вашего справки.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

## **Преобразование Рабочего листа в изображение**

Рабочие листы содержат данные, которые вы хотите проанализировать. Например, рабочий лист может содержать параметры, итоги, проценты, исключения и вычисления.

Как разработчик вам может понадобиться представить рабочие листы в виде изображений. Например, вам может потребоваться использовать изображение рабочего листа в приложении или на веб-странице. Вам может понадобиться вставить изображение в документ Microsoft Word, файл PDF, презентацию PowerPoint или в другой тип документа. Просто говоря, вам нужно, чтобы рабочий лист был отображен в виде изображения, чтобы вы могли его использовать в другом месте.

Aspose.Cells для Python via .NET поддерживает конвертацию листов Excel в изображения. Чтобы использовать эту функцию, вам нужно импортировать пространство имен [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/) в свою программу или проект. Он содержит несколько ценных классов для рендеринга и печати, например [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/), и другие.

Класс [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) представляет лист, который нужно преобразовать в изображения. Он имеет перегруженный метод [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str), который может конвертировать лист в файл(ы) изображения с различными атрибутами или опциями. Он возвращает объект System.Drawing.Bitmap и вы можете сохранить файл изображения на диск или поток. Поддерживаются несколько форматов изображений, таких как BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Ниже приведен фрагмент кода, демонстрирующий, как преобразовать рабочий лист в Excel-файле в файл изображения.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

В настоящее время API для преобразования листов в изображения не поддерживает 3D-графики в виде пузырьков.

{{% /alert %}}

## **Преобразование Рабочего листа в SVG**

SVG означает масштабируемую векторную графику. SVG является спецификацией на основе стандартов XML для двумерной векторной графики. Это открытый стандарт, над разработкой которого работает Консорциум Всемирной паутины (W3C) с 1999 года.

Aspose.Cells для Python via .NET смог конвертировать рабочие листы в изображения SVG с версии 7.1.0. Приведенный ниже фрагмент кода показывает, как конвертировать рабочий лист в Excel файле в файл изображения SVG.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

## **Продвинутые темы**
- [Конвертировать диаграмму Excel в изображение](/cells/ru/python-net/convert-an-excel-chart-to-image/)
- [Преобразование диаграммы в изображение в формате SVG](/cells/ru/python-net/converting-chart-to-image-in-svg-format/)
- [Экспорт диаграммы в SVG с атрибутом viewBox](/cells/ru/python-net/export-chart-to-svg-with-viewbox-attribute/)
