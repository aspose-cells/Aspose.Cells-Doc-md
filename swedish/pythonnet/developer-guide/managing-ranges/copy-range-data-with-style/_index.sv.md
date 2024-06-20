---
title: Kopiera dataområde med stil
type: docs
weight: 610
url: /sv/python-net/copy-range-data-with-style/
description: Denna artikel beskriver hur man kopierar omfattning av data med stil med Aspose.Cells for Python via .NET bibliotek.
keywords: Python Excel bibliotek, Python Hur man kopierar omfattning av data med stil, Python Hur man kopierar omfattning av data med stil med python excel bibliotek.
---

{{% alert color="primary" %}}

[Kopiera endast dataomfattning](/cells/sv/python-net/kopiera-endast-dataomfattning/) förklarade hur man kopierar datan från en cellomfattning till en annan cellomfattning. Specifikt behandlade den en ny uppsättning stilar som applicerades på de kopierade cellerna. Aspose.Cells för Python via .NET kan också kopiera en omfattning med formatering. Denna artikel förklarar hur.

{{% /alert %}}

Aspose.Cells for Python via .NET tillhandahåller en rad klasser och metoder för att arbeta med omfattningar, till exempel [**create_range(upper_left_cell, lower_right_cell)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str), [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) och [**apply_style(style, flag)**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag).

Detta exempel:

1. Skapar en arbetsbok.
1. Fyller ett antal celler i den första arbetsboken med data.
1. Skapar en [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).
1. Skapar ett [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objekt med specificerade formateringsattribut.
1. Tillämpa stilen på dataområdet.
1. Skapar en andra cellintervall.
1. Kopierar data med formatering från det första området till det andra området.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeDataWithStyle-1.py" >}}
