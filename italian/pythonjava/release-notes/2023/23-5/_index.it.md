---
title: Aspose.Cells for Python via Java 23.5 Note di rilascio
type: docs
weight: 8
url: /it/python-java/aspose-cells-for-python-via-java-23-5-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Python via Java 23.5](https://downloads.aspose.com/cells/python-java/new-releases/aspose.cells-for-python-via-java-23.5/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
| :- | :- | :- |
|CELLSJAVA-45230|Supporto per aggiungere filigrana durante il rendering in pdf|
|CELLSJAVA-45334|I dati nella casella di testo sono fuori limite|
|CELLSJAVA-45336|Il testo viene spostato durante la conversione di forme automatiche raggruppate in pdf|
|CELLSJAVA-45364|Il testo verticale nella figura in Excel è inclinato quando viene convertito in PDF|
|CELLSJAVA-45366|Errore di visualizzazione della forma ovale durante l'esportazione del file in html|
|CELLSJAVA-45369| Font sostituito dei problemi delle caselle di testo|
|CELLSJAVA-45290|Le regole di riferimento per la formattazione condizionale non vengono aggiornate correttamente quando si copiano intervalli da una cartella di lavoro a un'altra cartella di lavoro|
|CELLSJAVA-45362|Il grafico degli errori non viene visualizzato|
|CELLSJAVA-45363|Ciclo infinito durante la conversione di grafici in immagine|
|CELLSJAVA-45239|Cell l'allineamento della giustificazione verticale non ha effetto quando si salva in html|
|CELLSJAVA-45335|Il testo è fuori posto quando la cella è formattata come numero nell'output html|
|CELLSJAVA-45323| La rimozione delle impostazioni di adattamento automatico sulle colonne della tabella pivot rimuove lo stile/la formattazione della tabella pivot|
|CELLSJAVA-45341|Lo stile dei grafici viene perso durante il caricamento e il salvataggio del vecchio flusso della cartella di lavoro|
|CELLSJAVA-45351|L'area pivot del formato include solo i totali parziali del campo pivot|
|CELLSJAVA-45374|Il programma si blocca all'apertura del file XML|
|CELLSJAVA-45319|L'angolo di fetta del grafico a torta 3D non è corretto durante la conversione del file in ODS|

##  **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

###  **Modifica il comportamento dei metodi ExternalLinkCollection.Clear(bool)/RemoveAt(int,bool).**

Nelle versioni precedenti, quando "updateReferencesAsLocal" è vero, aggiorniamo solo quei riferimenti di nomi esterni ai nomi locali della cartella di lavoro corrente. Per i riferimenti dei dati dei fogli esterni, li abbiamo aggiornati come "#REF!" Sempre. Dal 23.5, se nella cartella di lavoro corrente è presente un foglio di lavoro con lo stesso nome del foglio del riferimento esterno, anche il riferimento verrà aggiornato al foglio locale.

###  **Aggiunge il metodo Row.iterator(bool reversed, bool sync).**

Fornire all'utente la possibilità di attraversare Cell in ordine inverso.

###  **Obsoleti Cells.getRowEnumerator()**

Utilizzare invece RowCollection.iterator().

###  **Obsolesce il metodo Chart.IsReferedByChart() e aggiunge il metodo Chart.IsCellReferedByChart()**

Utilizzare invece Chart.IsCellReferedByChart().

###  **Aggiunge la proprietà SeriesLayoutProperties.IsIntervalLeftClosed**

Indica se l'intervallo è chiuso sul lato sinistro.

###  **Aggiunge la proprietà ShapeTextAlignment.IsLockedText**

Indica se il testo della forma è bloccato.

###  **Rimuove la classe ShapeFormat obsoleta e Shape.ShapeFormat**

Usare invece la proprietà Shape.Line e Shape.Fill.

###  **Aggiunge la proprietà ListColumn.TotalsRowLabel**

Ottiene e imposta l'etichetta della riga toals nella tabella.

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
