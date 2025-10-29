---
title: Данные в неprimitive форме с помощью Golang через C++
linktitle: Данные в не примитивной форме
type: docs
weight: 300
url: /ru/go-cpp/data-in-non-primitive-shape/
description: Получение и управление данными в непредметных фигурах с помощью Aspose.Cells на Golang через C++.
---

## **Доступ к данным не примитивной формы**

Иногда вам может потребоваться получить доступ к данным из формы, которая не встроена. Встроенные формы называют примитивными, а те, которых нет, называют не примитивными. Например, вы можете определить свои собственные формы, используя разные кривые соединенные линии.

## **Форма не примитивной формы**

В Aspose.Cells нетипичным формам присваивается тип [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/go-cpp/autoshapetype/). Вы можете проверить их тип, используя свойство [**Shape.AutoShapeType**](https://reference.aspose.com/cells/go-cpp/autoshapetype/).

Доступ к данным формы с использованием свойства [**Shape.GetPaths()**](https://reference.aspose.com/cells/go-cpp/shape/getpaths/). Оно возвращает все связанные пути, составляющие нетипичную форму. Эти пути имеют тип [**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/) и содержат список всех сегментов, в свою очередь содержащих точки в каждом сегменте.

|**Показывает пример нетипичной формы**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataInNonPrimitiveShape.go" >}}
