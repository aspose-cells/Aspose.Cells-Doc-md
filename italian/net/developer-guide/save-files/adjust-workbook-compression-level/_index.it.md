---
title: Regola il livello di compressione del workbook
type: docs
weight: 180
url: /it/net/adjust-workbook-compression-level/
---

## **Regola il Livello di Compressione del Foglio di Lavoro**

Gli sviluppatori possono regolare il livello di compressione del foglio di lavoro quando si lavora con fogli di lavoro più grandi. Gli sviluppatori possono dare priorità alle dimensioni del file più piccole rispetto al tempo di elaborazione o viceversa. Aspose.Cells fornisce l'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) che è possibile utilizzare per impostare il livello di compressione del foglio di lavoro. L'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) fornisce i seguenti membri.

- Livello1: La compressione più veloce ma meno efficace.
- Livello2: Un po' più lento, ma migliore, rispetto al livello 1.
- Livello3: Un po' più lento, ma migliore, rispetto al livello 2.
- Livello4: Un po' più lento, ma migliore, rispetto al livello 3.
- Livello5: Un po' più lento del livello 4, ma con una migliore compressione.
- Livello6: Un buon equilibrio tra velocità ed efficienza di compressione.
- Livello7: Compressione abbastanza buona!
- Livello8: Migliore compressione rispetto al Livello 7!
- Livello9: La compressione "migliore", dove migliore significa la maggiore riduzione delle dimensioni del flusso di dati in ingresso. Questa è anche la compressione più lenta.

Il seguente frammento di codice mostra l'uso dell'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) e confronta il tempo di conversione per Livello1, Livello6 e Livello9. Puoi anche confrontare le dimensioni dei file generati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
