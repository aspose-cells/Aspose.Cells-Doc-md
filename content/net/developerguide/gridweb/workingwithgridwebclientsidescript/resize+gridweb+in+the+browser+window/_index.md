---
title : "Resize GridWeb in the browser window" 
description : "" 
weight : 16681 
toc : false
type: docs
url: /net/developerguide/gridweb/workingwithgridwebclientsidescript/resize+gridweb+in+the+browser+window/
---

# Aspose.Cells for .NET : Resize GridWeb in the browser window


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Using GridWeb’s resize method](#using-gridweb’s-resize-method)
    *   2.1 [Sample Code](#sample-code)
*   3 [Making GridWeb resizable using resizable jquery ui feature](#making-gridweb-resizable-using-resizable-jquery-ui-feature)
    *   3.1 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

Sometimes you want Aspose.Cells.GridWeb should resize itself in accordance with browser window. You might need GridWeb should always adjust its size (height, width) and compatible with browser window’s size. Aspose.Cells.GridWeb provides client-side *resize()* function for the purpose. Moreover, you can even make GridWeb control resizable in the browser window. For example, you may use the bottom right handle (via mouse) to customize its width/height in the window. You also need to include/specify jquery Javascript files to make it work in the page source in your project.

## Using GridWeb’s resize method

The following code will check if there is resizing action taken place every 100 milliseconds. When there is no more resizing action, then it thinks the resize operation is finished now. We use a sample template file which is imported into GridWeb. We use client side code for resize the GridWeb. The screenshot shows that GridWeb resizes itself accordingly when resizing the browser window.

![image](https://docs2.aspose.com/cells/net/attachments/48136872/48496688.png)

### Sample Code

## Making GridWeb resizable using resizable jquery ui feature

The following code will  make GridWeb control resizable in the browser window. For example, you may use the bottom right handle to customize its size of GridWeb in the window. We use the same template file which is imported into GridWeb first. We use jquery scripts to make the GridWeb resizable. The screenshot shows that GridWeb has been resized using its bottom right handle in the browser window.

![image](https://docs2.aspose.com/cells/net/attachments/48136872/48496689.png)

### Sample Code

