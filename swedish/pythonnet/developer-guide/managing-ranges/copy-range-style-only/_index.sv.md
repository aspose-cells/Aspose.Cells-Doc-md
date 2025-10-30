---
title: Kopiera endast stilområde
type: docs
weight: 620
url: /sv/python-net/copy-range-style-only/
description: Denna artikel beskriver hur man endast kopierar omfattning av stil med Aspose.Cells for Python via .NET bibliotek.
keywords: Python Excel bibliotek, Python Hur man kopierar omfattning av stil endast, Python Hur man kopierar omfattning av stil endast med python excel bibliotek.
---

{{% alert color="primary" %}}

[Kopiera endast dataomfattning](/cells/sv/python-net/kopiera-endast-dataomfattning/) och [Kopiera omfattning av data med stil](/cells/sv/python-net/kopiera-omfattning-av-data-med-stil/) förklarade hur man kopierar data från en omfattning till en annan endast med formatering eller tillsammans med formatering. Det är också möjligt att endast kopiera formateringen. Denna artikel visar hur.

{{% /alert %}} 

Detta exempel skapar en arbetsbok, fyller den med data och kopierar endast stil från ett intervall.

1. Skapa ett område.
1. Skapa ett [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objekt med specificerade formateringsattribut.
1. Tillämpa stilformatering på området.
1. Skapa en andra cellintervall.
1. Kopiera det första områdets formatering till det andra området.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeStyleOnly-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
