---
title: Kopiera dataområde med stil
type: docs
weight: 340
url: /sv/java/copy-range-data-with-style/
---

{{% alert color="primary" %}} 

[Kopiera endast räckviddsdata](/cells/sv/java/kopiera-rangedata-endast/) förklarade hur du kopierar data från en radie av celler till en annan radie. Aspose.Cells kan också kopiera en radie komplett med formatering. Denna artikel förklarar hur.

{{% /alert %}} 
## **Kopiera områdesdata med stil**
Aspose.Cells tillhandahåller ett utbud av klasser och metoder för att arbeta med intervall, till exempel [createRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), [StyleFlag](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [applyStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\)), osv.

Detta exempel:

1. Skapar en arbetsbok.
1. Fyller ett antal celler i den första arbetsboken med data.
1. Skapar en radie.
1. Skapa ett stilobjekt med angivna formateringsattribut.
1. Tillämpa stilen på dataområdet.
1. Skapar en andra cellintervall.
1. Kopierar data med formatering från det första området till det andra området.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

