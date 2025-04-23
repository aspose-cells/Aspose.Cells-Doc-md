---
title: Copia l altezza delle righe dell intervallo di origine nell intervallo di destinazione
type: docs
weight: 250
url: /it/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

A volte l'utente ha bisogno di copiare l'altezza delle righe dell'intervallo di origine all'intervallo di destinazione. Aspose.Cells fornisce l'enumerazione [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) per questo scopo. Quando si imposta la proprietà [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) con l'enumerazione [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS), le altezze di tutte le righe all'interno dell'intervallo di origine verranno copiate nell'intervallo di destinazione.

{{% /alert %}} 
## **Copia l'altezza delle righe dell'intervallo di origine nell'intervallo di destinazione**
Il seguente esempio mostra come utilizzare l'enumerazione [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) per copiare le altezze delle righe dell'intervallo di origine nell'intervallo di destinazione. Una volta aperto il file Excel di output generato da questo codice in Microsoft Excel, si noterà che le altezze delle righe dell'intervallo di destinazione sono uguali alle altezze di quello di origine.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
{{< app/cells/assistant language="java" >}}
