---
title: Hitta absolut position av formen innanför arbetsbladet
type: docs
weight: 7000
url: /sv/java/finding-absolute-position-of-shape-inside-the-worksheet/
description: Lär dig hur man hittar absolut position av formen innanför arbetsbladet genom Aspose.Cells for Java API er.
keywords: Hitta absolut position av formen i Java, Få absolut position av formen med Java, Få absolut position av formen innanför arbetsbladet via Java, Mäta absolut position av formen med Java.
---

{{% alert color="primary" %}}

Ibland behöver du veta formens absoluta position på ett arbetsblad. Aspose.Cells tillhandahåller egenskaperna [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) och [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) för detta ändamål. Dessa egenskaper returnerar formens absoluta position på ett arbetsblad i pixlar.

{{% /alert %}}

## **Förklaring av egenskaperna Shape.getLeftToCorner() och Shape.getTopToCorner()**

Denna skärmbild förklarar vilka avstånd egenskaperna [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) och [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) mäter.

**Hur man mäter absolut position**

![todo:image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

Följande exempelkod visar den absoluta positionen för den första formen på ett arbetsblad i pixlar. Koden visar följande utdata i konsolen:

{{< highlight java >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
{{< app/cells/assistant language="java" >}}
