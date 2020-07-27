+++
title = "Create Custom Command Buttons" 
description = "" 
weight = 16669 
+++

Aspose.Cells for .NET : Create Custom Command Buttons  

# Aspose.Cells for .NET : Create Custom Command Buttons


Aspose.Cells.GridWeb contains special buttons like **Submit**, **Save** and **Undo**. All these buttons perform specific tasks for Aspose.Cells.GridWeb.  
It is also possible to add custom buttons that performs custom tasks. This topic explains how to use this feature.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Creating Custom Command Buttons](#CreateCustomCommandButtons-CreatingCustomCommandButtons)
    *   1.1 [Event Handling of Custom Command Button](#CreateCustomCommandButtons-EventHandlingofCustomCommandButton)
{{< /panel >}}
 

## Creating Custom Command Buttons

To create a custom command button in Aspose.Cells.GridWeb:

1.  Add Aspose.Cells.GridWeb control to the web form.
2.  Access a worksheet.
3.  Create an instance of the `CustomCommandButton` class.
4.  Set button's `Command` to some value. This value is used in the button's event handler.
5.  Set the button's text.
6.  Set the button's image URL.
7.  Finally, add the `CustomCommandButton` object to the `CustomCommandButtons` collection of the GridWeb control.

Custom command buttons can also be added in WYSIWYG mode using Visual Studio's Properties dialog.

The output of code snippet is shown below:

**A custom command button added to GridWeb control**  
![](https://docs2.aspose.com/cells/net/attachments/5013753/5115333.png)

### Event Handling of Custom Command Button

The most important aspect of custom command buttons is the action they perform when clicked. To set the action, create an event handler for the GridWeb control's `CustomCommand` event.

The `CustomCommand` event is always triggered when a custom command button is clicked. So the event handler has to identify the specific custom command button that it applies to by the `Command` set when adding the button to the GridWib control. Finally, add custom code that is executed when the button is clicked.

In the code example below, a text message is added to the cell A1 when the button is clicked.

**Text added to A1 cell when custom command button is clicked**  
![](https://docs2.aspose.com/cells/net/attachments/5013753/5115334.png)

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Create Custom Command Buttons-001.png](https://docs2.aspose.com/cells/net/attachments/5013753/5115333.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Create Custom Command Buttons-002.png](https://docs2.aspose.com/cells/net/attachments/5013753/5115334.png) (image/png)  

