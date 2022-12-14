---
title: Aspose.Cells for Java Note sulla versione 19.11
type: docs
weight: 20
url: /it/java/aspose-cells-for-java-19-11-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 19.11.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43032|Aggiungere Validation.addArea (CellArea cellArea, boolean skipArea) o Validation.setAreas() metodo/overload alle API|Nuova caratteristica|
|CELLSJAVA-42851|Ottieni i dettagli della connessione ODATA|Nuova caratteristica|
|CELLSJAVA-43018|Esporta l'intervallo dell'area di stampa in HTML senza modificare implicitamente alcuni stati della stessa cartella di lavoro|Aumento|
|CELLSJAVA-43041|Cells.importCSV genera un'eccezione "il valore della stringa non può superare i 255 caratteri"|Aumento|
|CELLSJAVA-43043|Cells.removeDuplicates richiede più tempo per set di dati di grandi dimensioni|Aumento|
|CELLSJAVA-43019|Grafico radiale non visualizzato correttamente in HTML|Insetto|
|CELLSJAVA-43027|Dopo il rendering in formato PNG, il ridimensionamento dell'asse è diverso.|Insetto|
|CELLSJAVA-42474|La tabella pivot non viene aggiornata e danneggiata dopo l'aggiornamento dei dati di origine|Insetto|
|CELLSJAVA-43033|La conversione in PDF non finisce.|Insetto|
|CELLSJAVA-43034|Viene recuperato un output in formato di data russo (personalizzato) non valido|Insetto|
|CELLSJAVA-43040|LoadFilter non considera il foglio richiesto|Insetto|
|CELLSJAVA-43035|I bordi vengono persi durante la conversione del file Excel in EMF|Insetto|
|CELLSJAVA-43016|Conteggio pagine non valido da SheetRender|Insetto|
|CELLSJAVA-43026|Dopo aver eseguito il rendering del grafico in un'immagine, le etichette dati cambiano stile e i valori non sono gli stessi|Insetto|
|CELLSJAVA-43038|I collegamenti ipertestuali non vengono esportati utilizzando Cell.setHtmlString()|Insetto|
|CELLSJAVA-43039|Cell.setHtmlString() non esegue il rendering di determinati tag/script HTML nell'esportazione in Excel|Insetto|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge metodi: Validation.AddArea(CellArea,bool,bool),AddAreas(CellArea[], bool, bool),RemoveAreas(CellArea[])**
Aggiunge/rimuove le impostazioni di convalida da determinate aree tenendo conto delle prestazioni.
### **Aggiunge il metodo Workbook.ImportXml(Stream stream, string sheetName, int row, int col).**
Importa un flusso di file XML nella cartella di lavoro.
### **Aggiunge il metodo Workbook.ExportXml(string mapName, Stream stream).**
Esporta i dati XML in un flusso.
### **Aggiunge la proprietà HtmlSaveOptions.ExportArea**
Ottiene o imposta la CellArea di esportazione del foglio di lavoro attivo corrente. Se si imposta questo attributo, l'area di stampa del foglio di lavoro attivo corrente verrà omessa. Solo l'area specificata verrà esportata durante il salvataggio del file in HTML.
### **Aggiunge classi: DataMashup,PowerQueryFormula,PowerQueryFormulaCollection,PowerQueryFormulaItem e PowerQueryFormulaItemCollection**
Ottiene informazioni nel DataMashup.
### **Aggiunge la proprietà DBConnection.SeverCommand.**
Ottiene e imposta una seconda stringa di testo del comando che viene resa persistente quando sono in uso i campi della pagina basata sul server della tabella pivot.
### **Aggiunge il metodo CellsHelper.GetTextWidth().**
Ottiene la larghezza del testo nell'unità di punti.
