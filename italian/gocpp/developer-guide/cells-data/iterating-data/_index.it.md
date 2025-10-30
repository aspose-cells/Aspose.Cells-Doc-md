---
title: Come e dove usare gli enumeratori con Golang tramite C++
linktitle: Iterare i dati
type: docs
weight: 55
url: /it/go-cpp/how-and-where-to-use-enumerators/
description: Impara come Come e Dove Usare gli Enumeratori tramite l API Aspose.Cells for C++.
keywords: Come utilizzare gli enumeratori, enumeratore celle, enumeratore righe, enumeratore colonne
---

{{% alert color="primary" %}}

 Un enumeratore è un oggetto che consente di attraversare un contenitore o una collezione. Gli enumeratori possono essere usati per leggere i dati nella collezione, ma non possono essere usati per modificare la collezione sottostante, mentre IEnumerable è un'interfaccia che definisce un metodo GetEnumerator che restituisce un'interfaccia IEnumerator, che, a sua volta, permette l'accesso in sola lettura a una collezione.

Le API di Aspose.Cells forniscono una serie di enumeratori, tuttavia, questo articolo discute principalmente dei tre tipi come di seguito elencati.

1. Enumeratore celle
1. Enumeratore righe
1. Enumeratore colonne

{{% /alert %}}

## **Come utilizzare gli enumeratori**

### **Enumeratore celle**

Esistono vari modi per accedere all'enumeratore delle celle, e si può utilizzare uno qualsiasi di questi metodi in base ai requisiti dell'applicazione. Ecco i metodi che restituiscono l'enumeratore delle celle.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/range/getenumerator/)

Tutti i metodi sopra menzionati restituiscono l'enumeratore che consente di attraversare la raccolta di celle che sono state inizializzate.

{{% alert color="primary" %}}

Durante il passaggio delle celle, la raccolta non dovrebbe essere modificata (operazioni che causeranno l'istantanea di una nuova Cell o la cancellazione di una Cell esistente). In caso contrario, l'enumeratore potrebbe non essere in grado di attraversare correttamente tutte le celle (alcuni elementi potrebbero essere attraversati più volte o saltati).

{{% /alert %}}

Nell'esempio di codice seguente viene dimostrata l'implementazione dell'interfaccia IEnumerator per una raccolta di celle.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData.go" >}}
### **Enumeratore di righe**

 L'Enumerator delle Righe può essere accesso durante l'utilizzo del metodo [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/rowcollection/getenumerator/). Il seguente esempio di codice dimostra l'implementazione dell'interfaccia IEnumerator per [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-1.go" >}}
### ** Ottieni Colonne Get**

 Le Colonne possono essere accesso durante l'utilizzo del metodo [**ColumnCollection.Get**](https://reference.aspose.com/cells/go-cpp/columncollection/get/). Il seguente esempio di codice dimostra l'implementazione del metodo Get per [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-2.go" >}}
## **Dove utilizzare gli enumeratori**

Per discutere i vantaggi dell'uso degli enumeratori, prendiamo un esempio in tempo reale.

**Scenario**

 Un requisito dell'applicazione è attraversare tutte le celle di un [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) dato per leggere i loro valori. Potrebbero esserci diversi modi per implementare questo obiettivo. Alcuni sono dimostrati di seguito.

### **Utilizzo della gamma di visualizzazione**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-3.go" >}}
### **Utilizzo di MaxDataRow e MaxDataColumn**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-4.go" >}}
Come puoi osservare, entrambi gli approcci sopra menzionati utilizzano più o meno una logica simile, cioè; attraversa tutte le celle nella raccolta per leggere i valori delle celle. Questo potrebbe essere problematico per un certo numero di motivi come discusso di seguito.

1. API come [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/cells/getmaxrow/), [**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/), [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/), [**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) & [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) richiedono tempo extra per raccogliere le statistiche corrispondenti. Nel caso in cui la matrice di dati (righe x colonne) sia grande, utilizzare queste API potrebbe influire sulle prestazioni.
1. Nella maggior parte dei casi, non tutte le celle in un dato intervallo sono istanziate. In tali situazioni controllare ogni cella nella matrice non è così efficiente rispetto al controllo solo delle celle inizializzate.
1. Accedere a una cella in un ciclo come celle riga, colonna farà istanziare tutti gli oggetti cella in un intervallo, che potrebbe alla fine causare OutOfMemoryException.

## **Conclusioni**

Sulla base dei fatti sopra menzionati, di seguito sono riportati i possibili scenari in cui dovrebbero essere utilizzati gli enumeratori.

1. È richiesto l'accesso in sola lettura alla collezione di celle, cioè; il requisito è di ispezionare solo le celle.
1. Deve essere attraversato un gran numero di celle.
1. Si devono attraversare solo le celle/righe/colonne inizializzate.
