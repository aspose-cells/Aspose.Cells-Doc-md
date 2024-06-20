---
title: Данные в не примитивной форме
type: docs
weight: 300
url: /ru/net/data-in-non-primitive-shape/
---

## **Доступ к данным не примитивной формы**

Иногда вам может потребоваться получить доступ к данным из формы, которая не встроена. Встроенные формы называют примитивными, а те, которых нет, называют не примитивными. Например, вы можете определить свои собственные формы, используя разные кривые соединенные линии.

## **Форма не примитивной формы**

В Aspose.Cells нетипичным формам присваивается тип [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype). Вы можете проверить их тип, используя свойство [**Shape.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype).

Доступ к данным формы с использованием свойства [**Shape.Paths**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths). Оно возвращает все связанные пути, составляющие нетипичную форму. Эти пути имеют тип [**ShapePath**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath) и содержат список всех сегментов, в свою очередь содержащих точки в каждом сегменте.

|**Показывает пример нетипичной формы**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
