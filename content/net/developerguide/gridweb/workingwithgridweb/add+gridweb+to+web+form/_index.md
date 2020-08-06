---
title : "Add GridWeb to Web Form" 
description : "" 
weight : 16660 
toc : false
type: docs
url: /net/developerguide/gridweb/workingwithgridweb/add+gridweb+to+web+form/
---

# Aspose.Cells for .NET : Add GridWeb to Web Form


This topic provides a basic step by step guide for beginners to help them create and use the Aspose.Cells.GridWeb control in web applications.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Creating & Using Aspose.Cells.GridWeb Control](#creating-&-using-aspose.cells.gridweb-control)
    *   1.1 [Step 1: Creating a Web Application Project](#step-1:-creating-a-web-application-project)
    *   1.2 [Step 2: Embedding Control to the Web Form](#step-2:-embedding-control-to-the-web-form)
    *   1.3 [Step 3: Resizing Control](#step-3:-resizing-control)
    *   1.4 [Step 4: Setting Control Properties](#step-4:-setting-control-properties)
        *   1.4.1 [Custom Command Buttons](#custom-command-buttons)
    *   1.5 [Important](#important)
    *   1.6 [Step 5: Running Web Application](#step-5:-running-web-application)
{{< /panel >}}
 

## Creating & Using Aspose.Cells.GridWeb Control

### Step 1: Creating a Web Application Project

First, create a web application project in which to use the Aspose.Cells.GridWeb control:

1.  Open Visual Studio.
2.  From the **File** menu, select **New** followed by **Project**.  
      
    ![image](5115093.png)  
      
    A New Project Dialog appears.
3.  Select **ASP.NET Web Application** for desired language.  
      
    ![image](5115094.png)
4.  Select **Web Forms** template.  
      
    ![image](5115095.png)
5.  Add a new web form to the project.

### Step 2: Embedding Control to the Web Form

Drag and drop the Aspose.Cells.GridWeb control from the Visual Studio toolbox to the web form.  
  
![image](5115096.png)

To learn how to add Aspose.Cells Grid controls to the Visual Studio Toolbox, please read [Integrate Aspose.Cells.Grid Controls with Visual Studio.NET](https://docs2.aspose.com/cells/net/gettingstarted/gridsuiteandvsnet/integrate+aspose.cells+grid+controls+with+visual+studio.net).

When the control has been added to the form, it is rendered like this:  
  
![image](5115097.png)

### Step 3: Resizing Control

The form is rendered at a default size. Adjust the size by dragging the borders or corners.  
  
![image](5115098.png)

### Step 4: Setting Control Properties

Aspose.Cells.GridWeb control can also be configured using various properties.  
  
![image](5115099.png)

It is possible to adjust many properties of the control with the Properties dialog. Basic properties include height, width, color and visual styles. Advanced properties include the edit mode, session mode and double-click mode. Moreover, it is possible to set customized event handlers in the Properties dialog.

There are also some extra configuration tools for Aspose.Cells.GridWeb that can be seen at the bottom of the Properties dialog as hyperlinks, or right\_click on the GridWeb control to find them. These configuration tools include:

*   Custom Command Buttons

#### Custom Command Buttons

To open the custom command buttons editor:  
Right-click the GridWeb control and select **Custom Command Buttons**.  
  
![image](5115102.png)  
  
The CustomCommandButton Collection Editor dialog os displayed.  
  
![image](5115103.png)

The dialog lets developers add and remove custom command buttons in the GridWeb control.

### Important

Aspose.Cells.GridWeb also provides its resource files with the control. The "acw\_client" is a folder (@ your installation directory) that contains files and Aspose.Cells.GridWeb uses this folder to manage its internal configuration and other functionality, it has scripts files, image files and other files to specify GridWeb's behavior and set other operations. The config file is used to manage the embedded client resources (images, scripts, etc.). Moreover, when you need to deploy the web application having GridWeb control, you would also copy the "acw\_client" directory into your project folder least your web application (deployed over the server) could not find it. You can always specify the resource folder by adding the following lines of code into the configuration section (e.g in the web.config file in your VS.NET Project):

{{< code lang="cs" >}}
<appSettings>
  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> 
</appSettings>
{{< /code >}}

The path is always related to the project's directory. You should not use any directory which is outside of the project's directory. So it is necessary to copy the "acw\_client" directory (@ your GridWeb installation folder) into the project's directory/sub-directory.

### Step 5: Running Web Application

Run the application by pressing Ctrl+F5 or clicking the **Start** button.  
  
When the application runs in a browser, the WebForm1.aspx page is displayed, now containing an empty Aspose.Cells.GridWeb control. Add values to cells by clicking them. It is also possible to perform other tasks like changing the height of a row or the width of a column, copying (Ctrl+C) or cutting (Ctrl+X) cell data to the clipboard and pasting (Ctrl+V) data to cell. To performing more operations, right-click the control to see full list of options.  
  
**Context menu of GridWeb control**  
![image](5115122.png)

