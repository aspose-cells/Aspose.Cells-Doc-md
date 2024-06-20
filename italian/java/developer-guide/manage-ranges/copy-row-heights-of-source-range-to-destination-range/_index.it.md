---
title: Copia l altezza delle righe dell intervallo di origine nell intervallo di destinazione
type: docs
weight: 250
url: /it/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

A volte l'utente ha bisogno di copiare l'altezza delle righe dell'intervallo di origine nell'intervallo di destinazione. Aspose.Cells fornisce l'enum [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) a questo scopo. Quando si imposterà la proprietà [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) con l'enum [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) all'altezza di tutte le righe all'interno dell'intervallo di origine verrà copiata nell'intervallo di destinazione.

{{% /alert %}} 
## **Copia l'altezza delle righe dell'intervallo di origine nell'intervallo di destinazione**
Il seguente codice di esempio spiega come utilizzare l'enum [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) per copiare l'altezza delle righe dell'intervallo di origine nell'intervallo di destinazione. Una volta aperto il file excel di output generato da questo codice in Microsoft Excel, vedrete che le altezze delle righe dell'intervallo di destinazione sono esattamente le stesse delle altezze delle righe dell'intervallo di origine.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
