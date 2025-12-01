---
title: Opening an Excel File
type: docs
weight: 10
url: /net/aspose-cells-griddesktop/openg-an-excel-file/
keywords: GridDesktop,open,file
description: This article introduces how to open file in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

A unique feature of Aspose.Cells Grid Suite is its compatibility with Excel files. In this topic, we will demonstrate that how users can open Excel files in their windows applications using Aspose.Cells.GridDesktop control.

{{% /alert %}} 
## **Introduction**
To open an Excel file using Aspose.Cells.GridDesktop you have to create a desktop application with GridDesktop Control in it. If you don't know about how to add Aspose.Cells.GridDesktop control to your windows form then you should refer to [How to use Aspose.Cells.GridDesktop](/cells/net/how-to-use-aspose-cells-griddesktop/)

Aspose.Cells.GridDesktop provides three following different ways to open an Excel file.

1. **Opening from a File**
1. **Opening a CSV file**
1. **Opening from a Stream**
## **Opening Excel File**
In this example create a desktop application and do the following.

- Add one GridControl Control to the form.
- Add three buttons with their text properties set as following:
  - **Open Excel File**
  - **Open CSV File**
  - **Open from Stream**
### **Opening from a File**
To load the content from an Excel file to Aspose.Cells.GridDesktop control, you will have to call a method of the control to specify the path of the Excel file. After that, Aspose.Cells.GridDesktop control will automatically find the file from the specified path and display its contents. The code snippet to load the contents of an Excel file is provided in the below example. Create the Click event of the **Open Excel File** button and paste the following code inside it.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


The above code snippet can be used by developers in any way they want. For example, if you want to load an Excel file automatically when a windows form loads then you can add this code under the Load event of your Form.
### **Opening a CSV file**
Aspose.Cells.GridDesktop control supports loading CSV file also. Create the Click event of the **Open CSV File** button and paste the following code inside it.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **Opening from a Stream**
In our above discussion, we have discussed about loading an Excel file by using its file path but Aspose.Cells.GridDesktop control also supports loading Excel file from a stream. Create the Click event of the **Open from Stream** button and paste the following code inside it.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



Using file as a stream is a better approach to prohibit any kind of file access or sharing violation problems because this approach ensures closing all connections to the files by closing the stream.

{{% alert color="primary" %}} 

IMPORTANT: An important point to discuss is that Aspose.Cells.GridDesktop control also contains a method named LoadFromExcel, which is also used to load the contents of an Excel file to the Grid. But, this method is now obsolete. So, it is recommended for all developers to use the ImportExcelFile method that is more robust and efficient than the obsolete one.

{{% /alert %}}
