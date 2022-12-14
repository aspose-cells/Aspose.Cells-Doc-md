---
title: Aspose.Cells for Java 17.1.0 Note di rilascio
type: docs
weight: 120
url: /it/java/aspose-cells-for-java-17-1-0-release-notes/
---
|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42132|Metodi GetPaperWidth e GetPaperHeight aggiunti nella classe PageSetup|Nuova caratteristica|
|CELLSJAVA-41950|Supporta il riempimento sfumato per WordArt durante la conversione di fogli di calcolo in HTML|Nuova caratteristica|
|CELLSJAVA-42129|Salvare in HTML è sbagliato|Insetto|
|CELLSJAVA-42125|Le griglie dietro le forme non vengono esportate quando vengono convertite in HTML|Insetto|
|CELLSJAVA-42110|Alcune regole CSS ignorate durante l'importazione di HTML|Insetto|
|CELLSJAVA-42094|I contenuti sono barrati nell'HTML convertito|Insetto|
|CELLSJAVA-42091|Lo stile del testo di alcune celle è errato quando viene salvato in HTML|Insetto|
|CELLSJAVA-42088|DataBar errato quando la cella ha impostato il colore di sfondo|Insetto|
|CELLSJAVA-42018|L'immagine del grafico non viene salvata quando si utilizza il formato EMF o SVG|Insetto|
|CELLSJAVA-41980|HtrmlSaveOptions.ExportGridLines non sembra funzionare per un particolare foglio di calcolo|Insetto|
|CELLSJAVA-42131|Il ricalcolo di un numero di formule utilizzando le API Aspose Cells restituisce "#NUM!" errore|Insetto|
|CELLSJAVA-42124|Problema di formato della data durante l'importazione di CSV con ICustomParser|Insetto|
|CELLSJAVA-42118|Name.getRanges() API produce risultati imprevisti|Insetto|
|CELLSJAVA-42117|Impossibile accedere alla variabile di istanza m_LoadDataFilterOptions durante l'override del metodo startSheet della classe LoadFilter|Insetto|
|CELLSJAVA-41882|Cell valore stringa e problema di arrotondamento basato su diverse versioni JDK|Insetto|
|CELLSJAVA-42142|I caratteri di controllo da destra a sinistra e da sinistra a destra non vengono visualizzati correttamente in PDF quando la conversione viene eseguita su Linux|Insetto|
|CELLSJAVA-42136|Ebraico - Nella tabella le righe a capo automatico sono allineate a destra in PDF mentre dovrebbero essere centrate come in Excel|Insetto|
|CELLSJAVA-42113|Conversione errata del foglio di lavoro arabo in SVG|Insetto|
|CELLSJAVA-42135|Ebraico: il testo a capo non è allineato a destra in PDF come in Excel|Insetto|
|CELLSJAVA-42134|Ebraico - Le etichette delle serie quando è presente un ritorno a capo automatico i caratteri non vengono visualizzati nella sequenza corretta|Insetto|
|CELLSJAVA-42127|Shape to image Errore durante il rendering di 03.xls in PDF|Insetto|
|CELLSJAVA-42126|Shape to image Errore durante il rendering di 02.xls in PDF|Insetto|
|CELLSJAVA-42087|L'immagine del grafico nell'HTML è errata|Insetto|
|CELLSJAVA-42079|Spessore irregolare delle linee alle intersezioni durante il rendering del foglio di calcolo con diagramma in PDF|Insetto|
|CELLSJAVA-42078|Le etichette dei grafici non vengono visualizzate/renderizzate allo stesso modo (come per il file Excel originale) nel file PDF di output|Insetto|
|CELLSJAVA-42076|L'angolo delle etichette dell'asse x non è corretto nel PDF del grafico|Insetto|
|CELLSJAVA-42065|Rendering errato dei grafici a barre durante il rendering del foglio di calcolo in HTML|Insetto|
|CELLSJAVA-42152|L'impostazione della formula che fa riferimento alla cartella di lavoro esterna crea una formula 3d|Insetto|
|CELLSJAVA-42146|Errore di contenuto illeggibile in Excel 2007 dopo aver salvato nuovamente un foglio di calcolo|Insetto|
|CELLSJAVA-42121|L'espressione di formato condizionale cambia all'eliminazione delle righe|Insetto|
|CELLSJAVA-42114|Cell.getFormula() restituisce una formula scomposta per una cella|Insetto|
|CELLSJAVA-42112|Il file di output viene danneggiato dopo l'esecuzione del metodo DataLabels.setPosition()|Insetto|
|CELLSJAVA-42108|L'ordine di priorità del formato condizionale cambia nel metodo Cells.deleteRows()|Insetto|
|CELLSJAVA-42069|Il modulo Vba viene perso durante il salvataggio di un file XLSM su Linux|Insetto|
|CELLSJAVA-42025|API aggiunge ulteriori apostrofi alla formula modificata|Insetto|
|CELLSJAVA-41984|Formula dinamica nel foglio di lavoro del designer utilizzando {-1} {-2} restituisce Errore di formula non valida|Insetto|
|CELLSJAVA-41739|La trasparenza delle forme viene reimpostata su 0 durante la conversione da XLS a XLSB|Insetto|
|CELLSJAVA-42122|NullPointerException quando si apre un file Excel di grandi dimensioni|Eccezione|
|CELLSJAVA-42123|Errore da forma a immagine - nel rendering di un file Excel|Eccezione|
|CELLSJAVA-42144|new Workbook() potrebbe generare un'eccezione in Aspose.Cells for Java 16.12.6|Eccezione|
|CELLSJAVA-42143|Eccezione: java.lang.ArrayIndexOutOfBoundsException sul metodo Workbook.save()|Eccezione|
|CELLSJAVA-42137|Eccezione dell'indice di colonna non valida durante il rendering di Excel|Eccezione|
|CELLSJAVA-42111|Eccezione formula non valida per l'ultima cella|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge il setter per la proprietà LoadFilter.LoadDataFilterOptions per sostituire la variabile m_LoadDataFilterOptions.**
L'utente può modificare la proprietà LoadDataFilterOptions nell'implementazione di LoadFilter per modificare il comportamento del caricamento della cartella di lavoro.
### **Aggiunge la proprietà CellsHelper.SignificantDigits.**
Ottiene e imposta il numero di cifre significative.
### **Aggiunge la proprietà GlowEffect.Color.**
Ottiene il colore dell'effetto bagliore.
### **Aggiunge la proprietà PageSetup.PaperWidth.**
Rappresenta la larghezza in pollici della carta, considerata l'orientamento della pagina.
### **Aggiunge la proprietà PageSetup.PaperHeight.**
Rappresenta l'altezza in pollici della carta, considerata l'orientamento della pagina.
### **Aggiunge la proprietà WorkbookSettings.CheckCustomNumberFormat.**
Indica se controllare il formato numerico personalizzato durante l'impostazione di Style.Custom.
### **Aggiunge alcuni tipi di grafici.**
Aggiunge più tipi di grafici per MS Office 2016.
### **Aggiunge l'enumerazione DisplayUnitType.Percentage.**
Rappresenta i valori sul grafico devono essere divisi per 0,01.
