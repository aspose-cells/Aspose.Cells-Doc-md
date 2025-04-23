---
title: Regola il livello di compressione del workbook
type: docs
weight: 130
url: /it/java/adjust-workbook-compression-level/
---

## **Regola il livello di compressione del workbook**

Gli sviluppatori possono regolare il livello di compressione del workbook quando lavorano con workbook più grandi. Gli sviluppatori possono dare priorità alle dimensioni dei file più piccole rispetto al tempo di elaborazione o viceversa. Aspose.Cells fornisce l'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) che puoi utilizzare per impostare il livello di compressione del workbook. L'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) fornisce i seguenti membri.

- [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-1): La compressione più veloce ma meno efficace.
- [**LEVEL_2**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-2): Un po' più lenta ma migliore del livello 1.
- [**LEVEL_3**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-3): Un po' più lenta ma migliore del livello 2.
- [**LEVEL_4**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-4): Un po' più lenta ma migliore del livello 3.
- [**LEVEL_5**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-5): Un po' più lenta del livello 4, ma con una migliore compressione.
- [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-6): Un buon equilibrio tra velocità ed efficienza di compressione.
- [**LEVEL_7**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-7): Buona compressione!
- [**LEVEL_8**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-8): Migliore compressione rispetto al livello 7!
- [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-9): La compressione "migliore", dove migliore significa la maggiore riduzione delle dimensioni del flusso di dati in ingresso. Questa è anche la compressione più lenta.

Il seguente frammento di codice dimostra l'uso dell'enumerazione [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) e confronta il tempo di conversione per [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-1), [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-6) e [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-9). È inoltre possibile confrontare le dimensioni dei file generati.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}
{{< app/cells/assistant language="java" >}}
