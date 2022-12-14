---
title: Hitta den absoluta positionen av formen i arbetsbladet
type: docs
weight: 7000
url: /sv/java/finding-absolute-position-of-shape-inside-the-worksheet/
---
{{% alert color="primary" %}}

Ibland behöver du veta den absoluta positionen för en form på ett kalkylblad. Aspose.Cells tillhandahåller[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) och[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) fastigheter för detta ändamål. Dessa egenskaper returnerar den absoluta positionen för en form i ett kalkylblad i pixlar.

{{% /alert %}}

## **Förklaring av egenskaperna Shape.getLeftToCorner() och Shape.getTopToCorner()**

 Den här skärmdumpen förklarar vilka avstånd[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) och[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)egenskaper mått.

**Mätning av absolut position**

![todo:image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

Följande exempelkod visar den absoluta positionen för den första formen i ett kalkylblad i pixlar. Koden visar följande utdata i konsolen:

{{< highlight "java" >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
