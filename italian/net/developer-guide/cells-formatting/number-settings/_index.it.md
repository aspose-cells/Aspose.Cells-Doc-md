---
title: Impostazioni numero
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo che supporta molte impostazioni diverse del numero di cellulare. Questo articolo introdurrà come utilizzare la libreria Aspose.Cells per gestire le impostazioni del numero delle celle in modo che gli utenti possano regolare il formato del numero nel foglio di calcolo secondo necessità.
keywords: Aspose.Cells, .NET library, electronic spreadsheet, cell number settings, formatting, management, Formats of Numbers and Dates
type: docs
weight: 10
url: /it/net/cells-number-settings/
---
##  **Come impostare i formati di visualizzazione di Numbers e le date**

Una caratteristica molto importante di Microsoft Excel è che consente agli utenti di impostare i formati di visualizzazione di valori numerici e date. Sappiamo che i dati numerici possono essere utilizzati per rappresentare diversi valori tra cui decimali, valuta, percentuali, frazioni o valori contabili, ecc. Tutti questi valori numerici vengono visualizzati in formati diversi a seconda del tipo di informazioni che rappresentano. Allo stesso modo, esistono molti formati in cui è possibile visualizzare una data o un'ora.
Aspose.Cells supporta questa funzionalità e consente agli sviluppatori di impostare qualsiasi formato di visualizzazione per un numero o una data.

###  **Come impostare i formati di visualizzazione in Microsoft Excel**

Per impostare i formati di visualizzazione in Microsoft Excel:

1. Fare clic con il pulsante destro del mouse su qualsiasi cella.
1. Seleziona *Formato Cells**. Apparirà una finestra di dialogo che consente di impostare i formati di visualizzazione di qualsiasi tipo di valore.

 Nella parte sinistra della finestra di dialogo ci sono molte categorie di valori come**Generale**, **Numero**, **Valuta**, **Contabilità**, **Data**, **Ora**, **Percentuale,**ecc. Aspose.Cells supporta tutti questi formati di visualizzazione.

 Aspose.Cells fornisce una lezione,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene a[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. IL[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. Ogni elemento in[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la raccolta rappresenta un oggetto del[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Aspose.Cells fornisce[**Ottieni Stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) E[**Imposta stile**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) metodi per il[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe. Questi metodi vengono utilizzati per ottenere e impostare la formattazione di una cella. IL[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)fornisce alcune proprietà utili per gestire i formati di visualizzazione di numeri e date.

###  **Come utilizzare i formati numerici incorporati**

 Aspose.Cells offre alcuni formati numerici integrati per configurare i formati di visualizzazione dei numeri e delle date. Questi formati numerici incorporati possono essere applicati utilizzando il file[**Numero**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) proprietà del[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) oggetto. A tutti i formati numerici incorporati vengono assegnati valori numerici univoci. Gli sviluppatori possono assegnare qualsiasi valore numerico desiderato al file[**Numero**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) proprietà del[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style)oggetto per applicare il formato di visualizzazione. Questo approccio è veloce. I formati numerici integrati supportati da Aspose.Cells sono elencati di seguito.

|**Valore**|**Tipo**|**Stringa di formato**|
| :- | :- | :- |
|0|General|Generale|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|# ,##0
|
|4|Decimal|# ,##0.00
|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Rosso]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Rosso]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|#  ?/?
|
|13|Fraction|#  */*
|
|14|Date|m/g/aaaa|
|15|Date|d-mm-aa|
|16|Date|d-mmm|
|17|Date|mmm-aa|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|Hmm|
|21|Time|h:mm:ss|
|22|Time|m/g/aa h:mm|
|37|Currency|# ,##0;-#,##0
|
|38|Currency|# ,##0;[Rosso]-#,##0
|
|39|Currency|# ,##0.00;-#,##0.00
|
|40|Currency|# ,##0.00;[Rosso]-#,##0.00
|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h:mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|## 0.0E+00
|
|49|Text|@|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

###  **Come utilizzare formati numerici personalizzati**

 Per definire la stringa di formato personalizzata per l'impostazione del formato di visualizzazione, utilizzare il file[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) dell'oggetto[**Costume**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)proprietà. Questo approccio non è veloce come l'utilizzo di formati preimpostati ma è più flessibile.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

 Se usi il[**Costume**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) proprietà per impostare il formato del numero, qualsiasi formato precedente impostato utilizzando il file[**Numero**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)la proprietà viene sovrascritta e viceversa.

{{% /alert %}}

##  **Argomenti avanzati**
- [Controlla il formato del numero personalizzato quando imposti la proprietà Style.Custom](/cells/it/net/check-custom-number-format-when-setting-style-custom-property/)
- [Elenco dei formati numerici supportati](/cells/it/net/list-of-supported-number-formats/)
- [Rendering Formato data personalizzato Modello ge ge mm gg](/cells/it/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Specificare il numero decimale personalizzato e i separatori di gruppo per la cartella di lavoro](/cells/it/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Specifica della formattazione del modello personalizzato DBNum](/cells/it/net/specifying-dbnum-custom-pattern-formatting/)
