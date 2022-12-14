---
title: Aspose.Cells for Java 19.2 Note di rilascio
type: docs
weight: 110
url: /it/java/aspose-cells-for-java-19-2-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 19.2.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42827|Inserisci riga con InsertOptions simile a MS Excel|Nuova caratteristica|
|CELLSJAVA-42712|Migliora JavaDocs per Aspose.Cells for Java|Aumento|
|CELLSJAVA-42823|L'utilizzo di FontUnderlineType.WORDS genera un'eccezione|Aumento|
|CELLSJAVA-42826|Dati con formattazione condizionale omessi durante la conversione da XLSX a HTML|Insetto|
|CELLSJAVA-42815|L'aggiunta di un riferimento complesso a un nome definito risulta in una cartella di lavoro MS Excel corrotta|Insetto|
|CELLSJAVA-42822|Cell.getValidationValue restituisce un valore errato per il valore specificato|Insetto|
|CELLSJAVA-42829|Nome della funzione personalizzata all'interno delle formule condivise sostituito da un altro nome|Insetto|
|CELLSJAVA-42824|Titoli degli assi mancanti e altra formattazione è errata dei grafici nella conversione da Excel a PDF/A|Insetto|
|CELLSJAVA-42814|Le frecce nell'output PNG non corrispondono alle frecce nel grafico di Excel|Insetto|
|CELLSJAVA-42777|Modifica dell'altezza delle righe errata durante l'utilizzo dell'operazione di adattamento automatico delle righe|Insetto|
|CELLSJAVA-42813|L'impostazione della cartella di lavoro "ReCalculateOnOpen" non è stata mantenuta|Insetto|
|CELLSJAVA-42816|Visualizzazione incompleta per AutoFitterOptions.setAutoFitMergedCells(true)|Insetto|
|CELLSJAVA-42817|Il colore di sfondo delle caselle di testo viene modificato in modo imprevisto|Insetto|
|CELLSJAVA-42821|Quando si elimina la prima riga di un intervallo, l'intervallo viene aggiornato in modo errato|Insetto|
|CELLSJAVA-42828|Quando si utilizza Cell.setHtmlString viene aggiunta una nuova riga alla fine del testo|Insetto|
|CELLSJAVA-42820|Eccezione "Valore stringa IMEModeType non valido" durante il caricamento di un formato di file XLSX|Eccezione|
Pubblico API e modifiche incompatibili con le versioni precedenti

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge la proprietà Cells.CountLarge**
Dal punto di vista funzionale è uguale alla proprietà Count, ad eccezione del fatto che la proprietà Count può generare un errore di overflow quando sono presenti troppe istanze di oggetti Cell.
#### **Aggiunge il metodo Hyperlink.Delete()**
Elimina questo collegamento ipertestuale.
#### **Aggiunge la proprietà Range.Hyperlinks**
Ottiene tutti i collegamenti ipertestuali nell'intervallo.
#### **Aggiunge enum CopyFormatType**
Rappresenta il tipo di formato di copia durante l'inserimento delle righe.
#### **Aggiunge la classe InsertOptions e il metodo Cells.InsertRows(int, int , InsertOptions)**
Inserimento di righe con alcune opzioni.
#### **Aggiunge i metodi FileFormatUtil.DetectFileFormat(Stream,String) e FileFormatUtil.DetectFileFormat(String,String)**
Rileva il formato file del file OOXML crittografato.
#### **Aggiunge le proprietà ListObject.AlternativeDescription e ListObject.AlternativeText**
Ottiene e imposta il testo alternativo e la descrizione della tabella.
#### **Aggiunge la proprietà Line.ThemeColor**
Ottiene e imposta il colore del tema della linea.
#### **Aggiunge la classe Mode3d e MsoModel3dFormat**
Incapsula l'oggetto che rappresenta un singolo modello 3D in un foglio di calcolo.
#### **Aggiunge l'enumerazione ImageType.Gltf**
Rappresenta il tipo di modello 3D.
