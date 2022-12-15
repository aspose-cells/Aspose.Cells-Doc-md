---
title: Aspose.Cells for Java 21.4 Note di rilascio
type: docs
weight: 9
url: /it/java/aspose-cells-for-java-21-4-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 21.4](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.4/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43396|La conversione di un foglio Excel in un file di testo rimuove le virgolette dall'inizio|
|CELLSJAVA-43386|L'ordinamento non funziona quando i dati contengono caratteri non alfanumerici|
|CELLSJAVA-43403|Posizionamento del testo spostato a sinistra durante il salvataggio come HTML|
|CELLSJAVA-43421|caratteri di escape e di interruzione di riga non vengono visualizzati correttamente durante la conversione da HTML a Excel|
|CELLSJAVA-43427|Formato condizionale con barre dei dati Mostra i valori nell'esportazione HTML|
|CELLSJAVA-43428| Il formato contabile combinato con il carattere a 6 punti distorce i numeri in HTML|
|CELLSJAVA-43429|Il testo con allineamento verticale del testo scompare in HTML|
|CELLSJAVA-43407|Le formule di Excel vengono saltate/modificate dopo il salvataggio del file|
|CELLSJAVA-43419| Formato numerico personalizzato non visualizzato correttamente nel PDF|
|CELLSJAVA-43374|Etichette del grafico ripetute durante la conversione dei file Excel allegati in PDF|
|CELLSJAVA-43409| Le etichette dei dati imprevisti sono apparse nell'immagine di output del grafico|
|CELLSJAVA-43411|Gli avvisi di sostituzione dei caratteri non funzionano nella conversione da grafico a immagine|
|CELLSJAVA-43414|Problema di conversione da Xls a Pdf|
|CELLSJAVA-43425|Intestazione-Piè di pagina non disponibile nella prima pagina se esportato in Excel|
|CELLSJAVA-43432|Il contenuto del grafico non corrispondeva durante il nuovo salvataggio di un formato di file XLS|
|CELLSJAVA-43433|L'immagine di riferimento non viene visualizzata in PDF|
|CELLSJAVA-43434|La formula dinamica SmartMarker ha uno stile di cella in espansione errato|
|CELLSJAVA-43435| La formula dinamica degli indicatori intelligenti inserisce le celle in base alla colonna espansa a sinistra ma non in base alle colonne nella formula|
|CELLSJAVA-43417|Eccezione sollevata durante l'apertura di XLSX da file di grandi dimensioni|
|CELLSJAVA-43431|java.lang.NullPointerException sollevata durante la chiamata a Cells.deleteColumn() con l'ultima versione 21.3 mentre funziona con 21.2|
|CELLSJAVA-43437|IndexOutOfBoundsException quando si fa clic su altre pagine del foglio in modalità di valutazione|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.

### **Aggiunge i metodi StartAccessCache()/CloseAccessCache() per la cartella di lavoro e il foglio di lavoro.**

Fornire agli utenti la possibilità di accedere ai dati in modalità batch con prestazioni migliori.

### **Aggiunge le proprietà TxtSaveOptions.ExportQuotePrefix e TxtLoadOptions.TreatQuotePrefixAsValue.**

Fornisci agli utenti la possibilità di decidere come fare con le virgolette singole iniziali del valore della cella durante l'esportazione/importazione di file CSV/TSV.

### **Aggiunge i metodi GlobalizationSettings.GetCollationKey(string,bool) e Compare(string,string,bool).**

Fornisci agli utenti la possibilità di sovrascrivere le regole predefinite del confronto tra stringhe. Per alcune impostazioni locali o valori di stringa, la regola predefinita del confronto delle stringhe potrebbe non essere quella prevista (il risultato di alcune funzionalità, come il calcolo della formula, l'ordinamento, ecc., è diverso da quello che dovrebbe essere ottenuto in ms excel). In tal caso, l'utente può sovrascrivere tali metodi con la regola prevista (ad esempio, l'utente può utilizzare l'implementazione della libreria icu).

### **Aggiunge enum ImageType.WebP.**

Rappresenta l'immagine Weppy.

### **Aggiunge il metodo OleObject.SetEmbeddedObject().**

Per verificare se l'icona di aggiornamento automatico.

### **Aggiunge la proprietà WorkbookDesigner.LineByLine.**

Indica se elaborare i marcatori intelligenti riga per riga.

### **Aggiunge la proprietà HtmlSaveOptions.ExportCellCoordinate.**

Indica se esportare coordinate Excel di celle non vuote durante il salvataggio del file in html. Il valore predefinito è false. Se desideri importare l'output html in Excel, mantieni il valore predefinito.

### **Aggiunge la proprietà AutoFitterOptions.DefaultEditLanguage.**

Ottiene o imposta la lingua di modifica predefinita.
