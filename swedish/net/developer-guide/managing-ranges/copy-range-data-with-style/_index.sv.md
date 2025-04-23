---
title: Kopiera dataområde med stil
type: docs
weight: 610
url: /sv/net/copy-range-data-with-style/
---

{{% alert color="primary" %}}

[Kopiera endast dataområde](/cells/sv/net/copy-range-data-only/) förklarar hur du kopierar data från en cellintervall till en annan. Specifikt behandlade det en ny uppsättning stilar som applicerades på de kopierade cellerna. Aspose.Cells kan också kopiera en intervall komplett med formatering. Den här artikeln förklarar hur.

{{% /alert %}}

Aspose.Cells tillhandahåller en mängd olika klasser och metoder för att arbeta med områden, till exempel [**CreateRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) och [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

Detta exempel:

1. Skapar en arbetsbok.
1. Fyller ett antal celler i den första arbetsboken med data.
1. Skapar en [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. Skapar ett [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-objekt med specificerade formateringsattribut.
1. Tillämpa stilen på dataområdet.
1. Skapar en andra cellintervall.
1. Kopierar data med formatering från det första området till det andra området.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
