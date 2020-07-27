+++
title = "Working with Visual Studio" 
description = "" 
weight = 16657 
+++

Aspose.Cells for .NET : Working with Visual Studio  

# Aspose.Cells for .NET : Working with Visual Studio


This topic explains how to use Aspose.Cells.GridWeb in ASP.NET applications using Visual Studio.NET 2005. This topic is useful for the beginner-level developers working with Aspose.Cells.GridWeb.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Working with Aspose.Cells.GridWeb Using Visual Studio 2013](#WorkingwithVisualStudio-WorkingwithAspose.Cells.GridWebUsingVisualStudio2013)
    *   1.1 [Step 1: Creating New Web Site](#WorkingwithVisualStudio-Step1:CreatingNewWebSite)
    *   1.2 [Step 2: Checking Source & Design Views of a Web Page](#WorkingwithVisualStudio-Step2:CheckingSource&DesignViewsofaWebPage)
    *   1.3 [Step 3: Adding Aspose.Cells.GridWeb to Web Page](#WorkingwithVisualStudio-Step3:AddingAspose.Cells.GridWebtoWebPage)
    *   1.4 [Step 4: Change the <!DOCTYPE> tag](#WorkingwithVisualStudio-Step4:Changethe<!DOCTYPE>tag)
    *   1.5 [Step 5: Resizing Aspose.Cells.GridWeb Control](#WorkingwithVisualStudio-Step5:ResizingAspose.Cells.GridWebControl)
    *   1.6 [Step 6: Configuring the Properties of Aspose.Cells.GridWeb](#WorkingwithVisualStudio-Step6:ConfiguringthePropertiesofAspose.Cells.GridWeb)
    *   1.7 [Step 7: Running Your First Web Site Containing Aspose.Cells.GridWeb](#WorkingwithVisualStudio-Step7:RunningYourFirstWebSiteContainingAspose.Cells.GridWeb)
{{< /panel >}}
## Working with Aspose.Cells.GridWeb Using Visual Studio 2013

This topic shows how to use Aspose.Cells.GridWeb by making a sample website in Visual Studio 2013. The process has been divided into steps.

### Step 1: Creating New Web Site

1.  Open Visual Studio 2013.
2.  From the **File** menu, select **New Menu**, then **Web Site**.  
      
    ![](https://docs2.aspose.com/cells/net/attachments/5013734/5115368.png)  
    The New Web Site dialog is opened.
3.  Select **ASP.NET Web Forms Site** from Visual Studio installed templates.
4.  Choose HTTP mode for the location of the web site.  
      
    ![](https://docs2.aspose.com/cells/net/attachments/5013734/5115367.png)  
      
    
5.  Specify a location where the web site files will be created and stored.
    1.  Click **Browse** in the New Web Site dialog.  
          
        ![](https://docs2.aspose.com/cells/net/attachments/5013734/5115298.png)  
          
        The Choose Location dialog is displayed.
    2.  Click the **Local IIS** tab.  
        All folders and web applications stored in your IIS root folder are displayed (for example: C:\\Inetpub\\wwwroot).  
          
        ![](https://docs2.aspose.com/cells/net/attachments/5013734/5115294.png)  
          
        
    3.  Now create a new web application in your local IIS where the website files will be stored.  
        The Choose Location dialog lets you create and delete web applications or virtual directories in your local IIS. To create a web application, click a button as shown below in the figure.  
          
        ![](https://docs2.aspose.com/cells/net/attachments/5013734/5115293.png)  
          
        A new web application with the default name WebSite is created.
    4.  Rename the web application. We renamed it GridWebOn2013.
    5.  Click **Open**.  
          
        ![](https://docs2.aspose.com/cells/net/attachments/5013734/5115304.png)  
          
        You return to the New Web Site dialog. The path of web site location is set to [http://localhost/GridWebOn2013](http://localhost/GridWebOn2013).
6.  Click **OK** to let Visual Studio create a web site.  
      
    ![](https://docs2.aspose.com/cells/net/attachments/5013734/5115303.png)

### Step 2: Checking Source & Design Views of a Web Page

A default web site will have been created by Visual Studio 2013. It contains a default.aspx web page with some dummy text and markup.  
  
**Source view of default.aspx page**  
![](https://docs2.aspose.com/cells/net/attachments/5013734/5115306.png)  
  
All web pages (including ASP.NET) can be opened in two modes. One is the source view that lets developers access and modify the source code. The second mode is design view that can be used to design web pages in a WYSIWYG manner. The above screenshot shows a source view of default.aspx web page. To view the design view, click **Design**.  
  
**Design view of default.aspx page**  
![](https://docs2.aspose.com/cells/net/attachments/5013734/5115305.png)  
  

Delete the Default.aspx page added by Visual Studio and add a new blank Default.aspx page.

![](https://docs2.aspose.com/cells/net/attachments/5013734/5115300.png)

### Step 3: Adding Aspose.Cells.GridWeb to Web Page

You can simply add Aspose.Cells.GridWeb (or GridWeb) control to a web page by dragging it from the toolbox.  
  
![](https://docs2.aspose.com/cells/net/attachments/5013734/5115299.png)  
  

If you don't know about how to add Aspose.Cells.GridWeb to the toolbox, refer to [Integrate Aspose.Cells Grid Controls with Visual Studio.NET](https://docs2.aspose.com/cells/net/gettingstarted/asposecellsgridsuiteandvsnet/integrate+aspose.cells+grid+controls+with+visual+studio.net).

Once GridWeb control is dropped to web page, it would render like this:  
  
![](https://docs2.aspose.com/cells/net/attachments/5013734/5115302.png)  
  

### Step 4: Change the <!DOCTYPE> tag

1.  Switch to source view and find the following **<!DOCTYPE>** tag in the source code:
    
    **ASP.NET**
    
{{< code lang="cs" >}}
 
<!DOCTYPE html>
 
{{< /code >}}
    
2.  Select the complete tag.  
      
    ![](https://docs2.aspose.com/cells/net/attachments/5013734/5115301.png)  
      
    
3.  Retain, change or delete the <!DOCTYPE> tag.
4.  Or modify the <!DOCTYPE> tag with the following one:
    
{{< code lang="cs" >}}
 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
 
{{< /code >}}
    

### Step 5: Resizing Aspose.Cells.GridWeb Control

You can change the width and height of the GridWeb control after dragging it to the website.

In design view, you can resize the width and height of the GridWeb.  
  
![](https://docs2.aspose.com/cells/net/attachments/5013734/5115312.png)  
  

### Step 6: Configuring the Properties of Aspose.Cells.GridWeb

Configure the Aspose.Cells.GridWeb properties in WYSIWYG by clicking the **Properties** button on the right side of Visual Studio 2013 IDE.  
A Properties dialog is displayed.  
  
![](https://docs2.aspose.com/cells/net/attachments/5013734/5115314.png)  
  
The Properties pane makes it possible to configure the look & feel of the GridWeb and some other properties to control GridWeb's behaviour.

### Step 7: Running Your First Web Site Containing Aspose.Cells.GridWeb

Build and run the web site.

1.  Run the web site directly from Visual Studio by pressing Ctrl+F5 or clicking **Start Debugging**.  
      
    ![](https://docs2.aspose.com/cells/net/attachments/5013734/5115313.png)

Now, you can start playing with GridWeb control.  
  
**GridWeb control in action**  
![](https://docs2.aspose.com/cells/net/attachments/5013734/5115276.png)

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-001.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115420.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-002.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115421.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-003.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115422.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-004.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115415.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-005.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115416.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-006.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115417.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-007.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115418.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-008.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115476.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-009.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115475.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-010.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115474.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-011.png.jpg](https://docs2.aspose.com/cells/net/attachments/5013734/5115473.jpg) (image/jpeg)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-012.png.jpg](https://docs2.aspose.com/cells/net/attachments/5013734/5115480.jpg) (image/jpeg)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-013.png.jpg](https://docs2.aspose.com/cells/net/attachments/5013734/5115479.jpg) (image/jpeg)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-014.png.jpg](https://docs2.aspose.com/cells/net/attachments/5013734/5115478.jpg) (image/jpeg)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-015.png.jpg](https://docs2.aspose.com/cells/net/attachments/5013734/5115477.jpg) (image/jpeg)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-016.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115484.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working With VS.NET 2005 VWD 2005-017.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115483.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-001.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115366.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-002.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115295.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-001.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115373.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-001.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115372.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-001.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115371.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-001.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115370.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-001.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115296.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-001.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115297.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-002.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115292.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-003.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115291.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-001.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115368.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-002.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115309.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-003.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115310.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-004.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115294.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-005.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115293.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-006.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115304.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-007.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115303.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-008.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115319.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-009.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115320.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-010.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115321.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-011.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115322.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-012.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115318.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-013.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115311.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-013.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115307.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-014.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115308.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-016.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115277.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-015.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115278.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-013.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115315.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-014.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115279.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-002.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115367.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-003.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115298.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-008.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115306.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-009.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115305.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-010.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115316.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-011.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115317.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-013.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115280.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-010.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115300.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-011.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115299.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-012.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115302.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-013.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115301.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-014.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115312.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-015.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115314.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-016.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115313.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Working with Visual Studio-017.png](https://docs2.aspose.com/cells/net/attachments/5013734/5115276.png) (image/png)  

