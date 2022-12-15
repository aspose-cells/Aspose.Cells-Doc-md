---
title: Aspose.Cells for Java 8.8.0 Note di rilascio
type: docs
weight: 110
url: /it/java/aspose-cells-for-java-8-8-0-release-notes/
---
## **1) Aspose.Cells**

|**Chiave** |**Riepilogo** |**Categoria** |
|:- |:- |:- |
|CELLSJAVA-41812 | I marcatori immagine non sono supportati durante il raggruppamento dei dati in marcatori intelligenti| Aumento|
|CELLSJAVA-41772 | La conversione in HTML risulta in una pagina vuota| Insetto|
|CELLSJAVA-41738 | L'allineamento verticale del testo in una casella di testo cambia dal centro verso l'alto durante il rendering del foglio di calcolo in immagine e PDF| Insetto|
|CELLSJAVA-41503 | Gli avvisi di sostituzione dei caratteri non funzionano durante la conversione del foglio di calcolo in formato HTML| Insetto|
|CELLSJAVA-41797 | Aspose.Cells non calcola correttamente il valore della cella| Insetto|
|CELLSJAVA-41779 | Il metodo Cell.calculate() non calcola correttamente i valori| Insetto|
|CELLSJAVA-41813 | Distorsione dello spazio alla fine della seconda pagina evidenziata in rosso nel file Excel di esempio| Insetto|
|CELLSJAVA-41744 | Testo disallineato nel PDF di output| Insetto|
|CELLSJAVA-41723 | Aspose.Cells mancate corrispondenze del PDF generato con il PDF generato da Excel dello stesso foglio di calcolo| Insetto|
|CELLSJAVA-41802 |Le etichette delle tacche dell'asse delle categorie non corrispondono nel PDF di output nel rendering da Excel a PDF| Insetto|
|CELLSJAVA-41800 | L'angolo delle etichette del grafico è cambiato nel PDF del grafico| Insetto|
|CELLSJAVA-41798 | La voce della legenda viene tagliata durante la conversione del grafico in PDF| Insetto|
|CELLSJAVA-41792 | La barra di colore rosso non è presente in Excel ma viene visualizzata in PDF| Insetto|
|CELLSJAVA-41785 | Il foglio di calcolo viene danneggiato dopo aver copiato la cartella di lavoro e aver impostato la posizione di DataLabel| Insetto|
|CELLSJAVA-41784 | Manca la barra degli errori durante la copia della cartella di lavoro| Insetto|
|CELLSJAVA-41780 | Il testo in TextBox viene reso incompleto durante la conversione del foglio di lavoro in immagine| Insetto|
|CELLSJAVA-41773 | Etichette dati mancanti per un grafico nell'immagine di output/PDF per il foglio di calcolo| Insetto|
|CELLSJAVA-41757 | Le barre con valori positivi vengono visualizzate sotto la regola dell'asse x del valore 0 nel PDF del grafico| Insetto|
|CELLSJAVA-41734 | L'ordine della legenda del grafico viene invertito durante il rendering del foglio di lavoro in immagine| Insetto|
|CELLSJAVA-41811 | Aspose.Cells interrompe le tabelle Power Pivot all'apertura e al nuovo salvataggio del formato di file XLSM| Insetto|
|CELLSJAVA-41807 | Problema con le righe raggruppate durante la copia di intervalli nel file XLSX| Insetto|
|CELLSJAVA-41806 | Problema con le righe raggruppate durante la copia di intervalli nel file XLS| Insetto|
|CELLSJAVA-41804 |La formula per WordArt non reagisce alla modifica dell'argomento dopo la conversione da XLS a XLSB| Insetto|
|CELLSJAVA-41803 | L'intervallo di formattazione condizionale non è corretto e non corrisponde a Microsoft Excel| Insetto|
|CELLSJAVA-41809 | Worksheet.calculateFormula genera un'eccezione di puntatore nullo quando la formula viene impostata tramite NameCollection| Eccezione|
|CELLSJAVA-41808 | "java.lang.NullPointerException" in Workbook.save| Eccezione|
## **2) Aspose.Cells Griglia Suite**

|**Chiave** |**Riepilogo** |**Categoria** |
|:- |:- |:- |
|CELLSJAVA-41615 | L'impostazione degli stili della barra dell'intestazione e della scheda non funziona| Insetto|
## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà HTMLLoadOptions.DeleteRedundantSpaces**
 Indica se eliminare gli spazi ridondanti quando il testo va a capo utilizzando le righe<br>etichetta.
### **Rende obsoleta la proprietà LoadOptions.ConvertNumericData e aggiunge la proprietà TxtLoadOptions.ConvertNumericData.**
Utilizzare invece la proprietà TxtLoadOptions.ConvertNumericData o HTMLLoadOptions.ConvertNumericData.
### **Aggiunge la proprietà Style.QuotePrefix.**
Indica se il valore della cella inizia con virgolette singole.
### **Aggiunge la proprietà QueryTable.ConnectionId.**
Ottiene l'ID connessione della tabella di query.
### **Aggiunge la proprietà ExternalConnection.Id.**
Ottiene l'id della connessione.
### **Aggiunge la proprietà ListObject.QueryTable.**
Ottiene la QueryTable collegata della tabella.
### **Aggiunge la proprietà HTMLLoadOptions.KeepPrecision.**
Indica se non analizzare un valore stringa se la lunghezza è 15.

{{% alert color="primary" %}} 

Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.8.0 sono inclusi anche in questo Aspose.Cells for Java v8.8.0.

{{% /alert %}}
