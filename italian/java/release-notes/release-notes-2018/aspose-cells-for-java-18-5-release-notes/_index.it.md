---
title: Aspose.Cells for Java 18.5 Note di rilascio
type: docs
weight: 80
url: /it/java/aspose-cells-for-java-18-5-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 18.5.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42550|La conversione simultanea in PDF mentre ogni cartella di lavoro ha il proprio set privato (esclusivo) di caratteri|Nuova caratteristica|
|CELLSJAVA-42594|Rileva LoadFormat e FileFormatType di XLAM|Aumento|
|CELLSJAVA-42604|La formattazione e il comportamento della tabella pivot sono cambiati dopo l'apertura/salvataggio del file modello|Insetto|
|CELLSJAVA-41918|Il foglio di calcolo (XLS) viene danneggiato dopo un semplice caricamento e salvataggio|Insetto|
|CELLSJAVA-42616|Aspose.Cells interrompe l'interfaccia dell'iteratore quando si chiama Iterator.hasnext() due volte|Insetto|
|CELLSJAVA-42607|Valori delle proprietà alterati durante l'estrazione delle proprietà del documento|Insetto|
|CELLSJAVA-42601|La cartella di lavoro è danneggiata dopo l'aggiunta di una filigrana|Insetto|
|CELLSJAVA-42600|Lo stesso codice viene eseguito più lentamente nelle nuove versioni|Insetto|
|CELLSJAVA-42598|Le proprietà non vengono estratte nel file modello|Insetto|
|CELLSJAVA-42589|NullPointerException quando si aggiunge HTML a una cella|Insetto|
|CELLSJAVA-41414|Le linee sono scomparse dal grafico quando il file XLSX viene nuovamente salvato|Insetto|
|CELLSJAVA-42602|Eccezione "IndexOutOfBoundsException" quando si uniscono le celle in modalità semplificata|Eccezione|
|CELLSJAVA-42610|Eccezione "java.lang.IllegalStateException: codifica non valida: null" durante il caricamento di un file XLS|Eccezione|
|CELLSJAVA-42608|ArrayIndexOutOfBoundsException si verifica all'apertura di un file Excel|Eccezione|
|CELLSJAVA-42596|"java.lang.ArrayIndexOutOfBoundsException" si verifica all'apertura di un file Excel|Eccezione|
|CELLSJAVA-42595|"java.io.IOException: il file è danneggiato" si verifica all'apertura di un file Excel|Eccezione|
|CELLSJAVA-42591|"com.aspose.cells.CellsException: formula non valida" al caricamento di un file Excel|Eccezione|
## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.
### **Aggiunge nuove proprietà Cell.IsTableFormula/IsArrayFormula per sostituire Cell.IsInTable/IsInArray**
Indica se una cella fa parte della formula della tabella o della formula di matrice. I vecchi nomi creano ambiguità, quindi li abbiamo resi obsoleti e ne abbiamo forniti di nuovi.
### **Aggiunge la classe IndividualFontConfigs**
Rappresenta le configurazioni dei caratteri per ogni oggetto della cartella di lavoro.
### **Aggiunge la proprietà LoadOptions.FontConfigs**
Ottiene e imposta le singole configurazioni dei caratteri.
### **Elimina la proprietà FontSetting.ShapeFont obsoleta**
Usare invece la proprietà FontSetting.TextOptions.
### **Aggiunge l'enumerazione OoxmlCompliance e la proprietà WorkbookSettings.Compliance**
Supporta il foglio di calcolo Strict Open Xml.
### **Aggiunge il metodo GroupShape.Ungroup()**
Separa le forme.
### **Aggiunge la proprietà MsoFormatPicture.Gamma**
Ottiene e imposta la gamma dell'immagine.
### **Aggiunge le proprietà TextOptions.FarEastName e TextOptions.LatinName**
Ottiene e imposta l'Estremo Oriente e il nome latino del carattere.
