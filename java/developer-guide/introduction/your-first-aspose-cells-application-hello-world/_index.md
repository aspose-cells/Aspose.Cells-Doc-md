---
title: Your First Aspose.Cells Application - Hello World
type: docs
weight: 30
url: /java/your-first-aspose-cells-application-hello-world/
---

{{% alert color="primary" %}}

This beginner's topic shows how developers can create a simple first application (Hello World) using Aspose.Cells' simple API. The application creates a Microsoft Excel file with the words Hello World in a specified cell of a worksheet.

{{% /alert %}}

### **Creating the Hello World Application**

To create the Hello World application using Aspose.Cells API:

1. Create an instance of the **[Workbook](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook)** class.
1. Apply the license:
   1. If you have purchased a license, then use the license in your application to get access to Aspose.Cells' full functionality
   1. If you are using the evaluation version of the component (if you're using Aspose.Cells without a license), skip this step.
1. Create a new Microsoft Excel file, or open an existing file in which you want to add/update some text.
1. Access any cell of a worksheet in the Microsoft Excel file.
1. Insert the words **Hello World!** into a cell accessed.
1. Generate the modified Microsoft Excel file.

The examples below demonstrate the above steps.

#### **Creating a Workbook**

The following example creates a new workbook from scratch, writes the words "Hello World!" into cell A1 on the first worksheet, and saves the file.

**The generated spreadsheet** 

![todo:image_alt_text](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CreatingWorkbook-1.java" >}}

#### **Opening an Existing File**

The following example opens an existing Microsoft Excel template file called **book1.xls**, writes the words "Hello World!" in cell A1 in the first worksheet, and saves the workbook as a new file.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-OpeningExistingFile-1.java" >}}
