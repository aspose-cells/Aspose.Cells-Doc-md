---
title: Aspose.Cells for Python via Java 22.10 Note di rilascio
type: docs
weight: 3
url: /it/python-java/aspose-cells-for-python-via-java-22-10-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Python via Java 22.10](https://releases.aspose.com/cells/python-java/new-releases/aspose.cells-for-python-via-java-22.10/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-44890|supporta il file di importazione con openpassword per GridWeb|
|CELLSJAVA-44884| I numeri di elenco non sono corretti dopo la conversione da XLSX a HTML o PDF|
|CELLSJAVA-44883|La cartella di lavoro contenente la tabella pivot viene danneggiata dopo l'elaborazione della tabella pivot al suo interno|
|CELLSJAVA-44879|Il risultato formattato per GridWeb era diverso da Cell.DisplayStringValue|
|CELLSJAVA-44327|Bordi e meno linee mostrate nelle fette di torta in bianco e nero nel grafico per il rendering dell'immagine|
|CELLSJAVA-44853|I dati sull'angolo dell'asse x non sono gli stessi di Excel nel grafico per il rendering dell'immagine|
|CELLSJAVA-44854|I dati sul passaggio dell'asse y non sono gli stessi di Excel nel rendering da grafico a immagine|
|CELLSJAVA-44904|Problemi durante il rendering dei grafici Excel nella conversione JPG|
|CELLSJAVA-44850|Importando un file XLT, il testo non viene visualizzato completamente utilizzando le demo più recenti con l'ultima versione Aspose.Cells.GridWeb con i file di risorse più recenti|
|CELLSJAVA-44857|Quando si utilizza la versione Aspose.Cells.GridWeb for Java v22.8 con i file di risorse più recenti per aprire un documento Excel, l'effetto delle celle è diverso dal documento originale|
|CELLSJAVA-44903|La resa SVG non funziona come previsto|
|CELLSJAVA-44909| Quando più righe sono in grassetto, sembra che trabocchi inutilmente sulle altre righe|
|CELLSJAVA-44898|La lettura da GZIPInputStream a volte genera un falso errore "File danneggiato" nelle versioni 22.7 e successive|
|CELLSJAVA-44881|Eccezione "java.lang.ArrayIndexOutOfBoundsException: 15070" durante il caricamento di un file XLS|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.

### **Modificato il limite di spostamento delle celle fuori dal foglio per l'inserimento di righe**

Nelle vecchie versioni, se ci sono celle che hanno impostazioni di formattazione ma non hanno valore e verranno spostate fuori dal foglio, l'operazione di inserimento non è consentita. Dal 22.10, l'operazione di inserimento è consentita per questo tipo di situazione e tale comportamento è lo stesso con ms excel ora.

### **Aggiunge la classe DataModelConnection**

Specifica una connessione al modello di dati.

### **Aggiunge i metodi Chart.ChangeTemplate(byte[]).**

Modifica il tipo di grafico con il file modello preimpostato.

### **Aggiunge il metodo ChartCollection.Add(byte[] data, string dataRange, bool isVertical, int topRow, int leftColumn,int rightRow, int bottomColumn).**

Aggiunge grafico con file modello preimpostato.