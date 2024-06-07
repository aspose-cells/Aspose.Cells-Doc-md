---
title: 查找工作表中形状的绝对位置
type: docs
weight: 7000
url: /zh/java/finding-absolute-position-of-shape-inside-the-worksheet/
description: 了解如何通过Aspose.Cells for Java API在工作表中查找形状的绝对位置。
keywords: 如何在Java中查找形状的绝对位置，在Java中获取形状的绝对位置，通过Java在工作表中获取形状的绝对位置，使用Java测量形状的绝对位置。
---

{{% alert color="primary" %}}

有时，您需要知道工作表上形状的绝对位置。Aspose.Cells提供了[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner)和[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)属性以实现这个目的。这些属性以像素为单位返回形状在工作表中的绝对位置。

{{% /alert %}}

## **Shape.getLeftToCorner()和Shape.getTopToCorner()属性的解释**

此截图说明了[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner)和[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)属性测量的距离。

**如何测量绝对位置**

![todo:image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

以下示例代码显示工作表中第一个形状的绝对位置（以像素为单位）。 该代码在控制台显示以下输出：

{{< highlight java >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
