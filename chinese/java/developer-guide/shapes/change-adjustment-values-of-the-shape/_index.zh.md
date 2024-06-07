---
title: 修改形状的调整值
type: docs
weight: 3200
url: /zh/java/change-adjustment-values-of-the-shape/
---

{{% alert color="primary" %}} 

Aspose.Cells提供[Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues)属性，以更改形状的调整点。在Microsoft Excel UI中，调整显示为黄色菱形节点。例如：

- 圆角矩形具有改变圆弧的调整
- 三角形具有改变指针位置的调整
- 梯形具有调整宽度的调整
- 箭头有两个调整设置，可以改变头部和尾部的形状

本文将解释[Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues)属性的用法，以更改不同形状的调整值。

{{% /alert %}} 
## **更改形状的调整值**
以下示例代码访问了源Excel文件中第一个工作表的前三个形状，然后更改了形状的调整值。下面的截图显示了在更改调整值之前形状的外观，以及在更改调整值之后形状的外观。
### **更改调整值前的绘图形状**
![todo:image_alt_text](change-adjustment-values-of-the-shape_1.png)
### **更改调整值后的绘图形状**
![todo:image_alt_text](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
