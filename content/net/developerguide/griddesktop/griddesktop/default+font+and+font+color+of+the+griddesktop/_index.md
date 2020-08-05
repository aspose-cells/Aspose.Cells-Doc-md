---
title : "Default Font and Font Color of the GridDesktop" 
description : "" 
weight : 16602 
toc : false
type: docs
url: /net/developerguide/griddesktop/griddesktop/default+font+and+font+color+of+the+griddesktop/
---

# Aspose.Cells for .NET : Default Font and Font Color of the GridDesktop


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Change Default Font and Font Color at Design Time](#change-default-font-and-font-color-at-design-time)
*   3 [Change Default Font and Font Color at Run Time](#change-default-font-and-font-color-at-run-time)
{{< /panel >}}
 

## Possible Usage Scenarios

Sometimes, you want to change the default font and font color of the GridDesktop. Please use the following two properties for this purpose. You can access these properties at Design Time or at Runtime depending upon your needs.

*   `GridDesktop.DefaultCellFont`
*   `GridDesktop.DefaultCellFontColor`

## Change Default Font and Font Color at Design Time

The following screenshot shows how to change the default font and font color of GridDesktop at Design Time.

![image](https://docs2.aspose.com/cells/net/attachments/50266230/50528264.png)

## Change Default Font and Font Color at Run Time

The following sample code explains how to change the default font and font color of GridDesktop at Run Time.

{{< code lang="cs" >}}
//Assign your desired Font object to DefaultCellFont property
System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);
this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property
this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;
{{< /code >}}

