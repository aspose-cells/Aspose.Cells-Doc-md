---
title: Regola il livello di compressione del workbook
type: docs
weight: 180
url: /it/python-net/adjust-workbook-compression-level/
---

## **Regola il Livello di Compressione del Foglio di Lavoro**

Gli sviluppatori possono impostare il livello di compressione del workbook quando lavorano con file di grandi dimensioni. Possono privilegiare dimensioni di file più piccole rispetto ai tempi di elaborazione o viceversa. Aspose.Cells per Python via .NET fornisce l'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) che puoi usare per impostare il livello di compressione del workbook. L'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) fornisce i seguenti membri.

- Livello1: La compressione più veloce ma meno efficace.
- Livello2: Un po' più lento, ma migliore, rispetto al livello 1.
- Livello3: Un po' più lento, ma migliore, rispetto al livello 2.
- Livello4: Un po' più lento, ma migliore, rispetto al livello 3.
- Livello5: Un po' più lento del livello 4, ma con una migliore compressione.
- Livello6: Un buon equilibrio tra velocità ed efficienza di compressione.
- Livello7: Compressione abbastanza buona!
- Livello8: Migliore compressione rispetto al Livello 7!
- Livello9: La compressione "migliore", dove migliore significa la maggiore riduzione delle dimensioni del flusso di dati in ingresso. Questa è anche la compressione più lenta.

Il seguente frammento di codice mostra l'uso dell'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) e confronta il tempo di conversione per Livello1, Livello6 e Livello9. Puoi anche confrontare le dimensioni dei file generati.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-AdjustCompressionLevel-1.py" >}}

