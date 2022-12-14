---
title: Ottimizzazione dell'utilizzo della memoria mentre si lavora con file di grandi dimensioni con set di dati di grandi dimensioni
type: docs
weight: 110
url: /it/nodejs-java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

Quando si crea una cartella di lavoro con set di dati di grandi dimensioni o si legge un file Excel di grandi dimensioni Microsoft, la quantità totale di RAM occupata dal processo è sempre un problema. Esistono misure che possono essere adattate per far fronte alla sfida. Aspose.Cells fornisce alcune opzioni rilevanti e API chiama per ridurre, ridurre e ottimizzare l'utilizzo della memoria. Inoltre, può aiutare il processo a funzionare in modo più efficiente e a funzionare più velocemente.

 Uso[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) opzione per ottimizzare la memoria utilizzata per i dati delle celle per ridurre il costo complessivo della memoria. Quando si creano set di dati di grandi dimensioni per le celle, è possibile risparmiare una certa quantità di memoria rispetto all'utilizzo dell'impostazione predefinita[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **Ottimizzazione della memoria**

L'esempio seguente mostra come ottimizzare l'utilizzo della memoria durante l'utilizzo di dati di grandi dimensioni in Aspose.Cells per Node.js tramite Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-nodejs-optimize-memory-usage-while-working-with-large-data.java" >}}

## **Attenzione**

 L'opzione predefinita,[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)è applicato per tutte le versioni. Per alcune situazioni, come la creazione di una cartella di lavoro con un set di dati di grandi dimensioni per le celle, il file[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)opzione può ottimizzare l'uso della memoria e diminuire il costo della memoria per l'applicazione. Tuttavia, questa opzione potrebbe peggiorare le prestazioni in alcuni casi speciali come follow.

1. **Accesso allo Cells in modo casuale e ripetuto** : La sequenza più efficiente per accedere alla raccolta di celle è cella per cella in una riga, quindi riga per riga. Soprattutto se accedi a righe/celle dall'enumeratore acquisito da[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) e[**Riga**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) , le prestazioni sarebbero massimizzate con[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE).
1. **Inserimento e cancellazione Cells e righe** : Si prega di notare che se ci sono molte operazioni di inserimento/cancellazione per Cells/Rows, il degrado delle prestazioni sarà notevole per[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) modalità rispetto alla[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)modalità.
1. **Funzionante su diversi tipi Cell** : Se la maggior parte delle celle contiene valori stringa o formule, il costo della memoria sarà lo stesso di[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)mode ma se ci sono molte celle vuote o i valori delle celle sono numerici, bool e così via, il[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)l'opzione darà prestazioni migliori.

