---
title: 更改形状的调整值
type: docs
weight: 3200
url: /zh/java/change-adjustment-values-of-the-shape/
---

{{% alert color="primary" %}} 

Aspose.Cells提供[Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues)属性以更改形状的调整点。在Microsoft Excel UI中，调整显示为黄色菱形节点。例如：

- 圆角矩形有一个调整来改变拱形
- 三角形有一个调整来改变顶点的位置
- 梯形有一个调整来改变顶部的宽度
- 箭头有两个调整，可改变箭头头部和尾部的形状

本文将解释如何使用[Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) 属性来改变不同形状的调整值。

{{% /alert %}} 
## **改变形状的调整值**
以下示例代码访问源Excel文件中第一个工作表的前三个形状，然后更改形状的调整值。下面的屏幕截图显示在更改调整值之前形状的外观以及在更改调整值之后的外观。
### **更改调整值之前的绘图形状**
![todo:image_alt_text](change-adjustment-values-of-the-shape_1.png)
### **更改调整值之后的绘图形状**
![todo:image_alt_text](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
{{< app/cells/assistant language="java" >}}
