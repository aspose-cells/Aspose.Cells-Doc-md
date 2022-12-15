---
title: Aspose.Cells for Java 8.9.0 Note di rilascio
type: docs
weight: 70
url: /it/java/aspose-cells-for-java-8-9-0-release-notes/
---
## **1) Aspose.Cells**

|**Chiave** |**Riepilogo** |**Categoria** |
|:- |:- |:- |
|CELLSJAVA-41901 | Le barre si muovono verso l'alto nel PDF di output| Aumento|
|CELLSJAVA-41909 | La specifica di numeri decimali personalizzati e separatori di gruppo per la cartella di lavoro non funziona| Insetto|
|CELLSJAVA-41895 | Il risultato del calcolo della formula differisce dal calcolo nativo di Excel| Insetto|
|CELLSJAVA-41917 | Le caselle di controllo non vengono visualizzate correttamente quando si utilizza il metodo SheetRender.toImage()| Insetto|
|CELLSJAVA-41903 | L'orientamento dei caratteri è diverso durante il rendering in PDF| Insetto|
|CELLSJAVA-41896 | Alcuni caratteri mancano o non sono incollati direttamente nella conversione da Excel a PDF| Insetto|
|CELLSJAVA-41740 | Alcune delle immagini DataBar sono vuote| Insetto|
|CELLSJAVA-41769 | Barre del grafico non allineate correttamente con le celle in PDF| Insetto|
|CELLSJAVA-41905 | Barre disallineate dopo il rendering del foglio di calcolo in EMF| Insetto|
|CELLSJAVA-41894 |Problema relativo agli spazi dei caratteri durante il rendering del foglio di calcolo in PDF| Insetto|
|CELLSJAVA-41893 | L'immagine di sfondo è distorta o sfocata nel PDF di output| Insetto|
|CELLSJAVA-41892 | L'immagine di sfondo viene allungata nel PDF di output| Insetto|
|CELLSJAVA-41916 | Riferimenti di formule esterne interrotti durante l'utilizzo di Cells.copyColumns| Insetto|
|CELLSJAVA-41915 | File XLSX danneggiato dopo la sostituzione del testo| Insetto|
|CELLSJAVA-41912 | Problema con removeFormula su un foglio di calcolo che fa riferimento a intervalli denominati| Insetto|
|CELLSJAVA-41899 | Impossibile rilevare il formato di caricamento XLSX con FileFormatUtil.detectFileFormat| Insetto|
|CELLSJAVA-41328 | Perdita del blocco di testo in frenchCommonWords.xlsx| Insetto|
|CELLSJAVA-40307 | Problema con il controllo dell'overflow del testo| Insetto|
|CELLSJAVA-41919 | CellsException: 2"="Stra?e zu breit",", in Cartella di lavoro ctor| Eccezione|
|CELLSJAVA-41914 | java.lang.ArrayIndexOutOfBoundsException: 4 durante il recupero del carattere della cella| Eccezione|
|CELLSJAVA-41920 | StringIndexOutOfBoundsException: Indice stringa fuori intervallo: 7, durante l'esportazione del grafico nell'immagine| Eccezione|
|CELLSJAVA-41913 | Eccezione: "IllegalArgumentException: length" durante il caricamento di un file Excel (XLS).| Eccezione|
|CELLSJAVA-41911 | Eccezione: "Errore in Cell: ... -Formula non valida" durante il caricamento di un file Excel tramite API Aspose.Cells| Eccezione|
|CELLSJAVA-41906 |Il costruttore della cartella di lavoro genera l'eccezione: "java.lang.NumberFormatException: stringa vuota"| Eccezione|
## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà HtmlSaveOptions.DefaultFontName**
Specifica il nome del carattere predefinito durante l'esportazione HTML, il carattere predefinito verrà utilizzato quando il carattere di stile non esiste. Se questa proprietà è nulla, Aspose.Cells utilizzerà il carattere universale che ha la stessa famiglia con il carattere originale, il valore predefinito è nullo.
### **Aggiunge la proprietà PivotTable.IsExcel2003Compatible**
Specifica se la tabella pivot è compatibile con Excel2003 durante l'aggiornamento della tabella pivot. Se vero, una stringa deve essere inferiore o uguale a 255 caratteri, quindi se la stringa è maggiore di 255 caratteri, verrà troncata. Se false, una stringa non avrà la suddetta restrizione. Il valore predefinito è vero.
### **Aggiunge la proprietà ImageOrPrintOptions.DefaultFont**
Quando i caratteri in Excel sono unicode e non devono essere impostati con il carattere corretto nello stile della cella, possono apparire come blocchi in PDF e immagine.
Imposta il DefaultFont come MingLiu o MS Gothic per mostrare questi caratteri. Se questa proprietà non è impostata, Aspose.Cells utilizzerà il carattere predefinito di System per mostrare questi caratteri unicode.
### **Aggiunge il metodo GetVersion in GridWeb.**
Ottieni la versione di rilascio.

{{% alert color="primary" %}} 

Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.9.0 sono inclusi anche in questo Aspose.Cells for Java v8.9.0.

{{% /alert %}}
