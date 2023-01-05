---
title: Kopiera endast intervalldata
type: docs
weight: 600
url: /sv/net/copy-range-data-only/
---
{{% alert color="primary" %}}

Ibland måste du kopiera data från ett cellområde till ett annat, bara kopiera data, inte formateringen. Aspose.Cells erbjuder denna funktion.

Den här artikeln innehåller en exempelkod som använder Aspose.Cells för att kopiera en rad data.

{{% /alert %}}

Det här exemplet visar hur man:

1. Skapa en arbetsbok.
1. Lägg till data i celler i det första kalkylbladet.
1.  Skapa en[**Räckvidd**](https://reference.aspose.com/cells/net/aspose.cells/range).
1.  Skapa en[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt med specificerade formateringsattribut.
1. Använd stilformateringen på intervallet.
1. Skapa ytterligare ett cellområde.
1. Kopiera data från det första intervallet till detta andra intervall.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataOnly-1.cs" >}}
