---
title: Aspose.Cells for Java Note sulla versione 20.11
type: docs
weight: 2
url: /it/java/aspose-cells-for-java-20-11-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 20.11](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.11/).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43322|Proprietà Shape.getWorksheet() obbligatoria|Nuova caratteristica|
|CELLSJAVA-43191| Fornire mezzi per gestire gli scenari quando si specificano tipi di carattere errati?|Aumento|
|CELLSJAVA-43319|Problema di ottenere il valore della cella con la formula|Insetto|
|CELLSJAVA-43330|Problema dopo aver salvato nuovamente il file XLSB - file danneggiato|Insetto|
|CELLSJAVA-43333|Immagini e posizionamento del testo errato durante il rendering di Excel come HTML|Insetto|
|CELLSJAVA-43321|Problema con il filtro automatico: vengono visualizzate righe vuote|Insetto|
|CELLSJAVA-43335|Si è verificato un deadlock durante il calcolo delle formule sulla cartella di lavoro|Insetto|
|CELLSJAVA-43313|L'etichetta del grafico cambia posizione quando viene stampata|Insetto|
|CELLSJAVA-43314|Riga 0/100% non stampata per grafici a torta 100%.|Insetto|
|CELLSJAVA-43316| Vari problemi durante la stampa dei grafici|Insetto|
|CELLSJAVA-40582|Il testo grafico intelligente non viene visualizzato correttamente in PDF/image|Insetto|
|CELLSJAVA-41639|Le larghezze delle colonne non vengono mantenute durante la conversione dal formato "XML Spreadsheet 2003" al formato XLSX|Insetto|
|CELLSJAVA-43315|La conversione da XLS a XLSX danneggia il file e restituisce l'errore "Shape to Image" durante la conversione dell'output da XLSX a PDF|Insetto|
|CELLSJAVA-43334|Filtro automatico sul problema della tabella|Insetto|
|


## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

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

### **Aggiunge il metodo override XmlMapCollection.Clear().**

Cancella tutte le mappe xml.

### **Aggiunge l'enumerazione SaveFormat.Docx.**

Rappresenta il salvataggio come file .docx.

### **Aggiunge ImageType.OfficeCompatibleEmf enum.**

Windows Enhanced Metafile che è più compatibile con Office.

