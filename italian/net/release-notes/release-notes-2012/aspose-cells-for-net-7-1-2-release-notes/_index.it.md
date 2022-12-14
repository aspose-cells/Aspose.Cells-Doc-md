---
title: Aspose.Cells for .NET 7.1.2 Note di rilascio
type: docs
weight: 90
url: /it/net/aspose-cells-for-net-7-1-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 7.1.2](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-7.1.2/)

{{% /alert %}} 

Siamo felici di annunciare Aspose.Cells for .NET v7.1.2!1) Aspose.Cells

 Nuove caratteristiche

 ` `- Tabelle di supporto nei file XLS - Personalizzazione della barra multifunzione XML40452 - Support Workbook.ContentTypePropertiesEnhancements

 ` `- La formula IF() restituisce "0" invece di "#N/A" - Problemi con la proprietà FirstPageNumber - Layout modificato quando il documento viene convertito in PDF - La proprietà 'DragData' non è presente in 'PivotField' - Cambia DataSource sulla tabella pivot . - Problemi con le tabelle pivot - Conversione di diagrammi/forme del flusso di lavoro in prestazioni di immagini

 ` `- Worksheet.RemoveFormulas - problema di prestazioni - Pdf Generation => OutOfMemoryException - Utilizzo eccessivo della memoria durante la conversione da Excel a PDF - Il salvataggio in PDF utilizza 3 GB per un file Excel da 10 MB - L'apertura della cartella di lavoro impiega troppo tempo per aprire le eccezioni

` `- Eccezione NullReference durante l'operazione di salvataggio se si copia il foglio di lavoro da un'altra cartella di lavoro - Arresto anomalo del metodo Workbook.CalculateFormula() - L'attributo RowSpan genera un'eccezione - Si è verificata un'eccezione ArgumentOutOfRange durante l'inizializzazione di fileBugs

` `- Problemi con le funzioni VLOOKUP e OFFSET - IRR non viene calcolato correttamente - Problemi con i calcoli di MS Excel - La formula di matrice che utilizza la funzione Indirect() copia solo 1 valore - CellsException nel calcolo della formula TREND() - Copia foglio di lavoro sostituisce intestazione e piè di pagina - Problema Stampa Excel file con immagini EMF incorporate - Problema della tabella pivot - Bug del filtro di formattazione - PivotField - Lettura di elementi dalla cache - Problemi multipli durante l'aggiornamento alle versioni più recenti - La creazione della cartella di lavoro con InputStream non funziona - Il file XLS generato si arresta in modo anomalo MS Excel - Il menu a discesa e il grafico sono rimosso dalla cartella di lavoro dopo il salvataggio - Aspose.Cells non applica correttamente la formattazione della cella personalizzata - I file XLSM sono danneggiati in determinate condizioni - Il formato della dimensione del carattere Cell con un numero non intero è cambiato - Inserisci simbolo alla fine di un valore di cella2) GridDesktop

 Insetti

` `- I valori del grafico vengono visualizzati in modo errato per il file XLSX - Problema SUM() nel foglio di lavoro di GridDesktop - GridDesktop.ImportExcelFile() genera un'eccezione - L'indice era al di fuori dei limiti dell'array - Problema di GridDestop sulle celle della formula- Griddesktop.ImportExcelFile() lancia OutOfMemoryException
