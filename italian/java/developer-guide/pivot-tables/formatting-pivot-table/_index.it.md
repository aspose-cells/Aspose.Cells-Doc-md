---
title: Formattazione della tabella pivot
type: docs
weight: 60
url: /it/java/formatting-pivot-table/
---
## **Aspetto della tabella pivot**

[Come creare una tabella pivot](/cells/it/java/create-pivot-table/) ha mostrato come creare una semplice tabella pivot. Questo articolo va oltre e illustra come personalizzare l'aspetto di una tabella pivot impostando le proprietà.

### **Impostazione delle opzioni di formato della tabella pivot**

 Il[**Tabella pivot**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) class ti consente di impostare varie opzioni di formattazione per una tabella pivot.

#### **Impostazione dei tipi AutoFormat e PivotTableStyle**

 L'esempio di codice che segue illustra come impostare il tipo di formato automatico e il tipo di stile della tabella pivot utilizzando il[**Tipo di formattazione automatica**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) e[**Tipo di stile tabella pivot**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType) proprietà.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **Impostazione delle opzioni di formato**

L'esempio di codice che segue illustra come impostare una serie di opzioni di formattazione per un rapporto tabella pivot, inclusa l'aggiunta di totali complessivi per righe e colonne.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **Impostazione delle opzioni di formato dei campi pivot**

Oltre a controllare la formattazione dell'intera tabella pivot, Aspose.Cells for Java consente un controllo preciso della formattazione per campi riga, campi colonna e campi pagina.

#### **Impostazione del formato dei campi riga, colonna e pagina**

L'esempio di codice che segue mostra come accedere ai campi riga, accedere a una particolare riga, impostare subtotali, applicare l'ordinamento automatico e utilizzare l'opzione autoShow.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **Impostazione del formato dei campi dati**

Le seguenti righe di codice illustrano come formattare i campi dati.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **Modifica lo stile rapido di una tabella pivot**

Gli esempi di codice che seguono mostrano come modificare lo stile rapido applicato a una tabella pivot.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **Cancellazione dei campi pivot**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) ha un metodo chiamato[**chiaro()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear()che cancella i campi pivot. Usalo per cancellare i campi pivot in tutte le aree, ad esempio pagina, colonna, riga o dati.
L'esempio di codice seguente mostra come cancellare tutti i campi pivot nell'area dati.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **Funzione di consolidamento**

### **Applicazione di ConsolidationFunction ai campi dati della tabella pivot**

 Aspose.Cells può essere utilizzato per applicare ConsolidationFunction ai campi dati (o campi valore) della tabella pivot. In Microsoft Excel è possibile fare clic con il pulsante destro del mouse sul campo del valore e quindi selezionare**Impostazioni campo valore...** opzione e quindi selezionare la scheda**Riepiloga valori per**. Da lì, puoi selezionare qualsiasi ConsolidationFunction di tua scelta come Sum, Count, Average, Max, Min, Product, Distinct Count ecc.

 Aspose.Cells fornisce[**Funzione di consolidamento**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) enumerazione per supportare le seguenti funzioni di consolidamento.

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**ConsolidationFunction.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**Funzione di consolidamento.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT_NUMS)
- [**Funzione di consolidamento.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT_COUNT)
- [**ConsolidationFunction.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**ConsolidamentoFunzione.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**ConsolidationFunction.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**ConsolidationFunction.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEV)
- [**ConsolidationFunction.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEVP)
- [**ConsolidationFunction.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**ConsolidationFunction.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**ConsolidationFunction.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

 Si applica il seguente codice**Media** funzione di consolidamento al primo campo dati (o campo valore) e**DistinctCount** funzione di consolidamento al secondo campo dati (o campo valore).

{{% alert color="primary" %}}

La funzione di consolidamento DistinctCount è supportata solo da Microsoft Excel 2013.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
