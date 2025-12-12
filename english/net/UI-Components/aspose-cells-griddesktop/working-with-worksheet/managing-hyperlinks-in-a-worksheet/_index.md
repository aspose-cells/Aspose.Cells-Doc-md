---
title: Managing Hyperlinks in a Worksheet
type: docs
weight: 90
url: /net/aspose-cells-griddesktop/manage-hyperlinks-in-a-worksheet/
keywords: GridDesktop,hyper,link,hyperlink,hyperlinks
description: This article introduces how to work with hyperlink in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Using Aspose.Cells.GridDesktop, it is also possible to add hyperlinks to simple values stored in cells of a worksheet. Let's say that in some cells, you might have values that you would like to link to more detailed information on a webpage. In that case, it would be desirable to add a hyperlink to that cell so that if a user clicks on the cell, they will be directed to that webpage. In this topic, we will explain how developers can add and manipulate hyperlinks in their worksheets.

{{% /alert %}} 
## **Adding Hyperlinks**
To add a hyperlink to a cell using Aspose.Cells.GridDesktop, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- Access a desired **Cell** in the worksheet that will be hyperlinked
- Add some value to the cell to be hyperlinked
- Add **Hyperlink** to the worksheet by specifying the cell name on which the hyperlink would be applied

**Hyperlinks** collection in the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) object provides an overloaded **Add** method. Developers can use any overloaded version of the **Add** method according to their specific needs.

The code below will add a hyperlink to **B2** and **C3** cells of the worksheet.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **Accessing Hyperlinks**
Once a hyperlink has been added to a cell, it may also be required to access and modify the hyperlink at runtime. To do so, developers can simply access the hyperlink from the **Hyperlinks** collection of the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) by specifying the cell (using cell name or its location in terms of row and column number) to which the hyperlink is added. Once the hyperlink is accessed, developers can modify its URL at runtime.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **Removing Hyperlinks**
To remove an existing hyperlink, developers can simply access a desired worksheet and then remove the hyperlink from the **Hyperlinks** collection of the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) by specifying the hyperlinked cell (using its name or row & column number).



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

If you want to add a hyperlink to a cell and display the hyperlink URL in the cell instead of some value, then do not add any value to the cell and simply add the hyperlink to that cell. Doing so, the cell will be hyperlinked and the hyperlink URL will also be displayed in the cell as its value.

{{% /alert %}}
