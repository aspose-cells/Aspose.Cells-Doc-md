---
title: Данные в непримитивной форме
type: docs
weight: 500
url: /ru/java/data-in-non-primitive-shape/
---
## **Доступ к данным не примитивной формы**

Иногда вам нужно получить доступ к данным из фигуры, которая не встроена. Встроенные фигуры называются примитивными фигурами; те, которые не называются непримитивными. Например, вы можете определить свои собственные формы, используя различные кривые, соединенные линиями.

## **Непримитивная форма**

В Aspose.Cells непримитивным формам присваивается тип[**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT_PRIMITIVE) . Вы можете проверить их тип с помощью[**Форма.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType)метод.

 Доступ к данным формы с помощью[**Форма.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)метод. Он возвращает все связанные пути, которые составляют не примитивную форму. Эти пути относятся к типу ShapePath, который содержит список всех сегментов, которые, в свою очередь, содержат точки в каждом сегменте.

Следующий фрагмент кода демонстрирует использование[**Форма.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)метод для доступа к информации о пути не примитивной формы.

**Показывает пример непримитивной формы** 

![дело:изображение_альтернативный_текст](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
