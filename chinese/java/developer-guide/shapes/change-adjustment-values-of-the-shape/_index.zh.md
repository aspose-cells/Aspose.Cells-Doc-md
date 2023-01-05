---
title: 更改形状的调整值
type: docs
weight: 3200
url: /zh/java/change-adjustment-values-of-the-shape/
---
{{% alert color="primary" %}} 

Aspose.Cells提供[Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues)属性来更改形状的调整点。在 Microsoft Excel UI 中，调整显示为黄色菱形节点。例如：

- 圆角矩形有个调整改变圆弧
- 三角形有一个调整改变点的位置
- 一个梯形有一个调整来改变顶部的宽度
- 箭头有两个调整来改变头部和尾部的形状

本文将解释使用[Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues)属性改变不同形状的调整值。

{{% /alert %}} 
## **更改形状的调整值**
以下示例代码访问源 Excel 文件中第一个工作表的前三个形状，然后更改形状的调整值。下面的屏幕截图显示了更改调整值之前和更改调整值之后形状的外观。
### **更改调整值之前绘制形状**
![待办事项：图片_替代_文本](change-adjustment-values-of-the-shape_1.png)
### **更改调整值后绘制形状**
![待办事项：图片_替代_文本](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
