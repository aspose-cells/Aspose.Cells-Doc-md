---
title: Gestione degli intervalli con Golang tramite C++
linktitle: Intervalli
type: docs
weight: 105
url: /it/go-cpp/managing-ranges/
description: Impara come gestire gli intervalli nei file Excel usando Aspose.Cells con Golang tramite C++. Crea, modifica e stila gli intervalli programmaticamente.
---

## **Introduzione**

In Excel, è possibile selezionare più celle con una selezione del riquadro del mouse, l'insieme di celle selezionate è chiamato "Intervallo".

Ad esempio, è possibile fare clic con il pulsante sinistro del mouse nella cella "A1" di Excel e quindi trascinare fino alla cella "C4". L'area rettangolare selezionata può anche essere facilmente creata come oggetto utilizzando Aspose.Cells.

Ecco come creare un intervallo, inserire un valore, impostare uno stile e fare altre operazioni sull'oggetto "Intervallo".

## **Gestione degli intervalli utilizzando Aspose.Cells**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

### **Crea Intervallo**

Quando si desidera creare un'area rettangolare che si estende da A1 a C4, è possibile utilizzare il seguente codice:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges.go" >}}
### **Inserire un valore nelle celle dell'Intervallo**

Supponiamo di avere un intervallo di celle che si estende da A1 a C4. La matrice crea 4 * 3 = 12 celle. Le singole celle dell'intervallo sono disposte in sequenza: Intervallo[0,0], Intervallo[0,1], Intervallo[0,2], Intervallo[1,0], Intervallo[1,1], Intervallo[1,2], Intervallo[2,0], Intervallo[2,1], Intervallo[2,2], Intervallo[3,0], Intervallo[3,1], Intervallo[3,2].

Nell'esempio seguente viene mostrato come inserire alcuni valori nelle celle dell'Intervallo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges-1.go" >}}
### **Impostare lo stile delle celle dell'Intervallo**

Nell'esempio seguente viene mostrato come impostare lo stile delle celle dell'Intervallo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges-2.go" >}}
### **Ottieni la CurrentRegion del Range**

CurrentRegion è una proprietà che restituisce un oggetto Range che rappresenta la regione corrente. 

La regione corrente è una gamma delimitata da qualsiasi combinazione di righe o colonne vuote. Solo lettura.

In Excel, puoi ottenere l'area CurrentRegion tramite:
1. Seleziona un'area (range1) con il mouse.
2. Clicca su "Home - Modifica - Trova e seleziona - Vai a speciale - Regione corrente", oppure usa "Ctrl+Shift+*", vedrai che Excel ti aiuterà automaticamente a selezionare un'area (range2), ora l'hai fatta, range2 è la CurrentRegion di range1.

Utilizzando Aspose.Cells, puoi utilizzare la proprietà "Range.CurrentRegion" per eseguire la stessa funzione.

Si prega di scaricare il file di test seguente, aprirlo in Excel, utilizzare il mouse per selezionare un'area "A1:D7", quindi fare clic su "Ctrl+Shift+*", vedrai che l'area "A1:C3" è selezionata.

[current_region.xlsx](current_region.xlsx)

Ora si prega di eseguire il seguente esempio, vedere come funziona in Aspose.Cells:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingRanges-3.go" >}}

## **Argomenti avanzati**
- [Riempimento automatico dell'area del file Excel](/cells/it/cpp/autofill-ranges/)
- [Copia dei range di Excel](/cells/it/cpp/copy-ranges-of-Excel/)
- [Copia solo i dati dell'intervallo.](/cells/it/cpp/copy-range-data-only/)
- [Copia intervallo dati con stile.](/cells/it/cpp/copy-range-data-with-style/)
- [Copia solo lo stile dell'intervallo](/cells/it/cpp/copy-range-style-only/)
- [Crea un intervallo di unione](/cells/it/cpp/create-union-range/)
- [Taglia e incolla il range](/cells/it/cpp/cut-and-paste-cells/)
- [Elimina ranges](/cells/it/cpp/delete-ranges-from-Excel/)
- [Ottieni l'indirizzo, il conteggio delle celle, lo spostamento, l'intera colonna e la riga intera del range](/cells/it/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Inserisci ranges](/cells/it/cpp/insert-ranges-to-Excel/)
- [Unisci o Separa Intervallo di Celle](/cells/it/cpp/merge-or-unmerge-range-of-cells/)
- [Sposta Intervallo di Celle in un Foglio di Lavoro](/cells/it/cpp/move-range-of-cells-in-a-worksheet/)
- [Crea Riferimenti con Nome a Livello di Cartella e Foglio di Lavoro](/cells/it/cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Cerca e Sostituisci Dati in un Intervallo](/cells/it/cpp/search-and-replace-data-in-a-range/)
