+++
title = "Saving an Excel File" 
description = "" 
weight = 16597 
+++

Aspose.Cells for .NET : Saving an Excel File  

# Aspose.Cells for .NET : Saving an Excel File


Using Aspose.Cells.GridDesktop control, users cannot only create new Excel files but also manage existing ones. But, in both cases, it would be necessary to save the contents of the Aspose.Cells.GridDesktop. So, this is the topic of our discussion now to let our users know about how can they save their Grid contents as an Excel file.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#SavinganExcelFile-Introduction)
*   2 [Saving File](#SavinganExcelFile-SavingFile)
    *   2.1 [Saving as a File](#SavinganExcelFile-SavingasaFile)
    *   2.2 [Saving as a Stream](#SavinganExcelFile-SavingasaStream)
{{< /panel >}}
 

 

## Introduction

To save the content of Aspose.Cells.GridDesktop control as an Excel file, `Aspose.Cells.GridDesktop` provides follwoing methods.

1.  **Saving as a File**
2.  **Saving as a Stream**

## Saving File

Create a desktop application and add two buttons with a GridControl control to the form. Set text properties of buttons as **Save as File** and **Save as Stream** respectively.

### Saving as a File

Create the `Click` event of the **Save as File** button and paste the following code inside it.

IMPORTANT: An important point to discuss is that Aspose.Cells.GridDesktop control also contains a method named `SaveToExcel` , which is also used to load the contents of an Excel file to the Grid. But, this method is now obsolete. So, it is recommended for all developers to use `ExportExcelFile` method that is more robust and efficient than the obsoleted one.

### Saving as a Stream

Sometimes, it might be required by developers to save their Grid contents to a stream (For example, `MemoryStream`). To facilitate this task, Aspose.Cells.GridDesktop control also supports saving Grid data to a stream. Create the `Click` event of the **Save as Stream** button and paste the following code inside it.

IMPORTANT: Microsoft Excel supports Excel sheets can contain 65,536 rows and 256 columns max. Aspose.Cells.GridDesktop also follows the same standards. In the Aspose.Cells.GridDesktop control, developers can create more rows and columns than the standard limit but when saving the grid data to an Excel file, an exception will be thrown. It means that only data contained in the 65,536 rows and 256 columns can be saved to an Excel file using Aspose.Cells.GridDesktop.

