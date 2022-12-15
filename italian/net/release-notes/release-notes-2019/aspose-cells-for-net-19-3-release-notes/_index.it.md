---
title: Aspose.Cells for .NET 19.3 Note di rilascio
type: docs
weight: 100
url: /it/net/aspose-cells-for-net-19-3-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 19.3](https://www.nuget.org/packages/Aspose.Cells/19.3.0).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-46598|Aggiungere il metodo Name.GetReferredAreas (ricalcolo booleano) per fornire dati più ricchi (inclusi riferimenti esterni e dati collegati)|Nuova caratteristica|
|CELLSNET-46580|Rendering errato delle forme ruotate nella conversione da forma a immagine|Insetto|
|CELLSNET-46587|La tabella pivot si interrompe quando si eliminano righe e colonne|Insetto|
|CELLSNET-46608|I filtri della tabella pivot vengono cancellati dopo il caricamento e il salvataggio|Insetto|
|CELLSNET-46623|Problemi negli URL dei file condivisi incorporati durante la conversione del file Excel in HTML|Insetto|
|CELLSNET-46590|Errore in una cella che chiama una macro dopo che il file è stato elaborato da Aspose.Cells|Insetto|
|CELLSNET-46597|Valore errato in PDF nel rendering da Excel a PDF|Insetto|
|CELLSNET-46613|Problemi durante il recupero e la creazione di intervalli denominati|Insetto|
|CELLSNET-46625|Sfondo della tabella errato nell'output PDF e HTML|Insetto|
|CELLSNET-46628|Differenza nel PDF di output|Insetto|
|CELLSNET-46589|Griglie impreviste sono apparse in SVG convertite dal foglio di lavoro MS Excel|Insetto|
|CELLSNET-46600|La doppia sottolineatura scompare durante la conversione del file Excel in PDF|Insetto|
|CELLSNET-46626|Problemi di formattazione dello spazio durante la conversione di file XLSX in PDF|Insetto|
|CELLSNET-46585|Problema con il carattere DataLabel|Insetto|
|CELLSNET-46602|OutOfMemoryException durante il rendering di un grafico a barre verticale o orizzontale|Insetto|
|CELLSNET-46605|La riga aumenta di altezza dopo l'operazione di adattamento automatico delle righe (opzioni).|Insetto|
|CELLSNET-46609|L'opzione di inserimento CopyFormatType.Clear non funziona correttamente|Insetto|
|CELLSNET-46611|Problemi con i collegamenti esterni e la sua visualizzazione|Insetto|
|CELLSNET-46616|Gestione di ListObject.ConvertToRange su tabelle gigantesche|Insetto|
|CELLSNET-46620|Line.SolidFill.Color funziona in modo improprio sulle forme quando si passa il colore da Argb o da un nome noto|Insetto|
|CELLSNET-46622|Cells.ImportData importa un numero errato di colonne da datatable|Insetto|
|CELLSNET-46624|Problema di caricamento del file XLSX|Insetto|
|CELLSNET-46635|Troppe interruzioni di pagina nel file ODS (rendering da XLSX a ODS)|Insetto|
|CELLSNET-46618|Eccezione "L'istanza è di sola lettura"|Eccezione|
|CELLSNET-46617|Eccezione durante il caricamento di una cartella di lavoro|Eccezione|
|CELLSNET-46636|Eccezione durante il caricamento di un file XLSX|Eccezione|
### **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.
#### **Modifiche per il carattere predefinito del file modello XLS caricato**
Nelle versioni precedenti, non supportavamo l'applicazione del carattere definito nel tema (funzionalità avanzata in MS Excel 2007 e versioni successive) in base alla regione durante il caricamento dei file modello XLS. Su richiesta di alcuni utenti, lo abbiamo supportato dalla v19.3. Se la regione è stata specificata nel file modello XLS, applicheremo il carattere definito nel tema in base al valore della regione specificato salvato. Altrimenti applicheremo il carattere definito nel tema in base alle impostazioni regionali dell'ambiente dell'applicazione. Ciò causerà la modifica del carattere predefinito della cartella di lavoro (caricato dal file modello XLS che ha specificato i dati del tema) e quindi influenzerà altre funzionalità, come la larghezza della colonna, la dimensione della forma, l'effetto di rendering, ... ecc.
#### **Aggiunge il metodo Name.GetReferredAreas(bool recalculate).**
Fornisce i riferimenti a cui fa riferimento il nome definito come metodo GetRanges(bool recalculate). Ma i riferimenti restituiti sono rappresentati dall'oggetto ReferredArea che fornisce funzionalità più ricche, inclusi collegamenti esterni.
#### **Aggiunge la proprietà TxtSaveOptions.KeepSeparatorsForBlankRow**
Indica se i separatori devono essere emessi per la riga vuota. Il valore predefinito è false, il che significa che il contenuto della riga vuota sarà vuoto.
#### **Aggiunge enum AutoFitMergedCellsType**
Rappresenta il tipo di celle unite con adattamento automatico.
#### **Obsoleta la proprietà AutoFitterOptions.AutoFitMergedCells e aggiunge la proprietà AutoFitterOptions.AutoFitMergedCellsType**
Ottiene e imposta il tipo di altezza della riga di adattamento automatico.
#### **Aggiunge le classi JSONUtility e JsonLayoutOptions**
È usato per importare file json.
#### **Aggiunge la classe TableToRangeOptions e il metodo ListObject.ConvertToRange(TableToRangeOptions options)**
Converte la tabella in un intervallo con opzioni.
