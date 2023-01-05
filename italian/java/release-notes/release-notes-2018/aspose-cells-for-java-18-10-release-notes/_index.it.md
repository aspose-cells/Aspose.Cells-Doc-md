---
title: Aspose.Cells for Java Note sulla versione 18.10
type: docs
weight: 30
url: /it/java/aspose-cells-for-java-18-10-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 18.10.

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42634|Converti la forma del nastro sinistra destra in immagine|Aumento|
|CELLSJAVA-42713|Aspose.Cells for Java JavaDocs - manca il file dell'elenco dei pacchetti|Aumento|
|CELLSJAVA-42528|Il carattere non è un HTML5 valido e un tag di chiusura automatica e i browser web ne travisano il contenuto|Aumento|
|CELLSJAVA-42728|Viene sollevata un'eccezione (StackOverFlow) durante il salvataggio nell'output PDF|Insetto|
|CELLSJAVA-42729|Valore errato calcolato da ROUNDUP()|Insetto|
|CELLSJAVA-42724|Copia un intervallo con PasteType.ALL (opzioni Incolla) che non copia correttamente le altezze delle righe|Insetto|
|CELLSJAVA-42722|La formattazione del testo del collegamento ipertestuale viene persa quando viene impostato un nuovo testo|Insetto|
|CELLSJAVA-42688|Output formato data russo non valido|Insetto|
|CELLSJAVA-42721|Problema con i font SheetRender|Insetto|
|CELLSJAVA-42723|Eccezione "java.lang.OutOfMemoryError: Java spazio heap" durante il rendering del file MS Excel in PDF|Insetto|
|CELLSJAVA-42725|Le virgolette appaiono nella formula quando si recupera la formula della cella tramite Aspose.Cells|Insetto|
|CELLSJAVA-42720|Degrado delle prestazioni quando si utilizza la formattazione condizionale|Insetto|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà HtmlSaveOptions.WidthScalable**
Indica se si utilizza l'unità scalabile per descrivere la larghezza della colonna durante l'esportazione del file in HTML. Il valore predefinito è false.
### **Aggiunge la proprietà WorkbookDesigner.UpdateEmptyStringAsNull**
Indica se elaborare il valore della stringa vuota come null.
### **Aggiorna il valore restituito del metodo DocumentProperty.ToDateTime(), le proprietà BuiltInDocumentPropertyCollection.CreatedTime, BuiltInDocumentPropertyCollection.LastPrinted e BuiltInDocumentPropertyCollection.LastSavedTime.**
Restituisce l'ora nel fuso orario locale.
### **Richiede un vincolo più forte per l'input dell'utente per FormatCondition.Formula1/Formula2**
La semplice stringa di input non può essere determinata se deve fare riferimento a un riferimento al nome o è solo un valore di stringa costante. Quindi, ora richiediamo che la formula inizi con il segno '='. Per il valore di stringa semplice "sss", utilizza un formato come "=\"sss\"".
