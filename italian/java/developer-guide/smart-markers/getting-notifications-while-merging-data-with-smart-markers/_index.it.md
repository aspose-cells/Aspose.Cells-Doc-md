---
title: Ricezione di notifiche durante la fusione dei dati con Smart Markers
type: docs
weight: 460
url: /it/java/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Le API di Aspose.Cells forniscono la classe [WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) per [lavorare con Smart Markers](/cells/it/java/smart-markers/) dove la formattazione e le formule sono inserite nei [fogli di lavoro design](/cells/it/java/what-is-a-designer-spreadsheet/) e quindi elaborate con la classe [WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) per compilare i dati secondo gli Smart Markers specificati. A volte, potrebbe essere necessario ricevere le notifiche riguardo il riferimento della cella o l'Smart Marker particolare in fase di elaborazione. Questo può essere ottenuto utilizzando la proprietà [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) e l'interfaccia [ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) esposte con il rilascio di Aspose.Cells for Java 8.6.2.

{{% /alert %}} 
## **Ricevere notifiche durante la fusione dei dati con Smart Markers**
Il seguente esempio di codice mostra l'uso dell'interfaccia [ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) per definire una nuova classe che gestisce il richiamo alla funzione [WorkbookDesigner.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process--)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


Per mantenere l'esempio semplice e chiaro, il seguente snippet crea un foglio di lavoro designer vuoto, inserisce uno Smart Marker e lo elabora con la sorgente dati creata dinamicamente.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
{{< app/cells/assistant language="java" >}}
