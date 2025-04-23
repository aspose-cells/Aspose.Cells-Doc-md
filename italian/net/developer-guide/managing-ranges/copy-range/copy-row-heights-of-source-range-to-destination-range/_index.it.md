---
title: Copia l altezza delle righe dell intervallo di origine nell intervallo di destinazione
type: docs
weight: 590
url: /it/net/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}}

A volte l'utente ha bisogno di copiare le altezze delle righe dell'intervallo di origine nell'intervallo di destinazione. Aspose.Cells fornisce l'enum [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) a questo scopo. Quando imposti la proprietà [**PasteOptions.PasteType**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions/properties/pastetype) con l'enum [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype), le altezze di tutte le righe all'interno dell'intervallo di origine verranno copiate nell'intervallo di destinazione.

{{% /alert %}}

Il seguente codice di esempio spiega come utilizzare l'enum [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) per copiare le altezze delle righe dell'intervallo di origine nell'intervallo di destinazione. Una volta aperto il file Excel di output generato da questo codice in Microsoft Excel, vedrai che le altezze delle righe dell'intervallo di destinazione sono esattamente le stesse delle altezze delle righe dell'intervallo di origine.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetRowHeights-GetRowHeightsOfSourceRangeToDestinationRange.cs" >}}
{{< app/cells/assistant language="csharp" >}}
