---
title: Endast kopiera intervallstil
type: docs
weight: 350
url: /sv/java/copy-range-style-only/
---
{{% alert color="primary" %}} 

[Kopiera endast intervalldata](/cells/sv/java/copy-range-data-only/) och[Kopiera intervalldata med stil](/cells/sv/java/copy-range-data-with-style/) förklarade hur man kopierar data från ett område till ett annat med eller utan formatering. Det är också möjligt att kopiera endast formateringen av intervallet. Den här artikeln visar hur.

{{% /alert %}} 
## **Endast kopiera intervallstil**
Det här exemplet skapar en arbetsbok, fyller den med data och kopierar endast ett intervalls stil.

1. Skapa ett intervall.
1. Skapa ett stilobjekt med specificerade formateringsattribut.
1. Använd stilformateringen på intervallet.
1. Skapa ett andra cellområde.
1. Kopiera det första intervallets formatering till det andra intervallet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeStyleOnly-CopyRangeStyleOnly.java" >}}
