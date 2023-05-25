---
title: Aspose.Cells for .NET 23.5 Note di rilascio
type: docs
weight: 8
url: /it/net/aspose-cells-for-net-23-5-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 23.5](https://www.nuget.org/packages/Aspose.Cells/23.5.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
| :- | :- | :- |
|CELLSNET-53234|Supporto per aggiornare i riferimenti dei dati del foglio esterno al foglio locale durante la rimozione dei collegamenti esterni|
|CELLSNET-46133|Renderizza il controllo Casella di controllo come controllo e non come immagine statica|
|CELLSNET-53252|Imposta la dimensione desiderata dell'immagine e mantieni le proporzioni durante la conversione della cartella di lavoro in immagini|
|CELLSNET-53267|Righe AutoFit per il rendering|
|CELLSNET-53109|Supporto per ottenere PivotArea e PivotFormat|
|CELLSNET-53216| La dimensione del file del pdf generato è troppo grande durante la conversione in pdf|
|CELLSNET-53181|Indice di colonna non valido.' sul salvataggio del pdf|
|CELLSNET-53192|Il simbolo di spunta non viene visualizzato correttamente durante la conversione di Excel in pdf|
|CELLSNET-53292|Rotazione anomala del testo durante la conversione del file in Pdf|
|CELLSNET-53293|Errore di posizione della linea di connessione durante la conversione del file in Pdf|
|CELLSNET-46629|Conversione da Excel a PDF con oggetto sequenza temporale|
|CELLSNET-53124| L'impostazione dei valori e il calcolo danneggiano la cartella di lavoro nella versione recente di Aspose.Cells|
|CELLSNET-53186| Impossibile analizzare la formula che contiene un'intera colonna nel file dei numeri Apple|
|CELLSNET-53208|Il file si rompe dopo la rimozione della formula|
|CELLSNET-53228|Il layout della legenda non è coerente con Excel quando dal grafico all'immagine|
|CELLSNET-53229|Il colore dell'asse non è coerente con Excel quando il grafico viene visualizzato sull'immagine|
|CELLSNET-53235| Il grafico degli errori non viene visualizzato|
|CELLSNET-53153|Impossibile generare PDF durante la conversione di un file con molte immagini|
|CELLSNET-53209| Un file danneggiato viene generato durante la conversione di un file di grandi dimensioni in PDF|
|CELLSNET-53286|Errore di conversione dell'immagine di intestazione durante la conversione del file in PDF|
|CELLSNET-49624|Problema di ritorno a capo durante la conversione da XLSX a HTML|
|CELLSNET-51101|Conversione da Excel a HTML: la formattazione/i contenuti sono distorti e disordinati|
|CELLSNET-53206| Esporta intervallo come HTML con collegamenti cambia stili/formattazione|
|CELLSNET-53133|Excel si arresta in modo anomalo con il documento salvato da Aspose.Cells|
|CELLSNET-53180|Consenti al testo di traboccare le impostazioni della forma da cancellare durante il salvataggio del file in xls|
|CELLSNET-53185|Dimensione del foro del grafico a ciambella persa durante il salvataggio come ODS|
|CELLSNET-53191|Errore del margine di testo della casella di testo durante il salvataggio del file in xls|
|CELLSNET-53207| Il foglio di calcolo Excel non viene visualizzato correttamente in PDF (con tutti i dati/contenuti) finché non viene salvato tramite MS Excel|
|CELLSNET-53218|Il grafico della tabella pivot viene visualizzato in modo diverso nel file PDF convertito dopo aver aggiornato la tabella pivot|
|CELLSNET-53258|Allineamento del titolo del grafico modificato da sinistra al centro durante il salvataggio del file|
|CELLSNET-53260|TextBox può essere modificato dopo aver impostato la protezione|
|CELLSNET-53268|Gli zeri iniziali vengono rimossi|
|CELLSNET-53271|La dimensione del carattere cambia durante il salvataggio del file come xls|
|CELLSNET-53279|Il tipo di carattere restituito del testo formattato RTF non è lo stesso di Excel.|
|CELLSNET-53283|Il carattere del grafico Lenged non è lo stesso di Excel|
|CELLSNET-53285|La tabella non dovrebbe espandersi se contiene una riga totale.|
|CELLSNET-53287| L'immagine nell'intestazione dovrebbe essere visualizzata in scala di grigi e in due colori (bianco e nero)|
|CELLSNET-53251|Riferimento alla tabella non valido CellsException durante il roundtrip|

##  **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

###  **Modifica il comportamento dei metodi ExternalLinkCollection.Clear(bool)/RemoveAt(int,bool).**

Nelle versioni precedenti, quando "updateReferencesAsLocal" è vero, aggiorniamo solo quei riferimenti di nomi esterni ai nomi locali della cartella di lavoro corrente. Per i riferimenti dei dati dei fogli esterni, li abbiamo aggiornati come "#REF!" Sempre. Dal 23.5, se nella cartella di lavoro corrente è presente un foglio di lavoro con lo stesso nome del foglio del riferimento esterno, anche il riferimento verrà aggiornato al foglio locale.

###  **Aggiunge il metodo Row.GetEnumerator(bool reversed, bool sync).**

Fornire all'utente la possibilità di attraversare Cell in ordine inverso.

###  **Obsoleti Cells.GetRowEnumerator()**

Utilizzare invece RowCollection.GetEnumerator().

###  **Obsolesce il metodo Chart.IsReferedByChart() e aggiunge il metodo Chart.IsCellReferedByChart()**

Utilizzare invece Chart.IsCellReferedByChart().

###  **Aggiunge la proprietà SeriesLayoutProperties.IsIntervalLeftClosed**

Indica se l'intervallo è chiuso sul lato sinistro.

###  **Aggiunge la proprietà ShapeTextAlignment.IsLockedText**

Indica se il testo della forma è bloccato.

###  **Rimuove la classe ShapeFormat obsoleta e Shape.ShapeFormat**

Usare invece la proprietà Shape.Line e Shape.Fill.

###  **Aggiunge la proprietà ListColumn.TotalsRowLabel**

Ottiene e imposta l'etichetta della riga dei totali nella tabella.

###  **Aggiunge il metodo ListObject.PutCellValue(Int32,Int32,Object,Boolean)**

Imposta il valore sulla cella nella tabella.

###  **Aggiunge l'enumerazione PivotAreaType e la proprietà PivotArea.RuleType**

Ottiene e imposta il tipo di area pivot nella tabella pivot.

###  **Aggiunge la classe PivotTableFormat**

Rappresenta il formato della tabella pivot.

###  **Aggiunge la classe PivotTableFormatCollection**

Rappresenta tutti i formati per la tabella pivot.

###  **Aggiunge la proprietà PivotTable.PivotFormats**

Ottiene e aggiunge tutti i formati per la tabella pivot.

###  **Aggiunge la proprietà PivotTable.AutofitColumnWidthOnUpdate**

Indica se l'adattamento automatico della larghezza della colonna durante l'aggiornamento della tabella pivot.

###  **Aggiunge la classe PivotAreaFilter e PivotAreaFilterCollection**

Rappresenta i filtri per selezionare l'area pivot nella tabella pivot.

###  **Aggiunge la proprietà PivotArea.Filters**

Rappresenta i filtri per selezionare l'area pivot nella tabella pivot.

###  **Aggiunge le proprietà PivotArea.IsRowGrandIncluded e PivotArea.IsColumnGrandIncluded**

Indica se includere il totale generale di riga o di colonna nell'area.

###  **Aggiunge la proprietà PivotArea.AxisType**

Ottiene e imposta l'area della tabella pivot a cui si applica questa regola.

###  **Aggiunge la proprietà PivotArea.IsOutline**

Indica se la regola fa riferimento all'area pivot in modalità struttura.

###  **Aggiunge il metodo ImageOrPrintOptions.SetDesiredSize(int desireWidth, int desireHeight, bool keepAspectRatio)**

Imposta la larghezza e l'altezza desiderate dell'immagine e specifica se mantenere le proporzioni dell'immagine di origine.

###  **Metodo ImageOrPrintOptions.SetDesiredSize(int desiredWidth, int desireHeight) obsoleto**

Utilizzare invece ImageOrPrintOptions.SetDesiredSize(desiredWidth, desireHeight, false).

###  **Aggiunge la proprietà PdfSaveOptions.Watermark**

Ottiene o imposta la filigrana sull'output.

###  **Aggiunge le classi RenderingFont e RenderingWatermark**

Per aggiungere filigrana all'output del rendering.

###  **Aggiunge la proprietà AutoFitterOptions.ForRendering**

Indica se adatto allo scopo di rendering.
 
###  **Modifica la definizione di EquationNodeParagraph.EquationHorizontalJustificationType**

Passaggio dalla variabile di istanza all'accesso a proprietà/metodo.

