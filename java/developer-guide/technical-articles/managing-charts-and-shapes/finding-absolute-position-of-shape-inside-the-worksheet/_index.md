---
title: Finding Absolute Position of Shape inside the Worksheet
type: docs
weight: 70
url: /java/finding-absolute-position-of-shape-inside-the-worksheet/
---

{{% alert color="primary" %}}

Sometimes, you need to know the absolute position of a shape on a worksheet. Aspose.Cells provides the [**Shape.getLeftToCorner()**](https://apireference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) and [**Shape.getTopToCorner()**](https://apireference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) properties for this purpose. These properties return the absolute position of a shape in a worksheet in pixels.

{{% /alert %}}

#### **Explanation of the Shape.getLeftToCorner() and Shape.getTopToCorner() properties**

This screenshot explains what distances the [**Shape.getLeftToCorner()**](https://apireference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) and [**Shape.getTopToCorner()**](https://apireference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) properties measure.

**Measuring absolute position**

![todo:image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

The following sample code displays the absolute position of the first shape in a worksheet in pixels. The code displays the following output in the console:

{{< highlight java >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
