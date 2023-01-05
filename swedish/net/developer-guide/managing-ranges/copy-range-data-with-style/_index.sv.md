---
title: Kopiera intervalldata med stil
type: docs
weight: 610
url: /sv/net/copy-range-data-with-style/
---
{{% alert color="primary" %}}

[Kopiera endast intervalldata](/cells/sv/net/copy-range-data-only/) förklarade hur man kopierar data från ett cellområde till ett annat område. Specifikt tillämpade den en ny uppsättning stilar på de kopierade cellerna. Aspose.Cells kan också kopiera ett intervall komplett med formatering. Den här artikeln förklarar hur.

{{% /alert %}}

Aspose.Cells tillhandahåller en rad klasser och metoder för att arbeta med intervall, till exempel,[**CreateRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**StilFlagga**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) och[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

Detta exempel:

1. Skapar en arbetsbok.
1. Fyller ett antal celler i det första kalkylbladet med data.
1.  Skapar en[**Räckvidd**](https://reference.aspose.com/cells/net/aspose.cells/range).
1.  Skapar en[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt med specificerade formateringsattribut.
1. Tillämpar stilen på dataintervallet.
1. Skapar ett andra cellområde.
1. Kopierar data med formateringen från det första intervallet till det andra intervallet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
