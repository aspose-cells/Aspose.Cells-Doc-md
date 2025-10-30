---
title: Copia l altezza delle righe dell intervallo di origine nell intervallo di destinazione con Golang tramite C++
linktitle: Copia l altezza delle righe dell intervallo di origine nell intervallo di destinazione
type: docs
weight: 590
url: /it/go-cpp/copy-row-heights-of-source-range-to-destination-range/
description: Impara come copiare l altezza delle righe da un intervallo di origine a uno di destinazione usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A volte, gli utenti devono copiare l'altezza delle righe da un intervallo di origine a uno di destinazione. Aspose.Cells fornisce l'enumerazione [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/) per questo scopo. Quando imposti la proprietà [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) con l'enumerazione [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/), le altezze di tutte le righe all'interno dell'intervallo di origine verranno copiate nell'intervallo di destinazione.

{{% /alert %}}

Il codice di esempio seguente spiega come usare l'enumerazione [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/) per copiare le altezze delle righe da un intervallo di origine a uno di destinazione. Una volta aperto il file Excel di output generato da questo codice in Microsoft Excel, vedrai che le altezze delle righe dell'intervallo di destinazione sono esattamente le stesse delle righe dell'intervallo di origine.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRowHeightsOfSourceRangeToDestinationRange.go" >}}
