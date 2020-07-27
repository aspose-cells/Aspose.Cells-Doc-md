+++
title = "Access Hyperlink object of the GridWeb Cell" 
description = "" 
weight = 16719 
+++

Aspose.Cells for .NET : Access Hyperlink object of the GridWeb Cell  

# Aspose.Cells for .NET : Access Hyperlink object of the GridWeb Cell


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#AccessHyperlinkobjectoftheGridWebCell-PossibleUsageScenarios)
*   2 [Open Hyperlink in New or Existing Window](#AccessHyperlinkobjectoftheGridWebCell-OpenHyperlinkinNeworExistingWindow)
*   3 [Access Hyperlink object of the GridWeb Cell](#AccessHyperlinkobjectoftheGridWebCell-AccessHyperlinkobjectoftheGridWebCell)
    *   3.1 [Sample Code](#AccessHyperlinkobjectoftheGridWebCell-SampleCode)
{{< /panel >}}
 

 

## Possible Usage Scenarios

You can check if cell contains hyperlink or not using the following two methods. These methods will return `null` if the cell does not contain a hyperlink and if it contains a hyperlink, it will return `GridHyperlink` object.

*   `GridHyperlinkCollection.GetHyperlink(GridCell cell)`
*   `GridHyperlinkCollection.GetHyperlink(int row,int column)`

## Open Hyperlink in New or Existing Window

If your excel file contains hyperlink which links to some URL like `[http://wwww.aspose.com/](http://wwww.aspose.com/)` and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to `_blank`. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of existing window. Please check the `GridHyperlink.Target` property in the following debug window. Besides, if you want to open the hyperlink in the existing window, then please set the `GridHyperlink.Target` to `_self`.

![](https://docs2.aspose.com/cells/net/attachments/5013575/5115150.png)

## Access Hyperlink object of the GridWeb Cell

The following sample code accesses the hyperlink of cell A1. If cell A1 contains hyperlink then it will return `GridHyperlink` object, otherwise, it will return `null`.

### Sample Code

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [gridweb-cell-link-in-debug-window.png](https://docs2.aspose.com/cells/net/attachments/5013575/5115150.png) (image/png)  

