---
title: Aspose.Cells for .NET Note sulla versione 20.11
type: docs
weight: 2
url: /it/net/aspose-cells-for-net-20-11-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 20.11](https://www.nuget.org/packages/Aspose.Cells/20.11.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-47706|Supporta il modello di formattazione dipendente dalle impostazioni locali "aaaa" per l'anno nella regione Spagna|Miglioramenti|
|CELLSNET-47641|Avviso generato durante l'aggiunta di 29 fogli e l'apertura del file XLS di output in MS Excel|Prestazione|
|CELLSNET-46716|Il testo è stato tagliato durante il rendering del PDF|Insetti|
|CELLSNET-47618|Un'immagine diventa completamente bianca e un po' di corruzione del testo in altre immagini/forme|Insetti|
|CELLSNET-47635| L'affettatrice su un tavolo diverso genera un file danneggiato|Insetti|
|CELLSNET-47642|Il file XLSB è danneggiato dopo il caricamento e il salvataggio|Insetti|
|CELLSNET-47660|Il campo del grafico contenente le date ha un formato diverso in formato PDF|Insetti|
|CELLSNET-47661|Aspose.Cells genera markup HTML non valido per un particolare foglio di lavoro di un particolare documento Cells|Insetti|
|CELLSNET-47680|Le tabelle pivot non sono state aggiornate|Insetti|
|CELLSNET-47659|Problema di ricerca di celle con stili specifici|Insetti|
|CELLSNET-47679|Differenza nel calcolo di Aspose.Cells ed Excel|Insetti|
|CELLSNET-47666|La cartella di lavoro non può essere visualizzata in SharePoint|Insetti|
|CELLSNET-47698|Sposta nella posizione del logo durante la conversione del file XLS in PDF|Insetti|
|CELLSNET-47651|L'esportazione della carta polare in pdf è distorta|Insetti|
|CELLSNET-47662|Le etichette dei dati errate vengono visualizzate durante la conversione del grafico Excel in immagine|Insetti|
|CELLSNET-47667|Barre mancanti nel grafico a barre nell'immagine di output|Insetti|
|CELLSNET-47697|Alcuni valori dell'asse Y escono dal grafico nel PDF di output|Insetti|
|CELLSNET-43579|La curvatura del testo WortArt viene modificata durante la conversione da Excel a PDF|Insetti|
|CELLSNET-47675|Il contenuto del file XLS viene modificato dopo il caricamento e il salvataggio|Insetti|
|CELLSNET-47704|Le proprietà personalizzate sono scomparse dopo aver modificato/salvato un file XLS protetto da password (crittografato).|Insetti|
|CELLSNET-47708|L'ordinamento non funzionava correttamente con le formule dinamiche (marcatori intelligenti)|Insetti|
|CELLSNET-47682|Eccezione durante il caricamento di particolari Htm|Eccezioni|
|CELLSNET-47683|Eccezione durante il caricamento di particolari Htm|Eccezioni|
|CELLSNET-47684|Eccezione durante il caricamento di particolari Htm|Eccezioni|
|CELLSNET-47689|Eccezione durante la conversione di XLSB in PNG e HTML|Eccezioni|
|CELLSNET-47701|Impossibile creare una copia della cartella di lavoro XLTX|Eccezioni|
|CELLSNET-47628|L'eliminazione di righe vuote dalle celle causa ArgumentOutOfRangeException|Eccezioni|
|CELLSNET-47629|La chiamata dei valori delle celle dopo l'eliminazione di righe e colonne vuote causa ArgumentException|Eccezioni|
|CELLSNET-47700|CalculateFormula genera un'eccezione InvalidCastException|Eccezioni|
|CELLSNET-47703|Eccezione sollevata durante la chiamata a Workbook.CalculateFormula()|Eccezioni|
|CELLSNET-47669|Indice di colonna non valido ArgumentException viene generata durante la conversione del primo foglio di lavoro in HTML|Eccezioni|
|CELLSNET-47677|DataBar.ToImage genera un'eccezione se la riga è nascosta.|Eccezioni|
|CELLSNET-47686|Impossibile convertire XLSB in XLSX|Eccezioni|
|CELLSNET-47687|Impossibile caricare Ods|Eccezioni|
|CELLSNET-47694|Eccezione quando si apre il file XLSX del documento|Eccezioni|
|CELLSNET-47695|Nome cella non valido dopo DeleteRange|Eccezioni|
|CELLSNET-47699|Eccezione quando si apre il file ODS|Eccezioni|
|CELLSNET-47702| Si è verificata un'eccezione durante il caricamento dei file crittografati "Microsoft Excel 5.0/95 Workbook".|Eccezioni|


## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.

### **Elimina il metodo CellsHelper.IsProtectedByRMS() obsoleto**

Usare invece la proprietà FileFormatUtil.DetectFileFormat().IsProtectedByRMS.

### **Elimina il metodo CellsHelper.DetectLoadFormat() e CellsHelper.DetectFileFormat() obsoleto**

Utilizzare invece FileFormatUtil.DetectFileFormat().

### **Elimina la proprietà CellsHelper.FontDir obsoleta.**

Usare invece FontConfigs.SetFontsFolder(string, bool).

### **Elimina la proprietà CellsHelper.FontDirs obsoleta.**

Usare invece FontConfigs.SetFontFolders(string[], bool).

### **Elimina la proprietà CellsHelper.FontFiles obsoleta.**

Usare invece FontConfigs.SetFontSources(FontSourceBase[]).

### **Aggiunge la proprietà CellsHelper.IsCloudPlatform.**

Indica se è in esecuzione sulla piattaforma could.

### **Aggiunge la proprietà Shape.Worksheet.**

Ottiene il foglio di lavoro che contiene questa forma.

### **Aggiunge la proprietà SaveOptions.SortExternalNames.**

Indica se ordinare i nomi esterni durante il salvataggio dei file .xlsx.

### **Aggiunge il metodo ListObject.Filter().**

Filtra la tabella.

### **Aggiunge il metodo XmlMapCollection.Clear().**

Cancella tutte le mappe xml.

### **Aggiunge l'enumerazione SaveFormat.Docx.**

Rappresenta il salvataggio come file .docx.

### **Aggiunge ImageType.OfficeCompatibleEmf enum.**

Metafile avanzato di Windows che è più compatibile con Office.

