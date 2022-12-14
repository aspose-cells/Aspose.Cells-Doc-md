---
title: Endast kopiera intervallstil
type: docs
weight: 620
url: /sv/net/copy-range-style-only/
---
{{% alert color="primary" %}}

[Kopiera endast intervalldata](/cells/sv/net/copy-range-data-only/) och[Kopiera intervalldata med stil](/cells/sv/net/copy-range-data-with-style/) förklarade hur man kopierar data från ett område till ett annat på egen hand eller komplett med formatering. Det är också möjligt att kopiera endast formateringen. Den här artikeln visar hur.

{{% /alert %}} 

Det här exemplet skapar en arbetsbok, fyller den med data och kopierar endast ett intervalls stil.

1. Skapa ett intervall.
1.  Skapa en[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)objekt med specificerade formateringsattribut.
1. Använd stilformateringen på intervallet.
1. Skapa ett andra cellområde.
1. Kopiera det första intervallets formatering till det andra intervallet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeStyleOnly-1.cs" >}}
