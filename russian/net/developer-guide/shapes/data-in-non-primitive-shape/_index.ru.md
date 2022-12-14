---
title: Данные в непримитивной форме
type: docs
weight: 300
url: /ru/net/data-in-non-primitive-shape/
---
## **Доступ к данным не примитивной формы**

Иногда вам нужно получить доступ к данным из фигуры, которая не встроена. Встроенные фигуры называются примитивными фигурами; те, которые не называются непримитивными. Например, вы можете определить свои собственные формы, используя различные кривые, соединенные линиями.

## **Непримитивная форма**

 В Aspose.Cells непримитивным формам присваивается тип[**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype) . Вы можете проверить их тип с помощью[**Форма.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype)имущество.

 Доступ к данным формы с помощью[**Форма.Пути**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths)имущество. Он возвращает все связанные пути, которые составляют не примитивную форму. Эти пути относятся к типу[**Путь формы**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath)который содержит список всех сегментов, которые, в свою очередь, содержат точки в каждом сегменте.

|**Показывает пример непримитивной формы**|
|:- |
|![дело:изображение_альтернативный_текст](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
