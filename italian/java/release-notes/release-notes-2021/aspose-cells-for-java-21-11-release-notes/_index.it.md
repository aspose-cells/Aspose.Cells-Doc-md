---
title: Aspose.Cells for Java Note sulla versione 21.11
type: docs
weight: 2
url: /it/java/aspose-cells-for-java-21-11-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 21.11](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.11/).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43844| Un miglioramento necessario per il formato dei numeri contabili|
|CELLSJAVA-43953|Renderizza testo/parte specifici "Cell" e "Commento" da tradurre in giapponese in Excel alla conversione PDF|
|CELLSJAVA-43935|Problema relativo alla dimensione del carattere del testo della forma durante il salvataggio e il caricamento del file XLS|
|CELLSJAVA-43952|Problema di scadenza della licenza temporanea|
|CELLSJAVA-43954|Da XLSX a PDF: l'immagine causa un'eccezione "java.lang.OutOfMemoryError: Java spazio heap"|
|CELLSJAVA-43902|Alcuni bordi di Excel convertiti in HTML sono ridondanti|
|CELLSJAVA-43933|Quando si esporta in HTML con un solo dato, il formato condizionale è diverso da Excel|
|CELLSJAVA-43878| Posizione errata delle etichette dei dati del grafico a barre del cluster di Excel|
|CELLSJAVA-43895|La forma della linea e altre forme del grafico non vengono visualizzate correttamente durante la conversione da XLS a XLSX|
|CELLSJAVA-43932|Problema con l'impostazione della posizione delle etichette dei dati per i grafici a ciambella esplosi nell'immagine di output|
|CELLSJAVA-43934|Le etichette del grafico a torta non corrispondono a Excel dopo aver manipolato o aggiornato il grafico|
|CELLSJAVA-43519|Le celle unite incluse in righe o colonne nascoste producono una tabella HTML irregolare|
|CELLSJAVA-43962|L'effetto è incoerente dopo che il formato condizionale in Excel è stato convertito in HTML|
|CELLSJAVA-43969|Un nome con funzione CONTA.SE e riferimento esterno produce un'eccezione NullPointerException|
|CELLSJAVA-43903|java.lang.NumberFormatException: per la stringa di input durante il rendering del file Excel su HTML|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge enum CellValueFormatStrategy.DisplayString.**

Con questa strategia, Cell.GetStringValue(CellValueFormatStrategy) prenderà in considerazione il limite della larghezza della colonna durante la formattazione dei valori della cella con lo stile di visualizzazione. Se il risultato formattato supera la larghezza disponibile, possono essere restituiti uno o più "#", proprio come mostra ms excel per questo tipo di celle.

### **Aggiunge la proprietà WorksheetCollection.ActiveSheetName.**

Ottiene e imposta il nome del foglio attivo della cartella di lavoro.

### **Aggiunge le classi JsonLoadOptions e JsonSaveOptions.**

Rappresenta le opzioni di caricamento o salvataggio dei file.

### **Aggiunge la proprietà ImageSaveOptions.StreamProvider.**

Fornisci gli stream se sono presenti due o più pagine.

### **Aggiunge l'enumerazione LoadFormat.Image e LoadFormat.Json.**

Rappresenta l'immagine e il tipo json.

### **Aggiunge SaveFormat.Bmp, SaveFormat.Emf, SaveFormat.Gif, SaveFormat.Jpg, SaveFormat.Json e SaveFormat.Png enum**

Nuovi formati di salvataggio supportati.

### **Aggiunge FileFormatType.Emf,FileFormatType.Gif,FileFormatType.Jpg,FileFormatType.Json,FileFormatType.Png,FileFormatType.Wmf enum**

Nuovi tipi di formati di file supportati.

