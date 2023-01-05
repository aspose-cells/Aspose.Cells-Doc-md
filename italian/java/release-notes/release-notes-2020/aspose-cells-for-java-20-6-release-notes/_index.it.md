---
title: Aspose.Cells for Java 20.6 Note di rilascio
type: docs
weight: 10
url: /it/java/aspose-cells-for-java-20-6-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 20.6](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.6/).

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43186|Calcola il totale complessivo per ogni riga con colonna espansa|Aumento|
|CELLSJAVA-43191|Fornire mezzi per gestire gli scenari quando si specificano tipi di carattere errati|Aumento|
|CELLSJAVA-43187|Eccezione durante il caricamento di un file XLS "Microsoft Excel 5.0/95 Workbook"|Aumento|
|CELLSJAVA-43180|Conversione da HTML a Excel per la creazione di un foglio di lavoro nero|Insetto|
|CELLSJAVA-43181|La differenza nell'altezza della riga nella conversione di Excel in HTML|Insetto|
|CELLSJAVA-43188|Lo stile del colore di sfondo non viene mantenuto durante la conversione da HTML a Excel|Insetto|
|CELLSJAVA-43196|Rilevato un numero diverso di moduli VBA utilizzando Aspose.Cells for Java 20.4 e 20.5|Insetto|
|CELLSJAVA-43202|Risorse non rilasciate al completamento della creazione della cartella di lavoro|Insetto|
|CELLSJAVA-43203|Impossibile elaborare alcuni elenchi di convalida di Excel basati sugli intervalli denominati con nomi Unicode|Insetto|
|CELLSJAVA-43185|La qualità JPEG è sempre 75 su setImageResample su Linux|Insetto|
|CELLSJAVA-43192|Carica la cartella dei font /Sistema/Libreria/Fonts su macOS per impostazione predefinita|Insetto|
|CELLSJAVA-43157|Il colore delle serie di dati personalizzate non viene mantenuto durante la creazione di un grafico a cascata|Insetto|
|CELLSJAVA-43175|Un problema con il nome della serie di grafici quando si fa riferimento alla cartella di lavoro ad altre cartelle di lavoro|Insetto|
|CELLSJAVA-43201|Eccezione "java.util.EmptyStackException" al salvataggio in HTML|Eccezione|
|CELLSJAVA-43204|NegativeArraySizeException si verifica quando si utilizza Cell.getDisplayStringValue()|Eccezione|
|CELLSJAVA-43189|Eccezione sollevata durante il caricamento del file XLS|Eccezione|
|CELLSJAVA-43193|NullPointerException si è verificata durante il caricamento di alcuni file XLSX|Eccezione|
|CELLSJAVA-43200|Eccezione "java.lang.ArrayIndexOutOfBoundsException" al caricamento del file|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge il metodo ReferredArea.GetValues(boolcalculateFormulas)/GetValue(introwOffset, int colOffset, boolcalculateFormulas).**
Offre all'utente la possibilità di controllare se le formule devono essere calcolate in modo ricorsivo nell'implementazione di AbstractCalculationEngine.
### **Aggiunge l'enumerazione WarningType.InvalidFontName e WarningType.InvalidTextOfDefinedName.**
Rappresenta il tipo di avviso.
### **Aggiunge le proprietà WarningInfo.CorrectedObject e WarningInfo.ErrorObject.**
Rappresenta i dati errati e i dati aggiornati quando viene generato un avviso.
### **Aggiunge le proprietà WorkbookDesigner.RepeatFormulasWithSubtotal.**
Indica se si ripetono formule con righe di totale parziale.
### **Aggiunge la proprietà PlotArea.IsAutomaticSize.**
Indica se la dimensione dell'area del tracciato è automatica.
### **Elimina la proprietà Style.Rotation obsoleta.**
Utilizzare invece la proprietà Style.RotationAngle.
### **Aggiunge il metodo Gridweb.SetFontFolder(string fontFolder, bool recursive)/SetFontFolders(string[] fontFolders, bool recursive).**
Imposta la cartella/le cartelle dei font
