---
title: Gestione degli intervalli
linktitle: Intervalli
type: docs
weight: 75
url: /it/java/managing-ranges/
---
## **introduzione**

In Excel, puoi selezionare più celle con una selezione della casella del mouse, l'insieme di celle selezionate è chiamato "Intervallo".

Ad esempio, puoi fare clic con il pulsante sinistro del mouse in Cell "A1" di Excel e quindi trascinare sulla cella "C4". L'area rettangolare selezionata può anche essere facilmente creata come oggetto utilizzando Aspose.Cells.

Ecco come creare un intervallo, inserire un valore, impostare lo stile ed eseguire più operazioni sull'oggetto "Intervallo".

## **Gestione degli intervalli utilizzando Aspose.Cells**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collezione.

### **Crea intervallo**

Quando vuoi creare un'area rettangolare che si estende su A1:C4, puoi usare il seguente codice:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-Create.java" >}}

### **Metti valore nello Cells della Gamma**

Supponi di avere un intervallo di celle che si estende su A1: C4. La matrice fa 4 * 3 = 12 celle. Le singole celle dell'intervallo sono disposte in sequenza: Intervallo[0,0], Intervallo[0,1], Intervallo[0,2], Intervallo[1,0], Intervallo[1,1], Intervallo[1,2], Intervallo[2,0], Intervallo[2,1], Intervallo[2,2], Intervallo[3,0], Intervallo[3,1], Intervallo[3,2].

L'esempio seguente mostra come inserire alcuni valori nelle celle dell'intervallo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-PutValue.java" >}}

### **Imposta stile del Cells della gamma**

L'esempio seguente mostra come impostare lo stile delle celle dell'intervallo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-SetStyle.java" >}}

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-CSharp-Data-Range-CurrentRegion.java" >}}

## **Argomenti avanzati**
- [Intervallo di riempimento automatico del file Excel](/cells/it/java/autofill-ranges/)
- [Cambia l'origine dati del grafico nel foglio di lavoro di destinazione durante la copia di righe o intervalli](/cells/it/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Copia gli intervalli di Excel](/cells/it/java/copy-ranges-of-Excel/)
- [Copia solo i dati dell'intervallo](/cells/it/java/copy-range-data-only/)
- [Copia i dati dell'intervallo con lo stile](/cells/it/java/copy-range-data-with-style/)
- [Copia solo stile intervallo](/cells/it/java/copy-range-style-only/)
- [Copia le altezze delle righe dell'intervallo di origine nell'intervallo di destinazione](/cells/it/java/copy-row-heights-of-source-range-to-destination-range/)
- [Crea intervallo di unione](/cells/it/java/create-union-range/)
- [Intervalli taglia e incolla](/cells/it/java/cut-and-paste-cells/)
- [Elimina intervalli](/cells/it/java/delete-ranges-from-Excel/)
- [Rileva Cells unito in un foglio di lavoro](/cells/it/java/detect-merged-cells-in-a-worksheet/)
- [Ottieni indirizzo Cell Scostamento conteggio dell'intera colonna e dell'intera riga dell'intervallo](/cells/it/java/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Ottieni intervallo con collegamenti esterni](/cells/it/java/get-range-with-external-links/)
- [Implementazione di intervalli non sequenziali](/cells/it/java/implementing-non-sequential-ranges/)
- [Inserisci intervalli](/cells/it/java/insert-ranges-to-Excel/)
- [Unisci o separa l'intervallo di Cells](/cells/it/java/merge-or-unmerge-range-of-cells/)
- [Sposta l'intervallo di Cells in un foglio di lavoro](/cells/it/java/move-range-of-cells-in-a-worksheet/)
- [Intervalli denominati](/cells/it/java/named-ranges/)
- [Cerca e sostituisci i dati in un intervallo](/cells/it/java/search-and-replace-data-in-a-range/)

