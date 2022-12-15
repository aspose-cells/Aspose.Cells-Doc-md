---
title: Aspose.Cells for .NET Note sulla versione 19.11
type: docs
weight: 20
url: /it/net/aspose-cells-for-net-19-11-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 19.11](https://www.nuget.org/packages/Aspose.Cells/19.11.0).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-44956|Supporto per nascondere gli intervalli selezionati e ordinare i risultati visualizzati della tabella pivot|Nuova caratteristica|
|CELLSNET-46852|Supporta la lettura e la scrittura di tabelle la cui origine dati è una tabella di query nel file XLS.|Nuova caratteristica|
|CELLSNET-46967|Supporto per ottenere la dimensione del rientro in unità di pixel|Nuova caratteristica|
|CELLSNET-46973|La formula di Excel non funziona nel file XLS generato|Aumento|
|CELLSNET-46981|Supporto per lettura/scrittura con flusso di memoria per Workbook.ImportXml e Workbook.ExportXml|Aumento|
|CELLSNET-46905|Nessuna modifica per l'origine del collegamento salvata nel file XLS|Aumento|
|CELLSNET-46898|Lo sfondo del modello 3D diventa blu|Insetto|
|CELLSNET-46314|Problemi durante l'aggiornamento della tabella pivot con "Mostra valore come % del totale complessivo"|Insetto|
|CELLSNET-46789|Il metodo CalculateData non funziona correttamente con il formato PDF|Insetto|
|CELLSNET-46955|Il file da HTML a Excel solleva l'eccezione "L'elemento è già stato aggiunto"|Insetto|
|CELLSNET-46987|Impossibile calcolare la formula quando si fa riferimento alle celle|Insetto|
|CELLSNET-46968|La formula indiretta non funziona correttamente in MS Excel|Insetto|
|CELLSNET-46991|Il file XLSX è danneggiato.|Insetto|
|CELLSNET-46994|# Valore! nel file Excel di output (aperto in Excel 365) dopo aver chiamato Calcola formula
|Insetto|
|CELLSNET-47001|CalculateFormula() causa NullReferenceException|Insetto|
|CELLSNET-46953|Il contenuto viene tagliato durante la stampa|Insetto|
|CELLSNET-46966|Bordo destro mancante quando HorizontalAlignment è impostato su Fill|Insetto|
|CELLSNET-45362|Le opzioni delle immagini affiancate non funzionano per gli sfondi dei grafici nei file XLS|Insetto|
|CELLSNET-46949|Gli oggetti OLE diventano immagini durante la copia dei fogli di lavoro|Insetto|
|CELLSNET-46963|Le etichette dei grafici perdono la formattazione dopo il salvataggio del file Excel|Insetto|
|CELLSNET-46965|La chiamata a Chart.Calculate() su un grafico vuoto con un titolo di testo automatico vuoto genera un errore|Insetto|
|CELLSNET-46971|Il foglio appena copiato nasconde tutte le colonne nascoste e reimposta anche la larghezza delle colonne|Insetto|
|CELLSNET-46972|Virgola rimossa dai titoli dei grafici una volta decifrato il file Excel|Insetto|
|CELLSNET-46912|StackOverflowException generata durante la conversione di XLSX in HTML|Eccezione|
### **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.
#### **Aggiunge metodi: Validation.AddArea(CellArea,bool,bool),AddAreas(CellArea[], bool, bool),RemoveAreas(CellArea[])**
Aggiunge/rimuove le impostazioni di convalida da determinate aree tenendo conto delle prestazioni.
#### **Aggiunge il metodo Workbook.ImportXml(Stream stream, string sheetName, int row, int col).**
Importa un flusso di file XML nella cartella di lavoro.
#### **Aggiunge il metodo Workbook.ExportXml(string mapName, Stream stream).**
Esporta i dati XML in un flusso.
#### **Aggiunge la proprietà HtmlSaveOptions.ExportArea**
Ottiene o imposta la CellArea di esportazione del foglio di lavoro attivo corrente. Se si imposta questo attributo, l'area di stampa del foglio di lavoro attivo corrente verrà omessa. Solo l'area specificata verrà esportata durante il salvataggio del file in HTML.
#### **Aggiunge classi: DataMashup,PowerQueryFormula,PowerQueryFormulaCollection,PowerQueryFormulaItem e PowerQueryFormulaItemCollection**
Ottiene informazioni nel DataMashup.
#### **Aggiunge la proprietà DBConnection.SeverCommand.**
Ottiene e imposta una seconda stringa di testo del comando che viene resa persistente quando sono in uso i campi della pagina basata sul server della tabella pivot.
#### **Aggiunge il metodo CellsHelper.GetTextWidth().**
Ottiene la larghezza del testo nell'unità di punti.
