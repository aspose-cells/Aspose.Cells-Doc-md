---
title: Данные в не примитивной форме
type: docs
weight: 300
url: /ru/python-net/data-in-non-primitive-shape/
description: Эта статья показывает отображение данных в Непримитивной форме через API Aspose.Cells для Python via .NET.
keywords: Библиотека для Excel на Python, Данные в Непримитивной форме на Python, как получить доступ к данным Непримитивной формы на Python.
---

## **Доступ к данным не примитивной формы**

Иногда вам может потребоваться получить доступ к данным из формы, которая не встроена. Встроенные формы называют примитивными, а те, которых нет, называют не примитивными. Например, вы можете определить свои собственные формы, используя разные кривые соединенные линии.

## **Форма не примитивной формы**

В Aspose.Cells для Python via .NET, непримитивные формы имеют тип [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/autoshapetype). Вы можете проверить их тип, используя свойство [**Shape.auto_shape_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/auto_shape_type).

Доступ к данным формы с использованием свойства [**Shape.paths**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/paths). Оно возвращает все связанные пути, составляющие нетипичную форму. Эти пути имеют тип [**ShapePath**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapepath) и содержат список всех сегментов, в свою очередь содержащих точки в каждом сегменте.

|**Показывает пример нетипичной формы**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-AccessNonPrimitiveShape-1.py" >}}
