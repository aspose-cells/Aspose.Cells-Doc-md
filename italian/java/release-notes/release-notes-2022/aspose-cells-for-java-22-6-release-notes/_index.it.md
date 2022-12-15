---
title: Aspose.Cells for Java 22.6 Note di rilascio
type: docs
weight: 7
url: /it/java/aspose-cells-for-java-22-6-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 22.6](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-22.6/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-44632|Supporta la formattazione dell'intera riga di dati nella tabella pivot|
|CELLSJAVA-44611|Miglioramento per la lettura di celle vuote da file xlsx|
|CELLSJAVA-44616|Le impostazioni originali della formattazione condizionale nell'intervallo di destinazione devono essere rimosse durante la copia dell'intervallo|
|CELLSJAVA-44658|Supporto BouncyCastle v1.71|
|CELLSJAVA-44628|Come conservare il formato percentuale di determinate righe pivot quando si espandono i dati del nodo di una colonna/campo pivot|
|CELLSJAVA-44483|L'ordinamento non funziona dopo aver raggruppato le righe|
|CELLSJAVA-44609|Copia lenta con formattazione condizionale utilizzando la versione più recente|
|CELLSJAVA-44622|Quando si ordinano gruppi di grandi dimensioni con più chiavi, genera "java.lang.ArrayIndexOutOfBoundsException"|
|CELLSJAVA-44630|Problema con la funzione Smart Markers dal Aspose Cells 22.5|
|CELLSJAVA-44646|Il contenuto chiaro sul foglio copiato genera NullPointerException|
|CELLSJAVA-44656|Cells.getMaxDataColumn restituisce un valore diverso (errato) in 22.5|
|CELLSJAVA-44650|La pagina del documento Excel è disordinata durante il caricamento in Aspose.Cells.GridWeb(Java)|
|CELLSJAVA-44660|Problema con l'allineamento dei dati durante il caricamento di XLS in Aspose.Cells.GridWeb (Java)|
|CELLSJAVA-44661|Problema durante il caricamento del file et in Aspose.Cells.GridWeb (Java)|
|CELLSJAVA-44584|Il titolo dell'asse nel grafico viene ruotato nell'immagine di output - Conversione da grafico a immagine|
|CELLSJAVA-44615|Linea grigia tracciata nell'immagine di output dal file XLS|
|CELLSJAVA-44665|Il caricamento del file ODS si blocca|
|CELLSJAVA-44651|Errore "Non è un valore numerico" durante la conversione del foglio Excel in HTML/PDF|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.

### **Aggiunge la classe CellsDataTableFactory**

Questa classe fornisce API per creare un'istanza di ICellsDataTable da oggetti personalizzati per comodità dell'utente.

### **Aggiunge la proprietà Workbook.CellsDataTableFactory**

Fornire all'utente CellsDataTableFactory per creare un'istanza di ICellsDataTable da oggetti personalizzati.

### **Aggiunge il metodo Cell.GetDependentsInCalculation(bool).**

In base all'attuale catena di calcolo, ottieni tutte le celle il cui risultato calcolato dipende da questa cella.

### **Aggiunge il metodo Cell.GetPrecedentsInCalculation()**

In base all'attuale catena di calcolo, ottieni tutti i precedenti (riferimento alle celle nella cartella di lavoro corrente) utilizzati dalla formula di questa cella durante il calcolo.

### **Metodi obsoleti Cell.GetLeafs() e Cell.GetLeafs(bool)**

Utilizzare invece il metodo Cell.GetDependentsInCalculation(bool).

### **Aggiunge il metodo PivotTable.FormatRow(int row, Style style).**

Formatta i dati della riga nell'area della tabella pivot.

### **Aggiunge la proprietà Shapes.CreateId**

Ottiene l'ID di creazione della forma.

### **Aggiunge l'enumerazione WarningType.InvalidData**

Rappresenta il tipo di dati non valido.

### **Aggiunge il metodo di sovraccarico ChartCollection.Add()**

Aggiunge un grafico con l'origine dati.

### **Aggiunge il metodo Chart.GetActualSize()**

Ottiene la dimensione effettiva del grafico in unità di pixel.

### **Proprietà Chart.ActualChartSize obsoleta**

Utilizzare invece il metodo Chart.GetActualSize().

### **Proprietà PdfSaveOptions.ImageType obsoleta**

Il grafico e la forma sono sempre resi come elementi vettoriali (ad es. punto, linea) per la qualità del rendering.

### **Proprietà ImageOrPrintOptions.ChartImageType obsoleta**

Il grafico e la forma sono sempre resi come elementi vettoriali (ad es. punto, linea) per la qualità del rendering.

### **Elimina la proprietà obsoleta ImageOrPrintOptions.ImageFormat**

Utilizzare invece la proprietà ImageOrPrintOptions.ImageType.

### **Elimina la proprietà obsoleta ImageOrPrintOptions.IsImageFitToPage**

La proprietà è inutile.