---
title: Kopiera endast stilområde
type: docs
weight: 350
url: /sv/java/copy-range-style-only/
---

{{% alert color="primary" %}} 

[Kopiera endast räckviddsdata](/cells/sv/java/kopiera-rangedata-endast/) and [Kopiera radiedata med stil](/cells/sv/java/kopiera-rangedata-med-stil/) förklarade hur man kopierar data från en räckvidd till en annan med eller utan formatering. Det är också möjligt att endast kopiera formateringen av räckvidden. Denna artikel visar hur.

{{% /alert %}} 
## **Kopiera områdesstil endast**
Detta exempel skapar en arbetsbok, fyller den med data och kopierar endast stil från ett intervall.

1. Skapa ett område.
1. Skapa ett stilobjekt med angivna formateringsattribut.
1. Tillämpa stilformatering på området.
1. Skapa en andra cellintervall.
1. Kopiera det första områdets formatering till det andra området.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeStyleOnly-CopyRangeStyleOnly.java" >}}
{{< app/cells/assistant language="java" >}}
