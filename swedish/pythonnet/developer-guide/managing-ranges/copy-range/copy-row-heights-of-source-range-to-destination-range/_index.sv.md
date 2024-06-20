---
title: Kopiera radhöjderna i källområdet till destinationsområdet
type: docs
weight: 590
url: /sv/python-net/copy-row-heights-of-source-range-to-destination-range/
description: Den här artikeln beskriver hur man kopierar radhöjder från källointervall till målintervall med Aspose.Cells for Python via .NET biblioteket.
keywords: Python Excel bibliotek, Python Hur man kopierar radhöjder från källointervall till målintervall, Python Hur man kopierar radhöjder från källointervall endast med Python Excel biblioteket.
---

{{% alert color="primary" %}}

Ibland behöver användaren kopiera radhöjder från källointervall till målintervall. Aspose.Cells för Python via .NET tillhandahåller [**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype) enum för detta ändamål. När du ställer in [**PasteOptions.paste_type**](https://reference.aspose.com/cells/python-net/aspose.cells/pasteoptions/paste_type/) egenskapen med [**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype) enum kommer höjderna för alla rader inom källointervallet att kopieras till målintervallet.

{{% /alert %}}

Följande kodexempel förklarar hur man använder [**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype)-enumet för att kopiera radhöjder från källområdet till destinationsområdet. När du öppnar den genererade utfil i Microsoft Excel kommer du att se att destinationsområdets radhöjder är exakt desamma som källområdets radhöjder.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-GetRowHeightsOfSourceRangeToDestinationRange.py" >}}
