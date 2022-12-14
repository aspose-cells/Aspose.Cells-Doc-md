---
title: Aspose.Cells for .NET 19.6 Note di rilascio
type: docs
weight: 70
url: /it/net/aspose-cells-for-net-19-6-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 19.6](https://www.nuget.org/packages/Aspose.Cells/19.6.0).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-41277|Commenti nell'esportazione HTML di file XLS/XLSX|Nuova caratteristica|
|CELLSNET-45194|Supporta il disegno di Slicer durante il rendering in PDF|Nuova caratteristica|
|CELLSNET-46742|Aggiunto il supporto del formato di file OpenDocument Flat XML Spreadsheet (.fods).|Nuova caratteristica|
|CELLSNET-46744|Aggiunto il supporto del formato di file StarOffice Calc Spreadsheet (.sxc).|Nuova caratteristica|
|CELLSNET-46714|File OOXML incorporato come pacchetto per XLSX.|Aumento|
|CELLSNET-46722|Avviso di sicurezza dopo il nuovo salvataggio di un formato di file XLS|Aumento|
|CELLSNET-46737|Problemi con linee medie/linee spesse quando XLSX è stato salvato come ODS|Aumento|
|CELLSNET-46755|Rilevamento se il file oggetto è grafico o oleooggetto per ODS.|Aumento|
|CELLSNET-46731|Worksheet.Copy() blocca l'applicazione|Prestazione|
|CELLSNET-46770|Memoria insufficiente durante l'aggiornamento della tabella pivot con un'origine dati di grandi dimensioni|Prestazione|
|CELLSNET-46730|Chart.ToImage() blocca l'applicazione|Prestazione|
|CELLSNET-46670|contenuti dei file Excel vengono sovrapposti dopo l'aggiunta di proprietà personalizzate|Insetto|
|CELLSNET-46747|Le linee della griglia vengono stampate sull'oggetto incorporato durante il rendering in PDF|Insetto|
|CELLSNET-41479|Impostazioni Slicer nel PDF generato|Insetto|
|CELLSNET-41783|I file generati da un file modello che contiene un'affettatrice devono essere riparati|Insetto|
|CELLSNET-46733|Stile/formato perso durante il salvataggio della tabella pivot come HTML|Insetto|
|CELLSNET-46736|Problema di carattere quando l'HTML viene convertito in PDF|Insetto|
|CELLSNET-46751|XLSX non può essere convertito in HTML|Insetto|
|CELLSNET-46766|La funzione XIRR non funziona se l'ultima riga è maggiore di -62 nell'intervallo|Insetto|
|CELLSNET-46769|Cell valore estratto diverso da Excel nella cultura tedesca|Insetto|
|CELLSNET-46761|Problema con la visualizzazione Aspose.Cells.GridDesktop quando si impostano risoluzioni e si ingrandisce un monitor 4k|Insetto|
|CELLSNET-46592|Problemi di rendering del testo durante la conversione di XLSX in PDF|Insetto|
|CELLSNET-46735|Il numero di pagina non ricomincia da 1 su ciascun foglio nel PDF di output|Insetto|
|CELLSNET-46739|Il tipo di compressione tiff ignora l'ombreggiatura di sfondo per grafici e forme|Insetto|
|CELLSNET-46749|SheetRender.ToImage crea un'immagine EMF errata|Insetto|
|CELLSNET-46093|I grafici non rispettano l'impostazione della pagina in bianco e nero|Insetto|
|CELLSNET-46738|Aspose.Cells 19.4 Impossibile aprire alcuni file .ots e .ods|Insetto|
|CELLSNET-46741|Risultato errato quando si lavora con elenchi nidificati|Insetto|
|CELLSNET-46748|Il file di output è sempre danneggiato quando si utilizzano le licenze a consumo|Insetto|
|CELLSNET-46752|Il file XLSX di output viene danneggiato dopo aver chiamato InsertCutCells()|Insetto|
|CELLSNET-46754|Gli intervalli denominati cambiano quando viene chiamata la funzione InsertCutCells()|Insetto|
|CELLSNET-46759|Nessuna eccezione generata durante il caricamento di un flusso errato nella cartella di lavoro|Insetto|
|CELLSNET-46043|System.InvalidCastException|Eccezione|
|CELLSNET-46510|Errore da forma a immagine! durante la conversione di XLSX in PDF|Eccezione|
|CELLSNET-46765|Eccezione "System.StackOverflowException" durante il rendering di un file Excel in formato file PDF|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge enum FileFormatType.FODS,FileFormatType.SXC,LoadFormat.FODS,LoadFormat.SXC,SaveFormat.FODS e SaveFormat.SXC**
Rappresenta i tipi di formato file .FODS e .SXC.
#### **Aggiunge enum WarningType.UnsupportedFileFormat**
Rappresenta il formato di file non supportato per i tipi di avviso.
#### **Aggiunge enum ODSGeneratorType**
Rappresenta il tipo di generatore di ODS.
#### **OoxmlSaveOptions.EmbedOoxmlAsOleObject**
Indica se incorporare il file ooxml come OleObject.
#### **Aggiunge Row.CopySettings(Aspose.Cells.Row,System.Boolean)**
Copia le impostazioni della riga, come stile, altezza, visibilità, ...ecc.
