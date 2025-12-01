---
title: Finding Absolute Position of Shape inside the Worksheet
type: docs
weight: 7000
url: /java/finding-absolute-position-of-shape-inside-the-worksheet/
description: Learn how to Find Absolute Position of Shape inside the Worksheet through the Aspose.Cells for Java APIs.
keywords: How to Find Absolute Position of Shape in Java, Get Absolute Position of Shape using Java, Obtain Absolute Position of Shape inside the Worksheet via Java, Measure absolute position of Shape with Java.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to know the absolute position of a shape on a worksheet. Aspose.Cells provides the [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) and [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) properties for this purpose. These properties return the absolute position of a shape in a worksheet in pixels.

{{% /alert %}}

## **Explanation of the Shape.getLeftToCorner() and Shape.getTopToCorner() properties**

This screenshot explains what distances the [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) and [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) properties measure.

**How to Measure absolute position**

![todo:image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

The following sample code displays the absolute position of the first shape in a worksheet in pixels. The code displays the following output in the console:

{{< highlight java >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
{{< app/cells/assistant language="java" >}}
