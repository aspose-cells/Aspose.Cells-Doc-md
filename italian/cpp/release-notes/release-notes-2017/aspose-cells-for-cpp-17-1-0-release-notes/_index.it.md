---
title: Aspose.Cells per le note di rilascio di CPP 17.1.0
type: docs
weight: 40
url: /it/cpp/aspose-cells-for-cpp-17-1-0-release-notes/
---
|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSCPP-35|Lettura/Scrittura formato file XLSM|Nuova caratteristica|
|CELLSCPP-36|Lettura/Scrittura formato file CSV|Nuova caratteristica|
|CELLSCPP-37|Lettura/Scrittura formato file XLSB|Nuova caratteristica|
|CELLSCPP-38|Creare e manipolare intervalli denominati|Nuova caratteristica|
|CELLSCPP-39|Lettura/scrittura Formato di file delimitato da tabulazioni|Nuova caratteristica|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for C++. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Rimuove il metodo IPageSetup::GetDraft()/SetDraft()**
Utilizzare invece il metodo IPageSetup::GetPrintDraft()/SetPrintDraft().
#### **Rimuove il metodo ICell::GetConditionalIStyle()**
Utilizzare invece ICell::GetIConditionalFormattingResult().
#### **Rimuove il metodo ICells::MaxDataRowInColumn()**
Utilizzare invece ICells::GetLastDataRow().
#### **Elimina il metodo IPaneCollection::GetAcitvePaneType()/SetAcitvePaneType()**
Inutile, cancellato.
#### **Elimina il metodo IRange::ToString()**
Inutile, cancellato.
#### **Elimina il metodo IRow::Equals()**
Inutile, cancellato.
#### **Elimina il metodo IWorkbook::SetISettings()**
Inutile, cancellato.
#### **Elimina il metodo ICell::ToString()**
Inutile, cancellato.
#### **Elimina il metodo ICell::Equals(ObjectPtr).**
Inutile, cancellato.
#### **Elimina il metodo ICell::GetHashCode()**
Inutile, cancellato.
#### **Elimina il metodo IWorksheet::ToString()**
Inutile, cancellato.
#### **Aggiunge il metodo IBuiltInDocumentPropertyCollection::GetScaleCrop()/SetScaleCrop()**
Indica la modalità di visualizzazione della miniatura del documento.
#### **Aggiunge il metodo IBuiltInDocumentPropertyCollection::GetLinksUpToDate()/SetLinksUpToDate()**
Indica se i collegamenti ipertestuali in un documento sono aggiornati.
#### **Aggiunge il metodo IExternalLink::IsVisible()**
Indica se questo collegamento esterno è visibile in MS Excel.
#### **Aggiunge il metodo IListColumn::GetFormula()/SetFormula()**
Ottiene e imposta la formula della colonna elenco.
#### **Aggiunge il metodo IWorkbook::GetAbsolutePath()/SetAbsolutePath()**
Ottiene e imposta il percorso assoluto del file, utilizzato solo per i collegamenti esterni.
#### **Aggiunge il metodo IWorkbookSettings::GetCheckCompatibility()/SetCheckCompatibility()**
Indica se verificare la compatibilità durante il salvataggio della cartella di lavoro, il valore predefinito è true.
#### **Aggiunge il metodo IWorksheetCollection::CreateIRange()**
Crea un oggetto IRange da un indirizzo dell'intervallo.
#### **Aggiunge il metodo IWorkbookSettings::ClearPivottables()**
Cancella le tabelle pivot dal foglio di calcolo.
#### **Aggiunge il metodo ILoadOptions::GetCultureInfo/SetCultureInfo()**
Ottiene le informazioni sulle impostazioni cultura del sistema al momento del caricamento del file.
#### **Aggiunge il metodo ILoadOptions::GetILightCellsDataHandler()/SetILightCellsDataHandler()**
Indica il gestore dati per l'elaborazione dei dati delle celle durante la lettura del file modello.
#### **Aggiunge il metodo IWorksheet::GetIProtectedRangeCollection()**
Ottiene la raccolta di intervalli di modifica consentiti nel foglio di lavoro.
#### **Aggiunge il metodo IWorksheet::Dispose()**
Elimina il foglio di lavoro.
#### **Aggiunge il metodo ICells::ImportTwoDimensionArray()**
Importa una matrice di dati a due dimensioni in un foglio di lavoro
#### **Aggiunge il metodo ICells::ImportCSV()**
Importa un file CSV nelle celle.
#### **Aggiunge il metodo ICells::LinkToXmlMap()**
Collegamenti a una mappa xml.
