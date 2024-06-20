---
title: Formattazione della tabella pivot
type: docs
weight: 60
url: /it/java/formatting-pivot-table/
---

## **Aspetto della tabella pivot**

[Come creare una tabella pivot](/cells/it/java/create-pivot-table/) ha mostrato come creare una semplice tabella pivot. Questo articolo va oltre e discute come personalizzare l'aspetto di una tabella pivot impostando le proprietà.

### **Impostazione delle opzioni di formato della tabella pivot**

La classe [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) consente di impostare varie opzioni di formattazione per una tabella pivot.

#### **Impostare i tipi di AutoFormat e PivotTableStyle**

L'esempio di codice seguente illustra come impostare il tipo di auto formato e il tipo di stile della tabella pivot utilizzando le proprietà [**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) e [**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **Impostazione delle Opzioni di Formato**

Il campione di codice seguente illustra come impostare una serie di opzioni di formattazione per un rapporto di tabella pivot, inclusa l'aggiunta dei totali generali per righe e colonne.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **Impostazione delle Opzioni di Formato dei PivotFields**

Oltre a controllare la formattazione complessiva della tabella pivot, Aspose.Cells for Java consente di controllare in modo preciso la formattazione dei campi di riga, dei campi di colonna e dei campi di pagina.

#### **Impostazione del Formato dei Campi di Riga, Colonna e Pagina**

L'esempio di codice seguente mostra come accedere ai campi di riga, accedere a una riga particolare, impostare i subtotali, applicare un ordinamento automatico e utilizzare l'opzione autoShow.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **Impostazione delle Opzioni di Formato dei Campi Dati**

Le righe di codice seguenti illustrano come formattare i campi dati.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **Modifica dello Stile Veloce di una Tabella Pivot**

Gli esempi di codice che seguono mostrano come modificare lo stile rapido applicato a una tabella pivot.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **Cancellazione dei Campi di Tabella Pivot**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) ha un metodo chiamato [**clear()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear--) che cancella i campi di tabella pivot. Usalo per cancellare i campi di tabella pivot in tutte le aree ad esempio, pagina, colonna, riga o dati.
Il campione di codice qui sotto mostra come cancellare tutti i campi di tabella pivot nell'area dati.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **Funzione di consolidamento**

### **Applicazione della funzione di consolidamento ai campi dati della tabella pivot**

Aspose.Cells può essere utilizzato per applicare la funzione di consolidamento ai campi dati (o campi di valore) della tabella pivot. In Microsoft Excel, è possibile fare clic con il pulsante destro del mouse sul campo valore e quindi selezionare l'opzione **Impostazioni campo valore...** e quindi selezionare la scheda **Riepiloga valori per**. Da lì, è possibile selezionare qualsiasi funzione di consolidamento a scelta come Somma, Conteggio, Media, Massimo, Minimo, Prodotto, Conteggio distinto, ecc.

Aspose.Cells fornisce l'enumerazione [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) per supportare le seguenti funzioni di consolidamento.

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**ConsolidationFunction.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**ConsolidationFunction.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT_NUMS)
- [**ConsolidationFunction.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT_COUNT)
- [**ConsolidationFunction.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**ConsolidationFunction.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**ConsolidationFunction.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**ConsolidationFunction.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEV)
- [**ConsolidationFunction.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEVP)
- [**ConsolidationFunction.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**ConsolidationFunction.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**ConsolidationFunction.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

Il seguente codice applica la funzione di consolidamento **Media** al primo campo dati (o campo valore) e la funzione di consolidamento **ConteggioDistinto** al secondo campo dati (o campo valore).

{{% alert color="primary" %}}

La funzione di consolidamento DistinctCount è supportata solo da Microsoft Excel 2013.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
