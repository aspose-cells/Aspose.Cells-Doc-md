---
title: Изменить значения настройки формы
type: docs
weight: 3200
url: /ru/java/change-adjustment-values-of-the-shape/
---
{{% alert color="primary" %}} 

 Aspose.Cells предоставляет[Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) свойство для внесения изменений в точки настройки с фигурами. В пользовательском интерфейсе Excel Microsoft корректировки отображаются в виде желтых ромбовидных узлов. Например:

- Прямоугольник со скругленными углами имеет настройку для изменения дуги.
- Треугольник имеет корректировку для изменения положения точки
- Трапеция имеет регулировку для изменения ширины верха.
- Стрелы имеют две регулировки для изменения формы головы и хвоста.

 В этой статье объясняется использование[Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) свойство, чтобы изменить значение настройки различных фигур.

{{% /alert %}} 
## **Изменить значения настройки формы**
Следующий пример кода обращается к первым трем фигурам первого рабочего листа в исходном файле Excel, а затем изменяет значения настройки фигур. На приведенных ниже снимках экрана показано, как выглядят фигуры до изменения значений настройки, а затем после изменения значений настройки.
### **Рисование фигур перед изменением значений настройки**
![дело:изображение_альтернативный_текст](change-adjustment-values-of-the-shape_1.png)
### **Рисование фигур после изменения значений настройки**
![дело:изображение_альтернативный_текст](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
