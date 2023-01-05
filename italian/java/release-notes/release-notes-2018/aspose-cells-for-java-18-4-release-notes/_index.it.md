---
title: Aspose.Cells for Java 18.4 Note di rilascio
type: docs
weight: 90
url: /it/java/aspose-cells-for-java-18-4-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 18.4.

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42523|Usa la versione conforme a FIPS di Bouncy Castle nelle API Aspose.Cells|Nuova caratteristica|
|CELLSJAVA-42572|La formula non deve contenere più di 8192 caratteri|Aumento|
|CELLSJAVA-42569|Impossibile accedere agli elementi delle etichette dell'asse delle categorie orizzontali del grafico in XLS|Aumento|
|CELLSJAVA-42580|Ottieni/imposta la proprietà del documento Lingua|Aumento|
|CELLSJAVA-42565|Colore di primo piano vs Colore di sfondo vs Colore di riempimento: utilizzare un unico metodo che accetta due argomenti|Aumento|
|CELLSJAVA-42528|"<Font>" non è un HTML5 valido e un tag di chiusura automatica e i browser web ne travisano il contenuto|Aumento|
|CELLSJAVA-42413|Inserisci il tipo di immagine SVG nelle celle del foglio di lavoro entro Aspose.Cells|Aumento|
|CELLSJAVA-42551|Alcune forme non sono corrette nell'output PDF|Insetto|
|CELLSJAVA-42578|La formattazione condizionale viene persa durante il salvataggio di Excel in HTML|Insetto|
|CELLSJAVA-42571|L'output HTML non corrisponde a MS-Excel|Insetto|
|CELLSJAVA-42553|I collegamenti all'area denominata sono errati dopo l'esportazione in HTML|Insetto|
|CELLSJAVA-42530|Le tabelle pivot e i grafici corrispondenti non hanno il formato data corretto|Insetto|
|CELLSJAVA-42527|Il grafico ha molti valori nell'asse x e i valori si sovrappongono l'uno sull'altro|Insetto|
|CELLSJAVA-42581|Aspose.Cells restituisce un valore errato della cella A2|Insetto|
|CELLSJAVA-42583|La mappa XML non crea correttamente la tabella|Insetto|
|CELLSJAVA-42577|Ottieni/estrai i valori (0 per 0 e vuoto per vuoto) utilizzando il metodo DataPoint.getYValue() per un determinato grafico|Insetto|
|CELLSJAVA-42566|Inversione dei sottotitoli (voci della legenda) nel grafico MS Excel|Insetto|
|CELLSJAVA-42560|Le frecce mancano nell'output PNG del grafico di Excel|Insetto|
|CELLSJAVA-42508|Java metodo 'Shape.toImage' funziona diversamente con lo stesso metodo in .NET|Insetto|
|CELLSJAVA-42573|Aspose.Cells 18.3 rotazione per un TextBox non funziona per EXCEL_97_Formato di salvataggio TO_2003|Insetto|
|CELLSJAVA-42570|Una nuova riga vuota viene visualizzata all'interno del TextBox dopo l'elaborazione e il salvataggio del file Excel|Insetto|
|CELLSJAVA-42563|Eccezione "java.lang.NullPointerException" durante la firma digitale di un file XLSX|Eccezione|
# **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
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
Crea il grafico PDF con le dimensioni di pagina desiderate e lo salva in un flusso.
#### **Aggiunge il metodo Chart.ToPdf(System.String,System.Single,System.Single,Aspose.Cells.PageLayoutAlignmentType,Aspose.Cells.PageLayoutAlignmentType)**
Crea il grafico PDF con le dimensioni pagina desiderate e lo salva in un file.
#### **Aggiunge la proprietà PdfSaveOptions.OutputBlankPageWhenNothingToPrint**
Indica se emettere una pagina vuota quando non c'è niente da stampare.
