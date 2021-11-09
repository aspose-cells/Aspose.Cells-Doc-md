---
title: Getting Started
type: docs
weight: 10
url: /net/getting-started/
---

{{% alert color="primary" %}} 

This page will show you how to install Aspose Cells, and a simple Hello World program to get you started.

{{% /alert %}}

## **How To Install**
 
You can install Aspose Cells in the following ways:

### **Install Aspose Cells through NuGet.**

NuGet is the easiest way to download and install Aspose APIs for .NET. Open Microsoft Visual Studio and NuGet package manager. Search "aspose.cells" to find the desired Aspose Cells API. Click on "Install", the selected API will be downloaded and referenced in your project.

You can also download it from the nuget web page for aspose.cells: 
[Aspose.Cells for .NET NuGet Package](https://www.nuget.org/packages/Aspose.Cells/)

[More step for details](/cells/net/installation/)

### **Install Aspose Cells on windows.**

You can download Aspose Cells msi from the following page:
[Download Aspose.Cells msi](https://downloads.aspose.com/cells/net/)

On Windows, double-click the MSI installation package and follow the instructions to install it.

[More step for details](/cells/net/installing-aspose-cells-on-windows/)

## **Creating the Hello World Application**

The steps below creates the Hello World application using the Aspose.Cells API:

1. Create an instance of the [Workbook](https://apireference.aspose.com/cells/net/aspose.cells/workbook) class.
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
