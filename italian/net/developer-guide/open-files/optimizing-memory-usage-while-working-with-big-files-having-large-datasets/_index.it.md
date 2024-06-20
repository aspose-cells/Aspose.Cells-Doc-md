---
title: Ottimizzazione dell uso della memoria durante il lavoro con grandi file contenenti grandi set di dati
type: docs
weight: 180
url: /it/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Quando si costruisce un workbook con grandi set di dati o si legge un grande file Microsoft Excel, la quantità totale di RAM che il processo richiederà è sempre una preoccupazione. Esistono misure che possono essere adottate per far fronte alla sfida. Aspose.Cells fornisce alcune opzioni rilevanti e chiamate API per ridurre e ottimizzare l'uso della memoria. Inoltre, può aiutare il processo a lavorare in modo più efficiente e più veloce.

Usa l'opzione [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) per ottimizzare l'uso della memoria per i dati delle celle e diminuire il costo complessivo della memoria. Quando si costruisce un ampio set di dati per le celle, può risparmiare una certa quantità di memoria rispetto all'utilizzo dell'impostazione predefinita ([**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)).

{{% /alert %}}

## **Ottimizzazione della Memoria**

### **Lettura di File Excel di Grandi Dimensioni**

L'esempio seguente mostra come leggere un grande file Microsoft Excel in modalità ottimizzata.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **Scrittura di file Excel di grandi dimensioni**

L'esempio seguente mostra come scrivere un ampio dataset in un foglio di lavoro in modalità ottimizzata.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **Attenzione**

L'opzione predefinita, [**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) è applicata per tutte le versioni. Per alcune situazioni, come la costruzione di un workbook con un ampio set di dati per le celle, l'opzione [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) può ottimizzare l'uso della memoria e ridurre il costo della memoria dell'applicazione. Tuttavia, questa opzione può degradare le prestazioni in alcuni casi speciali come segue.

1. **Accesso Casuale e Ripetuto alle Celle**: La sequenza più efficiente per accedere alla collezione di celle è cella per cella in una riga e poi riga per riga. In particolare, se si accedono alle righe/celle tramite l'Enumerator acquisito da [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection) e [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row), le prestazioni sarebbero massimizzate con [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting).
1. **Inserimento ed eliminazione di celle e righe**: Si noti che se ci sono molte operazioni di inserimento/eliminazione per Celle/Righe, la degradazione delle prestazioni sarà notevole per la modalità *MemoryPreference* rispetto alla modalità *Normale*.
1. **Operare su diversi tipi di celle**: Se la maggior parte delle celle contiene valori di stringa o formule, il costo della memoria sarà lo stesso della modalità *Normale*, ma se ci sono molte celle vuote, o i valori delle celle sono numerici, booleani e così via, l'opzione [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) darà migliori prestazioni.
