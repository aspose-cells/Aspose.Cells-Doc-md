---
title: Impostazioni numero
description: Aspose.Cells è una libreria Python per lavorare con file di fogli di calcolo che supporta diverse impostazioni di numeri nelle celle. Questo articolo introdurrà come usare la libreria Aspose.Cells per gestire le impostazioni numeriche delle celle, permettendo agli utenti di modificare il formato dei numeri nel foglio di calcolo come necessario.
keywords: Aspose.Cells, libreria Python, foglio di calcolo elettronico, impostazioni di numeri di celle, formattazione, gestione, Formati di Numeri e Date
type: docs
weight: 10
url: /it/python-net/cells-number-settings/
---

## **Come impostare i formati di visualizzazione dei numeri e delle date**

Una caratteristica molto forte di Microsoft Excel è che consente agli utenti di impostare i formati di visualizzazione dei valori numerici e delle date. Sappiamo che i dati numerici possono essere utilizzati per rappresentare valori diversi, inclusi valori decimali, valute, percentuali, frazioni o valori contabili, ecc. Tutti questi valori numerici vengono visualizzati in formati diversi a seconda del tipo di informazione che rappresentano. Allo stesso modo, ci sono molti formati in cui una data o un'ora possono essere visualizzate.
Aspose.Cells per Python via .NET supporta questa funzionalità e permette agli sviluppatori di impostare qualsiasi formato di visualizzazione per un numero o una data.

### **Come impostare i formati di visualizzazione in Microsoft Excel**

Per impostare i formati di visualizzazione in Microsoft Excel:

1. Fai clic con il pulsante destro del mouse su qualsiasi cella.
1. Seleziona **Formato celle**. Comparirà una finestra di dialogo che servirà per impostare i formati di visualizzazione di qualsiasi tipo di valore.

Nella parte sinistra della finestra di dialogo, ci sono molte categorie di valori come **Generale**, **Numero**, **Valuta**, **Contabilità**, **Data**, **Orario**, **Percentuale,** etc. Aspose.Cells per Python via .NET supporta tutti questi formati di visualizzazione.

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che permette di accedere a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Ogni elemento nella collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells per Python via .NET fornisce metodi [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) e [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) per la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Questi metodi sono usati per ottenere e impostare la formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) fornisce alcune proprietà utili per gestire i formati di visualizzazione di numeri e date.

### **Come utilizzare i formati numerici incorporati**

Aspose.Cells per Python via .NET offre alcuni formati di numero integrati per configurare i formati di visualizzazione di numeri e date. Questi formati di numero integrati possono essere applicati usando la proprietà [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) dell'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Tutti i formati di numero integrati sono associati a valori numerici unici. Gli sviluppatori possono assegnare qualsiasi valore numerico desiderato alla proprietà [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) dell'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) per applicare il formato di visualizzazione. Questo metodo è veloce. I formati di numero integrati supportati da Aspose.Cells sono elencati di seguito.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingBuiltInNumberFormats-1.py" >}}

### **Come utilizzare i formati numerici personalizzati**

Per definire la propria stringa di formato personalizzata per impostare il formato di visualizzazione, utilizzare la proprietà [**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) dell'oggetto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Questo approccio non è veloce come l'uso dei formati preimpostati, ma è più flessibile.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCustomNumber-1.py" >}}

{{% alert color="primary" %}}

Se si utilizza la proprietà [**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) per impostare il formato numerico, qualsiasi formato precedente impostato utilizzando la proprietà [**number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) viene sovrascritto e viceversa.

{{% /alert %}}

## **Argomenti avanzati**
- [Verificare il formato numerico personalizzato quando si imposta Style.Custom Property](/cells/it/python-net/check-custom-number-format-when-setting-style-custom-property/)
- [Elenco dei formati numerici supportati](/cells/it/python-net/list-of-supported-number-formats/)
- [Render Personalizzare data formato modello g e ge mm dd](/cells/it/python-net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Specificare Personalizzare numerico Decimale e Gruppo Separatori per Cartella di lavoro](/cells/it/python-net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Specifica di formattazione pattern personalizzato DBNum](/cells/it/python-net/specifying-dbnum-custom-pattern-formatting/)

