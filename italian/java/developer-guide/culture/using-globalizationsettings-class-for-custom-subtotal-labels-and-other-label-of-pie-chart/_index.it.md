---
title: Utilizzo della classe GlobalizationSettings per le etichette di totale parziale personalizzate e altre etichette del grafico a torta
type: docs
weight: 50
url: /it/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **Possibili scenari di utilizzo**
 Aspose.Cells API hanno esposto il file[Impostazioni di globalizzazione](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) class per gestire gli scenari in cui l'utente desidera utilizzare etichette personalizzate per i subtotali in un foglio di calcolo. Inoltre, il[Impostazioni di globalizzazione](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)class può essere utilizzata anche per modificare il file**Altro** etichetta per il grafico a torta durante il rendering del foglio di lavoro o del grafico.
## **Introduzione alla classe GlobalizationSettings**
 Il[Impostazioni di globalizzazione](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) class attualmente offre i seguenti 3 metodi che possono essere sovrascritti in una classe personalizzata per ottenere le etichette desiderate per i subtotali o per rendere il testo personalizzato per il**Altro** etichetta di un grafico a torta.

1. [Impostazioni di globalizzazione.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)): Ottiene il nome totale della funzione.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)): Ottiene il nome del totale complessivo della funzione.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)): Ottiene il nome delle etichette "Altro" per i grafici a torta.
### **Etichette personalizzate per subtotali**
 Il[Impostazioni di globalizzazione](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) può essere utilizzata per personalizzare le etichette Subtotale sovrascrivendo il[Impostazioni di globalizzazione.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)) & [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)) metodi come dimostrato in precedenza.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 Per iniettare etichette personalizzate, è necessario assegnare il file[WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) proprietà a un'istanza di*Impostazioni personalizzate*class definita sopra prima di aggiungere i subtotali al foglio di lavoro.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

 Il[Impostazioni di globalizzazione](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)class funziona solo per l'aggiunta di nuovi subtotali. Se un foglio di calcolo contiene già subtotali, le relative etichette non possono essere modificate.

{{% /alert %}} 
### **Testo personalizzato per altra etichetta del grafico a torta**
 Il[Impostazioni di globalizzazione](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) classe offre il[getAltroNome](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\) ) utile per assegnare un valore personalizzato all'etichetta "Altro" dei grafici a torta. Il frammento di codice seguente definisce una classe personalizzata ed esegue l'override di[getAltroNome](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)) per ottenere un'etichetta personalizzata basata sulla lingua predefinita impostata per JVM.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 Il seguente frammento carica un foglio di calcolo esistente contenente un grafico a torta e visualizza il grafico in un'immagine mentre utilizza il file*Impostazioni personalizzate*classe creata sopra.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


 Di seguito è riportata l'immagine risultante quando la locale della macchina è impostata su Francia. Come puoi vedere, l'etichetta "Altro" è stata tradotta in "Autre" come definito in*Impostazioni personalizzate*classe.

![cose da fare:immagine_alt_testo](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
