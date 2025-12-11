---
title: Opening an Excel File
type: docs
weight: 10
url: /net/aspose-cells-griddesktop/open-an-excel-file/
keywords: GridDesktop,open,file
description: This article introduces how to open a file in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

A unique feature of Aspose.Cells Grid Suite is its compatibility with Excel files. In this topic, we will demonstrate how users can open Excel files in their Windows applications using the Aspose.Cells.GridDesktop control.

{{% /alert %}} 

## **Introduction**
To open an Excel file using Aspose.Cells.GridDesktop, you have to create a desktop application with a GridDesktop control in it. If you don't know how to add the Aspose.Cells.GridDesktop control to your Windows Form, then you should refer to [How to use Aspose.Cells.GridDesktop](/cells/net/how-to-use-aspose-cells-griddesktop/).

Aspose.Cells.GridDesktop provides the following three different ways to open an Excel file.

1. **Opening from a File**
2. **Opening a CSV file**
3. **Opening from a Stream**

## **Opening Excel File**
In this example, create a desktop application and do the following.

- Add one GridControl to the form.
- Add three buttons with their Text properties set as follows:
  - **Open Excel File**
  - **Open CSV File**
  - **Open from Stream**

### **Opening from a File**
To load the content from an Excel file into the Aspose.Cells.GridDesktop control, you will have to call a method of the control to specify the path of the Excel file. After that, Aspose.Cells.GridDesktop will automatically find the file from the specified path and display its contents. The code snippet to load the contents of an Excel file is provided in the below example. Create the Click event of the **Open Excel File** button and paste the following code inside it.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}

The above code snippet can be used by developers in any way they choose. For example, if you want to load an Excel file automatically when a Windows Form loads, you can add this code under the Load event of your form.

### **Opening a CSV file**
Aspose.Cells.GridDesktop also supports loading CSV files. Create the Click event of the **Open CSV File** button and paste the following code inside it.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}

### **Opening from a Stream**
In the discussion above, we talked about loading an Excel file using its file path, but Aspose.Cells.GridDesktop also supports loading an Excel file from a stream. Create the Click event of the **Open from Stream** button and paste the following code inside it.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}

Using a file as a stream is a better approach to avoid file access or sharing‑violation problems because it ensures that all connections to the file are closed when the stream is closed.

{{% alert color="primary" %}} 

**IMPORTANT:** An important point to note is that Aspose.Cells.GridDesktop also contains a method named **LoadFromExcel**, which is used to load the contents of an Excel file into the grid. However, this method is now obsolete. Therefore, it is recommended that developers use the **ImportExcelFile** method, which is more robust and efficient than the obsolete one.

{{% /alert %}}
