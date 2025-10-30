---
title: Ottimizzazione dell uso della memoria durante il lavoro con grandi file contenenti grandi set di dati
type: docs
weight: 180
url: /it/python-net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Quando si crea un workbook con grandi set di dati o si legge un grande file Microsoft Excel, la quantità totale di RAM richiesta dal processo è sempre una preoccupazione. Ci sono misure che possono essere adottate per gestire questa sfida. Aspose.Cells per Python via .NET offre opzioni e chiamate API rilevanti per ridurre, ottimizzare e migliorare l’uso della memoria. Inoltre, può aiutare il processo a funzionare più efficacemente e più velocemente.

Usa l'opzione [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) per ottimizzare l'uso della memoria per i dati delle celle e diminuire il costo complessivo della memoria. Quando si costruisce un ampio set di dati per le celle, può risparmiare una certa quantità di memoria rispetto all'utilizzo dell'impostazione predefinita ([**MemorySetting.NORMAL**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting)).

{{% /alert %}}

## **Ottimizzazione della Memoria**

### **Lettura di File Excel di Grandi Dimensioni**

L'esempio seguente mostra come leggere un grande file Microsoft Excel in modalità ottimizzata.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.py" >}}

### **Scrittura di file Excel di grandi dimensioni**

L'esempio seguente mostra come scrivere un ampio dataset in un foglio di lavoro in modalità ottimizzata.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OptimizingMemoryUsage-WritingLargeExcelFiles-1.py" >}}

## **Attenzione**

L'opzione predefinita, [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) è applicata per tutte le versioni. Per alcune situazioni, come la costruzione di un workbook con un ampio set di dati per le celle, l'opzione [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) può ottimizzare l'uso della memoria e ridurre il costo della memoria dell'applicazione. Tuttavia, questa opzione può degradare le prestazioni in alcuni casi speciali come segue.

1. **Accesso Casuale e Ripetuto alle Celle**: La sequenza più efficiente per accedere alla collezione di celle è cella per cella in una riga e poi riga per riga. In particolare, se si accedono alle righe/celle tramite l'Enumerator acquisito da [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), [**RowCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/rowcollection) e [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row), le prestazioni sarebbero massimizzate con [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting).
1. **Inserimento ed eliminazione di celle e righe**: Si noti che se ci sono molte operazioni di inserimento/eliminazione per Celle/Righe, la degradazione delle prestazioni sarà notevole per la modalità *MemoryPreference* rispetto alla modalità *Normale*.
1. **Operare su diversi tipi di celle**: Se la maggior parte delle celle contiene valori di stringa o formule, il costo della memoria sarà lo stesso della modalità *Normale*, ma se ci sono molte celle vuote, o i valori delle celle sono numerici, booleani e così via, l'opzione [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) darà migliori prestazioni.

{{< app/cells/assistant language="python-net" >}}
