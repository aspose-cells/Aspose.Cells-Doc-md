---
title: Gestione degli intervalli
linktitle: Intervalli
type: docs
weight: 105
url: /it/net/managing-ranges/
---
## **introduzione**

In Excel, puoi selezionare più celle con una selezione della casella del mouse, l'insieme di celle selezionate è chiamato "Intervallo".

Ad esempio, puoi fare clic con il pulsante sinistro del mouse in Cell "A1" di Excel e quindi trascinare sulla cella "C4". L'area rettangolare selezionata può anche essere facilmente creata come oggetto utilizzando Aspose.Cells.

Ecco come creare un intervallo, inserire un valore, impostare lo stile ed eseguire più operazioni sull'oggetto "Intervallo".

## **Gestione degli intervalli utilizzando Aspose.Cells**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione.

### **Crea intervallo**

Quando vuoi creare un'area rettangolare che si estende su A1:C4, puoi usare il seguente codice:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-Create.cs" >}}

### **Metti valore nello Cells della Gamma**

Supponi di avere un intervallo di celle che si estende su A1: C4. La matrice fa 4 * 3 = 12 celle. Le singole celle dell'intervallo sono disposte in sequenza: Intervallo[0,0], Intervallo[0,1], Intervallo[0,2], Intervallo[1,0], Intervallo[1,1], Intervallo[1,2], Intervallo[2,0], Intervallo[2,1], Intervallo[2,2], Intervallo[3,0], Intervallo[3,1], Intervallo[3,2].

L'esempio seguente mostra come inserire alcuni valori nelle celle dell'intervallo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-PutValue.cs" >}}

### **Imposta stile del Cells della gamma**

L'esempio seguente mostra come impostare lo stile delle celle dell'intervallo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-SetStyle.cs" >}}

### **Ottieni CurrentRegion dell'intervallo**

 CurrentRegion è una proprietà che restituisce un oggetto Range che rappresenta l'area corrente.

L'area corrente è un intervallo delimitato da qualsiasi combinazione di righe e colonne vuote. Sola lettura.

In Excel, puoi ottenere l'area CurrentRegion tramite:
1. Selezionare un'area (range1) con il riquadro del mouse.
2. Fai clic su "Home - Modifica - Trova e seleziona - Vai a speciale - Regione corrente" o usa "Ctrl + Maiusc + *", vedrai che Excel ti aiuta automaticamente a selezionare un'area (intervallo2), ora l'hai creata, l'intervallo2 è la CurrentRegion dell'intervallo1.

Utilizzando Aspose.Cells, è possibile utilizzare la proprietà "Range.CurrentRegion" per eseguire la stessa funzione.

Scarica il seguente file di prova, aprilo in Excel, usa la casella del mouse per selezionare un'area "A1:D7", quindi fai clic su "Ctrl+Maiusc+*", vedrai l'area "A1:C3" selezionata.

[regione_corrente.xlsx](current_region.xlsx)

Ora esegui il seguente esempio, guarda come funziona in Aspose.Cells:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Range-CurrentRegion.cs" >}}


## **Argomenti avanzati**
- [Intervallo di riempimento automatico del file Excel](/cells/it/net/autofill-ranges/)
- [Copia gli intervalli di Excel](/cells/it/net/copy-ranges-of-Excel/)
- [Copia solo i dati dell'intervallo](/cells/it/net/copy-range-data-only/)
- [Copia i dati dell'intervallo con lo stile](/cells/it/net/copy-range-data-with-style/)
- [Copia solo stile intervallo](/cells/it/net/copy-range-style-only/)
- [Crea intervallo di unione](/cells/it/net/create-union-range/)
- [Gamma taglia e incolla](/cells/it/net/cut-and-paste-cells/)
- [Elimina intervalli](/cells/it/net/delete-ranges-from-Excel/)
- [Ottieni indirizzo Cell Scostamento conteggio dell'intera colonna e dell'intera riga dell'intervallo](/cells/it/net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Inserisci intervalli](/cells/it/net/insert-ranges-to-Excel/)
- [Unisci o separa l'intervallo di Cells](/cells/it/net/merge-or-unmerge-range-of-cells/)
- [Sposta l'intervallo di Cells in un foglio di lavoro](/cells/it/net/move-range-of-cells-in-a-worksheet/)
- [Crea intervalli denominati con ambito cartella di lavoro e foglio di lavoro](/cells/it/net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Cerca e sostituisci i dati in un intervallo](/cells/it/net/search-and-replace-data-in-a-range/)
