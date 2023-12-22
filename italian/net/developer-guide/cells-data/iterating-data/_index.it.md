---
title: Come e dove utilizzare gli enumeratori
linktitle: Iterazione dei dati
type: docs
weight: 55
url: /it/net/how-and-where-to-use-enumerators/
description: Scopri come e dove utilizzare gli enumeratori tramite il numero Aspose.Cells for .NET API.
keywords: How to use Enumerators, Cells Enumerator, Rows Enumerator, Columns Enumerator
---
{{% alert color="primary" %}}

Un enumeratore è un oggetto che offre la possibilità di attraversare un contenitore o una raccolta. Gli enumeratori possono essere utilizzati per leggere i dati nella raccolta, ma non possono essere utilizzati per modificare la raccolta sottostante, mentre IEnumerable è un'interfaccia che definisce un metodo GetEnumerator che restituisce un'interfaccia IEnumerator, questa, a sua volta, consente l'accesso in sola lettura a una collezione.

Aspose.Cells Le API forniscono una serie di enumeratori, tuttavia questo articolo discute principalmente i tre tipi elencati di seguito.

1. Cells Enumeratore
1. Enumeratore di righe
1. Enumeratore di colonne

{{% /alert %}}

##  **Come utilizzare gli enumeratori**

###  **Cells Enumeratore**

Esistono vari modi per accedere all'enumeratore Cells ed è possibile utilizzare uno qualsiasi di questi metodi in base ai requisiti dell'applicazione. Ecco i metodi che restituiscono l'enumeratore di celle.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

Tutti i metodi sopra menzionati restituiscono l'enumeratore che consente di attraversare la raccolta di celle che sono state inizializzate.

{{% alert color="primary" %}}

Durante l'attraversamento delle celle, la raccolta non deve essere modificata (operazioni che comportino l'istanziazione di un nuovo Cell o la cancellazione di Cell esistente). In caso contrario, l'enumeratore potrebbe non essere in grado di attraversare correttamente tutte le celle (alcuni elementi potrebbero essere attraversati ripetutamente o ignorati).

{{% /alert %}}

Nell'esempio di codice seguente viene illustrata l'implementazione dell'interfaccia IEnumerator per una raccolta Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

###  **Enumeratore di righe**

 È possibile accedere all'enumeratore di righe durante l'utilizzo di[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) metodo. Nell'esempio di codice seguente viene illustrata l'implementazione dell'interfaccia IEnumerator per[**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

###  **Enumeratore di colonne**

 È possibile accedere all'enumeratore di colonne durante l'utilizzo di[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) metodo. Nell'esempio di codice seguente viene illustrata l'implementazione dell'interfaccia IEnumerator per[**ColonnaCollezione**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

##  **Dove utilizzare gli enumeratori**

Per discutere i vantaggi derivanti dall'utilizzo degli enumeratori, prendiamo un esempio in tempo reale.

**Scenario**

 Un requisito dell'applicazione è attraversare tutte le celle in un dato[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)leggere i loro valori. Potrebbero esserci diversi modi per realizzare questo obiettivo. Alcuni sono dimostrati di seguito.

###  **Utilizzo dell'intervallo di visualizzazione**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

###  **Utilizzo di MaxDataRow e MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

Come puoi osservare, entrambi gli approcci sopra menzionati utilizzano una logica più o meno simile, cioè; eseguire il loop su tutte le celle della raccolta per leggere i valori delle celle. Ciò potrebbe essere problematico per una serie di motivi, come discusso di seguito.

1.  API come[**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**Colonna massima**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**ColonnaDatiMax**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**Intervallo di visualizzazione massimo**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)richiedono più tempo per raccogliere le statistiche corrispondenti. Nel caso in cui la matrice dei dati (righe x colonne) sia di grandi dimensioni, l'utilizzo di queste API potrebbe comportare una riduzione delle prestazioni.
1. Nella maggior parte dei casi, non tutte le celle in un dato intervallo vengono istanziate. In tali situazioni controllare ogni cella della matrice non è così efficiente rispetto a controllare solo le celle inizializzate.
1. L'accesso a una cella in un ciclo come riga Cells, colonna causerà la creazione di un'istanza di tutti gli oggetti cella in un intervallo, il che potrebbe eventualmente causare OutOfMemoryException.

##  **Conclusione**

Sulla base dei fatti sopra menzionati, di seguito sono riportati i possibili scenari in cui dovrebbero essere utilizzati gli enumeratori.

1. È richiesto l'accesso in sola lettura alla raccolta di celle; il requisito è quello di ispezionare solo le celle.
1. È necessario attraversare un gran numero di celle.
1. Solo le celle/righe/colonne inizializzate da attraversare.
