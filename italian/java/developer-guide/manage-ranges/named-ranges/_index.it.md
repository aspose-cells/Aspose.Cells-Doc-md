---
title: Intervalli denominati
type: docs
weight: 40
url: /it/java/named-ranges/
---
{{% alert color="primary" %}} 

Normalmente, le etichette di colonna e riga vengono utilizzate per fare riferimento a singole celle. È possibile creare nomi descrittivi per rappresentare celle, intervalli di celle, formule o valori costanti. La parola**nome** può fare riferimento a una stringa di caratteri che rappresenta una cella, un intervallo di celle, una formula o un valore costante. Assegnare un nome a un intervallo significa che quell'intervallo di celle può essere indicato con il suo nome. Utilizzare nomi di facile comprensione, ad esempio Prodotti, per fare riferimento a intervalli di difficile comprensione, ad esempio Vendite!C20:C30. Le etichette possono essere utilizzate in formule che fanno riferimento a dati sullo stesso foglio di lavoro; se vuoi rappresentare un intervallo su un altro foglio di lavoro, puoi usare un nome. *Gli intervalli denominati sono tra le funzionalità più potenti di Microsoft Excel, soprattutto se utilizzati come intervallo di origine per controlli elenco, tabelle pivot, grafici e così via.

{{% /alert %}} 
## **Creazione di un intervallo denominato**
### **Utilizzando Microsoft Excel**
passaggi seguenti descrivono come denominare una cella o un intervallo di celle utilizzando Microsoft Excel. Questo metodo si applica a Microsoft Office Excel 2003, Microsoft Excel 97, 2000 e 2002.

1. Selezionare la cella, l'intervallo di celle a cui si desidera assegnare un nome.
1. Fare clic sulla casella del nome all'estremità sinistra della barra della formula.
1. Digitare il nome delle celle.
1. Premere Invio.

{{% alert color="primary" %}} 

Non puoi nominare una cella mentre stai modificando il contenuto della cella.

{{% /alert %}} 
### **Utilizzando Aspose.Cells**
Qui, usiamo lo Aspose.Cells API per svolgere l'attività.

 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) la classe fornisce a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collezione.

 È possibile creare un intervallo denominato chiamando l'overloaded[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ) metodo del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collezione. Una versione tipica del[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) accetta i seguenti parametri:

- Nome della cella in alto a sinistra, il nome della cella in alto a sinistra nell'intervallo.
- Nome della cella in basso a destra, il nome della cella in basso a destra nell'intervallo.

 Quando il[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ) viene chiamato, restituisce l'intervallo denominato appena creato come istanza di[Allineare](https://reference.aspose.com/cells/java/com.aspose.cells/range) classe.

L'esempio seguente mostra come creare un intervallo denominato di celle che si estende su B4:G14.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **Accesso a tutti gli intervalli denominati in un foglio di calcolo**
 Chiama il[getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) ) metodo del[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) per ottenere tutti gli intervalli denominati in un foglio di calcolo. Il[getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) ) restituisce un array di tutti gli intervalli denominati nel file[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection).

L'esempio seguente mostra come accedere a tutti gli intervalli denominati in una cartella di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **Accedi a un intervallo denominato specifico**
 Chiama il[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) della collezione[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) ) per ottenere un intervallo specificato per nome. Un tipico[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) ) prende il nome dell'intervallo denominato e restituisce l'intervallo denominato specificato come istanza di[Allineare](https://reference.aspose.com/cells/java/com.aspose.cells/range)classe.

L'esempio seguente mostra come accedere a un intervallo specificato in base al relativo nome.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **Identificare Cells in un intervallo denominato**
Utilizzando Aspose.Cells, è possibile inserire dati nelle singole celle di un intervallo. Supponiamo di avere un intervallo denominato di cells.ie, A1:C4. Quindi la matrice creerebbe 4 * 3 = 12 celle e le singole celle dell'intervallo sono disposte in sequenza. Aspose.Cells fornisce alcune utili proprietà della classe [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) per accedere alle singole celle nell'intervallo. È possibile utilizzare i seguenti metodi per identificare le celle nell'intervallo:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) restituisce l'indice della prima riga nell'intervallo denominato.
- [getPrimaColonna](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)restituisce l'indice della prima colonna nell'intervallo denominato.

L'esempio seguente mostra come inserire alcuni valori nelle celle di un intervallo specificato.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **Immettere i dati in Cells nell'intervallo denominato**
Utilizzando Aspose.Cells, è possibile inserire dati nelle singole celle di un intervallo. Supponiamo di avere un intervallo denominato di celle, ad esempio H1: J4. Quindi la matrice creerebbe 4 * 3 = 12 celle e le singole celle dell'intervallo sono disposte in sequenza. Aspose.Cells fornisce alcune utili proprietà della classe [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) per accedere alle singole celle nell'intervallo. È possibile utilizzare le seguenti proprietà per identificare le celle nell'intervallo:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow)restituisce l'indice della prima riga nell'intervallo denominato.
- [getPrimaColonna](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)restituisce l'indice della prima colonna nell'intervallo denominato.

L'esempio seguente mostra come inserire alcuni valori nelle celle di un intervallo specificato.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **Intervalli di formato...Impostazione del colore di sfondo e degli attributi dei caratteri su un intervallo denominato**
 Per applicare la formattazione, definire a[Stile](https://reference.aspose.com/cells/java/com.aspose.cells/style) oggetto per specificare le impostazioni di stile e applicarlo al file[Allineare](https://reference.aspose.com/cells/java/com.aspose.cells/range)oggetto.

L'esempio seguente mostra come impostare il colore di riempimento a tinta unita (colore di ombreggiatura) con le impostazioni del carattere su un intervallo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **Intervalli di formato...Aggiunta di bordi a un intervallo denominato**
 È possibile aggiungere bordi a un intervallo di celle invece che a una singola cella. Il[Allineare](https://reference.aspose.com/cells/java/com.aspose.cells/range) oggetto fornisce a[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)metodo che accetta i seguenti parametri per aggiungere un bordo all'intervallo di celle:

-  borderStyle: il tipo di bordo, selezionato dal file[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)enumerazione.
-  borderColor: il colore della linea del bordo, selezionato dal file[Colore](https://reference.aspose.com/cells/java/com.aspose.cells/Color) enumerazione.

L'esempio seguente mostra come impostare un bordo del contorno su un intervallo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


 Il seguente output verrebbe generato dopo l'esecuzione del codice precedente:

![cose da fare:immagine_alt_testo](named-ranges_1.png)
#### **Applicare lo stile alle celle in un intervallo**
A volte, vuoi creare applicare uno stile alle celle in a[Allineare](https://reference.aspose.com/cells/java/com.aspose.cells/range) . Per questo, puoi scorrere le celle nell'intervallo e utilizzare il[Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) per applicare lo stile alla cella.

L'esempio seguente mostra come applicare gli stili alle celle in un intervallo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **Rimuovi un intervallo denominato**
 Aspose.Cells fornisce il[NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\) ) metodo per cancellare il nome dell'intervallo. Per cancellare il contenuto dell'intervallo, utilizzare[Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\)) metodo.
L'esempio seguente mostra come rimuovere un intervallo denominato con il relativo contenuto.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


borderColors
