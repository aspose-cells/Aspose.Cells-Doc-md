---
title: Kopiera endast stilområde
type: docs
weight: 620
url: /sv/net/copy-range-style-only/
---

{{% alert color="primary" %}}

[Kopiera endast dataområde](/cells/sv/net/copy-range-data-only/) och [Kopiera dataområde med stil](/cells/sv/net/copy-range-data-with-style/) förklarade hur man kopierar data från ett område till ett annat på egen hand eller komplett med formatering. Det är också möjligt att endast kopiera formateringen. Den här artikeln visar hur.

{{% /alert %}} 

Detta exempel skapar en arbetsbok, fyller den med data och kopierar endast stil från ett intervall.

1. Skapa ett område.
1. Skapa ett [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-objekt med specificerade formateringsattribut.
1. Tillämpa stilformatering på området.
1. Skapa en andra cellintervall.
1. Kopiera det första områdets formatering till det andra området.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeStyleOnly-1.cs" >}}
