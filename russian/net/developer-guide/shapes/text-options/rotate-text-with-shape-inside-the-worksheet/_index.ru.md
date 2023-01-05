---
title: Поворот текста с фигурой внутри рабочего листа
type: docs
weight: 1300
url: /ru/net/rotate-text-with-shape-inside-the-worksheet/
---
## **Возможные сценарии использования**

Вы можете добавить текст внутрь любой фигуры, используя Microsoft Excel. Если вы добавите фигуру, используя очень старый Microsoft Excel 2003, то текст не будет вращаться вместе с фигурой. Но если вы добавите фигуру, используя более новые версии Microsoft Excel, например, 2007, 2010, 2013 или 2016 и т. д., тогда текст будет вращаться вместе с формой. Вы можете контролировать, должен ли текст вращаться вместе с фигурой или нет, используя[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) имущество. Его значение по умолчанию равно**истинный**что означает, что текст будет вращаться вместе с формой, но если вы установите его как**ЛОЖЬ**, то текст не будет вращаться вместе с формой.

## **Поворот текста с фигурой внутри рабочего листа**

 Следующий пример кода загружает[образец файла Excel](64716896.xlsx) который имеет треугольную форму, а его текст вращается вместе с формой. Если вы откроете образец файла Excel в Microsoft Excel и повернете треугольную фигуру, текст также будет вращаться вместе с ней. Затем код устанавливает[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) собственность как**ЛОЖЬ** и сохраняет его как[выходной файл Excel](64716897.xlsx). Если теперь вы откроете выходной файл Excel в Microsoft Excel и повернете треугольную фигуру, текст не будет вращаться вместе с ней. См. следующий снимок экрана, показывающий влияние кода на пример файла Excel для справки.

![дело:изображение_альтернативный_текст](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-RotateTextWithShapeInsideWorksheet.cs" >}}
