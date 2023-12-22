---
title: 查找工作表内形状的绝对位置
type: docs
weight: 7000
url: /zh/java/finding-absolute-position-of-shape-inside-the-worksheet/
description: 了解如何通过 Aspose.Cells for Java API 查找工作表内形状的绝对位置。
keywords: How to Find Absolute Position of Shape in Java, Get Absolute Position of Shape using Java, Obtain Absolute Position of Shape inside the Worksheet via Java, Measure absolute position of Shape with Java.
---
{{% alert color="primary" %}}

有时，您需要知道工作表上形状的绝对位置。 Aspose.Cells 提供[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner)和[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)用于此目的的属性。这些属性返回工作表中形状的绝对位置（以像素为单位）。

{{% /alert %}}

##  **Shape.getLeftToCorner() 和 Shape.getTopToCorner() 属性的说明**

此屏幕截图解释了距离[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner)和[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)属性测量。

**如何测量绝对位置**

![待办事项：图像_替代_文本](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

以下示例代码显示工作表中第一个形状的绝对位置（以像素为单位）。该代码在控制台中显示以下输出：

{{< highlight "java" >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
