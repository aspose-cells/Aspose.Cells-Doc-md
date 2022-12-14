---
title: Aspose.Cells for Java Note sulla versione 19.10
type: docs
weight: 30
url: /it/java/aspose-cells-for-java-19-10-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 19.10.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-41814|Supporta l'ordinamento personalizzato dei dati per l'area specifica nel rapporto di tabella pivot|Nuova caratteristica|
|CELLSJAVA-42988|Problema di prestazioni con calcolaFormula()|Aumento|
|CELLSJAVA-41103|La colorazione e la formattazione dei dati della tabella pivot non vengono visualizzate correttamente|Insetto|
|CELLSJAVA-43007|Il PDF non viene generato come previsto|Insetto|
|CELLSJAVA-43025|Cell.getStyle.getCustom restituisce un formato errato per la locale tedesca|Insetto|
|CELLSJAVA-43013|ArrayIndexOutOfBoundsException durante il caricamento del file Excel|Eccezione|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge il metodo Cells.RemoveDuplicates()**
Rimuove i dati duplicati dell'intervallo.
### **Aggiunge la proprietà OleObject.FullObjectBin**
Ottiene i dati binari dell'oggetto ole incorporati completi nel file modello.
### **Aggiunge la proprietà ContentTypeProperty.IsNillable**
Indica se la proprietà può essere nulla.
### **Aggiungere il metodo WorkbookDesigner.SetDataSource(String,ICellsDataTable).**
Imposta l'origine dati per Smart Marker Designer.
### **Aggiunge la proprietà ImageOrPrintOptions.PageSavingCallback**
Controlla/Indica l'avanzamento del processo di salvataggio della pagina.
### **Aggiunge la proprietà ImageOrPrintOptions.IsFontSubstitutionCharGranularity**
Indica se sostituire solo il carattere del carattere quando il carattere della cella non è compatibile con esso.
### **Rimuove la classe obsoleta HTMLLoadOptions**
Utilizzare invece la classe HtmlLoadOptions.
### **Rimuove la classe obsoleta ODSLoadOptions**
Utilizzare invece la classe OdsLoadOptions.
### **Rimuove la classe obsoleta JSONUtility**
Utilizzare invece la classe JsonUtility.
