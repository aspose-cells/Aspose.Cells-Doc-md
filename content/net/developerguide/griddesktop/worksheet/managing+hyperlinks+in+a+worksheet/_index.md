---
title : "Managing Hyperlinks in a Worksheet" 
description : "" 
weight : 16613 
toc : false
type: docs
url: /net/developerguide/griddesktop/worksheet/managing+hyperlinks+in+a+worksheet/
---

# Aspose.Cells for .NET : Managing Hyperlinks in a Worksheet


Using Aspose.Cells.GridDesktop, it is also possible to add hyperlinks to simple values stored in cells of a worksheet. Let's say that in some cells, you might have some values that you would like to link with more detailed information on a webpage. In that case, it would be desirable to add a hyperlink to that cell so that if a user click on the cell then he would be directed to that webpage. In this topic, we will explain that how developers can add and manipulate hyperlinks in their worksheets.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Adding Hyperlinks](#adding-hyperlinks)
*   2 [Accessing Hyperlinks](#accessing-hyperlinks)
*   3 [Removing Hyperlinks](#removing-hyperlinks)
{{< /panel >}}
 

 

## Adding Hyperlinks

To add a hyperlink to a cell using Aspose.Cells.GridDesktop, please follow the steps below:

*   Add `Aspose.Cells.GridDesktop` control to your **Form**
*   Access any desired **Worksheet**
*   Access a desired **Cell** in the worksheet that will be hyperlinked
*   Add some value to the cell to be hyperlinked
*   Add **Hyperlink** to the worksheet by specifying the cell name on which the hyperlink would be applied

**Hyperlinks** collection in the **Worksheet** object provides an overloaded **Add** method. Developers can use any overloaded version of **Add** method according to their specific needs.

Below code will add a hyperlink to **B2** and **C3** cells of the worksheet.

## Accessing Hyperlinks

Once a hyperlink will be added to a cell, it may also be required to access and modify the hyperlink at runtime. To do so, developers can simply access the hyperlink from the **Hyperlinks** collection of the **Worksheet** by specifying the cell (using cell name or its location in terms of row and column number) to which the hyperlink is added. Once the hyperlink is accessed, developers can modify its URL at runtime.

## Removing Hyperlinks

To remove an existing hyperlink, developers can simply access a desired worksheet and then **Remove** hyperlink from the **Hyperlinks** collection of the **Worksheet** by specifying the hyperlinked cell (using its name or row & column number).

If you want to add a hyperlink to a cell and want to display the hyperlink URL in the cell instead of some value then don't add any value to the cell and simply add the hyperlink to that cell. Doing so, the cell will be hyperlinked and the hyperlink URL will also be displayed in the cell as its value.

