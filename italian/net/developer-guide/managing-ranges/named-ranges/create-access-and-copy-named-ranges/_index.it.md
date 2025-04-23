---
title: Crea Accesso e Copia Intervalli con Nome
type: docs
weight: 200
url: /it/net/create-access-and-copy-named-ranges/
---

## **Introduzione**

Normalmente, le etichette di righe e colonne vengono utilizzate per fare riferimento a singole celle. È possibile creare nomi descrittivi per rappresentare celle, intervalli di celle, formule o valori costanti. La parola **nome** può fare riferimento a una stringa di caratteri che rappresenta una cella, un intervallo di celle, una formula o un valore costante. Assegnare un nome a un intervallo significa che quel intervallo di celle può essere riferito dal suo nome. Utilizza nomi di facile comprensione, come Prodotti, per fare riferimento a intervalli difficili da capire, come Vendite!C20:C30. Le etichette possono essere utilizzate in formule che fanno riferimento a dati sullo stesso foglio di lavoro; se vuoi rappresentare un intervallo su un altro foglio di lavoro, puoi usare un nome. *Gli intervalli con nome sono tra le funzionalità più potenti di Microsoft Excel, specialmente quando utilizzati come intervallo di origine per controlli di elenco, tabelle pivot, grafici e così via.

## **Lavorare con l'intervallo con nome usando Microsoft Excel**

### **Creare intervalli con nome**

I seguenti passaggi descrivono come nominare una cella o un intervallo di celle utilizzando **MS Excel**. Questo metodo si applica a **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** e **2002**.

1. Seleziona la cella o l'intervallo di celle che desideri nominare.
1. Fai clic sulla **Casella di nome** all'estremità sinistra della barra della formula.
1. Digita il nome delle celle.
1. Premi INVIO.

{{% alert color="primary" %}}

Non è possibile nominare una cella mentre si sta modificando il contenuto della cella.

{{% /alert %}}

## **Lavorare con l'intervallo nominato utilizzando Aspose.Cells**

Qui, utilizziamo l'API Aspose.Cells per svolgere il compito.
Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

### **Creare intervallo nominato**

È possibile creare un intervallo nominato chiamando il metodo sovraccaricato [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) della raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Una versione tipica del metodo [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) richiede i seguenti parametri:

- Nome della cella in alto a sinistra, il nome della cella in alto a sinistra nell'intervallo.
- Nome della cella in basso a destra, il nome della cella in basso a destra nell'intervallo.

Quando il metodo [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) è chiamato, restituisce il nuovo intervallo creato come un'istanza della classe [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). Utilizzare questo oggetto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) per configurare l'intervallo nominato. Ad esempio, impostare il nome dell'intervallo utilizzando la proprietà [**Name**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name). L'esempio seguente mostra come creare un intervallo nominato di celle che si estende da B4:G14.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **Inserimento dei dati nelle celle dell'intervallo nominato**

È possibile inserire dati nelle singole celle di un intervallo seguendo il modello

- **C#**: Range[row,column]
- **VB**: Range(row,column)

Supponiamo di avere un intervallo nominato di celle che va da A1:C4. La matrice contiene 4 * 3 = 12 celle. Le singole celle dell'intervallo sono disposte in sequenza: Intervallo[0,0], Intervallo[0,1], Intervallo[0,2], Intervallo[1,0], Intervallo[1,1], Intervallo[1,2], Intervallo[2,0], Intervallo[2,1], Intervallo[2,2], Intervallo[3,0], Intervallo[3,1], Intervallo[3,2].

Usa le seguenti proprietà per identificare le celle nell'intervallo:

- FirstRow restituisce l'indice della prima riga nell'intervallo nominato.
- FirstColumn restituisce l'indice della prima colonna nell'intervallo nominato.
- RowCount restituisce il numero totale di righe nell'intervallo nominato.
- ColumnCount restituisce il numero totale di colonne nell'intervallo nominato.

L'esempio seguente mostra come inserire alcuni valori nelle celle di un intervallo specificato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **Identifica le celle nell'intervallo nominato**

È possibile inserire dati nelle singole celle di un intervallo seguendo lo schema:

- **C#**: Range[row,column]
- **VB**: Range(row,column)

Se hai un intervallo nominato che comprende A1:C4. La matrice genera 4 * 3 = 12 celle. Le singole celle dell'intervallo sono disposte in sequenza: Intervallo[0,0], Intervallo[0,1], Intervallo[0,2], Intervallo[1,0] ,Intervallo[1,1], Intervallo[1,2], Intervallo[2,0], Intervallo[2,1], Intervallo[2,2], Intervallo[3,0], Intervallo[3,1], Intervallo[3,2].

Usa le seguenti proprietà per identificare le celle nell'intervallo:

- FirstRow restituisce l'indice della prima riga nell'intervallo nominato.
- FirstColumn restituisce l'indice della prima colonna nell'intervallo nominato.
- RowCount restituisce il numero totale di righe nell'intervallo nominato.
- ColumnCount restituisce il numero totale di colonne nell'intervallo nominato.

L'esempio seguente mostra come inserire alcuni valori nelle celle di un intervallo specificato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **Accedi agli intervalli nominati**

#### **Accedi a un intervallo nominato specifico**

Chiama il metodo [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) della collezione [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) per ottenere un intervallo con il nome specificato. Un tipico metodo [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) prende il nome dell'intervallo nominato e restituisce l'intervallo nominato specificato come un'istanza della classe [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). L'esempio seguente mostra come accedere a un intervallo specificato per nome.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **Accedi a tutti gli intervalli nominati in un foglio di calcolo**

Chiamare il metodo [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) della raccolta [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) per ottenere tutti i nomi definiti in un foglio di calcolo. Il metodo [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) restituisce un array di tutti i nomi definiti nella raccolta [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection).

L'esempio seguente mostra come accedere a tutti i nomi definiti in un libro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **Copiare i Nomi Definiti**

Aspose.Cells fornisce il metodo [**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) per copiare un intervallo di celle con formattazione in un altro intervallo.

L'esempio seguente mostra come copiare un intervallo di celle di origine in un altro nome definito.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
