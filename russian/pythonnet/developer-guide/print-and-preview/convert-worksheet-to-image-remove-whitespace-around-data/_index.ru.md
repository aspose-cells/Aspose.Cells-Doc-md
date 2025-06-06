---
title: Преобразование электронной таблицы в изображение  удалите пустое пространство вокруг данных
type: docs
weight: 40
url: /ru/python-net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

Иногда требуется отображать изображения листов в приложениях или веб-страницах. Например, нужно вставить изображения в документ Word, PDF-файл, презентацию PowerPoint или другой документ. В основном, необходимо отображать лист как изображение для вставки в другие приложения. API Aspose.Cells for Python via .NET позволяет конвертировать листы Microsoft Excel в изображения.

{{% /alert %}}

## **Удалите пустое пространство вокруг данных**

[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) API преобразует электронную таблицу в файл изображения с любыми указанными атрибутами, например, формат изображения, пагинированные листы и т.д. Поддерживается несколько форматов изображений, включая BMP, GIF, JPG, TIFF и EMF.

Когда вы используете функцию преобразования листа в изображение, выходное изображение по умолчанию имеет пустое пространство, то есть рамку вокруг нее. Вы можете удалить это, установив верхние, нижние, левые и правые поля макета страницы для исходного листа электронной таблицы на 0 и задав соответствующие [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) атрибуты.

Следующий фрагмент кода удаляет пустое пространство вокруг данных на выходном изображении.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RemoveWhitespaceAroundData-1.py" >}}

