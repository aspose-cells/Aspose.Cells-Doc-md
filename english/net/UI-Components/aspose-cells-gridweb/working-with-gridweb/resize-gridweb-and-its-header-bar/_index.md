---
title: Resize GridWeb and its Header Bar
type: docs
weight: 30
url: /net/aspose-cells-gridweb/resize-gridweb-and-its-header-bar/
keywords: GridWeb,resize
description: This article introduces how to resize in GridWeb.
---

{{% alert color="primary" %}} 

[Add GridWeb to Web Form](/cells/net/aspose-cells-gridweb/add-gridweb-to-web-form/), discussed resizing the Aspose.Cells.GridWeb control using WYSIWYG. This article explains how to do the same thing but at runtime using the Aspose.Cells.GridWeb API. It also explains how to resize the header bars of the Aspose.Cells.GridWeb control to make their data easier to read.

{{% /alert %}} 
## **Changing Width & Height of Aspose.Cells.GridWeb**
Changing the width and height of Aspose.Cells.GridWeb control is a simple but important feature. The Aspose.Cells.GridWeb control is represented by the GridWeb class in the API. To resize the width and height of the GridWeb control, simply use its width and height properties.

{{% alert color="primary" %}} 

The width and height of the control can be defined in pixels or points.

{{% /alert %}} 

The output of the code snippet that follows is shown below.

**Changed width and height of the GridWeb control** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **Changing Width & Height of Header Bar**
Aspose.Cells.GridWeb control contains two header bars as follows:

- Top header bar, this header bar represents columns as A , B , C , D etc.
- Left header bar, this header bar represents rows as 1 , 2 , 3 , 4 etc.

Both of these header bars are shown below.

**Header bars** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_2.png)

Change the height of the top header bar and the width of the left header bar using the GridWeb control's HeaderBarHeight and HeaderBarWidth properties respectively. The figure below shows the output of the code example that follows.

**Changed header bar width and height** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
