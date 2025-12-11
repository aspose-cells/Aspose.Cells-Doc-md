---
title: Getting Notifications while Merging Data with Smart Markers
type: docs
weight: 20
url: /net/getting-notifications-while-merging-data-with-smart-markers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells APIs provide the [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) class to **work with Smart Markers**, where the formatting and formulas are placed in the [designer spreadsheets](/cells/net/what-is-a-designer-spreadsheet/) and then processed with the **WorkbookDesigner** class to populate the data according to the specified Smart Markers. Sometimes, it may be required to receive notifications about the cell reference or the particular Smart Marker being processed. This can be achieved using the [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) property and the [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) interface introduced in Aspose.Cells for .NET 8.6.2.

{{% /alert %}} 

The following piece of code demonstrates the usage of the [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) interface to define a new class that handles the **callback** for the [WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) method.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}

The rest of the process includes loading the designer spreadsheet containing the Smart Markers with **WorkbookDesigner** and processing it by setting the data source. In order to keep the example simple, we used a predefined designer spreadsheet containing only two Smart Markers, as shown in the snapshot below, where the data source is created dynamically to merge the data according to the specified Smart Markers.

| ![Getting notifications while merging data with Smart Markers](/images/getting-notifications-while-merging-data-with-smart-markers_1.png) |
| :- |

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
