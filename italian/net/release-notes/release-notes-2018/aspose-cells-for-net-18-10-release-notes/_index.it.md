---
title: Aspose.Cells for .NET Note sulla versione 18.10
type: docs
weight: 30
url: /it/net/aspose-cells-for-net-18-10-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 18.10](https://www.nuget.org/packages/Aspose.Cells/18.10.0).

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-46311|Ottieni punti di connessione dalle forme|Nuova caratteristica|
|CELLSNET-46194|Cambia la larghezza della dimensione fissa delle colonne (ad esempio, pt/px) in unità scalabili come "em" o "percentuale"|Aumento|
|CELLSNET-46383|Problema con l'origine dell'immagine durante il rendering di Excel nel formato file HTML|Insetto|
|CELLSNET-46367|La dimensione del carattere è cambiata da 6,5 a 6 durante la conversione da XLSX a HTML|Insetto|
|CELLSNET-46353| Riconosci i tag vuoti come<td /> durante la conversione di HTML nel formato di file MS Excel|Insetto|
|CELLSNET-46341|Subtotale mancante quando le righe vengono compresse dopo l'aggiornamento|Insetto|
|CELLSNET-46330|Problema nei campi numerici durante la chiamata a Worksheet.AutoFitColumns()|Insetto|
|CELLSNET-42681|XLSB il file viene danneggiato all'apertura e al salvataggio|Insetto|
|CELLSNET-46382|CSV l'importazione crea una formattazione errata utilizzando PreferredParsers|Insetto|
|CELLSNET-46338|"_xll" attaccato davanti al nome della formula|Insetto|
|CELLSNET-46334|La formula dell'intervallo denominato ("=GET.CELL") non è stata creata correttamente nella lingua tedesca|Insetto|
|CELLSNET-46321|Il carattere di escape viene visualizzato così com'è in PDF|Insetto|
|CELLSNET-46376|PDF la dimensione della pagina di output (e i margini) non corrispondono all'output di MS Excel|Insetto|
|CELLSNET-46373|Altezza dell'immagine nell'intestazione troncata insieme a layout interrotto durante la conversione XLSM->PDF|Insetto|
|CELLSNET-46349|L'immagine non si ripete correttamente quando i titoli di stampa sono impostati per righe e colonne|Insetto|
|CELLSNET-46358|Il rendering dell'immagine da un semplice grafico prende tutte le risorse e quindi solleva un'eccezione|Insetto|
|CELLSNET-46343|L'accesso alle proprietà di visibilità ha modificato la visibilità del grafico nell'output risalvato|Insetto|
|CELLSNET-46390|La proprietà SourceFullName dell'oggetto OLE è vuota durante l'accesso in XLSB|Insetto|
|CELLSNET-46385|L'immagine/forma dell'intestazione non viene visualizzata correttamente quando si salva nuovamente un file XLSX|Insetto|
|CELLSNET-46384|Differenza negli oggetti OLE prima e dopo il salvataggio del file XLSB|Insetto|
|CELLSNET-46378|Guida fonetica mancante dopo copia e salvataggio|Insetto|
|CELLSNET-46375|Il ridimensionamento delle tabelle modifica il formato delle celle|Insetto|
|CELLSNET-46374|Rilevamento errato del colore di primo piano e di sfondo della cella|Insetto|
|CELLSNET-46369|L'adattamento automatico avviene automaticamente per le righe nascoste quando le righe vengono filtrate automaticamente|Insetto|
|CELLSNET-46368|Lo schema personalizzato 'm-files://...' viene convertito nell'operazione di salvataggio del documento|Insetto|
|CELLSNET-46357|XLSB i file non possono essere aperti utilizzando LoadDataFilterOption diverso da LoadDataFilterOption.All|Insetto|
|CELLSNET-46356|Nella formula mancano le virgolette singole|Insetto|
|CELLSNET-46351|LoadDataFilterOptions.SheetSettings non funziona per i file XLSB|Insetto|
|CELLSNET-46350|La vista è cambiata in protetta durante la conversione XLS -> XLSM -> XLS|Insetto|
|CELLSNET-46347|Il file XLSX è danneggiato dopo la conversione da un file XML (SpreadsheetML)|Insetto|
|CELLSNET-46344|Smart Marker non valuta correttamente ISBLANK|Insetto|
|CELLSNET-46319|FilterOperatorType.Contains mancante da API|Insetto|
|CELLSNET-46354|Si è verificata un'eccezione durante il caricamento di un file Excel|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge la proprietà HtmlSaveOptions.WidthScalable**
Indica se si utilizza l'unità scalabile per descrivere la larghezza della colonna durante l'esportazione del file in HTML. Il valore predefinito è false.
#### **Aggiunge la proprietà WorkbookDesigner.UpdateEmptyStringAsNull**
Indica se elaborare il valore della stringa vuota come null.
#### **Aggiorna il valore restituito del metodo DocumentProperty.ToDateTime(), le proprietà BuiltInDocumentPropertyCollection.CreatedTime, BuiltInDocumentPropertyCollection.LastPrinted e BuiltInDocumentPropertyCollection.LastSavedTime.**
Restituisce l'ora nel fuso orario locale.
#### **Richiede un vincolo più forte per l'input dell'utente per FormatCondition.Formula1/Formula2**
La semplice stringa di input non può essere determinata se deve fare riferimento a un riferimento al nome o è solo un valore di stringa costante. Quindi, ora richiediamo che la formula inizi con il segno '='. Per il valore di stringa semplice "sss", utilizza un formato come "=\"sss\"".
