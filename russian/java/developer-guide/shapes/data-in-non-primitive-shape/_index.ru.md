---
title: Данные в не примитивной форме
type: docs
weight: 500
url: /ru/java/data-in-non-primitive-shape/
---

## **Доступ к данным не примитивной формы**

Иногда вам может потребоваться получить доступ к данным из формы, которая не встроена. Встроенные формы называют примитивными, а те, которых нет, называют не примитивными. Например, вы можете определить свои собственные формы, используя разные кривые соединенные линии.

## **Форма не примитивной формы**

В Aspose.Cells, не примитивным формам назначается тип [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT_PRIMITIVE). Вы можете проверить их тип, используя метод [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType).

Получите доступ к данным формы, используя метод [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths). Это возвращает все соединенные пути, которые составляют не примитивную форму. Эти пути имеют тип FormPath, который содержит список всех сегментов, которые в свою очередь содержат точки в каждом сегменте.

Ниже приведен фрагмент кода, демонстрирующий использование метода [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths) для доступа к информации о пути не примитивной формы.

**Показывает пример не примитивной формы** 

![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
