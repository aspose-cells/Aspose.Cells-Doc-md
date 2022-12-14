---
title: Aspose.Cells for .NET 19.9 Note di rilascio
type: docs
weight: 40
url: /it/net/aspose-cells-for-net-19-9-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 19.9](https://www.nuget.org/packages/Aspose.Cells/19.9.0).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-46864|Supporta la lettura e il rendering Controllo dei file ODS|Nuova caratteristica|
|CELLSNET-46877|Aggiungere l'overload SheetRender.ToPrinter(PrinterSettings PrinterSettings) alle API|Nuova caratteristica|
|CELLSNET-46907|Configura il livello di compressione ZIP per XLSX/XLSB|Nuova caratteristica|
|CELLSNET-46890|I risultati della divisione di numeri interi non devono essere assegnati a variabili in virgola mobile|Insetto|
|CELLSNET-46883|Le tabelle pivot non conservano più opzioni di selezione dopo l'elaborazione degli indicatori intelligenti|Insetto|
|CELLSNET-46874|Valori non derivati dalla formula e richiedono la pressione di F2 per ottenere i valori nelle celle|Insetto|
|CELLSNET-46904|I collegamenti ipertestuali vengono persi durante l'importazione di dati da DataTable|Insetto|
|CELLSNET-46875|I contenuti fuoriescono dalla pagina durante la conversione PDF|Insetto|
|CELLSNET-46865|Un oggetto viene modificato dopo l'apertura e il salvataggio|Insetto|
|CELLSNET-46866|L'impostazione del carattere e della dimensione del carattere di Drawing.TextBox non funziona in ODS|Insetto|
|CELLSNET-46867|Caselle di controllo perse durante il nuovo salvataggio di XLSX|Insetto|
|CELLSNET-46873|Rif! visualizzato come formula non applicata|Insetto|
|CELLSNET-46876|Collegamento oggetto OLE non accessibile dal file XLS|Insetto|
|CELLSNET-46881|Raggruppare e separare non nasconde i bordi|Insetto|
|CELLSNET-46884|I fogli di lavoro vengono raggruppati durante l'utilizzo di VisibilityType.VeryHidden/Hidden|Insetto|
|CELLSNET-46886|Tabella con riga singola che si espande in una riga aggiuntiva sotto dopo aver salvato la cartella di lavoro|Insetto|
|CELLSNET-46887|La formattazione condizionale non viene mantenuta dopo aver aperto il file in MS Excel e averlo salvato.|Insetto|
|CELLSNET-46891|Il riempimento sfumato di OleObject viene letto come FillType.Solid|Insetto|
|CELLSNET-46894|Mostra l'impostazione della scheda del foglio deselezionata durante il salvataggio del file Excel|Insetto|
|CELLSNET-46906|Aspose.Cells impiccato all'apertura di un file XLSX|Insetto|
|CELLSNET-46909|La formattazione dell'oggetto OLE è cambiata dopo l'apertura e il salvataggio del file Excel|Insetto|
|CELLSNET-46857|Le connessioni del filtro sul grafico pivot perdono le impostazioni al salvataggio dopo l'aggiornamento delle tabelle pivot|Insetto|
|CELLSNET-46862|L'impostazione "Nascondi elementi senza dati" nell'affettatrice viene persa dopo l'aggiornamento delle tabelle pivot|Insetto|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Rimuove la proprietà Chart.Rotation obsoleta**
Usare invece la proprietà Chart.RotationAngle.
#### **Rimuove la proprietà Chart.IsDataTableShown obsoleta**
Usare invece Chart.ShowDataTableproperty.
#### **Rimuove la proprietà Chart.IsLegendShown obsoleta**
Usare invece la proprietà Chart.ShowLegend.
#### **Rimuove la proprietà obsoleta Axis.Crosses**
Utilizzare invece la proprietà Axis.Crosses.
#### **Rimuove la classe obsoleta HTMLLoadOptions**
Utilizzare invece la classe HtmlLoadOptions.
#### **Rimuove la classe obsoleta JSONUtility**
Utilizzare invece la classe JsonUtility.
#### **Aggiunge le proprietà enum OoxmlCompressionType e XlsbSaveOptions.CompressionType,OoxmlSaveOptions.CompressionType.**
Rappresenta il tipo di compressione per i file OOXML.
#### **Rimuove la classe obsoleta ODSLoadOptions**
Utilizzare invece la classe OdsLoadOptions.




