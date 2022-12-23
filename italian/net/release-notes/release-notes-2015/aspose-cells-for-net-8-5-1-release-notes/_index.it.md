---
title: Aspose.Cells for .NET 8.5.1 Note di rilascio
type: docs
weight: 60
url: /it/net/aspose-cells-for-net-8-5-1-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 8.5.1](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.5.1/)

{{% /alert %}}

Di seguito è riportato un elenco di miglioramenti e modifiche in questa versione di Aspose.Cells

## 1) Aspose.Cells

### **Altri miglioramenti e modifiche**

### **Nuove caratteristiche**

(CELLSNET-43703) - ICustomFunction - restituisce un intervallo anziché una singola cella

(CELLSNET-43777) - Cell.GetHeightOfValue() simile a Cell.GetWidthOfValue() necessario

### **Insetti**

(CELLSNET-43744) - La tabella pivot non si aggiorna durante il salvataggio in PDF

(CELLSNET-43735) - L'opzione Righe a banda della tabella pivot è stata persa

(CELLSNET-43759) - La tabella pivot non mantiene l'ordinamento durante la combinazione

(CELLSNET-43721) - Viene visualizzato un messaggio di errore dopo il salvataggio della cartella di lavoro

(CELLSNET-43724) - I valori non sono corretti quando i dati cambiano

(CELLSNET-43719) - Valore diverso dopo CalculateFormula

(CELLSNET-43713) - Workbook.CalculateFormula non calcola i valori corretti

(CELLSNET-43708) - La chiamata a Worksheet.GetPrintingPageBreaks modifica la larghezza della casella di testo

(CELLSNET-43695) - Cell.RemoveArrayFormula non rimuove la formula di matrice

(CELLSNET-41874) - Sintassi di Excel non supportata per le formule

(CELLSNET-43753) - Aspose.Cells esegue il rendering di 2 pagine

(CELLSNET-43731) - Il testo viene tagliato durante il rendering del foglio di lavoro nell'immagine EMF

(CELLSNET-43756) - L'immagine del grafico non contiene gli stessi valori dell'asse x del grafico Excel

(CELLSNET-43728) - L'aggiornamento della tabella pivot con nuovi dati modifica lo stile del colore del grafico

(CELLSNET-43726) - La combinazione di cartelle di lavoro modifica lo stile del grafico

(CELLSNET-43700) - Il colore dell'immagine appare diverso dopo la conversione in PDF

(CELLSNET-43199) - I contenuti e le forme cambiano quando Excel viene salvato in PDF

(CELLSNET-43767) - Excel mostra la visualizzazione protetta sul foglio di calcolo salvato Aspose.Cells

(CELLSNET-43762) - Cell.GetPrecedents() non restituisce il nome del foglio di lavoro corretto

(CELLSNET-43761) - Il colore di sfondo delle celle formattate in modo condizionale cambia

(CELLSNET-43760) - Regole del formato condizionale danneggiate

(CELLSNET-43742) - Comportamento di protezione della cartella di lavoro incoerente

(CELLSNET-43734) - Excel non può aprire il file dopo la conversione da XLSM a XLS

(CELLSNET-43727) - La combinazione di cartelle di lavoro provoca l'avviso "Impossibile modificare una tabella pivot in modalità di modifica di gruppo" di Excel

### **Eccezioni**

(CELLSNET-43768) - Errore di area sconosciuta durante la copia del foglio di lavoro da un'altra cartella di lavoro

(CELLSNET-43716) - Errore da forma a immagine durante la conversione in PDF

(CELLSNET-43764) - NullReferenceException al ctor della cartella di lavoro con foglio di calcolo salvato come Strict OpenXML

(CELLSNET-43740) - System.IndexOutOfRangeException in Workbook.Save

## 2) Aspose.Cells Griglia Suite

### **Altri miglioramenti e modifiche**

### **Nuove caratteristiche**

(CELLSNET-42783) - Il collegamento alla cartella di lavoro esterna crea #REF! in GrigliaDesktop

(CELLSNET-41744) - Display da destra a sinistra

### **Insetti**

(CELLSNET-43730) - Differenza tra GridWeb.ActiveCell e GridWeb.WorkSheets[0].ActiveCell

(CELLSNET-43175) - Errore X rossa casuale di GridDesktop

(CELLSNET-42321) - Formattazione personalizzata dei numeri non corrispondente a Excel in Aspose.Cells.GridDesktop

(CELLSNET-43763) - Metodi mancanti in Aspose.Cells.GridDesktop

(CELLSNET-43774) - Nuova modalità GridDesktop: bordi non visualizzati correttamente nelle celle unite

### **Eccezioni**

(CELLSNET-43670) - System.ArgumentException in GridDesktop.ImportExcelFile

### **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

Aggiunge enum TableDataSourceType e ListObject.DataSourceType

Viene utilizzato per ottenere il tipo di origine dati della tabella.

Aggiunge il metodo Workbook.Dispose().

Viene utilizzato per rilasciare risorse non gestite.

Aggiunge il metodo Cell.GetHeightOfValue().

Viene utilizzato per ottenere l'altezza del valore in unità di pixel.
