---
title: Ottimizzazione dell'utilizzo della memoria mentre si lavora con file di grandi dimensioni con set di dati di grandi dimensioni
type: docs
weight: 180
url: /it/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

Quando si crea una cartella di lavoro con set di dati di grandi dimensioni o si legge un file Excel di grandi dimensioni Microsoft, la quantità totale di RAM occupata dal processo è sempre un problema. Ci sono misure che possono essere adattate per far fronte alla sfida. Aspose.Cells fornisce alcune opzioni rilevanti e API chiama per ridurre, ridurre e ottimizzare l'utilizzo della memoria. Inoltre, può aiutare il processo a funzionare in modo più efficiente e a funzionare più velocemente.

 Utilizzare il[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) opzione per ottimizzare l'uso della memoria per i dati delle celle e ridurre il costo complessivo della memoria. Quando si crea un set di dati di grandi dimensioni per le celle, è possibile risparmiare una certa quantità di memoria rispetto all'utilizzo dell'impostazione predefinita ([**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)).

{{% /alert %}}

## **Ottimizzazione della memoria**

### **Lettura di file Excel di grandi dimensioni**

L'esempio seguente mostra come leggere un file Excel di grandi dimensioni Microsoft in modalità ottimizzata.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **Scrittura di file Excel di grandi dimensioni**

L'esempio seguente mostra come scrivere un set di dati di grandi dimensioni in un foglio di lavoro in modalità ottimizzata.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **Attenzione**

 L'opzione predefinita,[**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)è applicato per tutte le versioni. Per alcune situazioni, come la creazione di una cartella di lavoro con un set di dati di grandi dimensioni per le celle, il file[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)opzione può ottimizzare l'uso della memoria e diminuire il costo della memoria per l'applicazione. Tuttavia, questa opzione potrebbe peggiorare le prestazioni in alcuni casi speciali come follow.

1. **Accesso allo Cells in modo casuale e ripetuto** : La sequenza più efficiente per accedere alla raccolta di celle è cella per cella in una riga, quindi riga per riga. Soprattutto se accedi a righe/celle dall'enumeratore acquisito da[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection) e[**Riga**](https://reference.aspose.com/cells/net/aspose.cells/row) , le prestazioni sarebbero massimizzate con[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting).
1. **Inserimento e cancellazione Cells e righe** : Si prega di notare che se ci sono molte operazioni di inserimento/cancellazione per Cells/Rows, il degrado delle prestazioni sarà notevole per*MemoryPreference* modalità rispetto alla*Normale*modalità.
1. **Funzionante su diversi tipi Cell** : Se la maggior parte delle celle contiene valori stringa o formule, il costo della memoria sarà lo stesso di*Normale* mode ma se ci sono molte celle vuote o i valori delle celle sono numerici, bool e così via, il[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)l'opzione darà prestazioni migliori.
