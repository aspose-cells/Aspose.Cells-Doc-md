---
title: Regola il livello di compressione del workbook con Golang tramite C++
linktitle: Regola il livello di compressione del workbook
type: docs
weight: 180
url: /it/go-cpp/adjust-workbook-compression-level/
description: Impara come regolare il livello di compressione di un workbook usando Aspose.Cells for C++ per ottimizzare dimensione del file e tempo di elaborazione.
---

## **Regola il Livello di Compressione del Foglio di Lavoro**

Gli sviluppatori possono regolare il livello di compressione del foglio di lavoro quando si lavora con fogli di lavoro più grandi. Gli sviluppatori possono dare priorità alle dimensioni del file più piccole rispetto al tempo di elaborazione o viceversa. Aspose.Cells fornisce l'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) che è possibile utilizzare per impostare il livello di compressione del foglio di lavoro. L'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) fornisce i seguenti membri.

- Livello1: La compressione più veloce ma meno efficace.
- Livello2: Un po' più lento, ma migliore, rispetto al livello 1.
- Livello3: Un po' più lento, ma migliore, rispetto al livello 2.
- Livello4: Un po' più lento, ma migliore, rispetto al livello 3.
- Livello5: Un po' più lento del livello 4, ma con una migliore compressione.
- Livello6: Un buon equilibrio tra velocità ed efficienza di compressione.
- Livello7: Compressione abbastanza buona!
- Livello8: Migliore compressione rispetto al Livello 7!
- Livello9: La compressione "migliore", dove migliore significa la maggiore riduzione delle dimensioni del flusso di dati in ingresso. Questa è anche la compressione più lenta.

Il seguente frammento di codice mostra l'uso dell'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) e confronta il tempo di conversione per Livello1, Livello6 e Livello9. Puoi anche confrontare le dimensioni dei file generati.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AdjustWorkbookCompressionLevel.go" >}}
