---
title: Изменение значений коррекции формы
type: docs
weight: 3200
url: /ru/java/change-adjustment-values-of-the-shape/
---

{{% alert color="primary" %}} 

Aspose.Cells предоставляет свойство [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) для внесения изменений в точки коррекции формы. В пользовательском интерфейсе Microsoft Excel корректировки отображаются в виде желтых алмазных узлов. Например:

- У закругленного прямоугольника есть коррекция для изменения дуги
- У треугольника есть коррекция для изменения расположения вершины
- У трапеции есть коррекция для изменения ширины верхней стороны
- У стрелок есть две коррекции для изменения формы головы и хвоста

В данной статье будет объяснено, как использовать свойство [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) для изменения коррекции различных форм.

{{% /alert %}} 
## **Изменение значений коррекции формы**
В следующем образце кода осуществляется доступ к первым трём формам первого листа в исходном файле Excel, а затем изменяются значения коррекции форм. Ниже приведены снимки экрана, показывающие, как выглядят формы до изменения значений коррекции и после этого.
### **Рисование форм до изменения значений коррекции**
![todo:image_alt_text](change-adjustment-values-of-the-shape_1.png)
### **Рисование форм после изменения значений коррекции**
![todo:image_alt_text](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
