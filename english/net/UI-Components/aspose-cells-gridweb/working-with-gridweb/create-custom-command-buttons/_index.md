---
title: Create Custom Command Buttons
type: docs
weight: 100
url: /net/aspose-cells-gridweb/create-custom-command-buttons/
keywords: GridWeb,command,command buttons,custom
description: This article introduces how to custom command buttons in GridWeb.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb contains special buttons like **Submit**, **Save**, and **Undo**. All these buttons perform specific tasks for Aspose.Cells.GridWeb.  
It is also possible to add custom buttons that perform custom tasks. This topic explains how to use this feature.

{{% /alert %}} 

## **Creating Custom Command Buttons**
To create a custom command button in Aspose.Cells.GridWeb:

1. Add Aspose.Cells.GridWeb control to the web form.  
1. Access a worksheet.  
1. Create an instance of the `CustomCommandButton` class.  
1. Set the button's **Command** to some value. This value is used in the button's event handler.  
1. Set the button's text.  
1. Set the button's image URL.  
1. Finally, add the `CustomCommandButton` object to the `CustomCommandButtons` collection of the GridWeb control.

{{% alert color="primary" %}} 

Custom command buttons can also be added in WYSIWYG mode using Visual Studio's Properties dialog.

{{% /alert %}} 

The output of the code snippet is shown below:

**A custom command button added to GridWeb control** 

![todo:image_alt_text](create-custom-command-buttons_1.png)

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}

### **Event Handling of Custom Command Buttons**
The most important aspect of custom command buttons is the action they perform when clicked. To set the action, create an event handler for the GridWeb control's **CustomCommand** event.

The **CustomCommand** event is always triggered when a custom command button is clicked. Therefore, the event handler must identify the specific custom command button to which it applies, using the **Command** set when adding the button to the GridWeb control. Finally, add the custom code that is executed when the button is clicked.

In the code example below, a text message is added to cell **A1** when the button is clicked.

**Text added to A1 cell when custom command button is clicked** 

![todo:image_alt_text](create-custom-command-buttons_2.png)

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
