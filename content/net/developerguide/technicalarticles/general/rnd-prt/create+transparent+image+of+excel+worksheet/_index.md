---
title : "Create Transparent Image of Excel Worksheet" 
description : "" 
weight : 20372 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/rnd-prt/create+transparent+image+of+excel+worksheet/
---

# Aspose.Cells for .NET : Create Transparent Image of Excel Worksheet


Sometimes, you need to generate the image of your worksheet as transparent image. You want to apply transparency to all cells which have no fill colors. Aspose.Cells provides the [ImageOrPrintOptions.Transparent](https://apireference.aspose.com/net/cells/aspose.cells.rendering/imageorprintoptions/properties/transparent) property to apply transparency to worksheet image. When this property is **false**, then cells with no fill colors are drawn with white color and when it is **true**, cells with no fill colors are drawn transparent.

In the following worksheet image, transparency has not been applied. The cells with no fill colors are drawn white.

{{< table style="table-striped" >}}
|Output without transparency: the cell background is white|
|:----|
|![](https://docs2.aspose.com/cells/net/attachments/5017541/5112562.png)|
{{< /table >}}

While, in the following worksheet image, transparency has been applied. The cells with no fill colors are transparent.

{{< table style="table-striped" >}}
|Output with transparency enabled|
|:----|
|![](https://docs2.aspose.com/cells/net/attachments/5017541/5112565.png)|
{{< /table >}}

The following sample code generates a transparent image from an Excel worksheet.

