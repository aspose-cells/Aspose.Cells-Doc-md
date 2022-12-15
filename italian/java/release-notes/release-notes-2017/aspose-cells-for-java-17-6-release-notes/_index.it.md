---
title: Aspose.Cells for Java 17.6 Note di rilascio
type: docs
weight: 70
url: /it/java/aspose-cells-for-java-17-6-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 17.6](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.6/).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42315|Aggiunta dell'API client JS per l'evento AjaxCallFinished - GridWeb (JAVA)|Nuova caratteristica|
|CELLSJAVA-42194|Righe di gruppo nel foglio di lavoro - GridWeb (JAVA)|Nuova caratteristica|
|CELLSJAVA-42308|La tabella pivot è errata (righe mancanti, intestazioni dei campi pivot stampate due volte, data convertita in valori numerici e così via) nel rendering da Excel a HTML|Insetto|
|CELLSJAVA-42298|Caratteri aggiuntivi presenti nell'output HTML del file Excel|Insetto|
|CELLSJAVA-42277|L'immagine non viene visualizzata nell'HTML di output quando HtmlSaveOptions.setExportHiddenWorksheet è impostato su false|Insetto|
|CELLSJAVA-42259|L'HTML non può essere convertito correttamente nel file Excel|Insetto|
|CELLSJAVA-42256|Problema con il rendering della tabella HTML in Excel|Insetto|
|CELLSJAVA-42319|Problema con il calcolo dell'area di stampa quando si specificano le formule|Insetto|
|CELLSJAVA-42273|La funzione Set Column Header Tip non funziona in GridWeb (JAVA)|Insetto|
|CELLSJAVA-42269|GridWorksheet.setColumnHeaderToolTip() non funziona in GridWeb (JAVA)|Insetto|
|CELLSJAVA-42320|Il grafico non viene aggiornato se esiste in un foglio separato|Insetto|
|CELLSJAVA-42295|Il valore Cell viene aggiunto all'inizio quando facciamo clic su una cella esistente (con un valore)|Insetto|
|CELLSJAVA-42325|Quando XLSX viene salvato come PDF, le parole vengono rispecchiate|Insetto|
|CELLSJAVA-42299|Caratteri extra presenti nell'output PDF/immagine del file Excel|Insetto|
|CELLSJAVA-42301|Le barre non sono presenti nell'output PDF del grafico a barre|Insetto|
|CELLSJAVA-42293|L'immagine del grafico è errata nell'HTML di output|Insetto|
|CELLSJAVA-42292|L'immagine del grafico non è corretta nell'HTML di output|Insetto|
|CELLSJAVA-42270|Il contenuto è mancante quando il grafico di Excel viene convertito in PDF|Insetto|
|CELLSJAVA-42258|Il PDF del grafico ha un formato della data errato per le etichette dell'asse x|Insetto|
|CELLSJAVA-42252|Ridimensionamento errato dell'asse Y nel PDF di output|Insetto|
|CELLSJAVA-42245|Lo stile/formattazione è errato durante il salvataggio in HTML|Insetto|
|CELLSJAVA-42316|L'opzione per comprimere le immagini non viene conservata all'apertura e al salvataggio del file Excel|Insetto|
|CELLSJAVA-42306|Il colore di sfondo delle celle in File2 viene modificato all'apertura e al salvataggio della cartella di lavoro|Insetto|
|CELLSJAVA-42305|Il colore di sfondo delle celle in File1 viene modificato all'apertura e al salvataggio della cartella di lavoro|Insetto|
|CELLSJAVA-42303|La cella della formula di Excel diventa una cella senza formula quando si imposta il testo per la forma|Insetto|
|CELLSJAVA-42284|Workbook.getFonts() mostra un carattere aggiuntivo dopo aver ricaricato lo stesso foglio di calcolo|Insetto|
|CELLSJAVA-42307|Eccezione: "L'indice di riga non deve trovarsi all'interno del rapporto tabella pivot" si è verificato durante il rendering nel formato di file HTML|Eccezione|
|CELLSJAVA-42285|Eccezione: "L'indice di riga non può essere negativo" si è verificato se esiste una tabella pivot nel foglio di lavoro da convertire nel formato di file HTML|Eccezione|
|CELLSJAVA-42318|Viene generata un'eccezione quando si tenta di aprire la cartella di lavoro|Eccezione|
|CELLSJAVA-42311|Eccezione: "java.lang.NullPointerException" all'apertura di un file ODS tramite API Aspose.Cells|Eccezione|
|CELLSJAVA-42302|NullPointerException sulla creazione dell'istanza della cartella di lavoro dal file Excel di origine|Eccezione|
## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà Gridweb.OnAjaxCallFinishedClientFunction**
Ottiene o imposta il nome della funzione lato client da chiamare al termine di ajaxcall.
### **Aggiunge enum StyleModifyFlag.RelativeIndent**
Rappresenta il rientro relativo.
### **Aggiunge la proprietà TextureFill.IsTiling**
Indica se l'immagine del riquadro è una trama.


### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

- [Affianca l'immagine come texture all'interno della forma](/cells/it/java/tile-picture-as-a-texture-inside-the-shape/)
- [Utilizzando OnAjaxCallFinishedClientFunction di GridWeb](/cells/it/java/using-onajaxcallfinishedclientfunction-of-gridweb/)
- [Utilizzando il parametro Formula nel campo Smart Marker](/cells/it/java/using-formula-parameter-in-smart-marker-field/)
