---
title: Aspose.Cells for PHP via Java 20.2 Note di rilascio
type: docs
weight: 10
url: /it/php-java/aspose-cells-for-php-via-java-20-2-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for PHP via Java 20.2.

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43076|Imposta il tipo di immagine EMF nel file HTML renderizzato|Aumento|
|CELLSJAVA-43113|Conversione in PDF - java.lang.NumberFormatException: per la stringa di input|Aumento|
|CELLSJAVA-43114|Conversione in PDF - Formula non valida:"'APRIL''12'.A1:'APRIL''12'.I23"|Aumento|
|CELLSJAVA-43117|Conversione in PDF - hex non è un numero esadecimale valido|Aumento|
|CELLSJAVA-43118|Conversione in PDF - java.lang.NumberFormatException: per la stringa di input: "341,403,811.74"|Aumento|
|CELLSJAVA-43077|Eccezione "Tipo di immagine imprevisto" sollevata durante il rendering del foglio di lavoro su HTML|Insetto|
|CELLSJAVA-43096|Il programma si blocca durante la conversione del file Excel in HTML|Insetto|
|CELLSJAVA-43107|Conversione in PDF - com.aspose.cells.CellsException: Shape to image Error!|Insetto|
|CELLSJAVA-43108|Conversione in PDF - com.aspose.cells.CellsException|Insetto|
|CELLSJAVA-43088|Il grafico radar non viene visualizzato nel file di output nella conversione da XLSX a PDF|Insetto|
|CELLSJAVA-43091|Le etichette dei dati nel grafico Donuts sono sovrapposte nel file PDF|Insetto|
|CELLSJAVA-43099|L'immagine del foglio di lavoro non viene visualizzata correttamente|Insetto|
|CELLSJAVA-43093|Il controllo ActiveX non viene rilevato nel formato di file XLS|Insetto|
|CELLSJAVA-43104|Problemi con getShowTabs e setShowTabs|Insetto|
|CELLSJAVA-43121|OOM sta cercando di ottenere il numero di pagine in XLS|Insetto|
|CELLSJAVA-43125|Gli oggetti Form e ActiveX vengono duplicati|Insetto|
|CELLSJAVA-43094|Eccezione durante il caricamento di un formato di file XLSX|Eccezione|
|CELLSJAVA-43100|Eccezione "java.lang.ArrayIndexOutOfBoundsException" quando si chiama Workbook.calculateFormula() in un file Excel|Eccezione|
|CELLSJAVA-43123|ArrayIndexOutOfBoundsException durante l'utilizzo di MEMORY_PREFERENCE|Eccezione|
|CELLSJAVA-43105|Conversione in PDF - java.lang.ArrayIndexOutOfBoundsException: 60|Eccezione|
|CELLSJAVA-43106|Conversione in PDF - java.lang.IllegalArgumentException|Eccezione|
|CELLSJAVA-43109|Conversione in PDF - java.lang.NullPointerException|Eccezione|
|CELLSJAVA-43111|Conversione in PDF - com.aspose.cells.CellsException: dati non validi!|Eccezione|
|CELLSJAVA-43112|Conversione in PDF - java.lang.NullPointerException|Eccezione|
|CELLSJAVA-43115|Conversione in PDF - java.lang.NegativeArraySizeException|Eccezione|
|CELLSJAVA-43116|Conversione in PDF - java.lang.IllegalStateException: l'archiviazione strutturata sembra essere danneggiata.|Eccezione|
|CELLSJAVA-43120|java.lang.NumberFormatException durante la conversione della cartella di lavoro in PDF|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for PHP via Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo sul forum di supporto Aspose.Cells.
#### **Aggiunge la proprietà FormulaParseOptions.Parse.**
Indica se analizzare la formula durante l'impostazione di un'espressione di formula su cella. Il valore predefinito è vero. Se false, l'espressione della formula di input verrà mantenuta così com'è per la cella finché l'utente non chiama altri metodi per analizzarli o i dati della formula analizzati sono richiesti da altre operazioni come il calcolo delle formule.
#### **Aggiunge il metodo Workbook.ParseFormulas(bool ignoreError).**
Analizza tutte le formule che non sono state analizzate quando sono state caricate o impostate su una cella.
#### **Aggiunge la proprietà PivotTable.ExternalConnectionDataSource.**
Ottiene l'origine dati della connessione esterna.
#### **Aggiunge FileFormatType.Numbers35 enum.**
Rappresenta i file numero 3.5 dall'ufficio 2014. Solo per lanciare il formato del file durante la lettura.
#### **Aggiunge la proprietà LoadOptions.CheckDataValid.**
Indica se controllare i dati non validi durante il caricamento dei file.

