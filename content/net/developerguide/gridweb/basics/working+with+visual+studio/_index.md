---
title : "Working with Visual Studio" 
description : "" 
weight : 16657 
toc : false
type: docs
url: /net/developerguide/gridweb/basics/working+with+visual+studio/
---

# Aspose.Cells for .NET : Working with Visual Studio


This topic explains how to use Aspose.Cells.GridWeb in ASP.NET applications using Visual Studio.NET 2005. This topic is useful for the beginner-level developers working with Aspose.Cells.GridWeb.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Working with Aspose.Cells.GridWeb Using Visual Studio 2013](#working-with-aspose.cells.gridweb-using-visual-studio-2013)
    *   1.1 [Step 1: Creating New Web Site](#step-1:-creating-new-web-site)
    *   1.2 [Step 2: Checking Source & Design Views of a Web Page](#step-2:-checking-source-&-design-views-of-a-web-page)
    *   1.3 [Step 3: Adding Aspose.Cells.GridWeb to Web Page](#step-3:-adding-aspose.cells.gridweb-to-web-page)
    *   1.4 [Step 4: Change the <!DOCTYPE> tag](#step-4:-change-the-<!doctype>-tag)
    *   1.5 [Step 5: Resizing Aspose.Cells.GridWeb Control](#step-5:-resizing-aspose.cells.gridweb-control)
    *   1.6 [Step 6: Configuring the Properties of Aspose.Cells.GridWeb](#step-6:-configuring-the-properties-of-aspose.cells.gridweb)
    *   1.7 [Step 7: Running Your First Web Site Containing Aspose.Cells.GridWeb](#step-7:-running-your-first-web-site-containing-aspose.cells.gridweb)
{{< /panel >}}
## Working with Aspose.Cells.GridWeb Using Visual Studio 2013

This topic shows how to use Aspose.Cells.GridWeb by making a sample website in Visual Studio 2013. The process has been divided into steps.

### Step 1: Creating New Web Site

1.  Open Visual Studio 2013.
2.  From the **File** menu, select **New Menu**, then **Web Site**.  
      
    ![image](5115368.png)  
    The New Web Site dialog is opened.
3.  Select **ASP.NET Web Forms Site** from Visual Studio installed templates.
4.  Choose HTTP mode for the location of the web site.  
      
    ![image](5115367.png)  
      
    
5.  Specify a location where the web site files will be created and stored.
    1.  Click **Browse** in the New Web Site dialog.  
          
        ![image](5115298.png)  
          
        The Choose Location dialog is displayed.
    2.  Click the **Local IIS** tab.  
        All folders and web applications stored in your IIS root folder are displayed (for example: C:\\Inetpub\\wwwroot).  
          
        ![image](5115294.png)  
          
        
    3.  Now create a new web application in your local IIS where the website files will be stored.  
        The Choose Location dialog lets you create and delete web applications or virtual directories in your local IIS. To create a web application, click a button as shown below in the figure.  
          
        ![image](5115293.png)  
          
        A new web application with the default name WebSite is created.
    4.  Rename the web application. We renamed it GridWebOn2013.
    5.  Click **Open**.  
          
        ![image](5115304.png)  
          
        You return to the New Web Site dialog. The path of web site location is set to [http://localhost/GridWebOn2013](http://localhost/GridWebOn2013).
6.  Click **OK** to let Visual Studio create a web site.  
      
    ![image](5115303.png)

### Step 2: Checking Source & Design Views of a Web Page

A default web site will have been created by Visual Studio 2013. It contains a default.aspx web page with some dummy text and markup.  
  
**Source view of default.aspx page**  
![image](5115306.png)  
  
All web pages (including ASP.NET) can be opened in two modes. One is the source view that lets developers access and modify the source code. The second mode is design view that can be used to design web pages in a WYSIWYG manner. The above screenshot shows a source view of default.aspx web page. To view the design view, click **Design**.  
  
**Design view of default.aspx page**  
![image](5115305.png)  
  

Delete the Default.aspx page added by Visual Studio and add a new blank Default.aspx page.

![image](5115300.png)

### Step 3: Adding Aspose.Cells.GridWeb to Web Page

You can simply add Aspose.Cells.GridWeb (or GridWeb) control to a web page by dragging it from the toolbox.  
  
![image](5115299.png)  
  

If you don't know about how to add Aspose.Cells.GridWeb to the toolbox, refer to [Integrate Aspose.Cells Grid Controls with Visual Studio.NET](https://docs2.aspose.com/cells/net/gettingstarted/gridsuiteandvsnet/integrate+aspose.cells+grid+controls+with+visual+studio.net).

Once GridWeb control is dropped to web page, it would render like this:  
  
![image](5115302.png)  
  

### Step 4: Change the <!DOCTYPE> tag

1.  Switch to source view and find the following **<!DOCTYPE>** tag in the source code:
    
    **ASP.NET**
    
{{< code lang="cs" >}}
 
<!DOCTYPE html>
 
{{< /code >}}
    
2.  Select the complete tag.  
      
    ![image](5115301.png)  
      
    
3.  Retain, change or delete the <!DOCTYPE> tag.
4.  Or modify the <!DOCTYPE> tag with the following one:
    
{{< code lang="cs" >}}
 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
 
{{< /code >}}
    

### Step 5: Resizing Aspose.Cells.GridWeb Control

You can change the width and height of the GridWeb control after dragging it to the website.

In design view, you can resize the width and height of the GridWeb.  
  
![image](5115312.png)  
  

### Step 6: Configuring the Properties of Aspose.Cells.GridWeb

Configure the Aspose.Cells.GridWeb properties in WYSIWYG by clicking the **Properties** button on the right side of Visual Studio 2013 IDE.  
A Properties dialog is displayed.  
  
![image](5115314.png)  
  
The Properties pane makes it possible to configure the look & feel of the GridWeb and some other properties to control GridWeb's behaviour.

### Step 7: Running Your First Web Site Containing Aspose.Cells.GridWeb

Build and run the web site.

1.  Run the web site directly from Visual Studio by pressing Ctrl+F5 or clicking **Start Debugging**.  
      
    ![image](5115313.png)

Now, you can start playing with GridWeb control.  
  
**GridWeb control in action**  
![image](5115276.png)

