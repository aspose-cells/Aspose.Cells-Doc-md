---
title: Aspose.Cells for .NET 21.5 Note di rilascio
type: docs
weight: 8
url: /it/net/aspose-cells-for-net-21-5-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 21.5](https://www.nuget.org/packages/Aspose.Cells/21.5.0).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-47964| Supporta il report Slicer vincolante con tabella pivot e grafico pivot|Nuova caratteristica|
|CELLSNET-48003|Supporta l'importazione di html gratuito con immagine svg|Nuova caratteristica|
|CELLSNET-47988|Riferito al raggio di fuoriuscita con #|Nuova caratteristica|
|CELLSNET-47996|Supporta lo spostamento della colonna esistente in GridWeb|Nuova caratteristica|
|CELLSNET-48002|Supporta l'esportazione di tutti i fogli di lavoro in file .csv.|Nuova caratteristica|
|CELLSNET-47975|ArgumentException sul metodo CalculateFormula|Aumento|
|CELLSNET-47984|Supporta la funzione ELSE durante la conversione di xls in xlsx|Aumento|
|CELLSNET-47989| Supporto per l'impostazione del PageOrientationType globale|Aumento|
|CELLSNET-48051|PasteType.Values funziona solo se incollato in un intervallo diverso dall'origine|Aumento|
|CELLSNET-47956|Aspetta a calcolare la formula|Prestazione|
|CELLSNET-47982|La nuova cartella di lavoro si blocca su un file non valido|Prestazione|
|CELLSNET-48012|Migliora le prestazioni per la lettura di file .ods con un'ampia gamma di convalide.|Prestazione|
|CELLSNET-48039|Ciclo infinito durante il salvataggio della cartella di lavoro copiata|Prestazione|
|CELLSNET-44224|La filigrana WordArt non viene visualizzata nel formato file di output PDF|Insetto|
|CELLSNET-47887|Il testo all'interno della forma è fuori posto|Insetto|
|CELLSNET-47920|Alcuni contenuti mancano nella conversione da HTML a Excel|Insetto|
|CELLSNET-47981|Il risultato dell'esportazione dell'intervallo con celle unite in html non è corretto|Insetto|
|CELLSNET-47985|Meno numero di righe durante la conversione in html|Insetto|
|CELLSNET-47987|Sposta il campo pivot nella sezione Pagina o nei filtri pivot|Insetto|
|CELLSNET-47997|Colonne aggiuntive vengono create dopo aver salvato il file in html|Insetto|
|CELLSNET-48009|Il file è danneggiato dopo aver salvato la cartella di lavoro con Slicer|Insetto|
|CELLSNET-48036|Il controllo Slicer non viene aggiunto in base al campo Filtro pagina della tabella pivot|Insetto|
|CELLSNET-48044| Eccezione solleva durante la lettura di un file mhtml specifico|Insetto|
|CELLSNET-47118|Valore errato 'TRUE' recuperato da Cell invece del valore 'FALSE'|Insetto|
|CELLSNET-48042|I valori delle celle formattate recuperate sono errati nel foglio di lavoro di Excel|Insetto|
|CELLSNET-48031|"Errore da forma a immagine" viene generato durante la conversione di file xlsx in html|Insetto|
|CELLSNET-48037|L'immagine è distorta durante il salvataggio in PDF|Insetto|
|CELLSNET-47714|Il testo sull'asse verticale si sovrappone all'asse orizzontale sul grafico durante la conversione in EMF|Insetto|
|CELLSNET-47856|Problema di conversione da XLSX a PDF con le tabelle pivot|Insetto|
|CELLSNET-47986|Da grafico a immagine/PDF - output errato con tipo di grafico a cascata|Insetto|
|CELLSNET-48010|Eccezione durante il caricamento di un file Excel 2010 XLSX|Insetto|
|CELLSNET-48020|I controlli del modulo vengono eliminati dopo Carica e salva Excel 95 tramite Aspose.Cells|Insetto|
|CELLSNET-48033|File Excel danneggiato dopo il caricamento e il salvataggio|Insetto|
|CELLSNET-47957| "Errore da forma a immagine" viene generato durante la conversione di un file Excel nel formato file PDF|Eccezione|
|CELLSNET-48027|Eccezione di parametro non valido durante la conversione della forma in immagine|Eccezione|
|CELLSNET-48029|"Errore da forma a immagine" aumenta|Eccezione|
|CELLSNET-48017|Eccezione "La stringa di input non era in un formato corretto" durante l'importazione del file html|Eccezione|
|CELLSNET-48034|Dimensione carattere non valida nel file Mht.|Eccezione|
|CELLSNET-47977|Eccezione durante l'analisi della formula '[96]Foglio costi'!$D$6|Eccezione|
|CELLSNET-47979|Eccezione riferimento oggetto nel metodo Save|Eccezione|
|CELLSNET-48040|L'eccezione viene sollevata durante la conversione da XLSB a XLSX|Eccezione|
|CELLSNET-47980|Si è verificato un errore durante il salvataggio di un file Excel tramite Aspose.Cells|Eccezione|
|CELLSNET-48001|Eccezione indice di riga non valida durante la chiamata a GetPrintingPageBreaks()|Eccezione|
|CELLSNET-48022|Border.LineType imprevisto di una cella|Eccezione|
|CELLSNET-48032|Eccezione quando si apre il documento ODS file|Eccezione|
|


## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge il metodo Slicer.AddPivotConnection(PivotTable pivot).**

 Aggiunge la connessione alla tabella pivot per l'affettatrice.

### **Aggiunge il metodo Slicer.RemovePivotConnection(PivotTable pivot).**

 
Rimuove la connessione PivotTable dell'affettatrice.

### **Aggiunge la proprietà TxtSaveOptions.ExportAllSheets.**

 
Indica se esportare tutti i fogli di lavoro nel file. Il valore dafaut è falso come MS Excel.

### **Aggiunge FileFormatType.Numbers09 enum.**

  
Rappresenta il formato file .numbers 09. E FileFormatType.Number rappresenterà il tipo di formato di file latest.numbers in un secondo momento.

### **Aggiunge il metodo WorkbookSettings.SetPageOrientationType().**

 
Imposta il tipo di orientamento della pagina di stampa per l'intero file.

### **Elimina l'enumerazione DataBarAxisPosition.DataBarAxisAutomatic obsoleta.**

 
Usare invece l'enumerazione DataBarAxisPosition.Automatic.

### **Elimina DataBarAxisPosition.DataBarAxisMidpointe num obsoleto.**

 
 Usare invece l'enumerazione DataBarAxisPosition.Midpoint.

### **Elimina l'enumerazione DataBarAxisPosition.DataBarAxisNone obsoleta.**

 
 Usare invece l'enumerazione DataBarAxisPosition.None.

### **Elimina l'enumerazione DataBarBorderType.DataBarBorderNone obsoleta.**

 
Usare invece l'enumerazione DataBarBorderType.None.

### **Elimina l'enumerazione DataBarBorderType.DataBarBorderSolid obsoleta.**

 
Usare invece l'enumerazione DataBarBorderType.Solid.

### **Elimina l'enumerazione DataBarFillType.DataBarFillGradient obsoleta.**

 
 Usare invece l'enumerazione DataBarFillType.Gradient.

### **Elimina l'enumerazione DataBarFillType.DataBarFillSolid obsoleta.**

 
Usare invece l'enumerazione DataBarFillType.Solid.

### **Elimina l'enumerazione DataBarNegativeColorType.DataBarColor obsoleta.**

 
Usare invece l'enumerazione DataBarNegativeColorTypeColor.

### **Elimina l'enumerazione DataBarNegativeColorType.DataBarSameAsPositive obsoleta.**

 
 Usare invece l'enumerazione DataBarNegativeColorType.SameAsPositive.

### **Elimina l'enumerazione OleObject.FileFormatType obsoleta.**

 
 Usare invece l'enumerazione OleObject.FileFormatType.

### **Elimina l'enumerazione DynamicFilterType.Februray obsoleta.**

 
Utilizzare invece l'enumerazione DynamicFilterType.Feburay.

### **Rende obsoleta l'enumerazione FileFormatType.BMP e aggiunge l'enumerazione FileFormatType.Bmp.**

 
Usare invece l'enumerazione FileFormatType.Bmp.

### **Rende obsoleto FileFormatType.CSV enum e aggiunge FileFormatType.Csv enum.**

 
 Usare invece l'enumerazione FileFormatType.Csv.

### **Rende obsoleto FileFormatType.TSV enum e aggiunge FileFormatType.Tsv enum.**

 
 Usare invece l'enumerazione FileFormatType.Tsv.

### **Rende obsoleto FileFormatType.FODS enum e aggiunge FileFormatType.Fods enum.**

 Usare invece l'enumerazione FileFormatType.Fods.

### **Rende obsoleta l'enumerazione FileFormatType.MSEquation e aggiunge l'enumerazione FileFormatType.MsEquation.**

 
Usare invece l'enumerazione FileFormatType.MsEquation.

### **Rende obsoleta l'enumerazione FileFormatType.ODF e aggiunge l'enumerazione FileFormatType.Odf.**

 
 Usare invece l'enumerazione FileFormatType.Odf.

### **Rende obsoleta l'enumerazione FileFormatType.ODG e aggiunge l'enumerazione FileFormatType.Odg.**

 
 Usare invece l'enumerazione FileFormatType.Odg.

### **Rende obsoleta l'enumerazione FileFormatType.ODP e aggiunge l'enumerazione FileFormatType.Odp.**

 
 Usare invece l'enumerazione FileFormatType.Odp.

### **Rende obsoleta l'enumerazione FileFormatType.ODS e aggiunge l'enumerazione FileFormatType.Ods.**

 
 Usare invece l'enumerazione FileFormatType.Ods.

### **Rende obsoleta l'enumerazione FileFormatType.ODT e aggiunge l'enumerazione FileFormatType.Odt.**

 
 Usare invece l'enumerazione FileFormatType.Odt.

### **Rende obsoleta l'enumerazione FileFormatType.OTP e aggiunge l'enumerazione FileFormatType.Otp.**

 
 Usare invece l'enumerazione FileFormatType.Otp.

### **Rende obsoleta l'enumerazione FileFormatType.OTS e aggiunge l'enumerazione FileFormatType.Ots.**

 
 Usare invece l'enumerazione FileFormatType.Ots.

### **Rende obsoleta l'enumerazione FileFormatType.OTT e aggiunge l'enumerazione FileFormatType.Ott.**

 
 Usare invece FileFormatType.Ott enum.


### **Rende obsoleta l'enumerazione FileFormatType.SVG e aggiunge l'enumerazione FileFormatType.Svg.**

 
 Utilizzare invece l'enumerazione FileFormatType.Svg.

### **Rende obsoleta l'enumerazione FileFormatType.Sxc e aggiunge l'enumerazione FileFormatType.Sxc.**

 
 Usare invece l'enumerazione FileFormatType.Sxc.

### **Rende obsoleto FileFormatType.TIFF enum e aggiunge FileFormatType.Tiff enum.**

 
 Usare invece l'enumerazione FileFormatType.Tiff.

### **Rende obsoleto FileFormatType.VSD enum e aggiunge FileFormatType.Vsd enum.**

 
 Usare invece l'enumerazione FileFormatType.Vsd.

### **Rende obsoleta FileFormatType.VSDX enum e aggiunge FileFormatType.Vsdx enum.**

 
 Usare invece l'enumerazione FileFormatType.Vsdx.


### **Rende obsoleta l'enumerazione FileFormatType.XML e aggiunge l'enumerazione FileFormatType.Xml.**

 
 Usare invece l'enumerazione FileFormatType.Xml.

### **Rende obsoleta l'enumerazione FileFormatType.XPS e aggiunge l'enumerazione FileFormatType.Xps.**

 
 Usare invece l'enumerazione FileFormatType.Xps.

### **Rende obsoleta l'enumerazione FileFormatType.Excel2003XML e aggiunge l'enumerazione FileFormatType.SpreadsheetML.**

 
 Usare invece FileFormatType.SpreadsheetML enum.

### **Rende obsoleto SaveFormat.XPS enum e aggiunge SaveFormat.Xps enum.**

 
 Usare invece l'enumerazione SaveFormat.Xps.

### **Rende obsoleto SaveFormat.TSV enum e aggiunge SaveFormat.Tsv enum.**

 Usa invece SaveFormat.Tsv enum.

### **Rende obsoleto SaveFormat.TIFF enum e aggiunge SaveFormat.Tiff enum.**

 
Usare invece l'enumerazione SaveFormat.Tiff.

### **Rende obsoleto SaveFormat.SXC enum e aggiunge SaveFormat.Sxc enum.**

Usare invece l'enumerazione SaveFormat.Sxc.

### **Rende obsoleto SaveFormat.SVG enum e aggiunge SaveFormat.Svg enum.**

 
Usa invece SaveFormat.Svg enum.

### **Rende obsoleto SaveFormat.ODS enum e aggiunge SaveFormat.Ods enum.**

 
 Usare invece l'enumerazione SaveFormat.Ods.

### **Rende obsoleta l'enumerazione SaveFormat.Fods e aggiunge l'enumerazione SaveFormat.Fods.**

 
 Usare invece l'enumerazione SaveFormat.Fods.

### **Rende obsoleto SaveFormat.CSV enum e aggiunge SaveFormat.Csv enum.**

 
 Usare invece SaveFormat.Csv enum.

### **Rende obsoleto LoadFormat.CSV enum e aggiunge LoadFormat.Csv enum.**

 
 Usare invece l'enumerazione LoadFormat.Csv.

### **Rende obsoleto LoadFormat.TSV enum e aggiunge LoadFormat.Tsv enum.**

 
 Usare invece l'enumerazione LoadFormat.Tsv.

### **Rende obsoleto LoadFormat.ODS enum e aggiunge LoadFormat.Ods enum.**

 Usare invece l'enumerazione LoadFormat.Ods.

### **Rende obsoleto LoadFormat.SXC enum e aggiunge LoadFormat.Sxc enum.**

 
 Usare invece l'enumerazione LoadFormat.Sxc.

### **Rende obsoleto LoadFormat.FODS enum e aggiunge LoadFormat.Fods enum.**

 
 Usare invece l'enumerazione LoadFormat.Fods.

### **Aggiunge il metodo GridCells.MoveRange().**

 Sposta l'intervallo.

### **Aggiunge il metodo GridCells.InsertRange().**

 
Inserisce un intervallo con l'opzione di spostamento.

### **Aggiunge il metodo GridCells.DeleteRange().**

 
Elimina un intervallo con l'opzione di spostamento.

