---
title: Преобразование Excel в изображение с помощью Golang через C++
linktitle: Преобразовать Excel в изображение
type: docs
weight: 300
url: /ru/go-cpp/convert-excel-to-image/
description: Узнайте, как преобразовать рабочие листы Excel в изображения, включая форматы TIFF и SVG, с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет экспортировать лист из книги Excel и преобразовать его в различные форматы. В этой статье объясняется, как преобразовать лист в различные форматы.

{{% /alert %}}

## Преобразование книги в TIFF

Файл Excel может содержать несколько листов с несколькими страницами. [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/) позволяет преобразовать Excel в TIFF с несколькими страницами. Также вы можете контролировать несколько вариантов для TIFF, такие как [Сжатие](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/), [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/), Разрешение ([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/), [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).

В следующем фрагменте кода показано, как конвертировать Excel в TIFF с несколькими страницами. [Исходный файл Excel](workbook-to-tiff-with-mulitiple-pages.xlsx) и [созданное изображение TIFF](workbook-to-tiff-with-mulitiple-pages.tiff) приложены для вашего справки.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image.go" >}}
## **Преобразование Рабочего листа в изображение**

Рабочие листы содержат данные, которые вы хотите проанализировать. Например, рабочий лист может содержать параметры, итоги, проценты, исключения и вычисления.

Как разработчик вам может понадобиться представить рабочие листы в виде изображений. Например, вам может потребоваться использовать изображение рабочего листа в приложении или на веб-странице. Вам может понадобиться вставить изображение в документ Microsoft Word, файл PDF, презентацию PowerPoint или в другой тип документа. Просто говоря, вам нужно, чтобы рабочий лист был отображен в виде изображения, чтобы вы могли его использовать в другом месте.

Aspose.Cells поддерживает преобразование листов Excel в изображения. Для использования этой функции необходимо импортировать пространство имён [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/go-cpp/) в вашу программу или проект. В нем есть несколько полезных классов для рендеринга и печати, например [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/) и другие.

Класс [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/) представляет собой лист для рендеринга в виде изображений. В нем есть перегруженный метод [**ToImage**](https://reference.aspose.com/cells/go-cpp/sheetrender/toimage/), который может преобразовать лист в один или несколько файлов изображений с разными атрибутами или опциями. Он возвращает объект `System.Drawing.Bitmap`, и вы можете сохранить изображение в файл или поток. Поддерживаются несколько форматов изображений, например BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Ниже приведен фрагмент кода, демонстрирующий, как преобразовать рабочий лист в Excel-файле в файл изображения.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-1.go" >}}
{{% alert color="primary" %}}

В настоящее время API для преобразования листов в изображения не поддерживает 3D-графики в виде пузырьков.

{{% /alert %}}

## **Преобразование Рабочего листа в SVG**

SVG означает масштабируемую векторную графику. SVG является спецификацией на основе стандартов XML для двумерной векторной графики. Это открытый стандарт, над разработкой которого работает Консорциум Всемирной паутины (W3C) с 1999 года.

Aspose.Cells for C++ поддерживает преобразование листов в SVG изображения с версии 7.1.0. Следующий пример показывает, как преобразовать лист из файла Excel в SVG изображение.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-2.go" >}}
## **Продвинутые темы**
- [Конвертировать диаграмму Excel в изображение](/cells/ru/cpp/convert-an-excel-chart-to-image/)
- [Преобразование диаграммы в изображение в формате SVG](/cells/ru/cpp/converting-chart-to-image-in-svg-format/)
- [Экспорт диаграммы в SVG с атрибутом viewBox](/cells/ru/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [Отслеживание процесса преобразования Excel в TIFF](/cells/ru/cpp/track-conversion-progress-of-excel-to-tiff/)
