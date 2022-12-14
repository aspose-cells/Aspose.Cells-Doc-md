---
title: Crea accessi e copia intervalli denominati
type: docs
weight: 200
url: /it/net/create-access-and-copy-named-ranges/
---
## **introduzione**

Normalmente, le etichette di colonna e riga vengono utilizzate per riferirsi a singole celle. È possibile creare nomi descrittivi per rappresentare celle, intervalli di celle, formule o valori costanti. La parola**nome** può fare riferimento a una stringa di caratteri che rappresenta una cella, un intervallo di celle, una formula o un valore costante. Assegnare un nome a un intervallo significa che quell'intervallo di celle può essere indicato con il suo nome. Utilizzare nomi di facile comprensione, ad esempio Prodotti, per fare riferimento a intervalli di difficile comprensione, ad esempio Vendite!C20:C30. Le etichette possono essere utilizzate in formule che fanno riferimento a dati sullo stesso foglio di lavoro; se vuoi rappresentare un intervallo su un altro foglio di lavoro, puoi usare un nome. *Gli intervalli denominati sono tra le funzionalità più potenti di Microsoft Excel, soprattutto se utilizzati come intervallo di origine per controlli elenco, tabelle pivot, grafici e così via.

## **Lavorare con l'intervallo denominato utilizzando Microsoft Excel**

### **Crea intervalli denominati**

 I seguenti passaggi descrivono come denominare una cella o un intervallo di celle utilizzando**Microsoft Excel** . Questo metodo si applica a**Microsoft Ufficio Excel 2003**, **Microsoft Excel 97**, **2000** e**2002**.

1. Selezionare la cella, l'intervallo di celle a cui si desidera assegnare un nome.
1.  Clicca il**Casella del nome** all'estremità sinistra della barra della formula.
1. Digitare il nome delle celle.
1. Premere Invio.

{{% alert color="primary" %}}

Non puoi nominare una cella mentre stai modificando il contenuto della cella.

{{% /alert %}}

## **Lavorare con l'intervallo denominato utilizzando Aspose.Cells**

Qui, usiamo lo Aspose.Cells API per svolgere l'attività.
 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione.

### **Crea intervallo denominato**

 È possibile creare un intervallo denominato chiamando l'overloaded[**Crea intervallo**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione. Una tipica versione di[**Crea intervallo**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) metodo accetta i seguenti parametri:

- Nome della cella in alto a sinistra, il nome della cella in alto a sinistra nell'intervallo.
- Nome della cella in basso a destra, il nome della cella in basso a destra nell'intervallo.

 Quando il[**Crea intervallo**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) viene chiamato il metodo, restituisce l'intervallo appena creato come istanza di[**Gamma**](https://reference.aspose.com/cells/net/aspose.cells/range) classe. Usa questo[**Gamma**](https://reference.aspose.com/cells/net/aspose.cells/range) oggetto per configurare l'intervallo denominato. Ad esempio, imposta il nome dell'intervallo utilizzando il[**Nome**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name) proprietà. L'esempio seguente mostra come creare un intervallo denominato di celle che si estende su B4:G14.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **Immettere i dati in Cells nell'intervallo denominato**

È possibile inserire dati nelle singole celle di un intervallo seguendo il modello

- **C#**: Intervallo[riga,colonna]
- **V.B**: Intervallo(riga,colonna)

Supponi di avere un intervallo denominato di celle che si estende su A1: C4. La matrice fa 4 * 3 = 12 celle. Le singole celle dell'intervallo sono disposte in sequenza: Intervallo[0,0], Intervallo[0,1], Intervallo[0,2], Intervallo[1,0], Intervallo[1,1], Intervallo[1,2], Intervallo[2,0], Intervallo[2,1], Intervallo[2,2], Intervallo[3,0], Intervallo[3,1], Intervallo[3,2].

Utilizzare le seguenti proprietà per identificare le celle nell'intervallo:

- FirstRow restituisce l'indice della prima riga nell'intervallo denominato.
- FirstColumn restituisce l'indice della prima colonna nell'intervallo denominato.
- RowCount restituisce il numero totale di righe nell'intervallo denominato.
- ColumnCount restituisce il numero totale di colonne nell'intervallo denominato.

L'esempio seguente mostra come inserire alcuni valori nelle celle di un intervallo specificato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **Identificare Cells nell'intervallo denominato**

Puoi inserire dati nelle singole celle di un intervallo seguendo il modello:

- **C#**: Intervallo[riga,colonna]
- **V.B**: Intervallo(riga,colonna)

Se disponi di un intervallo denominato che si estende su A1:C4. La matrice fa 4 * 3 = 12 celle. Le singole celle dell'intervallo sono disposte in sequenza: Intervallo[0,0], Intervallo[0,1], Intervallo[0,2], Intervallo[1,0] ,Intervallo[1,1], Intervallo[1,2], Intervallo[2,0], Intervallo[2,1], Intervallo[2,2], Intervallo[3,0], Intervallo[3,1], Intervallo[3,2].

Utilizzare le seguenti proprietà per identificare le celle nell'intervallo:

- FirstRow restituisce l'indice della prima riga nell'intervallo denominato.
- FirstColumn restituisce l'indice della prima colonna nell'intervallo denominato.
- RowCount restituisce il numero totale di righe nell'intervallo denominato.
- ColumnCount restituisce il numero totale di colonne nell'intervallo denominato.

L'esempio seguente mostra come inserire alcuni valori nelle celle di un intervallo specificato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **Accedere a intervalli denominati**

#### **Accedi a un intervallo denominato specifico**

 Chiama il[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) della collezione[**Ottieni intervallo per nome**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) metodo per ottenere un intervallo in base al nome specificato. Un tipico[**Ottieni intervallo per nome**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) Il metodo accetta il nome dell'intervallo denominato e restituisce l'intervallo denominato specificato come istanza di[**Gamma**](https://reference.aspose.com/cells/net/aspose.cells/range) classe. L'esempio seguente mostra come accedere a un intervallo specificato in base al relativo nome.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **Accedi a tutti gli intervalli denominati in un foglio di calcolo**

 Chiama il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) della collezione[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) metodo per ottenere tutti gli intervalli denominati in un foglio di calcolo. Il[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) Il metodo restituisce un array di tutti gli intervalli di nomi nel file[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) collezione.

L'esempio seguente mostra come accedere a tutti gli intervalli denominati in una cartella di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **Copia intervalli denominati**

 Aspose.Cells fornisce[**Intervallo.Copia()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) metodo per copiare un intervallo di celle con formattazione in un altro intervallo.

L'esempio seguente mostra come copiare un intervallo di celle di origine in un altro intervallo denominato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
