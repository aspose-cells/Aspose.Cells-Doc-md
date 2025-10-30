---
title: Kopiera radhöjder från källområde till destinationsområde med Golang via C++
linktitle: Kopiera radhöjderna i källområdet till destinationsområdet
type: docs
weight: 590
url: /sv/go-cpp/copy-row-heights-of-source-range-to-destination-range/
description: Lär dig hur du kopierar radhöjder från en källområde till ett målområde med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Ibland behöver användare kopiera radhöjder från ett källområde till ett målområde. Aspose.Cells tillhandahåller enum [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/) för detta ändamål. När du sätter egenskapen [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) med enum [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/), kommer höjderna av alla rader i källdatan att kopieras till målområdet.

{{% /alert %}}

Följande exempel förklarar hur du använder enum [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/) för att kopiera radhöjder från ett källområde till ett målområde. När du öppnar den genererade Excel-filen i Microsoft Excel kommer du att se att radhöjderna i målområdet är exakt samma som i källdatan.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRowHeightsOfSourceRangeToDestinationRange.go" >}}
