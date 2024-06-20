---
title: Nomi delle celle
type: docs
weight: 40
url: /it/java/named-ranges/
---

{{% alert color="primary" %}} 

Normalmente, etichette di riga e colonna vengono utilizzate per fare riferimento a singole celle. È possibile creare nomi descrittivi per rappresentare celle, intervalli di celle, formule o valori costanti. La parola **nome** può fare riferimento a una serie di caratteri che rappresentano una cella, un intervallo di celle, una formula o un valore costante. Assegnare un nome a un intervallo significa che quel gruppo di celle può essere identificato dal suo nome. Utilizzare nominativi semplici da capire, come ad esempio Prodotti, per riferirsi a intervalli difficili da capire, come Vendite!C20:C30. Le etichette possono essere usate in formule che fanno riferimento a dati sullo stesso foglio di lavoro; se si vuole rappresentare un intervallo su un altro foglio di lavoro, è possibile utilizzare un nome. *Le aree denominate sono tra le funzionalità più potenti di Microsoft Excel, specialmente quando usate come intervallo di origine per i controlli di elenchi, le tabelle pivot, i grafici e così via.

{{% /alert %}} 
## **Creazione di un intervallo denominato**
### **Utilizzando Microsoft Excel**
I seguenti passaggi descrivono come dare un nome a una cella o a un intervallo di celle utilizzando Microsoft Excel. Questo metodo si applica a Microsoft Office Excel 2003, Microsoft Excel 97, 2000 e 2002.

1. Seleziona la cella o l'intervallo di celle che desideri nominare.
1. Fare clic sulla casella Nome all'estremità sinistra della barra della formula.
1. Digita il nome delle celle.
1. Premi INVIO.

{{% alert color="primary" %}} 

Non è possibile nominare una cella mentre si sta modificando il contenuto della cella.

{{% /alert %}} 
### **Usare Aspose.Cells**
Qui, utilizziamo l'API Aspose.Cells per svolgere il compito.

Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file di Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) che consente l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce una raccolta [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).

È possibile creare un intervallo nominato chiamando il metodo sovraccarico [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) della raccolta [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Una versione tipica del metodo [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) richiede i seguenti parametri:

- Nome della cella in alto a sinistra, il nome della cella in alto a sinistra nell'intervallo.
- Nome della cella in basso a destra, il nome della cella in basso a destra nell'intervallo.

Quando il metodo [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) viene chiamato, restituisce il nuovo intervallo nominato creato come un'istanza della classe [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range).

L'esempio seguente mostra come creare un intervallo nominato di celle che si estende su B4:G14.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **Accesso a Tutti gli Intervalli Nominati in un Foglio di Calcolo**
Chiamare il metodo [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\)) della [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) per ottenere tutti gli intervalli nominati in un foglio di calcolo. Il metodo [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\)) restituisce un array di tutti gli intervalli nominati nella [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection).

L'esempio seguente mostra come accedere a tutti i nomi definiti in un libro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **Accedi a un intervallo nominato specifico**
Chiamare il metodo [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\)) della raccolta [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) per ottenere un intervallo specificato per nome. Una tipica versione di [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\)) richiede il nome dell'intervallo nominato e restituisce l'intervallo nominato specificato come un'istanza della classe [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range).

L'esempio seguente mostra come accedere a un intervallo specifico tramite il relativo nome.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **Identificare le Celle in un Intervallo Nominato**
Usando Aspose.Cells, è possibile inserire dati nelle singole celle di un intervallo. Supponiamo di avere un intervallo di celle nominato, ad esempio A1:C4. Così la matrice avrebbe 4 * 3 = 12 celle e le celle dell'intervallo sono disposte in modo sequenziale. Aspose.Cells fornisce alcune utili proprietà della classe [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) per accedere alle singole celle nell'intervallo. È possibile utilizzare i seguenti metodi per identificare le celle nell'intervallo:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) restituisce l'indice della prima riga nell'intervallo nominato.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) restituisce l'indice della prima colonna nell'intervallo nominato.

L'esempio seguente mostra come inserire alcuni valori nelle celle di un intervallo specificato.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **Inserimento dei dati nelle celle dell'intervallo nominato**
Usando Aspose.Cells, è possibile inserire dati nelle singole celle di un intervallo. Supponiamo di avere un intervallo di celle nominato, ad esempio H1:J4. Quindi la matrice avrebbe 4 * 3 = 12 celle e le celle dell'intervallo sono disposte in modo sequenziale. Aspose.Cells fornisce alcune utili proprietà della classe [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) per accedere alle singole celle nell'intervallo. È possibile utilizzare le seguenti proprietà per identificare le celle nell'intervallo:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) restituisce l'indice della prima riga nell'intervallo nominato.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) restituisce l'indice della prima colonna nell'intervallo nominato.

L'esempio seguente mostra come inserire alcuni valori nelle celle di un intervallo specificato.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **Formato degli intervalli... Impostazione del colore di sfondo e degli attributi del carattere per un intervallo nominato**
Per applicare la formattazione, definire un oggetto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) per specificare le impostazioni dello stile e applicarlo all'oggetto [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range).

L'esempio seguente mostra come impostare un colore di riempimento solido (colore di ombreggiatura) con le impostazioni del carattere a un intervallo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **Formato degli intervalli... Aggiunta di bordi a un intervallo nominato**
È possibile aggiungere bordi a un intervallo di celle anziché a una singola cella. L'oggetto [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) fornisce un metodo [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) che richiede i seguenti parametri per aggiungere un bordo all'intervallo di celle:

- borderStyle: il tipo di bordo, selezionato dall'enumerazione [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).
- borderColor: il colore della linea del bordo, selezionato dall'enumerazione [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color).

L'esempio seguente mostra come impostare un bordo di contorno a un intervallo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


Il seguente output verrebbe generato dopo l'esecuzione del codice precedente: 

![todo:image_alt_text](named-ranges_1.png)
#### **Applicare uno stile alle celle in un intervallo**
A volte si desidera applicare uno stile alle celle in un [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range). Per fare ciò, è possibile iterare sulle celle nell'intervallo e utilizzare il metodo [Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) per applicare lo stile alla cella.

L'esempio seguente mostra come applicare stili alle celle in un intervallo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **Rimuovere un intervallo nominato**
Aspose.Cells fornisce il metodo [NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\)) per cancellare il nome dell'intervallo. Per cancellare i contenuti dell'intervallo, utilizzare il metodo [Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\)).
L'esempio seguente mostra come rimuovere un intervallo nominato con i relativi contenuti.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


borderColors 
