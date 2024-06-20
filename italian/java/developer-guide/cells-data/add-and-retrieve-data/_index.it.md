---
title: Aggiungere e recuperare dati
type: docs
weight: 20
url: /it/java/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

In [Accessing Cells of a Worksheet](/cells/it/java/accessing-cells-of-a-worksheet/), abbiamo discusso gli approcci di base per accedere alle celle in un foglio di lavoro. Questo articolo utilizza uno di quegli approcci per aggiungere diversi tipi di dati alle celle

{{% /alert %}} 
## **Aggiunta di dati alle celle**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che permette l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce una collezione di [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Ogni elemento della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) rappresenta un oggetto della classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)

Aspose.Cells permette ai programmatori di aggiungere dati alle celle nei fogli di lavoro chiamando la proprietà [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) della classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell). Utilizzando la proprietà [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value), è possibile aggiungere valori booleani, stringhe, double, interi o data/ora, ecc. alla cella.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **Miglioramento dell'efficienza**
{{% alert color="primary" %}} 

Se si utilizza la proprietà [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) per aggiungere una grande quantità di dati a un foglio di lavoro, è opportuno aggiungere i valori alle celle prima per righe e poi per colonne. Questo approccio migliora notevolmente l'efficienza delle applicazioni.

{{% /alert %}} 

Mentre si lavora sui fogli di lavoro, gli utenti possono aggiungere diversi tipi di dati alle celle. Questi elementi di dati possono includere valori booleani, interi, in virgola mobile, testo o valori di data/ora. È possibile ottenere i valori appropriati dalle celle in base ai rispettivi tipi di dati utilizzando Aspose.Cells
## **Recupero dei dati dalle celle**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) che rappresenta un file Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce una raccolta di [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Ciascun elemento nella raccolta di [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) rappresenta un oggetto della classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

La classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) fornisce diverse proprietà che consentono ai programmatori di recuperare i valori dalle celle in base ai rispettivi tipi di dati. Queste proprietà includono:

- [StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue), il valore stringa della cella.
- [DoubleValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue), restituisce il valore double della cella.
- [BoolValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue), il valore booleano della cella.
- [DateTimeValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue), il valore data/ora della cella.
- [FloatValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue), il valore float della cella.
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue), il valore intero della cella.

Inoltre, il tipo di dati contenuti in una cella può essere controllato utilizzando la proprietà [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) della classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell). In realtà, la proprietà [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) della classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) si basa sull'enumerazione [CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType) i cui valori predefiniti sono elencati di seguito:

|**Tipi di Valore della Cella**|**Descrizione**|
| :- | :- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)| Specifica che il valore della cella è booleano.
|[IS_DATE_TIME](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)| Specifica che il valore della cella è data/ora.
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)| Rappresenta che la cella contiene un valore di errore.
|[IS_NULL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)| Rappresenta una cella vuota.
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)| Specifica che il valore della cella è numerico.
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)| Specifica che il valore della cella è una stringa.
|[IS_UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)| Specifica che il valore della cella è sconosciuto.
È inoltre possibile utilizzare i tipi di valore predefiniti della cella sopra elencati per confrontare il tipo di dati presente in ciascuna cella.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
