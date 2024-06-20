---
title: Benachrichtigungen beim Zusammenführen von Daten mit Smart Markern erhalten
type: docs
weight: 460
url: /de/java/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells-APIs bieten die [WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner)-Klasse, um mit [Smart Markers](/cells/de/java/smart-markers/) zu arbeiten, wo das Formatieren & Formeln in den [Designer-Arbeitsmappen](/cells/de/java/what-is-a-designer-spreadsheet/) platziert und dann mit der [WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner)-Klasse verarbeitet werden, um die Daten gemäß den spezifischen Smart Markers zu füllen. Manchmal ist es erforderlich, Benachrichtigungen über den Zellbezug oder den bestimmten Smart Marker, der verarbeitet wird, zu erhalten. Dies kann mit der [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)-Eigenschaft und dem [ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)-Interface erreicht werden, das mit der Version Aspose.Cells for Java 8.6.2 veröffentlicht wurde.

{{% /alert %}} 
## **Benachrichtigungen beim Zusammenführen von Daten mit Smart Markern erhalten**
Der folgende Code zeigt die Verwendung des [ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)-Interface, um eine neue Klasse zu definieren, die den Rückruf für die Methode [WorkbookDesigner.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)) behandelt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


Um das Beispiel einfach und auf den Punkt zu halten, erstellt der folgende Codeausschnitt eine leere Designer-Tabelle, fügt einen Smart Marker ein und verarbeitet sie mit der dynamisch erstellten Datenquelle.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
