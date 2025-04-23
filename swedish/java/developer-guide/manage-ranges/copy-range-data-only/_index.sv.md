---
title: Kopiera endast dataområde
type: docs
weight: 330
url: /sv/java/copy-range-data-only/
---

{{% alert color="primary" %}} 

Ibland behöver du kopiera data från ett cellområde till ett annat, enbart kopiera datan, inte formateringen. Aspose.Cells erbjuder denna funktion genom att tillhandahålla metoden [Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData-com.aspose.cells.Range-).

{{% /alert %}} 
## **Kopiera områdesdata endast**
Detta exempel visar hur man:

1. Skapa en arbetsbok.
1. Lägga till data till celler i den första arbetsboken.
1. Skapa ett område.
1. Skapa ett stilobjekt med angivna formateringsattribut.
1. Tillämpa stilformatering på området.
1. Skapa en annan cellintervall.
1. Kopiera data från det första området till det andra området med hjälp av metoden [Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData-com.aspose.cells.Range-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataOnly-CopyRangeDataOnly.java" >}}
{{< app/cells/assistant language="java" >}}
