---
title: Установить шрифт по умолчанию при рендеринге электронной таблицы в изображения
type: docs
weight: 360
url: /ru/net/set-default-font-while-rendering-spreadsheet-to-images/
---
{{% alert color="primary" %}}

 Пожалуйста, используйте[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) для установки шрифта по умолчанию при преобразовании электронных таблиц в изображения. Это свойство будет эффективным только в том случае, если шрифт рабочей книги по умолчанию не может отображать ваши символы. Шрифт по умолчанию, указанный с помощью[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) свойство используется для всех тех ячеек, которые имеют недопустимые или несуществующие шрифты.

{{% /alert %}}

## Установить шрифт по умолчанию при рендеринге электронной таблицы в изображения

В следующем примере кода создается рабочая книга, добавляется текст в ячейку A4 первого рабочего листа и задается недопустимый или несуществующий шрифт. Затем он берет два изображения рабочего листа. Первое изображение делается путем установки[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) собственность на*Новый Курьер* а второе изображение делается путем установки[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) собственность на*Таймс Нью Роман*.

 Это выходное изображение после установки[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) собственность на*Новый Курьер*.

![дело:изображение_альтернативный_текст](set-default-font-while-rendering-spreadsheet-to-images_1.png)

 Это выходное изображение после установки[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) собственность на*Таймс Нью Роман*.

![дело:изображение_альтернативный_текст](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Образец кода

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}
