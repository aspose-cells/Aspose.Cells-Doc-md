---
title: Ottimizzazione dell uso della memoria durante il lavoro con grandi file contenenti grandi set di dati
type: docs
weight: 110
url: /it/nodejs-java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Quando si costruisce un foglio di lavoro con grandi set di dati, o si legge un file di Microsoft Excel di grandi dimensioni, la quantità totale di RAM che il processo occuperà è sempre una preoccupazione. Ci sono misure che possono essere adattate per far fronte alla sfida. Aspose.Cells fornisce alcune opzioni rilevanti e chiamate API per ridurre, diminuire e ottimizzare l'uso della memoria. Inoltre, può aiutare il processo a lavorare in modo più efficiente e veloce.

Utilizzare l'opzione [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) per ottimizzare la memoria utilizzata per i dati delle celle al fine di ridurre il costo complessivo della memoria. Quando si costruisce un grande set di dati per le celle, può risparmiare una certa quantità di memoria rispetto all'utilizzo dell'impostazione predefinita [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **Ottimizzazione della Memoria**

L'esempio seguente mostra come ottimizzare l'uso della memoria durante il lavoro con grandi dati in Aspose.Cells for Node.js via Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-nodejs-optimize-memory-usage-while-working-with-large-data.java" >}}

## **Attenzione**

L'opzione predefinita, [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) è applicata per tutte le versioni. Per alcune situazioni, come la costruzione di un workbook con un grande set di dati per le celle, l'opzione [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) potrebbe ottimizzare l'uso della memoria e ridurre il costo della memoria per l'applicazione. Tuttavia, questa opzione potrebbe degradare le prestazioni in alcuni casi speciali come segue.

1. **Accesso Casuale e Ripetuto alle Celle**: La sequenza più efficiente per accedere alla collezione di celle è cella per cella in una riga e poi riga per riga. In particolare, se si accedono alle righe/celle tramite l'Enumerator acquisito da [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) e [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row), le prestazioni sarebbero massimizzate con [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE).
1. **Inserimento ed Eliminazione di Celle e Righe**: Si noti che se ci sono molte operazioni di inserimento/eliminazione per Celle/Righe, la degradazione delle prestazioni sarà notabile per la modalità [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) rispetto alla modalità [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).
1. **Operare su Diversi Tipi di Celle**: Se la maggior parte delle celle contiene valori di stringa o formule, il costo della memoria sarà lo stesso della modalità [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) ma se ci sono molte celle vuote o i valori delle celle sono numerici, bool e così via, l'opzione [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) offrirà migliori prestazioni.

