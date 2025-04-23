---
title: Установить шрифт по умолчанию при преобразовании электронной таблицы в изображения
type: docs
weight: 360
url: /ru/net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

Используйте свойство [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont), чтобы установить шрифт по умолчанию при рендеринге электронных таблиц в изображения. Это свойство будет действительным только в том случае, если шрифт по умолчанию книги не может отобразить ваши символы. Шрифт по умолчанию, указанный с помощью свойства [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont), используется для всех тех ячеек, которые имеют недопустимые или отсутствующие шрифты.

{{% /alert %}}

## Установка шрифта по умолчанию при рендеринге электронных таблиц в изображения

Приведенный ниже образец кода создает книгу, добавляет текст в ячейку A4 первого рабочего листа и устанавливает его шрифт на недопустимый или отсутствующий шрифт. Затем он создает два изображения рабочего листа. Первое изображение создается, установив свойство [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) на *Courier New* и второе изображение создается, установив свойство [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) на *Times New Roman*.

Это выходное изображение после установки свойства [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) на *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Это выходное изображение после установки свойства [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) на *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Образец кода

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
