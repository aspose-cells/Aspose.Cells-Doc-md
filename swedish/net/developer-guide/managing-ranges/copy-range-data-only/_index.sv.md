---
title: Kopiera endast dataområde
type: docs
weight: 600
url: /sv/net/copy-range-data-only/
---

{{% alert color="primary" %}}

Ibland behöver du kopiera data från en cellintervall till en annan, kopiera bara datan, inte formateringen. Aspose.Cells erbjuder den här funktionen.

Den här artikeln ger en exempelkod som använder Aspose.Cells för att kopiera ett datintervall.

{{% /alert %}}

Detta exempel visar hur man:

1. Skapa en arbetsbok.
1. Lägga till data till celler i den första arbetsboken.
1. Skapa en [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. Skapa ett [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-objekt med specificerade formateringsattribut.
1. Tillämpa stilformatering på området.
1. Skapa en annan cellintervall.
1. Kopiera data från det första området till det andra området.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataOnly-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
