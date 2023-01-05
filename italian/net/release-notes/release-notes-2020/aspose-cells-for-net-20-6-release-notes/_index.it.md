---
title: Aspose.Cells for .NET 20.6 Note di rilascio
type: docs
weight: 20
url: /it/net/aspose-cells-for-net-20-6-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 20.6](https://www.nuget.org/packages/Aspose.Cells/20.6.0).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-47353|Supporto per l'archiviazione di file temporanei per le informazioni sulla sessione in GridWeb|Aumento|
|CELLSNET-47388|GridWeb SessionMode.File memorizzerà il file di cache per diverse pagine/schede|Aumento|
|CELLSNET-46062|La legenda del grafico non è resa correttamente a causa dei caratteri asiatici e latini|Aumento|
|CELLSNET-47373|Il salvataggio della cartella di lavoro in PDF MemoryStream dura più di 2 minuti|Aumento|
|CELLSNET-43418|Copia e incolla (solo dati) un intervallo non contiguo|Aumento|
|CELLSNET-47315|Non è stato possibile aprire il file quando è stato salvato in zip64|Aumento|
|CELLSNET-47384|Migliora le prestazioni di caricamento di immagini/forme|Prestazione|
|CELLSNET-47382|La conversione da HTML a Excel perde la formattazione|Insetto|
|CELLSNET-47390|Il colore di alcune parole è errato nel rendering da HTML a ODS|Insetto|
|CELLSNET-47385|Cells.InsertCutCells interrompe le cartelle di lavoro con un'intersezione di intervalli|Insetto|
|CELLSNET-47389|Calcolo CERCA.ORIZZ non corretto|Insetto|
|CELLSNET-47352|Dopo aver fatto clic sul testo, il testo scompare|Insetto|
|CELLSNET-47380|La colonna non è allineata|Insetto|
|CELLSNET-47366|Punti non resi nel file PDF|Insetto|
|CELLSNET-47364|Il rendering delle etichette degli assi non è corretto se il foglio di lavoro viene visualizzato come immagine|Insetto|
|CELLSNET-47370|Punto del grafico mancante e forma schiacciata durante il caricamento e il salvataggio del file Excel|Insetto|
|CELLSNET-47367|Direzione della freccia dell'asse errata durante la conversione del grafico in un'immagine|Insetto|
|CELLSNET-47362|SourceFullName e ImageType non sono corretti|Insetto|
|CELLSNET-47375|XLSX convertito nel file XLS danneggiato.|Insetto|
|CELLSNET-47398|Worksheet.Cells.ImportData salta le righe durante la suddivisione dei dati in più fogli|Insetto|
|CELLSNET-47371|Eccezione sull'aggiornamento delle tabelle pivot nel foglio|Eccezione|
|CELLSNET-47377|Worksheet.RefreshPivotTables() solleva un'eccezione|Eccezione|
|CELLSNET-47393|Aspose.Cells.CellsException: riferimenti circolari|Eccezione|
|CELLSNET-47365|Eccezione durante il caricamento di un file XLSX|Eccezione|
|CELLSNET-47381|La proprietà Picture.Data genera un'eccezione ArgumentOutOfRange|Eccezione|
|CELLSNET-47374|Interruzione della modifica in RemoveACell durante l'aggiornamento da 19.10 a 20.5|Regressione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge il metodo ReferredArea.GetValues(boolcalculateFormulas)/GetValue(introwOffset, int colOffset, boolcalculateFormulas).**
Offre all'utente la possibilità di controllare se le formule devono essere calcolate in modo ricorsivo nell'implementazione di AbstractCalculationEngine.
#### **Aggiunge l'enumerazione WarningType.InvalidFontName e WarningType.InvalidTextOfDefinedName.**
Rappresenta il tipo di avviso.
#### **Aggiunge le proprietà WarningInfo.CorrectedObject e WarningInfo.ErrorObject.**
Rappresenta i dati errati e i dati aggiornati quando viene generato un avviso.
#### **Aggiunge le proprietà WorkbookDesigner.RepeatFormulasWithSubtotal.**
Indica se si ripetono formule con righe di totale parziale.
#### **Aggiunge la proprietà PlotArea.IsAutomaticSize.**
Indica se la dimensione dell'area del tracciato è automatica.
#### **Elimina la proprietà Style.Rotation obsoleta.**
Utilizzare invece la proprietà Style.RotationAngle.
#### **Aggiunge il metodo Gridweb.SetFontFolder(string fontFolder, bool recursive)/SetFontFolders(string[] fontFolders, bool recursive).**
Imposta la cartella/le cartelle dei font
