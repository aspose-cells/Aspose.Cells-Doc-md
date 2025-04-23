---
title: Utilizzo della classe GlobalizationSettings per etichette subtotali personalizzate e altre etichette del grafico a torta
type: docs
weight: 50
url: /it/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **Possibili Scenari di Utilizzo**
Le API di Aspose.Cells hanno esposto la classe [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) al fine di gestire gli scenari in cui l'utente desidera utilizzare etichette personalizzate per i subtotale in un foglio di calcolo. Inoltre, la classe [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) può essere utilizzata anche per modificare l'etichetta **Altro** per il grafico a torta durante il rendering del foglio di lavoro o del grafico.
## **Introduzione alla classe GlobalizationSettings**
La classe [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) attualmente offre i seguenti 3 metodi che possono essere sovrascritti in una classe personalizzata per ottenere etichette desiderate per i subtotale o per rendere del testo personalizzato per l'etichetta **Altro** di un grafico a torta.

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName-int-): Ottiene il nome totale della funzione.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName-int-): Ottiene il nome del totale generale della funzione.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--): Ottiene il nome delle etichette "Altro" per i grafici a torta.
### **Etichette personalizzate per le subtotali**
La classe [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) può essere utilizzata per personalizzare le etichette del Subtotal sovrascrivendo i metodi [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName-int-) e [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName-int-) come mostrato in precedenza.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


Per iniettare etichette personalizzate, è richiesto assegnare la proprietà [WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) a un'istanza della classe *CustomSettings* definita precedentemente prima di aggiungere i subtotali al foglio di lavoro.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

La classe [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) funziona solo per l'aggiunta di nuovi subtotali. Se un foglio di calcolo contiene già dei subtotali, le loro etichette non possono essere modificate.

{{% /alert %}} 
### **Testo personalizzato per l'etichetta Altro del grafico a torta**
La classe [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) offre il metodo [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--) che è utile per attribuire un valore personalizzato all'etichetta "Altro" dei grafici a torta. Il codice seguente definisce una classe personalizzata e sovrascrive il metodo [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--) per ottenere un'etichetta personalizzata in base alla lingua predefinita impostata per JVM.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


Il seguente frammento carica un foglio di calcolo esistente contenente un grafico a torta e renderizza il grafico in un'immagine utilizzando la classe *CustomSettings* creata in precedenza.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


Di seguito è riportata l'immagine risultante quando la localizzazione della macchina è impostata su Francia. Come puoi vedere, l'etichetta "Altro" è stata tradotta in "Autre" come definito nella classe *CustomSettings*.

![todo:image_alt_text](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
{{< app/cells/assistant language="java" >}}
