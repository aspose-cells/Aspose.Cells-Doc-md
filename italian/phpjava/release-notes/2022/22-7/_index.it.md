---
title: Aspose.Cells for PHP via Java 22.7 Note di rilascio
type: docs
weight: 6
url: /it/php-java/aspose-cells-for-php-via-java-22-7-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for PHP via Java 22.7](https://releases.aspose.com/cells/php/new-releases/aspose.cells-for-php-via-java-22.7/).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-44721|Supporta l'ordinamento di PivotField tramite campo calcolato|
|CELLSJAVA-44733|Esamina le regole di ms excel per visualizzare il bordo della cella quando la colonna adiacente è nascosta: il bordo della cella non è stato sincronizzato|
|CELLSJAVA-44695| Conversione errata a PDF da XLS con Line Callout a sinistra del foglio|
|CELLSJAVA-44700|campi calcolati della tabella pivot non vengono aggiornati durante l'aggiornamento dell'origine dati|
|CELLSJAVA-44705|Cell.getDependents() genera un'eccezione o non può fornire tutti i dipendenti|
|CELLSJAVA-44717|Problema con lo stile del bordo (linea).|
|CELLSJAVA-44707| la linea di confine non viene visualizzata|
|CELLSJAVA-44670| Problema con le formule nell'output HTML - Conversione da Excel a HTML|
|CELLSJAVA-44202|Quando si esporta in HTML, la legenda nel grafico non è la stessa di MS Excel|
|CELLSJAVA-44591|La rotazione del testo delle etichette non corrisponde a Excel nell'immagine di output del grafico|
|CELLSJAVA-44655|Impossibile visualizzare il grafico Treemap con valore negativo, causando il proseguimento dell'esecuzione|
|CELLSJAVA-44686|Il testo del titolo di chart(2016) non è corretto quando Title.IsAutoText è true|
|CELLSJAVA-44689|Regressione: problema relativo alla lingua della legenda del grafico a cascata|
|CELLSJAVA-44687|Problema grafico durante la combinazione dei file|
|CELLSJAVA-44736|Stile della tabella perso durante la copia del foglio|
|CELLSJAVA-44725| Eccezione "java.util.zip.ZipException: dimensione voce non valida (previsto 0 ma ottenuto 1053 byte)" durante la conversione da XLSX a PDF|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge il metodo Cells.GetDependentsInCalculation(int,int,bool)**

Ottiene tutte le celle il cui risultato calcolato dipende dalla cella specificata da riga e colonna in base alla catena di calcolo corrente. Per la cella che è vuota e non è stata istanziata nel modello di celle corrente, l'utente può utilizzare questo metodo invece di Cell.GetDependentsInCalculation(bool) perché il successivo deve prima istanziare l'oggetto cella nel modello di celle corrente.

### **Cambia il bordo sinistro/destro della cella per Cell.GetStyle() quando la colonna adiacente è nascosta**

Nelle versioni precedenti, se la colonna adiacente è nascosta per una cella, il bordo sinistro/destro di questa cella non verrà verificato con la cella adiacente, quindi il bordo restituito potrebbe essere diverso da quello mostrato nella finestra di dialogo di ms excel quando si imposta il bordo di questa cella. Da 22.7, facciamo in modo che il bordo restituito sia sempre il valore effettivo (che dovrebbe essere coerente con il bordo della sua cella adiacente) della cella per Cell.GetStyle(). Se l'utente ha bisogno di quanto mostrato per la cella in ms excel (quando la colonna adiacente è nascosta, il bordo mostrato potrebbe essere quello della successiva colonna visibile), l'utente può provare Cell.GetDisplayStyle().

### **Aggiungere le proprietà Range.Top, Range.Left, Range.Height e Range.Width.**

Ottiene la posizione e le dimensioni dell'intervallo in unità di punti.

### **Elimina la classe PowerQueryFormulaCollction e aggiungi la classe PowerQueryFormulaCollection.**

C'è un errore di battitura nella vecchia classe.

### **Aggiungere le proprietà HtmlSaveOptions.ExportPageFooters e HtmlSaveOptions.ExportPageHeaders.**

Indica se esportare intestazioni e piè di pagina durante il salvataggio come singolo file html.

### **Aggiunge la proprietà HtmlSaveOptions.ShowAllSheets.**

Indica se visualizzare tutti i fogli durante il salvataggio come singolo file html.

### **Rende obsoleta la proprietà HtmlSaveOptions.ExportHeadings e aggiunge la proprietà HtmlSaveOptions.ExportRowColumnHeadings.**

Utilizzare invece HtmlSaveOptions.ExportRowColumnHeadings.

### **Obsoleto Chart.ToImage(string, ImageFormat) e aggiunto Chart.ToImage(string, ImageType)**

Utilizzare invece Chart.ToImage(string, ImageType).
