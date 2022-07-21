---
title: Your First Aspose.Cells Application - Hello World
type: docs
weight: 30
url: /net/your-first-aspose-cells-application-hello-world/
---

{{% alert color="primary" %}}

This tutorial shows how to create a very first application (Hello World) using Aspose.Cells' simple API. This simple application creates a Microsoft Excel file with the text 'Hello World' in a specified worksheet cell.

{{% /alert %}}

## **Creating the Hello World Application**

The steps below creates the Hello World application using the Aspose.Cells API:

1. Create an instance of the [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) class.
1. If you have a license, then [apply it](/cells/net/licensing/).
   If you are using the evaluation version, skip the license related code lines.
1. Create a new Excel file, or open an existing Excel file.
1. Access any desired cell of a worksheet in the Excel file.
1. Insert the words **Hello World!** into a cell accessed.
1. Generate the modified Microsoft Excel file.

The implementation of the above steps is demonstrated in the examples below.

### **Code Sample: Creating a New Workbook**

The following example creates a new workbook from the scratch, writes Hello World! into cell A1 on the first worksheet and saves the Excel file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Code Sample: Opening an Existing File**

The following example opens an existing Microsoft Excel template file named "Sample.xlsx", inputs "Hello World!" text into the A1 cell in the first worksheet and saves the workbook.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
