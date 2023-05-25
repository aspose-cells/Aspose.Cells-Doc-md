---
title: Aspose.Cells for PHP via Java 23.3 Note di rilascio
type: docs
weight: 10
url: /it/php-java/aspose-cells-for-php-via-java-23-3-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for PHP via Java 23.3](https://downloads.aspose.com/cells/php/new-releases/aspose.cells-for-php-via-java-23.3/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
| :- | :- | :- |
|CELLSJAVA-45149|Modificare la logica di generazione di un oggetto "gruppo" dall'oggetto smartart|
|CELLSJAVA-45172|Supporto loadoption per GridWeb|
|CELLSJAVA-45173| Supporta i margini del tag img durante il caricamento di html|
|CELLSJAVA-45110|L'immagine convertita non è la stessa di MS Excel.|
|CELLSJAVA-45190|I valori dei campi calcolati non vengono recuperati dalla funzione getCalculatedValue().|
|CELLSJAVA-45056|Dal grafico all'immagine: l'altezza dei caratteri e della legenda non è visualizzata correttamente|
|CELLSJAVA-45089|Convertito PDF mostra le etichette del diagramma in posizioni diverse e punti dell'asse errati|
|CELLSJAVA-45141| Etichette dati mancanti dal grafico nella cartella di lavoro copiata nella v23|
|CELLSJAVA-45178|Quando si converte xlsx in html, il programma richiederà che la cella iniziale dell'oggetto Chart abbia un contenuto '}' non valido|
|CELLSJAVA-45195|Linea della serie mancante in un grafico a dispersione|
|CELLSJAVA-45054|Impossibile cambiare foglio di lavoro per il file specificato dal cliente|
|CELLSJAVA-45143|CSV file diverso dal file WPS|
|CELLSJAVA-45072|Il PDF convertito da Aspose.Cells dal file MS Excel non può essere letto normalmente con iText|
|CELLSJAVA-45200|Mostrando "#" per i numeri nel PDF convertito|
|CELLSJAVA-45159|Il testo non è allineato al centro durante il rendering nell'immagine png|
|CELLSJAVA-41794|HTML è errato quando alcune righe sono nascoste|
|CELLSJAVA-45189|Seleziona il campo dati pivot di una tabella pivot a cui applicare il formato|
|CELLSJAVA-45197|Problemi di formattazione nella conversione da HTML a Excel|
|CELLSJAVA-45051| La password non funziona all'apertura del file LibreOffice Calc (ODS)|
|CELLSJAVA-44070|Eccezione "Indice riga finale non valido" nel rendering da CSV a PDF|
|CELLSJAVA-45107|Un'eccezione IllegalArgumentException viene generata durante l'esportazione di file in html|

##  **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

###  **Aggiunge la proprietà CalculationOptions.LinkedDataSources**

Consente all'utente di impostare origini dati collegate per i collegamenti esterni utilizzati nella formula per il calcolo.

###  **Classe SvgSaveOptions obsoleta**

Utilizzare invece la classe ImageSaveOptions.

###  **Costruttore SvgSaveOptions() obsoleto**

Utilizzare invece ImageSaveOptions(SaveFormat.Svg) e impostare ImageSaveOptions.ImageOrPrintOptions.OnePagePerSheet su true.

###  **Proprietà SvgSaveOptions.SheetIndex obsoleta**

Utilizzare invece ImageSaveOptions.ImageOrPrintOptions.SheetSet.

###  **Aggiunge l'enumerazione StyleModifyFlag.FontVerticalText**

Indica se il testo è allineato verticalmente.

###  **Aggiunge l'enumerazione WarningType.InvalidOperator**

Rappresenta l'operatore di avviso non valido durante l'utilizzo di file Excel.

###  **Supporta l'impostazione delle proprietà Row.GroupLevel e Column.GroupLevel**

Supporta l'impostazione del livello di gruppo di righe e colonne.

###  **Rende obsoleto HtmlLoadOptions.ConvertFormulasData e aggiunge le proprietà HtmlLoadOptions.HasFormula**

Utilizzare invece HtmlLoadOptions.HasFormula.

###  **Rende obsoleto PivotGlobalizationSettings.GetTextOfProtection() e aggiunge i metodi PivotGlobalizationSettings.GetTextOfProtectedName(String)**

Utilizzare invece PivotGlobalizationSettings.GetTextOfProtectedName(String).

###  **Aggiunge il metodo Chart.IsReferedByChart(Int32,Int32).**

Indica se il grafico fa riferimento a questa cella.

###  **Aggiunge la proprietà PasteOptions.IgnoreLinksToOriginalFile**

Non collegare al file originale durante la copia dell'intervallo.

###  **Aggiunge PivotArea,PivotTableSelectionType e PivotTable.Format(Pivot.PivotArea,Style)**

Selezionare l'area e formattarla della tabella pivot.

###  **Aggiunge la proprietà SheetSet.Active**

Ottiene un set con il foglio attivo della cartella di lavoro.
