---
title: Повернуть текст с фигурой внутри таблицы
type: docs
weight: 1300
url: /ru/net/rotate-text-with-shape-inside-the-worksheet/
---

## **Возможные сценарии использования**

Вы можете добавить текст внутри любой формы с помощью Microsoft Excel. Если вы добавляете форму с помощью очень старой версии Microsoft Excel 2003, то текст не будет поворачиваться вместе с формой. Но если вы добавляете форму с более новыми версиями Microsoft Excel, например 2007, 2010, 2013 или 2016, и т.д., то текст будет поворачиваться вместе с формой. Вы можете контролировать, должен ли текст поворачиваться вместе с формой или нет, используя свойство [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape). Значение по умолчанию - **true**, что означает, что текст будет поворачиваться вместе с формой, но если вы установите его как **false**, то текст не будет поворачиваться вместе с формой.

## **Повернуть текст с фигурой внутри таблицы**

Приведенный нижеследующий образец кода загружает [образец Excel файла](64716896.xlsx), в котором есть форма треугольника, и его текст вращается вместе с формой. Если вы откроете образец Excel файла в Microsoft Excel и повернете форму треугольника, текст также будет поворачиваться вместе с ним. Затем код устанавливает свойство [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) как **false** и сохраняет его в [файле вывода Excel](64716897.xlsx). Если вы теперь откроете файл вывода Excel в Microsoft Excel и повернете форму треугольника, текст не будет вращаться вместе с ним. Пожалуйста, ознакомьтесь со следующим снимком экрана, показывающим эффект кода на образце Excel файла в качестве справки.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-RotateTextWithShapeInsideWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
