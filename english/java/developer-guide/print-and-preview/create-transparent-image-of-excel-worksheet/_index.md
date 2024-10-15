---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 80
url: /java/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

Sometimes, you need to generate the image of your worksheet as a transparent image. You want to apply transparency to all cells which have no fill colors. Aspose.Cells provides the [**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent) property to apply transparency to worksheet image. When this property is **false**, then cells with no fill colors are drawn with white color and when it is **true**, cells with no fill colors are drawn transparent.

{{% /alert %}}

In the following worksheet image, transparency has not been applied. The cells with no fill colors are drawn white.

**Worksheet image without applying transparency**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)

While, in the following worksheet image, transparency has been applied. The cells with no fill colors are transparent.

**Worksheet image after applying transparency**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)

You can use the following sample code to generate a transparent image of your Excel worksheet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
{{< app/cells/assistant language="java" >}}