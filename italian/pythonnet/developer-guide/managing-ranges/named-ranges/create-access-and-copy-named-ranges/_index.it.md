---
title: Crea Accesso e Copia Intervalli con Nome
type: docs
weight: 200
url: /it/python-net/create-access-and-copy-named-ranges/
description: Questo articolo mostra come creare accesso e copiare intervalli con nome tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Python Creare accesso e copiare intervalli con nome, Python Creare intervalli con nome, Python Copiare intervalli con nome, Python Accedere a tutti gli intervalli con nome in un foglio di calcolo.
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

## **Lavorare con l'intervallo nominato utilizzando Aspose.Cells per la libreria Excel di Python**

Qui, utilizziamo l'API Aspose.Cells per Python via .NET per svolgere il compito.
Aspose.Cells for Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una raccolta di [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) che consente di accedere a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una raccolta di [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

### **Creare intervallo nominato**

È possibile creare un intervallo nominato chiamando il metodo sovraccaricato [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) della raccolta [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Una versione tipica del metodo [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) richiede i seguenti parametri:

- Nome della cella in alto a sinistra, il nome della cella in alto a sinistra nell'intervallo.
- Nome della cella in basso a destra, il nome della cella in basso a destra nell'intervallo.

Quando il metodo [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) è chiamato, restituisce il nuovo intervallo creato come un'istanza della classe [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). Utilizzare questo oggetto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) per configurare l'intervallo nominato. Ad esempio, impostare il nome dell'intervallo utilizzando la proprietà [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/range/name). L'esempio seguente mostra come creare un intervallo nominato di celle che si estende da B4:G14.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CreateNamedRangeofCells-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-InputDataInCellsInRange-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IdentifyCellsinNamedRange-1.py" >}}

### **Accedi agli intervalli nominati**

#### **Accedi a un intervallo nominato specifico**

Chiama il metodo [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str) della collezione [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) per ottenere un intervallo con il nome specificato. Un tipico metodo [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str) prende il nome dell'intervallo nominato e restituisce l'intervallo nominato specificato come un'istanza della classe [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). L'esempio seguente mostra come accedere a un intervallo specificato per nome.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessSpecificNamedRange-1.py" >}}

#### **Accedi a tutti gli intervalli nominati in un foglio di calcolo**

Chiamare il metodo [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#) della raccolta [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) per ottenere tutti i nomi definiti in un foglio di calcolo. Il metodo [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#) restituisce un array di tutti i nomi definiti nella raccolta [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/).

L'esempio seguente mostra come accedere a tutti i nomi definiti in un libro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessAllNamedRanges-1.py" >}}

### **Copiare i Nomi Definiti**

Aspose.Cells per Python via .NET fornisce il metodo [**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range) per copiare un intervallo di celle con formattazione in un altro intervallo.

L'esempio seguente mostra come copiare un intervallo di celle di origine in un altro nome definito.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CopyNamedRanges-1.py" >}}
