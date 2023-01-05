---
title: Aspose.Cells for .NET 20.3 Note di rilascio
type: docs
weight: 50
url: /it/net/aspose-cells-for-net-20-3-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 20.3](https://www.nuget.org/packages/Aspose.Cells/20.3.0).

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-47130|Supporto per FLOOR.MATH(-555,5,1)|Nuova caratteristica|
|CELLSNET-47168|Supporto per la funzione FILTRO|Nuova caratteristica|
|CELLSNET-47204|Ottieni l'ID univoco del foglio di lavoro|Nuova caratteristica|
|CELLSNET-47229|Supporto per l'impostazione di chart.series.dataLables.TextDirection su verticale|Nuova caratteristica|
|CELLSNET-47092|Rendi disponibili le icone per IStreamProvider come le normali immagini durante il salvataggio del documento in HTML|Aumento|
|CELLSNET-47094|Riduci lo sfarfallio in GridDesktop per un ridimensionamento fluido|Aumento|
|CELLSNET-47173|Distingue i fogli nascosti/molto nascosti in Aspose.Cells.GridDesktop|Aumento|
|CELLSNET-47101|Migliora le prestazioni di salvataggio della formattazione condizionale e della convalida con intere righe.|Aumento|
|CELLSNET-47178|Rientro perso durante la creazione di una tabella e la conversione in HTML|Insetto|
|CELLSNET-47199|La differenza nel calcolo per l'intervallo denominato durante l'impostazione di CreateCalcChain su true e false|Insetto|
|CELLSNET-47077|Impossibile applicare bordi alle celle (con dati) durante l'importazione di un file Excel in GridDesktop|Insetto|
|CELLSNET-47172|Problema nell'applicazione della formattazione condizionale|Insetto|
|CELLSNET-47177|Il nome e la linea della serie del grafico ParetoLine non vengono visualizzati nell'immagine|Insetto|
|CELLSNET-47191|Il grafico alla differenza di immagine|Insetto|
|CELLSNET-47202|Le voci della legenda sono sovrapposte nell'immagine di output del grafico|Insetto|
|CELLSNET-47167|Numero errato di link visibili|Insetto|
|CELLSNET-47184|BIFF5 con contenuto cirillico viene convertito erroneamente in XLSX|Insetto|
|CELLSNET-47205|Range.ApplyStyle() sull'intervallo di colonne ha aumentato notevolmente le dimensioni del file della cartella di lavoro|Insetto|
|CELLSNET-47210|Il valore di stringa in formato ricco di una cella è vuoto in Apple Numbers'09|Insetto|
|CELLSNET-47213|Copia del foglio in un'altra cartella di lavoro: le celle nascoste (righe) scompaiono|Insetto|
|CELLSNETCORE-53|Il punto dati sulla riga del grafico di Excel viene rimosso dopo la conversione in PDF|Insetto|
|CELLSNET-47212|NullReferenceException durante il salvataggio di particolari da XLSM a XLS|Eccezione|
|CELLSNET-47222|Aspose.Cells 20.2: Eccezione durante la conversione di un particolare file XLSB in Excel97To2003|Eccezione|
|CELLSNET-47226|Aspose.Cells 20.2: Eccezione durante il tentativo di eliminare colonne vuote|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Modifica il comportamento delle funzioni di formattazione per alcuni CultureInfo specificati dall'utente.(SOLO .NET)**
Nelle vecchie versioni, il nostro motore di formattazione potrebbe modificare alcune proprietà di alcune culture speciali per ottenere il risultato di formattazione generale. Ad esempio, per la maggior parte delle situazioni, JapaneseCalendar dovrebbe essere utilizzato per formattare i valori data-ora, quindi nelle vecchie versioni facciamo sempre in modo che CultureInfo di "ja-JP" utilizzi JapaneseCalendar per la formattazione. Tuttavia, non è sempre destinato agli utenti quando specificano il loro CultureInfo personalizzato tramite API, ad esempio WorkbookSettings.CultureInfo o CustomImplementationFactory.CreateCultureInfo(). Quindi, dalla versione 20.3, utilizziamo la proprietà CultureInfo.UseUserOverride per decidere se modificare automaticamente le proprietà per la formattazione. Per l'oggetto CultureInfo specificato, se questa proprietà è**VERO** , quindi lo consideriamo come se l'utente abbia sovrascritto tutte le proprietà necessarie, quindi non lo cambieremo più per la formattazione. Se questa proprietà è**falso**, allora possiamo modificare automaticamente altre sue proprietà se necessario.
#### **Aggiungere la proprietà LoadFilter.SheetsInLoadingOrder.**
Gli utenti possono sovrascrivere questa proprietà per specificare i fogli e l'ordine da caricare durante l'importazione delle cartelle di lavoro dal file modello.
#### **Elimina la proprietà TickLabels.Background obsoleta**
Utilizzare invece la proprietà TickLabels.BackgroundMode.
#### **Rende obsoleta la proprietà TickLabels.TextDirection e aggiunge la proprietà TickLabels.ReadingOrder**
Utilizzare invece la proprietà TickLabels.ReadingOrder.
#### **Obsoleta TickLabels.DirectionTypeproperty e aggiunge enum ChartTextDirectionType**
Rappresenta la direzione del testo.
#### **Aggiunge il metodo Shape.RemoveActiveXControl().**
Rimuove i dati ActiveX dalla forma.
#### **Aggiunge la proprietà ThreadedComment.CreatedTime.**
Ottiene e imposta l'ora di creazione dei commenti in thread.
#### **Aggiunge la proprietà Worksheet.UniqueId.**
Ottiene e imposta l'ID univoco del foglio di lavoro.
#### **Aggiunge enum IconSetType.ColorSmilies3 e IconSetType.Smilies3.**
Rappresenta le formattazioni condizionali del set di icone 3smiles. Solo per file .ods
#### **Aggiunge enum TimePeriodType.LastYear,TimePeriodType.NextYear e ThisYear.**
Rappresenta le formattazioni condizionali dell'anno scorso, dell'anno prossimo e di quest'anno. Solo per file .ods.
#### **Aggiunge il metodo WorksheetCollection.RefreshPivotTables().**
Aggiornamento di tutte le tabelle pivot nel file.
