---
title: Come e dove utilizzare gli iteratori
linktitle: Iterare i dati
type: docs
weight: 640
url: /it/java/how-and-where-to-use-iterators/
---

{{% alert color="primary" %}} 

Un oggetto di un'interfaccia di iteratore può essere utilizzato per attraversare tutti gli elementi di una collezione. Gli iteratori possono essere utilizzati per ispezionare i dati in una collezione, ma non possono essere utilizzati per modificare la collezione sottostante. In generale, per utilizzare un iteratore per ciclare attraverso i contenuti di una collezione, devono essere seguiti i seguenti passaggi:

1. Ottenere un iteratore all'inizio della collezione chiamando il metodo iteratore della collezione.
1. Impostare un ciclo che effettua una chiamata al metodo hasNext. Fare in modo che il ciclo si ripeta finché il metodo hasNext restituisce true.
1. All'interno del ciclo, ottenere ciascun elemento chiamando il metodo successivo.

Le API di Aspose.Cells forniscono un insieme di iteratori, tuttavia, questo articolo discute principalmente i tre tipi di seguito elencati.

1. Iteratore celle
1. Iteratore righe
1. Iteratore colonne

{{% /alert %}} 
## **Come utilizzare gli iteratori**
### **Iteratore celle**
Ci sono vari modi per accedere all'iteratore delle celle, e si può utilizzare uno qualsiasi di questi metodi in base alle esigenze dell'applicazione. Ecco i metodi che restituiscono l'iteratore delle celle.

1. Cells.iterator
1. Row.iterator
1. Range.iterator

Tutti i metodi sopra menzionati restituiscono l'iteratore che consente di attraversare la collezione di celle che sono state inizializzate.

{{% alert color="primary" %}} 

Durante il attraversamento delle celle, la collezione non dovrebbe essere modificata (operazioni che causerebbero l'istanziazione di una nuova Cell o la cancellazione di una Cell esistente). Altrimenti l'iteratore potrebbe non essere in grado di attraversare correttamente tutte le celle (alcuni elementi potrebbero essere attraversati ripetutamente o saltati).

{{% /alert %}} 

L'esempio di codice seguente dimostra l'implementazione della classe Iterator per una collezione di celle.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **Iteratore delle righe**
L'Iteratore delle righe può essere accessibile utilizzando il metodo RowCollection.iterator. L'esempio di codice seguente dimostra l'implementazione dell'Iterator per la classe RowCollection.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **Iteratore delle colonne**
L'Iteratore delle colonne può essere accessibile utilizzando il metodo ColumnCollection.iterator. L'esempio di codice seguente dimostra l'implementazione dell'Iteratore per la classe ColumnCollection.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **Dove utilizzare gli iteratori**
Per discutere i vantaggi dell'utilizzo degli iteratori, prendiamo un esempio in tempo reale.
##### **Scenario**
Un requisito dell'applicazione è attraversare tutte le celle in un dato Foglio di lavoro per leggere i loro valori. Potrebbero esserci diversi modi per implementare questo obiettivo. Ne vengono dimostrati alcuni di seguito.
###### **Utilizzo della gamma di visualizzazione**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **Utilizzo di MaxDataRow e MaxDataColumn**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





Come puoi osservare, entrambi i suddetti approcci utilizzano più o meno la stessa logica, cioè; iterare su tutte le celle nella collezione per leggere i valori delle celle. Questo potrebbe essere problematico per diversi motivi come discusso di seguito.

1. Le API come MaxRow, MaxDataRow, MaxColumn, MaxDataColumn e MaxDisplayRange richiedono tempo aggiuntivo per raccogliere le statistiche corrispondenti. Nel caso la matrice dei dati (righe x colonne) sia ampia, utilizzare queste API potrebbe infliggere una penalità sulle prestazioni.
1. Nella maggior parte dei casi, non tutte le celle in un dato intervallo sono istanziate. In tali situazioni controllare ogni cella nella matrice non è così efficiente rispetto al controllo solo delle celle inizializzate.
1. L'accesso a una cella in un ciclo come Cells.get(rowIndex, columnIndex) causerà l'istanziazione di tutti gli oggetti cella in un intervallo, il che potrebbe alla fine causare OutOfMemoryError.
##### **Conclusioni**
Sulla base dei fatti sopra menzionati, di seguito sono riportati i possibili scenari in cui dovrebbero essere utilizzati gli iteratori.

1. È richiesto l'accesso in sola lettura della raccolta di celle, cioè; il requisito è solo ispezionare le celle.
1. È necessario attraversare un grande numero di celle.
1. Devono essere attraversate solo celle/righe/colonne inizializzate.
{{< app/cells/assistant language="java" >}}
