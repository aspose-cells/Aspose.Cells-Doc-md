---  
title: Saving an Excel File  
type: docs  
weight: 20  
url: /net/aspose-cells-griddesktop/save-an-excel-file/  
keywords: GridDesktop,save,file  
description: This article introduces how to save file in GridDesktop.  
ai_search_scope: cells_net  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

Using Aspose.Cells.GridDesktop control, users can not only create new Excel files but also manage existing ones. In both cases, it is necessary to save the contents of the Aspose.Cells.GridDesktop. This article explains how users can save their grid contents as an Excel file.  

{{% /alert %}}  

## **Introduction**  
To save the content of Aspose.Cells.GridDesktop control as an Excel file, Aspose.Cells.GridDesktop provides the following methods.  

1. **Saving as a File**  
2. **Saving as a Stream**  

## **Saving File**  
Create a desktop application and add two buttons with a GridControl control to the form. Set the text properties of the buttons as **Save as File** and **Save as Stream**, respectively.  

### **Saving as a File**  
Create the Click event of the **Save as File** button and paste the following code inside it.  

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}  

{{% alert color="primary" %}}  

**IMPORTANT:** An important point to discuss is that the Aspose.Cells.GridDesktop control also contains a method named **SaveToExcel**, which is used to load the contents of an Excel file into the grid. However, this method is now obsolete. Therefore, it is recommended for all developers to use the **ExportExcelFile** method, which is more robust and efficient than the obsolete one.  

{{% /alert %}}  

### **Saving as a Stream**  
Sometimes it might be required by developers to save their grid contents to a stream (for example, a `MemoryStream`). To facilitate this task, the Aspose.Cells.GridDesktop control also supports saving grid data to a stream. Create the Click event of the **Save as Stream** button and paste the following code inside it.  

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}  

{{% alert color="primary" %}}  

**IMPORTANT:** Microsoft Excel sheets can contain a maximum of 65,536 rows and 256 columns. Aspose.Cells.GridDesktop follows the same standards. In the Aspose.Cells.GridDesktop control, developers can create more rows and columns than the standard limit, but when saving the grid data to an Excel file, an exception will be thrown. It means that only data contained within the 65,536 rows and 256 columns can be saved to an Excel file using Aspose.Cells.GridDesktop.  

{{% /alert %}}
