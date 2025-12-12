---
title: Managing Pictures in a Worksheet
type: docs
weight: 100
url: /net/aspose-cells-griddesktop/manage-pictures-in-a-worksheet/
keywords: GridDesktop,picture,pictures
description: This article introduces how to work with picture in worksheet in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Most people believe that a picture can explain things better than words. That's why Aspose.Cells.GridDesktop supports adding pictures to worksheets to fulfill this belief. In this topic, we will discuss adding and manipulating pictures in worksheets.

{{% /alert %}} 
## **Adding Pictures**
To add a picture to a worksheet using Aspose.Cells.GridDesktop, please follow the steps below:

- Add Aspose.Cells.GridDesktop control to your **Form**
- Access any desired **Worksheet**
- Add **Picture** to the worksheet by specifying the file path of the picture and the cell name where the picture will be inserted

**Pictures** collection in the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) object provides an overloaded **Add** method. Developers can use any overload of the **Add** method according to their specific needs. Using these overloads of the **Add** method, it is possible to add a picture from a file, a stream, or an **Image** object.

Below is the sample code for adding pictures into worksheets.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **Accessing Pictures**
To access and modify an existing picture in the worksheet, developers can retrieve the picture from the **Pictures** collection of the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) by specifying the cell (using the cell name or its location in terms of row and column number) in which the picture is inserted. Once the picture is accessed, developers can modify its image at runtime.

Below is the sample code to access and modify the pictures in a worksheet.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **Removing Pictures**
To remove an existing picture, developers can simply access the desired worksheet and then remove the picture from the **Pictures** collection of the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) by specifying the cell (using its name or row and column numbers) that contains the picture.

The code below shows how to remove pictures from a worksheet.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
