---
title: Your First Aspose.Cells Application - Hello World
type: docs
weight: 30
url: /net/your-first-aspose-cells-application-hello-world/
description: Create, edit, and save your first Excel file in any supported format using Aspose.Cells for .NET to experience its simplicity and power in C#.
keywords: C# Hello World, Aspose.Cells for .NET Hello World, The first application using Aspose.Cells for .NET, The first program via Aspose.Cells for .NET.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

This tutorial shows how to create the very first application (Hello World) using Aspose.Cells' simple API. This simple application creates a Microsoft Excel file with the text **Hello World** in a specified worksheet cell.

{{% /alert %}}

## **How to Create the Hello World Application**

The steps below create the Hello World application using the Aspose.Cells API:

1. Create an instance of the [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) class.  
2. If you have a license, then [apply it](/cells/net/licensing/). If you are using the evaluation version, skip the license‑related code lines.  
3. Create a new Excel file, or open an existing Excel file.  
4. Access any desired cell of a worksheet in the Excel file.  
5. Insert the words **Hello World!** into the accessed cell.  
6. Generate the modified Microsoft Excel file.

The implementation of the above steps is demonstrated in the examples below.

### **How to Create a New Workbook**

The following example creates a new workbook from scratch, writes **Hello World!** into cell A1 on the first worksheet, and saves the Excel file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **How to Open an Existing File**

The following example opens an existing Microsoft Excel template file named **Sample.xlsx**, inputs the **Hello World!** text into the A1 cell in the first worksheet, and saves the workbook.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
