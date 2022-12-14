---
title: Regola il livello di compressione della cartella di lavoro
type: docs
weight: 130
url: /it/java/adjust-workbook-compression-level/
---
## **Regola il livello di compressione della cartella di lavoro**

Gli sviluppatori possono regolare il livello di compressione della cartella di lavoro quando lavorano con cartelle di lavoro più grandi. Gli sviluppatori possono dare la priorità a file di dimensioni inferiori rispetto al tempo di elaborazione o viceversa. Aspose.Cells fornisce**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)**enumerazione che è possibile utilizzare per impostare il livello di compressione della cartella di lavoro. Il**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)** enumerazione fornisce i seguenti membri.

- **[LEVEL_1](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**: la compressione più veloce ma meno efficace.
- **[LEVEL_2](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_2)**: Un po' più lento, ma migliore, del livello 1.
- **[LEVEL_3](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_3)**Un po' più lento, ma migliore, del livello 2.
- **[LEVEL_4](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_4)**: Un po' più lento, ma migliore, del livello 3.
- **[LEVEL_5](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_5)**: Un po' più lento del livello 4, ma con una migliore compressione.
- **[LEVEL_6](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)**: Un buon equilibrio tra velocità ed efficienza di compressione.
- **[LEVEL_7](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_7)**: Compressione abbastanza buona!
- **[LEVEL_8](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_8)**: Migliore compressione rispetto a Level7!
- **[LEVEL_9](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**La compressione "migliore", dove migliore significa la massima riduzione delle dimensioni del flusso di dati di input. Questa è anche la compressione più lenta.

Il seguente frammento di codice illustra l'uso di**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)** enumerazione e confronta il tempo di conversione per**[LEVEL_1](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**, **[LEVEL_6](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)** , e**[LEVEL_9](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**. Puoi anche confrontare le dimensioni dei file generati.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}
