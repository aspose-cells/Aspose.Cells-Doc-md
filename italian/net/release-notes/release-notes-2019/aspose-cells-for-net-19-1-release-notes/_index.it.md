---
title: Aspose.Cells for .NET 19.1 Note di rilascio
type: docs
weight: 120
url: /it/net/aspose-cells-for-net-19-1-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 19.1](https://www.nuget.org/packages/Aspose.Cells/19.1.0).

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-46429|Aggiungi tabella pivot con l'opzione Mostra pagine filtro report|Nuova caratteristica|
|CELLSNET-46014|Supporta la gestione del contenuto della cella in eccesso durante il salvataggio come PDF e immagine|Nuova caratteristica|
|CELLSNET-46490|Supporta i file Excel95/5.0 XLS|Nuova caratteristica|
|CELLSNET-46500|Ordina per colore di sfondo della cella|Nuova caratteristica|
|CELLSNET-46544|Rileva se il file MHT generato è un foglio di lavoro o meno|Nuova caratteristica|
|CELLSNET-46538|Quando XLSX viene salvato come PDF o TIFF, manca la parte inferiore del testo|Insetto|
|CELLSNET-46509|Le formule R1C1 vengono lette in modo errato per alcune celle|Insetto|
|CELLSNET-46513|Aspose.Cells il motore di calcolo delle formule calcola una formula per la cella come "0" invece di "#RIF!" errore|Insetto|
|CELLSNET-46535|"#NOME?" per le formule salvate nel formato XLSB|Insetto|
|CELLSNET-46539|Formula con distinzione tra maiuscole e minuscole|Insetto|
|CELLSNET-46531|La ridenominazione di ListColumns corrompe la cartella di lavoro (quando è presente una tabella pivot)|Insetto|
|CELLSNET-46511|TIFF creato con pagine bianche aggiuntive|Insetto|
|CELLSNET-46522|Applicazione delle impostazioni internazionali per stampare le intestazioni di configurazione|Insetto|
|CELLSNET-46529|Immagine mancante dopo la conversione da XLSX a PDF|Insetto|
|CELLSNET-46451|Problema durante il rendering del file modello nel formato file PDF|Insetto|
|CELLSNET-46518|Problema di layout (alcune etichette degli assi sono su due righe) durante il rendering del file modello nel formato file PDF|Insetto|
|CELLSNET-46113|Il formato file non è supportato, ad eccezione del documento XLS|Insetto|
|CELLSNET-46504|Problema relativo al percorso dei collegamenti|Insetto|
|CELLSNET-46506|Differenza con il metodo ImportObjectArray|Insetto|
|CELLSNET-46541|Il grafico combinato non funziona con v18.12.x ma funziona con v18.4 e versioni precedenti|Insetto|
|CELLSNET-46543|Eccezione durante la chiamata a Cells.DeleteBlankRows|Eccezione|
|CELLSNET-46459|Viene sollevata un'eccezione durante la conversione nel formato Open Strict XML|Eccezione|
|CELLSNET-46485|Eccezione durante il caricamento di un formato di file XLSB|Eccezione|
|CELLSNET-46508|Eccezione durante il caricamento di un formato di file XLSM|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge il metodo PivotTable.ShowReportFilterPageByName(string fieldName).**
Mostra tutte le pagine del filtro del report in base al nome del PivotField, il PivotField deve trovarsi nei PageField.
#### **Aggiunge il metodo PivotTable.ShowReportFilterPageByIndex(int posIndex).**
Mostra tutte le pagine del filtro del report in base all'indice di posizione nei PageField.
#### **Aggiunge il metodo PivotTable.ShowReportFilterPage(PivotField pageField).**
Mostra tutte le pagine del filtro del report in base a PivotField, il PivotField deve trovarsi nei PageField.
#### **Aggiunge la classe DataSorterKey e DataSorterKeyCollection**
Rappresenta la chiave dell'ordinatore di dati.
#### **Aggiunge il metodo DataSorter.AddKey(Int32,SortOnType,SortOrder,Object)**
Aggiunge la chiave di ordinamento come il colore di sfondo della cella, il colore del carattere.
#### **Aggiunge la proprietà Aspose.Cells.DataSorter.Keys**
Ottiene tutte le chiavi dell'ordinatore dati.
#### **Aggiunge l'enumerazione SortOnType**
Rappresenta il tipo di dati ordinati.
#### **Aggiunge la classe ODSLoadOptions**
Rappresenta le opzioni di caricamento del file ODS.
#### **Aggiunge la proprietà HTMLLoadOptions.ProgId**
Ottiene l'ID del programma di creazione del file. utilizzato solo per i file MHT.
#### **Aggiunge la proprietà PdfSaveOptions.TextCrossType**
Ottiene o imposta la visualizzazione del tipo di testo quando la larghezza del testo è maggiore della larghezza della cella.
#### **Aggiunge la classe enum TextCrossType**
Enumera la visualizzazione del tipo di testo quando la larghezza del testo è maggiore della larghezza della cella.
#### **Aggiunge i metodi WorksheetCollection.RegisterAddInFunction()**
Sostituzione di Cell.SetAddInFormula(), un modo più conveniente ed efficiente per gli utenti di aggiungere e utilizzare funzioni aggiuntive.
#### **Metodo Cell.SetAddInFormula() obsoleto**
Si prega di registrare le funzioni addin in primo luogo da WorksheetCollection.RegisterAddInFunction() e quindi impostare la formula per Cell da Cell.Formula/Cell.SetFormula() invece.
