---
title: Impostazioni numero
type: docs
weight: 10
url: /it/java/cells-number-settings/
---
## **Impostazione dei formati di visualizzazione di Numbers e delle date**

Una caratteristica molto forte di Microsoft Excel è che consente agli utenti di impostare i formati di visualizzazione di valori numerici e date. Sappiamo che i dati numerici possono essere utilizzati per rappresentare diversi valori inclusi decimali, valuta, percentuale, frazione o valori contabili, ecc. Tutti questi valori numerici vengono visualizzati in diversi formati a seconda del tipo di informazioni che rappresentano. Allo stesso modo, ci sono molti formati in cui è possibile visualizzare una data o un'ora.
Aspose.Cells supporta questa funzionalità e consente agli sviluppatori di impostare qualsiasi formato di visualizzazione per un numero o una data.

## **Impostazione dei formati di visualizzazione in Microsoft Excel**

Per impostare i formati di visualizzazione in Microsoft Excel:

1. Fai clic con il pulsante destro del mouse su qualsiasi cella.
1.  Selezionare**Formato Cells**. Apparirà una finestra di dialogo utilizzata per impostare i formati di visualizzazione di qualsiasi tipo di valore.

 Nella parte sinistra della finestra di dialogo, ci sono molte categorie di valori come**Generale**, **Numero**, **Moneta**, **Contabilità**, **Data**, **Volta**, **Percentuale,**ecc. Aspose.Cells supporta tutti questi formati di visualizzazione.

## **Utilizzo di formati numerici incorporati**

 Aspose.Cells offre alcuni formati numerici integrati per configurare i formati di visualizzazione dei numeri e delle date. A tutti i formati numerici incorporati vengono assegnati valori numerici univoci. Gli sviluppatori possono assegnare qualsiasi valore numerico desiderato al file[**Numero**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) metodo del[**Stile**](https://reference.aspose.com/cells/java/com.aspose.cells/style) oggetto per applicare il formato di visualizzazione. Questo approccio è veloce. I formati numerici integrati supportati da Aspose.Cells sono elencati di seguito.

|**Valore**|**Tipo**|**Formato stringa**|
|:- |:- |:- |
|0|Generale|Generale|
|1|Decimale|0|
|2|Decimale|0.00|
|3|Decimale|# ,##0
|
|4|Decimale|# ,##0.00
|
|5|Moneta|$#,##0;$-#,##0|
|6|Moneta|$#,##0;[Rosso]$-#,##0|
|7|Moneta|$#,##0.00;$-#,##0.00|
|8|Moneta|$#,##0.00;[Rosso]$-#,##0.00|
|9|Percentuale|0%|
|10|Percentuale|0.00%|
|11|Scientifico|0.00E+00|
|12|Frazione|# ?/?
|
|13|Frazione|# */*
|
|14|Data|m/gg/aa|
|15|Data|d-mmm-aa|
|16|Data|d-mmm|
|17|Data|mmm-aa|
|18|Volta|h:mm AM/PM|
|19|Volta|h:mm:ss AM/PM|
|20|Volta|Hmm|
|21|Volta|h:mm:ss|
|22|Volta|m/gg/aa h:mm|
|37|Moneta|# ,##0;-#,##0
|
|38|Moneta|# ,##0;[Rosso]-#,##0
|
|39|Moneta|# ,##0.00;-#,##0.00
|
|40|Moneta|# ,##0.00;[Rosso]-#,##0.00
|
|41|Contabilità|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Contabilità|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Contabilità|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Contabilità|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Volta|mm:ss|
|46|Volta|h :mm:ss|
|47|Volta|mm:ss.0|
|48|Scientifico|## 0.0E+00
|
|49|Testo|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

## **Utilizzo di formati numerici personalizzati**

Per definire una stringa di formato personalizzata per l'impostazione del formato di visualizzazione, utilizzare il[**Costume**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Questo approccio non è veloce come l'utilizzo di formati preimpostati, ma è più flessibile.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

 Se usi il[**Costume**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) per impostare il formato del numero, qualsiasi formato precedente impostato utilizzando il[**Numero**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [Specifica numeri decimali personalizzati e separatori di gruppo per la cartella di lavoro](/cells/it/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Specifica della formattazione del modello personalizzato DBNum](/cells/it/java/specifying-dbnum-custom-pattern-formatting/)
