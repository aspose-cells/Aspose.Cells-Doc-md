---
title: Установить шрифт по умолчанию при преобразовании электронной таблицы в изображения
type: docs
weight: 360
url: /ru/python-net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

Используйте свойство [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font), чтобы установить шрифт по умолчанию при рендеринге электронных таблиц в изображения. Это свойство будет действительным только в том случае, если шрифт по умолчанию книги не может отобразить ваши символы. Шрифт по умолчанию, указанный с помощью свойства [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font), используется для всех тех ячеек, которые имеют недопустимые или отсутствующие шрифты.

{{% /alert %}}

## Установка шрифта по умолчанию при рендеринге электронных таблиц в изображения

Приведенный ниже образец кода создает книгу, добавляет текст в ячейку A4 первого рабочего листа и устанавливает его шрифт на недопустимый или отсутствующий шрифт. Затем он создает два изображения рабочего листа. Первое изображение создается, установив свойство [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) на *Courier New* и второе изображение создается, установив свойство [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) на *Times New Roman*.

Это выходное изображение после установки свойства [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) на *Courier New*.

![todo:image_alt_text](1.png)

Это выходное изображение после установки свойства [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) на *Times New Roman*.

![todo:image_alt_text](2.png)

## Образец кода

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}

