---
title: Размещение изображения в качестве текстуры внутри формы
type: docs
weight: 1700
url: /ru/python-net/tile-picture-as-a-texture-inside-the-shape/
---

## **Возможные сценарии использования**

Когда изображение маленькое и не покрывает всю поверхность формы без потери качества, то у вас есть возможность повторить его. Повторение заполняет поверхность формы маленьким изображением, повторяя их, как плитку.

## **Текстурное изображение внутри формы**

Вы можете заполнить поверхность фигуры некоторым изображением и наложить на нее плитки, используя свойство [**Shape.fill.texture_fill.is_tiling**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/texturefill/is_tiling) и установить его **true**. Пожалуйста, ознакомьтесь с следующим образцом кода, [образцом файла Excel](46465050.xlsx), а также снимком экрана для справки.

## **Снимок экрана**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Options-TilePictureAsTextureInsideShape.py" >}}
{{< app/cells/assistant language="python-net" >}}
