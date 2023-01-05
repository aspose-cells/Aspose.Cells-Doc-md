---
title: Ricezione di notifiche durante l'unione dei dati con i marcatori intelligenti
type: docs
weight: 460
url: /it/java/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 Aspose.Cells Le API forniscono il[Workbook Designer](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) classe a[lavorare con gli Smart Marker](/cells/it/java/smart-markers/) dove la formattazione e le formule sono inserite nel file[fogli di calcolo del progettista](/cells/it/java/what-is-a-designer-spreadsheet/) e poi elaborato con[Workbook Designer](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) class per riempire i dati in base agli Smart Marker specificati. A volte, potrebbe essere necessario ricevere le notifiche sul riferimento della cella o sul particolare Smart Marker in fase di elaborazione. Ciò può essere ottenuto utilizzando il[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) proprietà e[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)interfaccia esposta con il rilascio di Aspose.Cells for Java 8.6.2.

{{% /alert %}} 
## **Ricevi notifiche durante l'unione dei dati con i marcatori intelligenti**
 La parte di codice seguente illustra l'utilizzo di[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)interface per definire una nuova classe che gestisce la richiamata per[WorkbookDesigner.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)) metodo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


Per mantenere l'esempio semplice e pertinente, il seguente frammento di codice crea un foglio di calcolo del designer vuoto, inserisce uno Smart Marker e lo elabora con l'origine dati creata dinamicamente.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
