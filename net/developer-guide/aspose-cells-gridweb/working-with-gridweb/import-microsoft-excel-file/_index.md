---
title: Import Microsoft Excel File
type: docs
weight: 40
url: /net/import-microsoft-excel-file/
---

{{% alert color="primary" %}} 

Like Aspose.Cells.GridDesktop, Aspose.Cells.GridWeb control can open and load Microsoft Excel files - complete with data, formatting, charts, images etc. - but in web applications. This topic explains how.

{{% /alert %}} 
## **Import Excel Files**
### **Import from File**
To open an Excel file using Aspose.Cells.GridWeb control:

1. Add the Aspose.Cells.GridWeb control to a web form.
1. Import the Excel file by specifying the file path.
1. Run the application.

{{% alert color="primary" %}} 

If you don't know how to add the control to a web form, refer to [Add GridWeb to Web Form](/cells/net/add-gridweb-to-web-form-html/).

{{% /alert %}} 

When Aspose.Cells.GridWeb control is added to a web form, the control is automatically instantiated and added to the form with a default size. You don't have to create an Aspose.Cells.GridWeb control object, all you have to do is drag and drop the control and start using it.

However, to load the content from an Excel file to Aspose.Cells.GridWeb control, you have to call the ImportExcelFile method to specify the path of the Excel file. After that, Aspose.Cells.GridWeb control will automatically find the file from the specified path and display its contents. A code snippet that loads the contents of an Excel file is provided below.



{{< gist "aspose-cells" "18f6c28b77ee30c773fb2199168e73ed" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


The above code snippet can be used any way you want. For example, to load an Excel file automatically when a web form loads, add this code to the form's Page_Load event. If you want to open a file when a button is clicked, add a button to the web form and write the above code under the button's Click event.

**An Excel file is loaded when a button is clicked** 

![todo:image_alt_text](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

If your file system is NTFS, you should grant read access permission to the ASPNET or Everyone user accounts or you will get an access denied exception at runtime.

{{% /alert %}} 
### **Import from Stream**
As well as opening Excel files from file, the Aspose.Cells.GridWeb control can load Excel files from a stream. Using file as a stream is a better approach to prohibit any kind of file access or sharing violation problems because this approach ensures closing all connections to the files by closing the stream.



{{< gist "aspose-cells" "18f6c28b77ee30c773fb2199168e73ed" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
