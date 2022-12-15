---
title: Aspose.Cells for .NET 19.5 Note di rilascio
type: docs
weight: 80
url: /it/net/aspose-cells-for-net-19-5-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 19.5](https://www.nuget.org/packages/Aspose.Cells/19.5.0).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-46703|Il nuovo calendario giapponese non viene visualizzato correttamente|Nuova caratteristica|
|CELLSNET-46693|Supporta il background di ODS|Nuova caratteristica|
|CELLSNET-46695|Imposta lo sfondo del file ODS|Nuova caratteristica|
|CELLSNET-46706|Ordine numerico non valido durante la conversione del carattere arabo in PDF.|Aumento|
|CELLSNET-46692|Controlla tutti i dati esterni con l'interfaccia IStreamProvider|Aumento|
|CELLSNET-46711|ImportCustomObjects in un'area unita interrompe l'unione|Aumento|
|CELLSNET-46713|Il metodo "String.StartsWith("\0")" restituisce sempre true su macOS|Aumento|
|CELLSNET-46719|Eccezione durante l'impostazione della stringa HTML utilizzando il modello di colore RGBA|Aumento|
|CELLSNET-46701|L'elaborazione dei grafici a bolle si blocca con la versione 19.4|Insetto|
|CELLSNET-46682|L'opzione "Nascondi elementi senza dati" per le impostazioni Slicer è deselezionata|Insetto|
|CELLSNET-46707|PivotTable.GetChildren() restituisce un numero errato di dipendenze|Insetto|
|CELLSNET-46689|Il salvataggio di una cartella di lavoro come PDF è diverso dall'output nativo di Excel|Insetto|
|CELLSNET-46704|L'output della conversione di Excel in PDF utilizzando Aspose.Cells è diverso da Excel|Insetto|
|CELLSNET-46720|La struttura della pagina è danneggiata nell'ultima pagina nella conversione da Excel a PDF|Insetto|
|CELLSNET-46727|Numerazione delle pagine errata durante il salvataggio della cartella di lavoro come PDF|Insetto|
|CELLSNET-46700|Le etichette dei dati del grafico a torta si sovrappongono l'una all'altra|Insetto|
|CELLSNET-46696|La conversione di XLS con Microsoft graph chart in XLSX e XLSM causa un errore di contenuto illeggibile|Insetto|
|CELLSNET-46697|La conversione di XLSM con oggetto OLE in XLS causa un errore|Insetto|
|CELLSNET-46712|La conversione di XLS con Microsoft graph chart in XLSX e XLSM causa un errore di contenuto illeggibile|Insetto|
|CELLSNET-46715|Cells.InsertCutCells() Problema|Insetto|
|CELLSNET-46725|"_x000a_" la stringa viene aggiunta nella descrizione del testo alternativo del grafico multilinea|Insetto|
|CELLSNET-46683|Eccezione durante il rendering di un file Excel in PDF|Eccezione|
|CELLSNET-46690|Viene generata un'eccezione durante il caricamento della cartella di lavoro di Excel da Shape.ForeignData (Diagram)|Eccezione|
|CELLSNET-46728|Eccezione durante il salvataggio del flusso come cartella di lavoro|Eccezione|
### **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.
#### **Aggiunge il costruttore StreamProviderOptions**
Nuove opzioni StreamProvider.
#### **Aggiunge l'enumerazione FileFormatType.GraphChart**
Rappresenta il file grafico del grafico incorporato.
#### **Aggiunge le proprietà ImportTableOptions.CheckMergedCells**
Indica se controllare le celle unite durante l'importazione dei dati.
#### **Aggiunge le classi ODSCellFieldCollection, ODSCellField e l'enumerazione ODSCellFieldType.**
Rappresenta il campo cellulare di ODS.
#### **Aggiunge le proprietà Cells.ODSCellFields.**
Ottiene l'elenco dei campi cella di ODS.
#### **Aggiunge la classe ODSPageBackground e la proprietà PageSetup.ODSPageBackground**
Rappresenta lo sfondo di ODS.
