---
title: Повернуть текст с фигурой внутри таблицы
type: docs
weight: 110
url: /ru/java/rotate-text-with-shape-inside-the-worksheet/
---

## **Возможные сценарии использования**

Вы можете добавить текст в любую форму с помощью Microsoft Excel. Если вы добавляете форму с помощью очень старой версии Microsoft Excel 2003, то текст не будет вращаться вместе с формой. Но если добавляете форму, используя более новые версии Microsoft Excel, например 2007, 2010, 2013 или 2016, и т. д., то текст будет вращаться вместе с формой. Вы можете управлять тем, должен ли текст вращаться вместе с формой или нет, используя свойство [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape). Значение по умолчанию - **true**, что означает, что текст будет вращаться вместе с формой, но если вы установите его как **false**, то текст не будет вращаться вместе с формой.

## **Повернуть текст с фигурой внутри таблицы**

Приведенный ниже образец кода загружает [примерный файл Excel](64716919.xlsx), в котором есть фигура треугольника, и ее текст вращается вместе с формой. Если вы откроете примерный файл Excel в Microsoft Excel и повернете форму треугольника, текст также повернется вместе с ней. Затем код устанавливает свойство [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape) как **false** и сохраняет его как [выходной файл Excel](64716917.xlsx). Если теперь откроете выходной файл Excel в Microsoft Excel и повернете форму треугольника, текст не повернется вместе с ней. Пожалуйста, посмотрите следующий скриншот, показывающий эффект кода на примерном файле Excel в качестве ссылки.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-RotateTextWithShapeInsideWorksheet.java" >}}
