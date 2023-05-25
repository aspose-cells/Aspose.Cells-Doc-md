---
title: Aspose.Cells for Java 23.2 Note di rilascio
type: docs
weight: 11
url: /it/java/aspose-cells-for-java-23-2-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 23.2](https://releases.aspose.com/cells/java/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
| :- | :- | :- |
|CELLSJAVA-43438|Compila il tag `<Application>` in XLSX|
|CELLSJAVA-45119|Durante la lettura nel formato 03 excel, il 'FillType' della linea retta non viene elaborato|
|CELLSJAVA-45128|Il capovolgimento orizzontale sembra mancare durante la lettura delle linee delle frecce|
|CELLSJAVA-45061|Da XLS a HTML: immagine allungata|
|CELLSJAVA-45062|Da XLS a HTML: spostamento della freccia|
|CELLSJAVA-45085|Diagram problema sparso in Excel al rendering PDF|
|CELLSJAVA-45118|Visualizzazione della forma incompleta dopo la rotazione quando si salva in pdf|
|CELLSJAVA-45078|Calcolo SOMMA MEDIA `#VALUE!` |
|CELLSJAVA-45088|Il risultato visualizzato non è corretto per l'html risultante quando il valore della cella è una stringa con formato personalizzato|
|CELLSJAVA-45094|Intervalli con nomi globali con riferimenti come `=!$K$23` interrompono nella nuova versione|
|CELLSJAVA-45115|Il metodo deleteRows sta causando una formattazione errata|
|CELLSJAVA-45077|Il file salvato segnala un errore durante il caricamento e l'apertura nel disco Onedrive|
|CELLSJAVA-45109|Viene generata un'eccezione durante la conversione del grafico in immagine|
|CELLSJAVA-45112|Renderizza la griglia principale speciale per il grafico radar|
|CELLSJAVA-45103|Le immagini colorate inserite in excel diventano nere quando vengono convertite in pdf|
|CELLSJAVA-45155| Il testo Center Across viene tagliato se si trova nell'ultima colonna durante la conversione in pdf|
|CELLSJAVA-45160|Conversione da HTML a EXCEL non riuscita con errore Non valido `#`|
|CELLSJAVA-45079|Il formato numerico personalizzato con punti finali viene ignorato durante l'esportazione in HTML|
|CELLSJAVA-45084|Carattere modificato nel file xls risalvato|
|CELLSJAVA-45106|Il file dei risultati è anomalo durante la conversione di excel in html|
|CELLSJAVA-45117|Errore di rotazione della forma durante il salvataggio in html|
|CELLSJAVA-45123|La forma dell'arco deve essere capovolta orizzontalmente rispetto a Excel 95|
|CELLSJAVA-45132|Supporta il riempimento a motivo della forma in Excel95/5.0|
|CELLSJAVA-45147|Parte del testo nell'ultima colonna viene tagliata durante il salvataggio del file in html|
|CELLSJAVA-45148|Aree unite perse dopo il salvataggio come html|
|CELLSJAVA-45087|Il bordo viene visualizzato sul testo per il titolo del grafico in Excel fino al rendering PDF|

##  **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

###  **Aggiunge la proprietà ChartTextFrame.IsAutomaticRotation**

Indica se il testo del grafico viene ruotato automaticamente.

###  **Proprietà JsonLayoutOptions.IgnoreObjectTitle e JsonLayoutOptions.IgnoreArrayTitle obsolete**

Utilizzare invece la proprietà JsonLayoutOptions.IgnoreTitle.

###  **Aggiunge la proprietà JsonLayoutOptions.IgnoreTitle**

Ingorisce i titoli degli attributi Json durante la conversione di JSON in Excel.

###  **Aggiunge il metodo Style.ToJson()**

Converte lo stile dei file Excel in file json

###  **Aggiunge il metodo Cell.ToJson()**

Converte una cella di celle in un file json.

