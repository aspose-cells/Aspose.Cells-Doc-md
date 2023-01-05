---
title: Come e dove usare gli iteratori
linktitle: Iterare i dati
type: docs
weight: 640
url: /it/java/how-and-where-to-use-iterators/
---
{{% alert color="primary" %}} 

Un oggetto di un'interfaccia iteratore può essere utilizzato per attraversare tutti gli elementi di una raccolta. Gli iteratori possono essere utilizzati per ispezionare i dati in una raccolta, ma non possono essere utilizzati per modificare la raccolta sottostante. In generale, per utilizzare un iteratore per scorrere i contenuti di una raccolta, è necessario eseguire i seguenti passaggi:

1. Ottenere un iteratore all'inizio della raccolta chiamando il metodo iteratore della raccolta.
1. Imposta un ciclo che effettua una chiamata al metodo hasNext. Fai iterare il ciclo finché il metodo hasNext restituisce true.
1. All'interno del ciclo, ottenere ogni elemento chiamando il metodo next.

Aspose.Cells Le API forniscono una serie di iteratori, tuttavia, questo articolo discute principalmente i tre tipi elencati di seguito.

1. Cells Iteratore
1. Iteratore di righe
1. Iteratore di colonne

{{% /alert %}} 
## **Come usare gli iteratori**
### **Cells Iteratore**
Esistono vari modi per accedere all'iteratore delle celle e si può utilizzare uno qualsiasi di questi metodi in base ai requisiti dell'applicazione. Ecco i metodi che restituiscono l'iteratore delle celle.

1. Cells.iterator
1. Riga.iteratore
1. Intervallo.iteratore

Tutti i metodi sopra citati restituiscono l'iteratore che permette di attraversare la collezione di celle che sono state inizializzate.

{{% alert color="primary" %}} 

Durante l'attraversamento delle celle, la raccolta non deve essere modificata (operazioni che causeranno l'istanziazione di un nuovo Cell o l'eliminazione di Cell esistente). In caso contrario, l'iteratore potrebbe non essere in grado di attraversare correttamente tutte le celle (alcuni elementi potrebbero essere attraversati ripetutamente o ignorati).

{{% /alert %}} 

Nell'esempio di codice seguente viene illustrata l'implementazione della classe Iterator per una raccolta di celle.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **Iteratore di righe**
È possibile accedere a Rows Iterator durante l'utilizzo del metodo RowCollection.iterator. Nell'esempio di codice seguente viene illustrata l'implementazione della classe Iterator per RowCollection.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **Iteratore di colonne**
È possibile accedere a Columns Iterator durante l'utilizzo del metodo ColumnCollection.iterator. Nell'esempio di codice seguente viene illustrata l'implementazione della classe Iterator per ColumnCollection.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **Dove usare gli iteratori**
Per discutere i vantaggi dell'utilizzo degli iteratori, facciamo un esempio in tempo reale.
##### **Scenario**
Un requisito dell'applicazione è attraversare tutte le celle in un determinato foglio di lavoro per leggerne i valori. Ci potrebbero essere diversi modi per implementare questo obiettivo. Alcuni sono dimostrati di seguito.
###### **Utilizzo dell'intervallo di visualizzazione**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **Utilizzo di MaxDataRow e MaxDataColumn**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





Come puoi osservare, entrambi gli approcci sopra menzionati utilizzano una logica più o meno simile, ovvero; eseguire il ciclo su tutte le celle della raccolta per leggere i valori delle celle. Questo potrebbe essere problematico per una serie di motivi come discusso di seguito.

1. Le API come MaxRow, MaxDataRow, MaxColumn, MaxDataColumn e MaxDisplayRange richiedono più tempo per raccogliere le statistiche corrispondenti. Nel caso in cui la matrice di dati (righe x colonne) sia grande, l'utilizzo di queste API potrebbe imporre una riduzione delle prestazioni.
1. Nella maggior parte dei casi, non tutte le celle in un determinato intervallo vengono istanziate. In tali situazioni controllare ogni cella della matrice non è così efficiente rispetto a controllare solo le celle inizializzate.
1. L'accesso a una cella in un ciclo come Cells.get(rowIndex, columnIndex) causerà la creazione di un'istanza di tutti gli oggetti cella in un intervallo, che alla fine potrebbe causare OutOfMemoryError.
##### **Conclusione**
Sulla base dei fatti sopra menzionati, di seguito sono riportati i possibili scenari in cui è necessario utilizzare gli iteratori.

1. È richiesto l'accesso in sola lettura della raccolta di celle, ovvero; requisito è quello di ispezionare solo le cellule.
1. È necessario attraversare un gran numero di celle.
1. Devono essere attraversate solo celle/righe/colonne inizializzate.
