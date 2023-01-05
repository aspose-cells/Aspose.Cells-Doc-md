---
title: Regola il livello di compressione della cartella di lavoro
type: docs
weight: 180
url: /it/net/adjust-workbook-compression-level/
---
## **Regola il livello di compressione della cartella di lavoro**

Gli sviluppatori possono regolare il livello di compressione della cartella di lavoro quando lavorano con cartelle di lavoro più grandi. Gli sviluppatori possono dare la priorità a file di dimensioni inferiori rispetto al tempo di elaborazione o viceversa. Aspose.Cells fornisce**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** enumerazione che è possibile utilizzare per impostare il livello di compressione della cartella di lavoro. Il**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** enumerazione fornisce i seguenti membri.

- Level1: la compressione più veloce ma meno efficace.
- Livello 2: un po' più lento, ma migliore, del livello 1.
- Livello 3: un po' più lento, ma migliore, del livello 2.
- Livello 4: un po' più lento, ma migliore, del livello 3.
- Level5: un po' più lento del livello 4, ma con una migliore compressione.
- Livello 6: un buon equilibrio tra velocità ed efficienza di compressione.
- Level7: compressione abbastanza buona!
- Level8: compressione migliore rispetto a Level7!
- Level9: la "migliore" compressione, dove migliore indica la massima riduzione delle dimensioni del flusso di dati di input. Questa è anche la compressione più lenta.

 Il seguente frammento di codice illustra l'uso di**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)**enumerazione e confronta il tempo di conversione per Level1, Level6 e Level9. Puoi anche confrontare le dimensioni dei file generati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
