---
title: Aspose.Cells for Java 18.3 Note di rilascio
type: docs
weight: 100
url: /it/java/aspose-cells-for-java-18-3-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 18.3.

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42519|Aggiungere PdfSaveOptions.DrawObjectEventHandler simile a ImageOrPrintOptions.DrawObjectEventHandler|Nuova caratteristica|
|CELLSJAVA-42543|Estrai il nome dell'etichetta che può essere impostato per gli oggetti Package incorporati nel file MS Excel|Nuova caratteristica|
|CELLSJAVA-42535|L'utilizzo di stream per importare file Excel tramite GridWebBean.importExcelFile() non è valido o non esiste|Aumento|
|CELLSJAVA-42529|Come identificare le forme del foglio di lavoro tramite DrawObjectEventHandler|Aumento|
|CELLSJAVA-42558|Impossibile accedere agli elementi dell'etichetta dell'asse delle categorie orizzontale|Aumento|
|CELLSJAVA-42552|L'output HTML non corrisponde a MS Excel|Insetto|
|CELLSJAVA-42536|File Excel corrotti dopo l'apertura/salvataggio da parte delle API Aspose.Cells|Insetto|
|CELLSJAVA-42513|Colonne extra arrivano alla fine di ogni riga nell'output HTML per un intervallo|Insetto|
|CELLSJAVA-42542|Il file Excel è danneggiato e alcune celle sono state modificate dopo il salvataggio|Insetto|
|CELLSJAVA-42524|Sono presenti errori di calcolo nel foglio nascosto ovvero "KD020"|Insetto|
|CELLSJAVA-42514|ImportTableOptions.setInsertRows() non funziona durante l'importazione di ResultSet nel foglio di lavoro|Insetto|
|CELLSJAVA-42505|I commenti allegati alle celle (nel file modello) non vengono visualizzati quando si importa il file Excel in GridWeb|Insetto|
|CELLSJAVA-42520|Coordinate di cella incoerenti segnalate da ImageOrPrintOptions.DrawObjectEventHandler|Insetto|
|CELLSJAVA-42518|I bordi delle righe non sono allineati nell'output PDF|Insetto|
|CELLSJAVA-42561|La scala dell'asse X non è corretta nell'output PNG del grafico di Excel|Insetto|
|CELLSJAVA-42556|Il rendering del grafico non è corretto nell'output PDF|Insetto|
|CELLSJAVA-42547|Il grafico viene sostituito con una X rossa durante la conversione da XLSX a ODS|Insetto|
|CELLSJAVA-42546|Immagini perse durante la conversione da ODS a XLSX|Insetto|
|CELLSJAVA-42538|Le proprietà non vengono estratte dai file XLS e XLSX|Insetto|
|CELLSJAVA-42534|Il salvataggio da XLS a XLSB rimuove allowEditRanges|Insetto|
|CELLSJAVA-42532|Controlla le risorse esterne utilizzando WorkbookSetting.StreamProvider: funziona for .NET ma non funziona for Java|Insetto|
|CELLSJAVA-42525|Specifica i campi formula durante l'importazione dei dati nel foglio di lavoro: funziona for .NET ma non funziona for Java|Insetto|
|CELLSJAVA-42521|I caratteri cinesi nel nome del file incorporato (titolo) non sono ben visualizzati nel blocco note|Insetto|
|CELLSJAVA-42533|Si è verificata l'eccezione "NullPointerException" durante l'estrazione del testo della forma SmartArt|Eccezione|
|CELLSJAVA-42545|Eccezione "ReadElementString può essere chiamato solo quando il contenuto è semplice o vuoto" durante il caricamento di un file ODS|Eccezione|
|CELLSJAVA-42526|Errore nella cella B4-Formula non valida: si verifica un'eccezione durante l'impostazione della formula|Eccezione|
|CELLSJAVA-42522|ArrayIndexOutOfBoundsException all'apertura del file tramite Aspose.Cells|Eccezione|
|CELLSJAVA-42517|Eccezione "com.aspose.cells.CellsException: formula non valida:" durante il caricamento di un file ODS|Eccezione|
# **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge la proprietà HtmlSaveOptions.ExportSimilarBorderStyle**
Indica se esportare lo stile del bordo simile quando lo stile del bordo non è supportato dai browser. Se desideri importare il file HTML o MHT in Excel, mantieni il valore predefinito. Il valore predefinito è falso.
#### **Aggiunge la proprietà Axis.AxisLabels**
Ottiene le etichette dell'asse dopo aver chiamato il metodo Chart.Calculate().
#### **Aggiunge un nuovo tipo enum: GridValidationType.CustomServerFunction**
Rappresenta la convalida della funzione lato server personalizzata.
#### **Aggiunge l'enumerazione ChartType.Map**
Rappresenta il grafico della mappa.
#### **Aggiunge la proprietà OleObject.Label**
Ottiene e imposta l'etichetta di visualizzazione dell'oggetto Ole collegato.
#### **Aggiunge la proprietà BuiltInDocumentPropertyCollection.DocumentVersion**
Rappresenta la versione del file.
#### **Aggiunge l'enumerazione StyleFlag.QuotePrefix**
Indica se applicare la proprietà QuotePrefix dello stile.
#### **Aggiunge la classe DialogBox**
Rappresenta il foglio della finestra di dialogo.
#### **Aggiunge la proprietà PdfSaveOptions.DrawObjectEventHandler**
Ottiene e imposta DrawObjectEventHandler per ottenere DrawObject e Bound durante il rendering.
#### **Aggiunge la proprietà DrawObject.Shape**
Ottiene la Shape correlata durante il rendering.
