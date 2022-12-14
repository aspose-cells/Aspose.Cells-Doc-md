---
title: Aspose.Cells for .NET 18.4 Note di rilascio
type: docs
weight: 90
url: /it/net/aspose-cells-for-net-18-4-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 18.4](https://www.nuget.org/packages/Aspose.Cells/18.4.0).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-46045|Imposta la dimensione della pagina Pdf durante l'utilizzo del metodo Chart.ToPdf|Nuova caratteristica|
|CELLSNET-45590|Supporto per il rendering del grafico MS Excel 2016 dell'istogramma|Nuova caratteristica|
|CELLSNET-46007|Aggiungi una proprietà equivalente alla proprietà "FilterMode" dell'oggetto MS Excel Worksheet (VBA)|Nuova caratteristica|
|CELLSNET-46026|Supporta ulteriori modifiche alle celle in cellModifiedOnAjax - Aspose.Cells.GridWeb|Nuova caratteristica|
|CELLSNET-46013|Nuovo tipo incrociato che nasconde il contenuto sovrapposto durante il salvataggio come HTML|Aumento|
|CELLSNET-45965|Capacità di elaborare l'elemento LINK standard durante la conversione all'indietro|Aumento|
|CELLSNET-46032|Non generare PDF vuoto a pagina singola quando il file Excel è vuoto|Aumento|
|CELLSNET-46027|Rendering da Excel a PDF - Problema di intestazione/piè di pagina|Aumento|
|CELLSNET-45970|Quando si adatta automaticamente una colonna, Aspose.Cells non considera l'altezza della riga quando la cella è a capo automatico|Aumento|
|CELLSNET-44985|Problema con l'operazione di adattamento automatico delle colonne con testo a capo attivo|Aumento|
|CELLSNET-42701|Problema di testo a capo di AutoFitColumns|Aumento|
|CELLSNET-46005|Scritte invertite per fogli diversi nel formato file PDF di output|Insetto|
|CELLSNET-45958|Formattazione errata durante il salvataggio di XLSX come HTML|Insetto|
|CELLSNET-45907|Valori mancanti nel rendering del grafico|Insetto|
|CELLSNET-46034|Impossibile rimuovere le tabelle pivot (la cui origine dati è esterna) dal formato di file XLS|Insetto|
|CELLSNET-46016|Il file Excel viene danneggiato dopo l'aggiornamento della tabella pivot|Insetto|
|CELLSNET-45988|L'aggiornamento della tabella pivot in "Sample2.xlsx" genera un file Excel corrotto|Insetto|
|CELLSNET-46011|Workbook.Calculation fornisce un valore errato per la cella F155|Insetto|
|CELLSNET-46001|Valutazione errata dei valori DateTime durante il calcolo delle funzioni DateTime|Insetto|
|CELLSNET-46000|Riduci per adattare alle celle, il testo diventa leggermente più piccolo del normale nell'immagine renderizzata|Insetto|
|CELLSNET-45998|I margini sono ancora presenti quando tutti i margini sono impostati su zero e OnePagePerSheet è impostato su true.|Insetto|
|CELLSNET-45990|L'output PDF varia in base al tipo di ottimizzazione|Insetto|
|CELLSNET-46053|"La stringa di input non era in un formato corretto" durante il calcolo del grafico nel file modello|Insetto|
|CELLSNET-46029|Problemi con il filtro dei dati personalizzati|Insetto|
|CELLSNET-46024|Durante il salvataggio di OriginalDataSource con barra modificata in barra rovesciata|Insetto|
|CELLSNET-46018|Immagini e diagrammi mancano durante il salvataggio del file OTS|Insetto|
|CELLSNET-46003|ListFillRange in ActiveX ComboBox non si aggiorna|Insetto|
|CELLSNET-46002|Le righe di intestazione della pagina vengono visualizzate solo sulla prima pagina del PDF di output|Insetto|
|CELLSNET-45996|Bug in A30 - Le nuove righe vengono rimosse|Insetto|
|CELLSNET-45995|Bug in C32 - Lo spazio bianco viene rimosso|Insetto|
|CELLSNET-45968|Workbook.CalculateFormula è cambiato in "#REF!" per nominare?"|Insetto|
|CELLSNET-46031|La colonna non è presente nell'output di GridWeb dopo l'associazione di una classe personalizzata|Insetto|
|CELLSNET-46025|La convalida dei dati non è sempre riuscita in Aspose.Cells.GridWeb|Insetto|
|CELLSNET-46020|Il valore Cell non è corretto durante l'importazione di un file Excel in Aspose.Cells.GridWeb|Insetto|
|CELLSNET-46019|La posizione delle forme non è corretta in Aspose.Cells.GridWeb|Insetto|
|CELLSNET-46017|Dopo aver inserito una riga o una colonna, il foglio di lavoro diventa vuoto con una riga/colonna nel conteggio|Insetto|
|CELLSNET-46009|I valori e i controlli vengono persi quando le celle vengono modificate, ad esempio I13, I14, I15 ecc.|Insetto|
|CELLSNET-45994|Visualizza il messaggio di input di convalida in GridWeb|Insetto|
|CELLSNET-45991|Scorrendo fino alla riga in basso e facendo clic sul pulsante del gruppo non si comprimono le righe|Insetto|
|CELLSNET-45919|I controlli (pulsanti delle opzioni e barre di scorrimento) non vengono visualizzati durante l'importazione di un file Excel|Insetto|
|CELLSNET-45975|Cells nell'intervallo L10:L12 non può essere unito|Eccezione|
|CELLSNET-46008|Stringa non valida nel file: si verifica un'eccezione all'apertura del file XLS|Eccezione|
|CELLSNET-46004|Eccezione "La stringa di input non era in un formato corretto" all'apertura di un file XLSX|Eccezione|
|CELLSNET-45992|Aspose.Cells 18.2: l'apertura di un particolare file XLS causa ArgumentOutOfRangeException|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge il nuovo elemento "CrossHideRight" per l'enumerazione HtmlCrossType**
Visualizza la stringa incrociata HTML e nasconde la stringa destra quando il testo è sovrapposto.
#### **Aggiunge il nuovo elemento "TSV" per le enumerazioni LoadFormat, SaveFormat e FileFormatType**
Rappresenta un file TSV (valori separati da tabulazioni), lo stesso con "TabDelimited".
#### **Aggiunge enum ImageType**
Rappresenta il tipo di immagine.
#### **Aggiunge le proprietà MsoTextFrame.RotateTextWithShape e ShapeTextAlignment.RotateTextWithShape**
Indica se il testo ruota con la forma.
#### **Aggiunge le proprietà OleObject.ImageType e Picture.ImageType**
Ottiene il formato immagine dell'immagine.
#### **Obsolete le proprietà OleObject.ImageFormat e Picture.ImageFormat**
Usare invece le proprietà OleObject.ImageType e Picture.ImageType.
#### **Aggiunge un metodo AutoFilter.Refresh (System.Boolean) di overload**
Ottiene tutti gli indici delle righe nascoste e aggiorna il filtro automatico.
#### **Aggiunge il metodo di sovraccarico Cell.GetHtmlString(System.Boolean)**
Ottiene la stringa HTML che contiene dati e alcuni formati in questa cella.
#### **Aggiunge la proprietà BuiltInDocumentPropertyCollection.Language**
Ottiene e imposta la lingua del file.
#### **Aggiunge Style.SetPatternColor(Aspose.Cells.BackgroundType,System.Drawing.Color,System.Drawing.Color)**
Imposta il motivo e il colore della cella
#### **Aggiunge la proprietà ChartPoint.XValueType**
Ottiene il tipo di valore X del punto del grafico.
#### **Aggiunge la proprietà ChartPoint.YValueType**
Ottiene il tipo di valore Y del punto del grafico.
#### **Aggiunge enum PageLayoutAlignmentType**
Rappresenta i tipi di allineamento del layout di pagina.
#### **Aggiunge il metodo Chart.ToPdf(System.IO.Stream,System.Single,System.Single,Aspose.Cells.PageLayoutAlignmentType,Aspose.Cells.PageLayoutAlignmentType)**
Crea il PDF del grafico con le dimensioni di pagina desiderate e lo salva in un flusso.
#### **Aggiunge il metodo Chart.ToPdf(System.String,System.Single,System.Single,Aspose.Cells.PageLayoutAlignmentType,Aspose.Cells.PageLayoutAlignmentType)**
Crea il PDF del grafico con le dimensioni di pagina desiderate e lo salva in un file.
#### **Aggiunge la proprietà PdfSaveOptions.OutputBlankPageWhenNothingToPrint**
Indica se emettere una pagina vuota quando non c'è niente da stampare.
