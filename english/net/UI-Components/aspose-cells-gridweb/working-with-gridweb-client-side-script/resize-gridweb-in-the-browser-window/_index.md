---
title: Resize GridWeb in the browser window
type: docs
weight: 40
url: /net/aspose-cells-gridweb/resize-gridweb-in-the-browser-window/
keywords: GridWeb,resize
description: This article introduces how to resize in GridWeb.
---

## **Possible Usage Scenarios**
Sometimes you want Aspose.Cells.GridWeb should resize itself in accordance with browser window. You might need GridWeb should always adjust its size (height, width) and compatible with browser window’s size. Aspose.Cells.GridWeb provides client-side *resize()* function for the purpose. Moreover, you can even make GridWeb control resizable in the browser window. For example, you may use the bottom right handle (via mouse) to customize its width/height in the window. You also need to include/specify jquery Javascript files to make it work in the page source in your project.
## **Using GridWeb’s resize method**
The following code will check if there is resizing action taken place every 100 milliseconds. When there is no more resizing action, then it thinks the resize operation is finished now. We use a sample template file which is imported into GridWeb. We use client side code for resize the GridWeb. The screenshot shows that GridWeb resizes itself accordingly when resizing the browser window.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_1.png)
### **Sample Code**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **Making GridWeb resizable using resizable jquery ui feature**
The following code will  make GridWeb control resizable in the browser window. For example, you may use the bottom right handle to customize its size of GridWeb in the window. We use the same template file which is imported into GridWeb first. We use jquery scripts to make the GridWeb resizable. The screenshot shows that GridWeb has been resized using its bottom right handle in the browser window.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_2.png)
### **Sample Code**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
