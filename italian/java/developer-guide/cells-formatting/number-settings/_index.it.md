---
title: Impostazioni numero
type: docs
weight: 10
url: /it/java/cells-number-settings/
---

## **Impostazione dei formati di visualizzazione dei numeri e delle date**

Una caratteristica molto forte di Microsoft Excel è che consente agli utenti di impostare i formati di visualizzazione dei valori numerici e delle date. Sappiamo che i dati numerici possono essere utilizzati per rappresentare valori diversi, inclusi valori decimali, valute, percentuali, frazioni o valori contabili, ecc. Tutti questi valori numerici vengono visualizzati in formati diversi a seconda del tipo di informazione che rappresentano. Allo stesso modo, ci sono molti formati in cui una data o un'ora possono essere visualizzate.
Aspose.Cells supporta questa funzionalità e consente agli sviluppatori di impostare qualsiasi formato di visualizzazione per un numero o una data.

## **Impostazione dei formati di visualizzazione in Microsoft Excel**

Per impostare i formati di visualizzazione in Microsoft Excel:

1. Fai clic con il pulsante destro del mouse su qualsiasi cella.
1. Seleziona **Formato celle**. Comparirà una finestra di dialogo che servirà per impostare i formati di visualizzazione di qualsiasi tipo di valore.

Nella parte sinistra della finestra di dialogo, ci sono molte categorie di valori come **Generale**, **Numero**, **Valuta**, **Contabilità**, **Data**, **Ora**, **Percentuale**, ecc. Aspose.Cells supporte tutti questi formati di visualizzazione.

## **Utilizzo dei formati numerici incorporati**

Aspose.Cells offre alcuni formati numerici predefiniti per configurare i formati di visualizzazione dei numeri e delle date. Tutti i formati numerici predefiniti hanno valori numerici univoci. Gli sviluppatori possono assegnare qualsiasi valore numerico desiderato al metodo [**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) dell'oggetto [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) per applicare il formato di visualizzazione. Questo approccio è veloce. I formati numerici predefiniti supportati da Aspose.Cells sono elencati di seguito.

|**Valore**|**Tipo**|**Stringa di formato**|
| :- | :- | :- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|#,##0|
|4|Decimal|#,##0.00|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Red]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Red]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|# ?/?|
|13|Fraction|# */*|
|14|Date|m/d/yyyy|
|15|Date|d-mmm-yy|
|16|Date|d-mmm|
|17|Date|mmm-yy|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|h:mm|
|21|Time|h:mm:ss|
|22|Time|m/d/yy h:mm|
|37|Currency|#,##0;-#,##0|
|38|Currency|#,##0;[Red]-#,##0|
|39|Currency|#,##0.00;-#,##0.00|
|40|Currency|#,##0.00;[Red]-#,##0.00|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

## **Utilizzo dei formati numerici personalizzati**

Per definire la propria stringa di formato personalizzata per impostare il formato di visualizzazione, utilizzare il [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Questo approccio non è veloce come l'utilizzo di formati predefiniti ma è più flessibile.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

Se si utilizza [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) per impostare il formato del numero, qualsiasi formato precedente impostato utilizzando [**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) verrà sovrascritto e viceversa.

{{% /alert %}}

## **Argomenti avanzati**
- [Verificare il formato numerico personalizzato quando si imposta Style.Custom Property](/cells/it/java/check-custom-number-format-when-setting-style-custom-property/)
- [Specificare Personalizzare numerico Decimale e Gruppo Separatori per Cartella di lavoro](/cells/it/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Specifica di formattazione pattern personalizzato DBNum](/cells/it/java/specifying-dbnum-custom-pattern-formatting/)
{{< app/cells/assistant language="java" >}}
