+++
title = "Opening an Excel File" 
description = "" 
weight = 16596 
+++

Aspose.Cells for .NET : Opening an Excel File  

# Aspose.Cells for .NET : Opening an Excel File


A unique feature of Aspose.Cells Grid Suite is its compatibility with Excel files. In this topic, we will demonstrate that how users can open Excel files in their windows applications using Aspose.Cells.GridDesktop control.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#OpeninganExcelFile-Introduction)
*   2 [Opening Excel File](#OpeninganExcelFile-OpeningExcelFile)
    *   2.1 [Opening from a File](#OpeninganExcelFile-OpeningfromaFile)
    *   2.2 [Opening a CSV file](#OpeninganExcelFile-OpeningaCSVfile)
    *   2.3 [Opening from a Stream](#OpeninganExcelFile-OpeningfromaStream)
{{< /panel >}}
 

 

## Introduction

To open an Excel file using `Aspose.Cells.GridDesktop` you have to create a desktop application with GridDesktop Control in it. If you don't know about how to add Aspose.Cells.GridDesktop control to your windows form then you should refer to [How to use Aspose.Cells.GridDesktop](http://www.aspose.com/docs/display/cellsnet/How+to+Use+Aspose.Cells.GridDesktop)

`Aspose.Cells.GridDesktop` provides three following different ways to open an Excel file.

1.  **Opening from a File**
2.  **Opening a CSV file**
3.  **Opening from a Stream**

## Opening Excel File

In this example create a desktop application and do the following.

*   Add one GridControl Control to the form.
*   Add three buttons with their text properties set as following:
    *   **Open Excel File**
    *   **Open CSV File**
    *   **Open from Stream**

### Opening from a File

To load the content from an Excel file to Aspose.Cells.GridDesktop control, you will have to call a method of the control to specify the path of the Excel file. After that, Aspose.Cells.GridDesktop control will automatically find the file from the specified path and display its contents. The code snippet to load the contents of an Excel file is provided in the below example. Create the `Click` event of the **Open Excel File** button and paste the following code inside it.

  
The above code snippet can be used by developers in any way they want. For example, if you want to load an Excel file automatically when a windows form loads then you can add this code under the Load event of your Form.

### Opening a CSV file

Aspose.Cells.GridDesktop control supports loading CSV file also. Create the `Click` event of the **Open CSV File** button and paste the following code inside it.

### Opening from a Stream

In our above discussion, we have discussed about loading an Excel file by using its file path but Aspose.Cells.GridDesktop control also supports loading Excel file from a stream. Create the `Click` event of the **Open from Stream** button and paste the following code inside it.

Using file as a stream is a better approach to prohibit any kind of file access or sharing violation problems because this approach ensures closing all connections to the files by closing the stream.

IMPORTANT: An important point to discuss is that Aspose.Cells.GridDesktop control also contains a method named `LoadFromExcel`, which is also used to load the contents of an Excel file to the Grid. But, this method is now obsolete. So, it is recommended for all developers to use the `ImportExcelFile` method that is more robust and efficient than the obsolete one.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Opening an Excel File-001.png](https://docs2.aspose.com/cells/net/attachments/5017858/5113850.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Opening Excel File.png](https://docs2.aspose.com/cells/net/attachments/5017858/5115239.png) (image/png)  

