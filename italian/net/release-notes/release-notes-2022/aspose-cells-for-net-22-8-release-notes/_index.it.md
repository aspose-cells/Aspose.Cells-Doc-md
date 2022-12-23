---
title: Aspose.Cells for .NET 22.8 Note di rilascio
type: docs
weight: 5
url: /it/net/aspose-cells-for-net-22-8-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 22.8](https://www.nuget.org/packages/Aspose.Cells/22.8.0).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-51589|Supporta lo stile del pulsante espandi/comprimi per la tabella pivot|
|CELLSNET-51473|Converti i commenti in thread in html|
|CELLSNET-51570|Copia l'altezza della riga durante l'elaborazione degli indicatori intelligenti di una tabella|
|CELLSNET-51590|Elimina le forme raggruppate dal gruppo|
|CELLSNET-51595|Allineamento verticale errato del testo della cella durante la conversione in PDF dal file Excel con tabella pivot|
|CELLSNET-51621|Le formule condivise sono state copiate in modo errato per diversi formati di file|
|CELLSNET-51524|capo automatico errato durante la conversione in PDF da file Excel con tabella pivot|
|CELLSNET-51675|La forma viene persa durante la conversione in pdf|
|CELLSNET-51435|Nuove relazioni del foglio di lavoro vengono aggiunte durante la conversione di una cartella di lavoro XLSB in XLSM|
|CELLSNET-51545|La cartella di lavoro con i fogli di dialogo di MS Excel 5.0 non è stata caricata entro Aspose.Cells|
|CELLSNET-51546|I grafici vengono duplicati dopo l'apertura e il salvataggio con celle Aspose, quindi la visualizzazione in Excel|
|CELLSNET-51550|I collegamenti negli intervalli denominati vengono eliminati nella conversione da XLS a XLSM|
|CELLSNET-51551|I file sono stati danneggiati e il collegamento esterno è stato modificato in collegamento DDE durante la conversione dei file XLS in XLSM|
|CELLSNET-51558|La conversione di file XLS con collegamento di tipo xlAlternateStartup a XLSM sta generando file danneggiati|
|CELLSNET-51564|Dati duplicati dell'indicatore intelligente|
|CELLSNET-51574|Una casella di testo con due colonne viene visualizzata con una colonna solo quando si salva nuovamente un file XLSX|
|CELLSNET-51580|Un collegamento esterno di tipo xlPathMissing viene modificato nel normale tipo externalLinkPath nella conversione da XLS a XLSM|
|CELLSNET-51599|Nomi molto lunghi per le risorse del tipo di immagine durante il salvataggio come Html|
|CELLSNET-51627|Impossibile caricare il file specifico XLSM|
|CELLSNET-51632|RibbonXml non funziona|
|CELLSNET-51696|La conversione da XLS a XLSM comporta la modifica della proprietà di definizione della connessione dati "Salva password"|
|CELLSNET-51559|Conversione di un file XLSB in XLSM lancio dell'eccezione "startIndex non può essere maggiore della lunghezza della stringa"|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiungere il metodo FontSettingCollection.Replace().**

Sostituisci il testo della forma.

### **Aggiungere la proprietà ShapeTextAlignment.NumberOfColumns.**

Ottiene e imposta il numero di colonne del testo della forma.

### **Aggiungere la proprietà HtmlSaveOptions.ExportCommentsType.**

Ottiene e imposta il tipo di commenti di esportazione in html.

### **Aggiungere la classe base PaginatedSaveOptions per PdfSaveOptions e XpsSaveOptions.**

Rappresenta le opzioni per l'impaginazione.

### **Aggiungi gruppo di fogli di classe.**

Descrive una serie di fogli.

### **Aggiungere la proprietà PaginatedSaveOptions.SheetSet.**

Ottiene o imposta i fogli di cui eseguire il rendering.

### **Aggiungere la proprietà ImageOrPrintOptions.SheetSet.**

Ottiene o imposta i fogli di cui eseguire il rendering.

### **Aggiungere la proprietà GridWeb.IgnoreStyleWithNoData.**

Ottiene o imposta se GridWeb ignora la visualizzazione di righe o colonne che non contengono valori di cella ma hanno ancora uno stile

### **Proprietà ImageOrPrintOptions.SaveFormat obsoleta.**

Per Tiff/Svg, utilizza ImageType; Per Xps, utilizza Workbook.Save(string, SaveOptions) con XpsSaveOptions.

### **Costruttore obsoleto XpsSaveOptions(Aspose.Cells.SaveFormat saveFormat).**

Utilizzare invece il costruttore XpsSaveOptions().

### **Costruttore obsoleto SvgSaveOptions(Aspose.Cells.SaveFormat saveFormat).**

Utilizzare invece il costruttore SvgSaveOptions().

### **Rimuovere il costruttore PdfSaveOptions(Aspose.Cells.SaveFormat saveFormat).**

Utilizzare invece il costruttore PdfSaveOptions().
