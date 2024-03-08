---
title: Impostazioni numero
type: docs
weight: 10
url: /it/java/cells-number-settings/
---
##  **Impostazione dei formati di visualizzazione di Numbers e delle date**

Una caratteristica molto importante di Microsoft Excel è che consente agli utenti di impostare i formati di visualizzazione di valori numerici e date. Sappiamo che i dati numerici possono essere utilizzati per rappresentare diversi valori tra cui decimali, valuta, percentuali, frazioni o valori contabili, ecc. Tutti questi valori numerici vengono visualizzati in formati diversi a seconda del tipo di informazioni che rappresentano. Allo stesso modo, esistono molti formati in cui è possibile visualizzare una data o un'ora.
Aspose.Cells supporta questa funzionalità e consente agli sviluppatori di impostare qualsiasi formato di visualizzazione per un numero o una data.

##  **Impostazione dei formati di visualizzazione in Microsoft Excel**

Per impostare i formati di visualizzazione in Microsoft Excel:

1. Fare clic con il pulsante destro del mouse su qualsiasi cella.
1. Seleziona *Formato Cells**. Apparirà una finestra di dialogo che consente di impostare i formati di visualizzazione di qualsiasi tipo di valore.

 Nella parte sinistra della finestra di dialogo ci sono molte categorie di valori come**Generale**, **Numero**, **Valuta**, **Contabilità**, **Data**, **Ora**, **Percentuale,**ecc. Aspose.Cells supporta tutti questi formati di visualizzazione.

##  **Utilizzo dei formati numerici incorporati**

Aspose.Cells offre alcuni formati numerici integrati per configurare i formati di visualizzazione dei numeri e delle date. A tutti i formati numerici incorporati vengono assegnati valori numerici univoci. Gli sviluppatori possono assegnare qualsiasi valore numerico desiderato al file[**Numero**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) metodo del[**Stile**](https://reference.aspose.com/cells/java/com.aspose.cells/style) oggetto per applicare il formato di visualizzazione. Questo approccio è veloce. I formati numerici integrati supportati da Aspose.Cells sono elencati di seguito.

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

##  **Utilizzo di formati numerici personalizzati**

 Per definire la stringa di formato personalizzata per l'impostazione del formato di visualizzazione, utilizzare il file[**Costume**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Questo approccio non è veloce come l'utilizzo di formati preimpostati ma è più flessibile.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

 Se usi il[**Costume**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) per impostare il formato del numero, qualsiasi formato precedente impostato utilizzando il[**Numero**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [Specificare il numero decimale personalizzato e i separatori di gruppo per la cartella di lavoro](/cells/it/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Specifica della formattazione del modello personalizzato DBNum](/cells/it/java/specifying-dbnum-custom-pattern-formatting/)
