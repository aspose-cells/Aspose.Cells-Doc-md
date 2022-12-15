---
title: Aspose.Cells for Android via Java 19.9 Note di rilascio
type: docs
weight: 20
url: /it/java/aspose-cells-for-android-via-java-19-9-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Android via Java 19.9.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSANDROID-92|Supporta la licenza Product.Family|Nuova caratteristica|
|CELLSJAVA-42949|Aspose.Cells supporta gli algoritmi ECDSA e RSA|Nuova caratteristica|
|CELLSJAVA-42979|Ottieni il conteggio totale delle pagine prima della conversione in pdf/immagine|Nuova caratteristica|
|CELLSJAVA-42967|Inserisci il file SVG nel foglio di lavoro|Nuova caratteristica|
|CELLSJAVA-42969|Supporta Java 12 in Aspose.Cells for Java|Aumento|
|CELLSJAVA-42977|Elevato consumo di CPU e memoria durante la conversione da Excel a PDF|Aumento|
|CELLSJAVA-42861|Impossibile ottenere il testo alternativo della forma nel formato file ODS|Insetto|
|CELLSJAVA-42929|Il titolo del grafico cambia nella conversione da XLSX a PDF|Insetto|
|CELLSJAVA-42933|Il colore della grafica cambia durante la conversione del file Excel in PDF|Insetto|
|CELLSJAVA-42946|Rendering errato del grafico a barre in pila con serie in PDF|Insetto|
|CELLSJAVA-42942|Pagine stampate a livello di foglio di lavoro e non a livello di cartella di lavoro|Insetto|
|CELLSJAVA-42952|Rientro errato dalla parte superiore della cella in alcune parole|Insetto|
|CELLSJAVA-42902|Lo stile del grafico a cascata non viene copiato correttamente durante la copia della cartella di lavoro|Insetto|
|CELLSJAVA-42939|Avviso generato da Excel se chiamiamo Workbook.getVbaProject() solo per una cartella di lavoro|Insetto|
|CELLSJAVA-42940|Avviso di sicurezza dopo aver rimosso tutti gli script del modulo VBA|Insetto|
|CELLSJAVA-42955|L'apertura di VBAProject danneggia la cartella di lavoro|Insetto|
|CELLSJAVA-42902|Lo stile del grafico a cascata non viene copiato correttamente durante la copia della cartella di lavoro|Insetto|
|CELLSJAVA-42944|Errore durante la conversione di XLSX in HTML|Insetto|
|CELLSJAVA-42966|L'aggiornamento della tabella pivot e dei grafici pivot danneggia il file Excel|Insetto|
|CELLSJAVA-42975|Differenze nella conversione HTML|Insetto|
|CELLSJAVA-42971|# N/D è mostrato nel PDF renderizzato
|Insetto|
|CELLSJAVA-42970|Linea di confine estesa indesiderata nel rendering da Excel a PDF|Insetto|
|CELLSJAVA-42976|Mancata corrispondenza della posizione dell'immagine durante il rendering del file Excel in PDF|Insetto|
|CELLSJAVA-42961|Proprietà della tabella non copiate correttamente durante la copia dei dati utilizzando copyColumns|Insetto|
|CELLSJAVA-42980|L'immagine trasparente diventa opaca durante la copia dell'immagine|Insetto|
|CELLSJAVA-42990|Le righe nascoste vengono visualizzate durante la conversione del file Excel in HTML quando esiste il filtro automatico|Insetto|
|CELLSJAVA-42997|CalculateFormula() ha esito negativo con stringhe di formule di grandi dimensioni|Insetto|
|CELLSJAVA-43000|CalculateFormula() corrompe il file Excel|Insetto|
|CELLSJAVA-42987|Problemi di formattazione durante la conversione di file Excel in PDF|Insetto|
|CELLSJAVA-42986|Sovrapposizione di testo dopo aver convertito il file XLSX cinese in PDF|Insetto|
|CELLSJAVA-43012|Workbook.setRecalculateOnOpen(false) non funziona per le versioni di Excel più recenti|Insetto|
|CELLSJAVA-42996|Le etichette dati basate su formule non vengono visualizzate correttamente in PDF|Insetto|
|CELLSJAVA-42945|Salva come HTML genera un'eccezione se ExportImagesAsBase64 è impostato|Eccezione|
|CELLSJAVA-42953|NullPointerException durante la conversione di file XLS in HTML|Eccezione|
|CELLSJAVA-42951|java.lang.NullPointerException generata da comment.setHtmlNote()|Eccezione|
|CELLSJAVA-42954|Eccezione sollevata durante il caricamento e il salvataggio di XLSX|Eccezione|
|CELLSJAVA-42957|Viene generato un valore FontUnderlineType non valido durante il salvataggio di XLSX|Eccezione|
|CELLSJAVA-42992|Eccezione sollevata durante la conversione di XLSM in immagine|Eccezione|
|CELLSJAVA-42991|Eccezione "La larghezza della colonna deve essere compresa tra 0 e 255" durante la conversione di Excel in PDF in macOS|Eccezione|
|CELLSJAVA-43004|Eccezione java.lang.NumberFormatException: per la stringa di input: "0.0" durante la conversione di Excel in HTML|Eccezione|
|CELLSJAVA-43010|IllegalArgumentException durante l'esecuzione di deleteBlankColumns()|Eccezione|
## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Android via Java. sul forum di supporto Aspose.Cells.
### **Aggiorna la libreria BouncyCastle di riferimento a 1.60**
La libreria BouncyCastle utilizzata nell'archivio delle versioni è stata aggiornata alla versione 1.60.
### **Obsoleta la classe HTMLLoadOptions e aggiunta la classe HtmlLoadOptions**
Utilizzare invece la classe HtmlLoadOptions.
### **Obsoleta la classe ODSLoadOptions e aggiunta la classe OdsLoadOptions**
Utilizzare invece la classe OdsLoadOptions.
### **Rende obsoleta la classe JSONUtility e aggiunge la classe JsonUtility**
Usa invece la classe JsonUtility.
### **Aggiunge l'interfaccia IPageSavingCallback**
Controlla/Indica l'avanzamento del processo di salvataggio della pagina.
### **Aggiunge la classe PageSavingArgs**
Informazioni per un processo di salvataggio della pagina.
### **Aggiunge la classe PageStartSavingArgs**
Le informazioni per una pagina avviano il processo di salvataggio.
### **Aggiunge la classe PageEndSavingArgs**
Le informazioni per una pagina terminano il processo di salvataggio.
### **Aggiunge la classe SheetPrintingPreview**
Rappresenta l'anteprima di stampa del foglio di lavoro.
### **Aggiunge la classe WorkbookPrintingPreview**
Rappresenta l'anteprima di stampa della cartella di lavoro.
### **Aggiunge la proprietà QueryTable.ExternalConnection.**
Ottiene la connessione dell'oggetto querytable.
### **Aggiunge la proprietà Hyperlink.LinkType ed enum TargetModeType.**
Rappresenta il tipo di collegamento del collegamento ipertestuale.
### **Rimuove la proprietà Chart.Rotation obsoleta.**
Usare invece la proprietà Chart.RotationAngle.
### **Rimuove la proprietà Chart.IsDataTableShown obsoleta.**
Usare invece Chart.ShowDataTableproperty.
### **Rimuove la proprietà Chart.IsLegendShown obsoleta.**
Usare invece la proprietà Chart.ShowLegend.
### **Rimuove la proprietà obsoleta Axis.Crosses.**
Utilizzare invece la proprietà Axis.Crosses.
### **Aggiunge le proprietà enum OoxmlCompressionType e XlsbSaveOptions.CompressionType,OoxmlSaveOptions.CompressionType.**
Rappresenta il tipo di compressione per i file OOXML.
