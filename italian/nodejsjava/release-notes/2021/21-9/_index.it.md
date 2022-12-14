---
title: Aspose.Cells per Node.js tramite Java 21.9 Note di rilascio
type: docs
weight: 4
url: /it/nodejs-java/aspose-cells-for-node-js-via-java-21-9-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells per Node.js tramite Java 21.9](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-21.9/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43639|Data e ora di creazione e data di modifica non possono essere estratte|
|CELLSJAVA-43622|Da XLSX a PDF: errore da forma a immagine|
|CELLSJAVA-43756| Distorsione dell'immagine durante Excel in HTML|
|CELLSJAVA-43309|Dettagli modificati sulla conversione da Excel a HTML|
|CELLSJAVA-43578|Problemi di formattazione durante la conversione di Excel in HTML|
|CELLSJAVA-43579|Problema di allineamento del testo durante la conversione da Excel a HTML|
|CELLSJAVA-43630|Il collegamento ipertestuale della funzione di collegamento ipertestuale non è valido quando Excel viene convertito in HTML|
|CELLSJAVA-43635|Durante l'esportazione in HTML, la lunghezza della barra dei dati è inferiore a quella in Excel|
|CELLSJAVA-43709|Il file XLSM risalvato causa il popup di danneggiamento del file all'apertura da ms excel|
|CELLSJAVA-43758|Problema di valutazione della formula di matrice|
|CELLSJAVA-43680|Databar problema di formattazione condizionale nel pdf generato|
|CELLSJAVA-43689|Impostando la formattazione condizionale su cella e utilizzando DataBar.toImage si ottiene un'immagine vuota|
|CELLSJAVA-43723|Il carattere nella cella non viene visualizzato completamente quando il file Excel viene convertito in PDF|
|CELLSJAVA-43724|Impossibile convertire HTML complesso in CSV|
|CELLSJAVA-43728| Orientamento del testo modificato durante la conversione da Excel a PDF|
|CELLSJAVA-43752|Rendering da Excel a HTML: problema con la formattazione condizionale per nascondere i bordi|
|CELLSJAVA-43792|Il carattere non è corretto quando si imposta HtmlLoadOptions per la conversione da HTML a Excel|
|CELLSJAVA-43571| Problema di troncamento di DataLabels durante la conversione di XLSX in PDF|
|CELLSJAVA-43587|Etichette del grafico a ciambella fuori posto|
|CELLSJAVA-43620|I valori dell'asse verticale e le etichette dei punti non vengono visualizzati correttamente durante il rendering del file Excel (contenente il grafico a cascata) in HTML|
|CELLSJAVA-43621|I risultati del valore della funzione RANDBETWEEN(bottom, top) sono diversi dai risultati di Excel|
|CELLSJAVA-41710|Rendering errato dell'HTML dopo la conversione da XLSX|
|CELLSJAVA-43422|Conversione da HTML a Excel - "mso-ignore: padding" nei CSS non ha effetto|
|CELLSJAVA-43606|La formattazione del testo di sfondo è stata modificata durante l'unione dei file|
|CELLSJAVA-43769|Il documento MSO Excel (XLS) non può essere caricato|
|CELLSJAVA-43631|Eccezione "java.lang.NullPointerException" durante il caricamento del file XLSM|
|CELLSJAVA-43655|ArrayIndexOutOfBoundsException con getStringValue|
|CELLSJAVA-43788|Eccezione sollevata durante l'impostazione del valore per le serie di grafici|
|CELLSJAVA-43632| Eccezione "Valore stringa FontUnderlineType non valido" durante il caricamento di un file XLSX|
|CELLSJAVA-43633|Eccezione "Valore stringa MsoLineDashStyle non valido" durante il caricamento di un file XLSX|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge la proprietà AutoFitterOptions.FormatStrategy.**

Ottiene e imposta la strategia formattata per l'adattamento automatico.

### **Aggiunge la proprietà MsoFormatPicture.Transparency.**

Restituisce o imposta il grado di trasparenza dell'area come valore compreso tra 0,0 (opaco) e 1,0 (trasparente).

### **Aggiunge metodi PivotTableCollection.Remove() in overload.**

Elimina la tabella pivot specificata e controlla se conservare i dati delle celle.

### **Aggiunge la proprietà ImageOrPrintOptions.IsOptimized.**

 Indica se ottimizzare gli elementi di output. Il valore predefinito è falso. Attualmente solo le linee di confine vengono ottimizzate quando questa proprietà è impostata su true.

