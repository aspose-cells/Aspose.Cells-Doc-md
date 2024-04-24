---
title: Using a Common Button to Submit Grid Data
type: docs
weight: 20
url: /net/aspose-cells-gridweb/using-a-common-button-to-submit-grid-data/
keywords: GridWeb,submit,button,custom
description: This article describes the use of submit button in GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb provides some built-in command buttons like **Submit** and **Save**. Use these buttons to perform related tasks.

This article shows how to submit data to a server not just by clicking GridWeb's built-in **Save** command button, but by clicking a common ASP.NET Button (Web Control). The purpose of this article is to show the flexibility of Aspose.Cells.GridWeb. Moreover, this article also uses special functions exposed by Aspose.Cells.GridWeb to be used in the client side script.

{{% /alert %}} 
## **Submitting Grid Data Using an ASP.NET Button**
Aspose.Cells.GridWeb provides three built-in buttons (**Submit**, **Save** and **Undo**). After editing in GridWeb, a user may click the **Submit** or **Save** button in the Tab Bar to let GridWeb submit data to the server. If the user clicks a Sheet Tab, the GridWeb control performs the same task as that of the built-in command buttons. Aspose.Cells.GridWeb also supports adding this functionality to a common ASP.NET Button control, but you need to add some extra code to the application.
### **1. Creating a Test Application**
Open your Visual Studio.NET IDE and create a new ASP.NET Web Application project. Once the application is created, a default WebForm1.aspx page will be added to your project. Drag & drop GridWeb control from your Toolbox to Web Form . If you can't find GridWeb control in your Toolbox then refer to this page: [Integrate Aspose.Cells Grid Controls with Visual Studio.NET](/cells/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/) to learn more about it.After the GridWeb control is added to your Web Form, also add a Button web control from Toolbox to your Web Form.
### **2. Adding Code to Page_Load Event**
Now, it's time to add some code to Page_Load event of the Web Form. You can double click on the Web Form in design view and VS.NET IDE will automatically take you to the Page_Load event handler where you would need to use Attributes collection of the Button for overriding its OnClick event.

{{% alert color="primary" %}} 

ASP.NET Button control is a server side control. Whenever it is clicked, a server side event is triggered but if you want to use this Button control to execute some code on client side (normally using javascript) then you need to modify it's onclick attribute under Page_Load event. Aspose.Cells.GridWeb provides some functions that can be invoked in javascript to deal with GridWeb control from client side. In the example below, we have used updateData & validateAll functions (which are client side funtions) of GridWeb to update and validate Grid data.

{{% /alert %}} 
#### **Code Example**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. Running the Application**
Now, you can compile and run your application by pressing Ctrl+F5 and page will be opened in a new browser window. Let's add some values to GridWeb and press Submit Grid Data to Server button and you would see occurring a postback to update and validate GridWeb data.
## **Conclusion**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb offers great flexibility for working with GridWeb controls from either server or client side. Developers have wide number of options to use GridWeb control in different kinds of scenarios to provide better solutions to their customers.

{{% /alert %}}
