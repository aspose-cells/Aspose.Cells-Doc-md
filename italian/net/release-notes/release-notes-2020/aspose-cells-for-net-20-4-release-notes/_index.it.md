---
title: Aspose.Cells for .NET 20.4 Note di rilascio
type: docs
weight: 40
url: /it/net/aspose-cells-for-net-20-4-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 20.4](https://www.nuget.org/packages/Aspose.Cells/20.4.0).

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-47276|Da XLSX a CSV, virgole richieste per celle vuote simili anche a MS Excel|Nuova caratteristica|
|CELLSNET-47054|Supporta l'unione di più celle come intervallo|Nuova caratteristica|
|CELLSNET-47091|Opzione per aggiornare il campo di origine di PowerQueryFormulaItems|Nuova caratteristica|
|CELLSNET-47273|Impostare il carattere del testo latino e il carattere del testo asiatico per l'asse delle categorie del grafico|Aumento|
|CELLSNET-47217|Supporta la barra dati, la scala dei colori e le formattazioni condizionali iconset di ODS.|Aumento|
|CELLSNET-47201|Apri il file protetto da password utilizzando Aspose.Cells.GridDesktop|Aumento|
|CELLSNET-47254|Supporto per inserire una nuova riga come in MS-EXCEL nella barra della formula|Aumento|
|CELLSNET-47224|Migliora le prestazioni dei pivotable rinfrescanti.|Prestazione|
|CELLSNET-47243|Aspetta GetDisplayStyle per un foglio di lavoro con righe 65536|Prestazione|
|CELLSNET-47289|CalculateFormula() non ritorna mai|Prestazione|
|CELLSNET-47263|Sospeso durante il tentativo di aprire il documento ODP nel costruttore di cartelle di lavoro|Prestazione|
|CELLSNET-42556|L'ordinamento di PivotField non sembra funzionare|Insetto|
|CELLSNET-47046|Delimitatori di virgolette non aperte negli attributi IMG HTML nel markup HTML generato|Insetto|
|CELLSNET-47208|La tabella pivot non mantiene il formato con l'ultima versione|Insetto|
|CELLSNET-47219|Formula errata nella colonna della tabella dopo l'inserimento di una riga e l'aggiornamento|Insetto|
|CELLSNET-47261|Rendering da Excel a HTML: dimensione del carattere errata in una tabella esportata|Insetto|
|CELLSNET-47279|Il testo della prima colonna in tutte le righe non è contrassegnato durante l'esportazione del file in HTML|Insetto|
|CELLSNET-47163|Problema con l'inserimento della colonna e dell'aggiornamento del riferimento|Insetto|
|CELLSNET-47244|Formule (MROUND, MIN) non calcolate correttamente|Insetto|
|CELLSNET-47250|Rimuovi duplicati funziona per la prima colonna solo quando si specifica il parametro columnOffsets|Insetto|
|CELLSNET-47267|Le formule non vengono calcolate nel file modello|Insetto|
|CELLSNET-47268|TrimLeadingBlankRowAndColumn incoerenza|Insetto|
|CELLSNET-47269|Conversione da XLSX a CSV - virgola mancante nell'output|Insetto|
|CELLSNET-47200|Problema di sovrapposizione sui pulsanti di navigazione quando si imposta il foglio nascosto come foglio attivo|Insetto|
|CELLSNET-47274|Immagine di sfondo non impostata in GridWeb|Insetto|
|CELLSNET-47179|Firma VBA con Bouncy Castle lib|Insetto|
|CELLSNET-47258|Problema con le immagini dei codici a barre nel rendering da Foglio a TIFF|Insetto|
|CELLSNET-47216|PowerQueries andato dopo la sostituzione della fonte|Insetto|
|CELLSNET-47241|ODS il file si interrompe durante l'impostazione dello stile del carattere e il salvataggio|Insetto|
|CELLSNET-47252|Numeric Smart Marker che inserisce il valore della cella come testo|Insetto|
|CELLSNET-47262|Problema con 100% Stacked Bar e l'unità principale e l'unità minore|Insetto|
|CELLSNET-47271|Il salvataggio di XLSX con Visio incorporato danneggia il file|Insetto|
|CELLSNET-47282|Aspose.Cells 20.3: Problema di conversione da XLSB a XLS|Insetto|
|CELLSNET-47291|Carattere punto elenco errato letto dal file Excel|Insetto|
|CELLSNET-47096|Problema con la barra della formula di GridDesktop con SplitterPane|Insetto|
|CELLSNET-47247|Eccezione sollevata quando viene chiamato Cell.R1C1Formula|Eccezione|
|CELLSNET-47235|NullPointerException quando refreshPivotData|Eccezione|
|CELLSNET-47246|Eccezione "Impossibile accedere a un flusso chiuso" durante il salvataggio di un file Excel in PDF|Eccezione|
|CELLSNET-47086|Viene generata un'eccezione durante il rendering di un grafico|Eccezione|
|CELLSNET-47242|FormatException sul caricamento del file|Eccezione|
|CELLSNET-47266|Eccezione "L'indice dell'argomento è fuori dall'intervallo dell'array" durante il caricamento di tutti i file allegati|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge la proprietà ChartTextFrame.DirectionType.**
Ottiene e imposta la direzione del testo nel grafico.
#### **Aggiunge ChartTextFrame.ReadingOrder e rende obsoleta la proprietà ChartTextFrame.TextDirection.**
Usare invece la proprietà ChartTextFrame.ReadingOrder.
#### **Aggiunge classi per la funzionalità avanzata di Revisioni.**
Ottiene le informazioni sulla revisione.
#### **Modifica il valore predefinito della proprietà TxtSaveOptions.TrimLeadingBlankRowAndColumn.**
Per rendere il comportamento predefinito del salvataggio di CSV lo stesso con ms excel, abbiamo modificato il valore predefinito e il comportamento di questa proprietà. Per le vecchie versioni, il suo valore predefinito era "**falso**". Da 20.4, il suo valore predefinito diventa "**VERO**".
#### **Modifica il comportamento per il rilevamento di righe/colonne vuote per il salvataggio di CSV.**
Per le vecchie versioni, abbiamo preso quelle righe/colonne che non hanno dati ma hanno impostazioni personalizzate (visibilità, formattazione, ... ecc.) come vuote. Dalla 20.4 non li prendiamo più come vuoti, il nuovo comportamento è lo stesso con ms excel.
#### **Aggiunge la proprietà TxtSaveOptions.ExportArea.**
Specifica l'intervallo di dati delle celle da esportare. Gli utenti possono utilizzare questa opzione per ottenere lo stesso risultato con le versioni precedenti per il comportamento modificato di TxtSaveOptions.TrimLeadingBlankRowAndColumn e righe/colonne vuote.
#### **Aggiunge la classe UnionRange.**
Rappresenta l'intervallo di unione.
#### **Elimina la proprietà DrawObject.Image obsoleta.**
Usare invece la proprietà DrawObject.ImageBytes.
#### **Aggiunge la proprietà Bullet.FontName**
Ottiene e imposta il nome del carattere del punto elenco.
#### **Aggiunge il metodo WorksheetCollection.CreateUnionRange().**
Crea un intervallo di unione.
#### **Elimina l'enumerazione SaveType obsoleta.**
È inutilizzato.
#### **Elimina le proprietà OleObject.ImageFormat e Picture.ImageFormat obsolete.**
Usare invece le proprietà OleObject.ImageType e Picture.ImageType.
