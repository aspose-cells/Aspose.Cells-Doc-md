---
title: Working with Visual Studio
type: docs
weight: 20
url: /net/working-with-visual-studio/
---

{{% alert color="primary" %}} 

This topic explains how to use Aspose.Cells.GridWeb in ASP.NET applications using Visual Studio.NET 2005. This topic is useful for the beginner-level developers working with Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Working with Aspose.Cells.GridWeb Using Visual Studio 2013**
This topic shows how to use Aspose.Cells.GridWeb by making a sample website in Visual Studio 2013. The process has been divided into steps.
### **Step 1: Creating New Web Site**
1. Open Visual Studio 2013.
1. From the **File** menu, select **New Menu**, then **Web Site**. 

![todo:image_alt_text](working-with-visual-studio_1.png)


The New Web Site dialog is opened. 

1. Select **ASP.NET Web Forms Site** from Visual Studio installed templates.
1. Choose HTTP mode for the location of the web site. 

![todo:image_alt_text](working-with-visual-studio_2.png)




1. Specify a location where the web site files will be created and stored. 
   1. Click **Browse** in the New Web Site dialog. 

![todo:image_alt_text](working-with-visual-studio_3.png)



The Choose Location dialog is displayed. 

1. Click the **Local IIS** tab.
   All folders and web applications stored in your IIS root folder are displayed (for example: C:\Inetpub\wwwroot). 

![todo:image_alt_text](working-with-visual-studio_4.png)




1. Now create a new web application in your local IIS where the website files will be stored.
   The Choose Location dialog lets you create and delete web applications or virtual directories in your local IIS. To create a web application, click a button as shown below in the figure. 

![todo:image_alt_text](working-with-visual-studio_5.png)



A new web application with the default name WebSite is created. 

1. Rename the web application. We renamed it GridWebOn2013.
1. Click **Open**. 

![todo:image_alt_text](working-with-visual-studio_6.png)



You return to the New Web Site dialog. The path of web site location is set to <http://localhost/GridWebOn2013>. 

1. Click **OK** to let Visual Studio create a web site. 

![todo:image_alt_text](working-with-visual-studio_7.png)
### **Step 2: Checking Source & Design Views of a Web Page**
A default web site will have been created by Visual Studio 2013. It contains a default.aspx web page with some dummy text and markup. 

**Source view of default.aspx page** 

![todo:image_alt_text](working-with-visual-studio_8.png)



All web pages (including ASP.NET) can be opened in two modes. One is the source view that lets developers access and modify the source code. The second mode is design view that can be used to design web pages in a WYSIWYG manner. The above screenshot shows a source view of default.aspx web page. To view the design view, click **Design**. 

**Design view of default.aspx page** 

![todo:image_alt_text](working-with-visual-studio_9.png)




Delete the Default.aspx page added by Visual Studio and add a new blank Default.aspx page.

![todo:image_alt_text](working-with-visual-studio_10.png)
### **Step 3: Adding Aspose.Cells.GridWeb to Web Page**
You can simply add Aspose.Cells.GridWeb (or GridWeb) control to a web page by dragging it from the toolbox. 

![todo:image_alt_text](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

If you don't know about how to add Aspose.Cells.GridWeb to the toolbox, refer to [Integrate Aspose.Cells Grid Controls with Visual Studio.NET](/cells/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

Once GridWeb control is dropped to web page, it would render like this: 

![todo:image_alt_text](working-with-visual-studio_12.png)



### **Step 4: Change the <!DOCTYPE> tag**
1. Switch to source view and find the following **<!DOCTYPE>** tag in the source code: 

**ASP.NET**

{{< highlight csharp >}}



<!DOCTYPE html>



{{< /highlight >}}

1. Select the complete tag. 

![todo:image_alt_text](working-with-visual-studio_13.png)




1. Retain, change or delete the <!DOCTYPE> tag.
1. Or modify the <!DOCTYPE> tag with the following one: 

{{< highlight csharp >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **Step 5: Resizing Aspose.Cells.GridWeb Control**
You can change the width and height of the GridWeb control after dragging it to the website. 

In design view, you can resize the width and height of the GridWeb. 

![todo:image_alt_text](working-with-visual-studio_14.png)



### **Step 6: Configuring the Properties of Aspose.Cells.GridWeb**
Configure the Aspose.Cells.GridWeb properties in WYSIWYG by clicking the **Properties** button on the right side of Visual Studio 2013 IDE. 
A Properties dialog is displayed. 

![todo:image_alt_text](working-with-visual-studio_15.png)



The Properties pane makes it possible to configure the look & feel of the GridWeb and some other properties to control GridWeb's behaviour.
### **Step 7: Running Your First Web Site Containing Aspose.Cells.GridWeb**
Build and run the web site. 

1. Run the web site directly from Visual Studio by pressing Ctrl+F5 or clicking **Start Debugging**. 

![todo:image_alt_text](working-with-visual-studio_16.png)

Now, you can start playing with GridWeb control. 

**GridWeb control in action** 

![todo:image_alt_text](working-with-visual-studio_17.png)
