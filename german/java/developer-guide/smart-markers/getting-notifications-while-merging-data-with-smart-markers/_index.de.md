---
title: Benachrichtigungen erhalten, während Daten mit Smart Markern zusammengeführt werden
type: docs
weight: 460
url: /de/java/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 Aspose.Cells APIs bieten die[WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) Klasse zu[Arbeiten Sie mit Smart Markern](/cells/de/java/smart-markers/) wo die Formatierungen und Formeln platziert werden[Designer-Tabellen](/cells/de/java/what-is-a-designer-spreadsheet/) und dann mit verarbeitet[WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) Klasse, um die Daten gemäß den angegebenen Smart Markern aufzufüllen. Manchmal kann es erforderlich sein, Benachrichtigungen über den Zellbezug oder den bestimmten Smart Marker zu erhalten, der verarbeitet wird. Dies kann mit der erreicht werden[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) Eigentum und[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)Schnittstelle ausgesetzt mit der Veröffentlichung von Aspose.Cells for Java 8.6.2.

{{% /alert %}} 
## **Erhalten Sie Benachrichtigungen, während Sie Daten mit Smart Markern zusammenführen**
 Der folgende Codeabschnitt demonstriert die Verwendung von[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)-Schnittstelle, um eine neue Klasse zu definieren, die den Rückruf verarbeitet[WorkbookDesigner.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)) Methode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


Um das Beispiel einfach und auf den Punkt zu bringen, erstellt das folgende Snippet ein leeres Designer-Arbeitsblatt, fügt einen Smart Marker ein und verarbeitet es mit der dynamisch erstellten Datenquelle.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
