---
title: Aspose.Cells for .NET 18.3 Note di rilascio
type: docs
weight: 100
url: /it/net/aspose-cells-for-net-18-3-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 18.3](https://www.nuget.org/packages/Aspose.Cells/18.3.0).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-42655|Raggruppa i campi pivot nella tabella pivot|Nuova caratteristica|
|CELLSNET-45960|Cambia il punto da NumPad al separatore decimale (',') - Aspose.Cells.GridWeb|Nuova caratteristica|
|CELLSNET-45966|Causa dell'eccezione durante la conversione all'indietro da HTML a Cells|Aumento|
|CELLSNET-45976|Errore durante l'apertura del file ODS a causa di possibili framework diversi che mantengono una precisione diversa per i valori float|Aumento|
|CELLSNET-45981|Aggiungi la proprietà a StyleFlag da impostare su false per non sovrascrivere il valore QuotePrefix|Aumento|
|CELLSNET-45957|Supporta il mantenimento del grafico della mappa nel file modello|Aumento|
|CELLSNET-45941|Il controllo ActiveX diventa un'immagine quando si copia un foglio da una cartella di lavoro a un'altra cartella di lavoro|Aumento|
|CELLSNET-45928|Convalida dei dati: GridWeb dovrebbe visualizzare una finestra di dialogo con un messaggio di errore|Aumento|
|CELLSNET-45935|Workbook.CalculateFormula si blocca all'infinito quando si imposta un valore specifico sulla cella|Prestazione|
|CELLSNET-45920|La sottolineatura del testo "KEY DRIVERS:" è interrotta nell'immagine di output|Insetto|
|CELLSNET-45939|Oltre alla sottolineatura interrotta, anche il testo è disallineato, come mostrato nello screenshot fornito|Insetto|
|CELLSNET-45890|Alcune forme non vengono renderizzate completamente in quanto mancano alcune parti|Insetto|
|CELLSNET-45878|Il file Excel di output della nuova versione blocca Excel 2016 Microsoft|Insetto|
|CELLSNET-43360|Problema di stile con il rendering da HTML a Excel|Insetto|
|CELLSNET-45979|Il calcolo della formula CERCA.VERT non funziona correttamente|Insetto|
|CELLSNET-45949|Cell l'allineamento del testo (con caratteri misti) viene modificato nell'immagine convertita|Insetto|
|CELLSNET-45940|Formattazione condizionale non applicata durante la conversione di file Excel in formato file PDF|Insetto|
|CELLSNET-45896|I bordi indesiderati appaiono intorno all'immagine quando il file Excel viene salvato in PDF|Insetto|
|CELLSNET-45942|Il riferimento di cella per l'etichetta dati viene perso dopo l'apertura/salvataggio|Insetto|
|CELLSNET-45923|L'ultima etichetta dell'asse, ad esempio il 17 giugno, non è presente nell'immagine del grafico|Insetto|
|CELLSNET-45911|Posizione e linea errate nel rendering del grafico del rischio di mercato|Insetto|
|CELLSNET-45908|Posizione errata nel rendering del grafico|Insetto|
|CELLSNET-45906|Etichetta mancante nel rendering del grafico|Insetto|
|CELLSNET-45884|Grafico Smart Art su linguetta: i bordi dei coni sono frastagliati nel formato di file PDF di output|Insetto|
|CELLSNET-45989|Le finestre di dialogo non vengono salvate correttamente nei file XLSM|Insetto|
|CELLSNET-45977|Worksheet.Protect(ProtectionType.Objects) non funziona per i file XLS|Insetto|
|CELLSNET-45946|Il collegamento ipertestuale con trattino nello schema si interrompe durante il salvataggio|Insetto|
|CELLSNET-45944|Il metodo ConvertToRange() interrompe i nomi in Name Manager|Insetto|
|CELLSNET-45905|Excel si blocca quando si tenta di aprire due volte la cartella di lavoro di output, ad esempio "_function plot 2D.xlsx".|Insetto|
|CELLSNET-45904|Excel si blocca quando si tenta di aprire due volte la cartella di lavoro di output|Insetto|
|CELLSNET-45959|Aspose.Cells.GridWeb cultura problema data|Insetto|
|CELLSNET-45929|Il gruppo di colonne non funziona in GridWeb|Insetto|
|CELLSNET-45926|Le schede non sono visibili o parzialmente visibili su GridWeb in IE 11|Insetto|
|CELLSNET-45925|Problema di offset nel foglio di lavoro GridWeb su IE 11|Insetto|
|CELLSNET-45918|"<br>" è incorporato nella cella al cambio di cella in Aspose.Cells.GridWeb|Insetto|
|CELLSNET-45914|La formula scompare dopo aver convalidato/aggiornato il valore nella cella|Insetto|
|CELLSNET-45912|Errore dopo la convalida di una cella secondo il metodo di convalida|Insetto|
|CELLSNET-45894|I controlli non funzionano correttamente probabilmente a causa del caricamento di due GridWeb|Insetto|
|CELLSNET-45987|Eccezione all'apertura di un file XLSX tramite API Aspose.Cells|Eccezione|
|CELLSNET-45951|La formula non valida genera un'eccezione all'avvio|Eccezione|
|CELLSNET-45950|Eccezione durante il caricamento di un file ODS|Eccezione|
|CELLSNET-45947|Eccezione: formula non valida:"=sheet3!#ref!" quando si apre un file XLSX|Eccezione|
|CELLSNET-45938|System.IndexOutOfRangeException all'apertura di file XLSB|Eccezione|
|CELLSNET-45937|System.FormatException si verifica durante l'apertura del file XLSX|Eccezione|
|CELLSNET-45903|Il caricamento di XLSX causa StackOverflowException|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
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
