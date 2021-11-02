---
title: Getting Notifications while Merging Data with Smart Markers
type: docs
weight: 460
url: /java/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells APIs provide the [WorkbookDesigner](https://apireference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) class to [work with Smart Markers](http://aspose.com/docs/display/cellsjava/Smart+Markers) where the formatting & formulas are placed in the [designer spreadsheets](/cells/java/what-is-a-designer-spreadsheet/) and then processed with [WorkbookDesigner](https://apireference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) class to fill up the data according to specified Smart Markers. Sometimes, it may be required to get the notifications about the cell reference or the particular Smart Marker being processed. This can be achieved using the [WorkbookDesigner.CallBack](https://apireference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) property and [ISmartMarkerCallBack](https://apireference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) interface exposed with the release of Aspose.Cells for Java 8.6.2.

{{% /alert %}} 
## **Get Notifications while Merging Data with Smart Markers**
The following piece of code demonstrates the usage of [ISmartMarkerCallBack](https://apireference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) interface to define a new class that handles the call back for [WorkbookDesigner.process](https://apireference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)) method.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


In order to keep the example simple and to the point, the following snippet creates an empty designer spreadsheet, inserts a Smart Marker and processes it with the dynamically created data source.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
