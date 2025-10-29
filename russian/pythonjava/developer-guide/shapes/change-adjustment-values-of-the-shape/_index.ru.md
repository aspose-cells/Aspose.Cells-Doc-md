---
title: Изменение значений коррекции формы
type: docs
weight: 2000
url: /ru/python-java/change-adjustment-values-of-the-shape/
---


{{% alert color="primary" %}}

Aspose.Cells для Python через Java предоставляет метод [**Shape.getGeometry().getShapeAdjustValues()**](https://reference.aspose.com/cells/python-java/asposecells.api/geometry#ShapeAdjustValues) для внесения изменений в точки регулировки с формами. В интерфейсе Microsoft Excel регулировки отображаются как жёлтые ромбовидные узлы. Например:

- У закругленного прямоугольника есть коррекция для изменения дуги
- У треугольника есть коррекция для изменения расположения вершины
- Трапеция имеет корректировку для изменения ширины верха
- У стрелок есть две коррекции для изменения формы головы и хвоста

Эта статья объяснит использование метода [**Shape.getGeometry().getShapeAdjustValues()**](https://reference.aspose.com/cells/python-java/asposecells.api/geometry#ShapeAdjustValues) для изменения значения настройки различных фигур.

{{% /alert %}}

## **Изменить значения корректировки**

В нижеприведенном образце кода показано, как изменить значения корректировки формы.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-ChangeShapesAdjustmentValues-1.py" >}}

## **Как задать или изменить точку подсказки RoundedRectangularCallout в Excel**

Следующий пример показывает, как задать или изменить позицию точки подсказки округлого прямоугольного вызова в Excel.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-ChangeShapesAdjustmentValues-2.py" >}}


{{< app/cells/assistant language="csharp" >}}
