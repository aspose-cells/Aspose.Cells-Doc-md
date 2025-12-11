---
title: Zooming In or Out On the Worksheet in GridDesktop
type: docs
weight: 160
url: /net/aspose-cells-griddesktop/zoom-in-or-out-on-the-worksheet-in-griddesktop/
keywords: GridDesktop,zoom,zoom in,zoom out
description: This article introduces how to zoom in or zoom out in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Sometimes, when working with your data, you may want to enlarge the contents on the screen without actually changing the font size. For instance, you may have formatted your text so that it uses a small font. (This is often necessary to get all your information on a printout.) When working in the worksheet, however, the font is difficult to read because it is so small.

In Microsoft Excel, a zoom slider is available for zooming in and out of documents quickly and easily. The zoom slider is usually in the lower right corner of the software window.

Aspose.Cells also allows developers to set the worksheet's zoom factor, so the contents should appear as per your desired percentage value.

{{% /alert %}} 

## **Zooming In or Out Using Aspose.Cells.GridDesktop**

Aspose.Cells provides the **Aspose.Cells.GridDesktop.Worksheet** class that has a wide range of properties and methods for managing worksheets. To set a worksheet's zoom factor, use the Worksheet class's **Zoom** property. The zoom factor is set by assigning a numeric (integer) value to the **Zoom** property.

We build an MS Excel‑like zoom slider using a TrackBar (.NET) control. In a WinForm project, we place the Aspose.Cells.GridDesktop control from the Toolbox onto the form and specify some properties to set its name, size, or other aspects accordingly. Now, we place the TrackBar control at the lower right corner below the GridDesktop control; we also put a Label control that shows the percentage value you specify via the TrackBar control's handle. We add relevant lines of code in the TrackBar's **Scroll** event, so when you scroll the TrackBar control, GridDesktop should zoom in or out to show the data/contents in it.

A complete example is given below that demonstrates how to use the **Zoom** property to set the zoom factor of the active worksheet of GridDesktop. We first import a template Excel file to GridDesktop.

Write the following code in the **Load** event of the form to set the template Excel file in GridDesktop and the TrackBar value.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}

Now copy the following code inside the TrackBar's **Scroll** event and run the application. You will notice that moving the track bar will change the zoom property of the worksheet.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}
