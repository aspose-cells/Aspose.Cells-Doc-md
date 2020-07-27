+++
title = "Access Hyperlink object of the GridWeb Cell" 
description = "" 
weight = 12332 
+++

Aspose.Cells for Java : Access Hyperlink object of the GridWeb Cell  

# Aspose.Cells for Java : Access Hyperlink object of the GridWeb Cell


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#AccessHyperlinkobjectoftheGridWebCell-PossibleUsageScenarios)
*   2 [Open Hyperlink in New or Existing Window](#AccessHyperlinkobjectoftheGridWebCell-OpenHyperlinkinNeworExistingWindow)
*   3 [Access Hyperlink object of the GridWeb Cell](#AccessHyperlinkobjectoftheGridWebCell-AccessHyperlinkobjectoftheGridWebCell)
*   4 [Sample Code](#AccessHyperlinkobjectoftheGridWebCell-SampleCode)
{{< /panel >}}
 

 


## Possible Usage Scenarios

You can check if cell contains hyperlink or not using the following two methods. These methods will return `null` if the cell does not contain a hyperlink and if it contains a hyperlink, it will return `GridHyperlink` object.

*   `GridHyperlinkCollection.getHyperlink(GridCell cell)`
*   `GridHyperlinkCollection.getHyperlink(int row,int column)`

## Open Hyperlink in New or Existing Window

If your excel file contains hyperlink which links to some URL like `[http://wwww.aspose.com/](http://wwww.aspose.com/)` and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to `_blank`. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of the existing window. Besides, if you want to open the hyperlink in the existing window, then please set the `GridHyperlink.Target` to `_self`.

## Access Hyperlink object of the GridWeb Cell

The following sample code accesses the hyperlink of cell A1. If cell A1 contains hyperlink then it will return `GridHyperlink` object, otherwise, it will return `null`.

## Sample Code

