---
title: 在工作表中查找形状的绝对位置
type: docs
weight: 7000
url: /zh/java/finding-absolute-position-of-shape-inside-the-worksheet/
---
{{% alert color="primary" %}}

有时，您需要知道形状在工作表上的绝对位置。 Aspose.Cells 提供了[**Shape.getLeftToCorner() 方法**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner)和[**形状.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)用于此目的的属性。这些属性返回工作表中形状的绝对位置（以像素为单位）。

{{% /alert %}}

## **Shape.getLeftToCorner() 和 Shape.getTopToCorner() 属性的解释**

此屏幕截图解释了距离[**Shape.getLeftToCorner() 方法**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner)和[**形状.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)属性测量。

**测量绝对位置**

![待办事项：图像_替代_文本](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

以下示例代码显示工作表中第一个形状的绝对位置（以像素为单位）。该代码在控制台中显示以下输出：

{{< highlight "java" >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
