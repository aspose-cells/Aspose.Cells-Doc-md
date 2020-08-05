---
title : "Manage Hyperlinks in Worksheet" 
description : "" 
weight : 16692 
toc : false
type: docs
url: /net/developerguide/gridweb/workingwithgridwebworksheets/manage+hyperlinks+in+worksheet/
---

# Aspose.Cells for .NET : Manage Hyperlinks in Worksheet


This topic discusses what types of hyperlinks are supported in Aspose.Cells.GridWeb and how to manage them programmatically. Hyperlinks can be used for either creating links to web URLs or to perform postback to a server.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Working with Hyperlinks](#working-with-hyperlinks)
    *   1.1 [Types of Hyperlinks](#types-of-hyperlinks)
    *   1.2 [Adding Hyperlinks](#adding-hyperlinks)
        *   1.2.1 [URL Hyperlinks](#url-hyperlinks)
            *   1.2.1.1 [Text Hyperlinks](#text-hyperlinks)
            *   1.2.1.2 [Image Hyperlinks](#image-hyperlinks)
        *   1.2.2 [Cell Command Hyperlinks](#cell-command-hyperlinks)
            *   1.2.2.1 [Event Handling of Cell Command Hyperlinks](#event-handling-of-cell-command-hyperlinks)
    *   1.3 [Accessing Hyperlinks](#accessing-hyperlinks)
    *   1.4 [Removing Hyperlinks](#removing-hyperlinks)
{{< /panel >}}
 

## Working with Hyperlinks

### Types of Hyperlinks

Generally,the following hyperlinks are supported by Aspose.Cells.GridWeb:

*   [URL hyperlinks](https://docs2.aspose.com/cells/net/developerguide/gridweb/workingwithgridwebworksheets/manage+hyperlinks+in+worksheet), hyperlinks that can be linked to web URLs.
*   [Text hyperlinks](https://docs2.aspose.com/cells/net/developerguide/gridweb/workingwithgridwebworksheets/manage+hyperlinks+in+worksheet), URL hyperlinks applied to text.
*   [Image hyperlinks](https://docs2.aspose.com/cells/net/developerguide/gridweb/workingwithgridwebworksheets/manage+hyperlinks+in+worksheet), URL hyperlinks applied to images.
*   [Cell command hyperlinks](https://docs2.aspose.com/cells/net/developerguide/gridweb/workingwithgridwebworksheets/manage+hyperlinks+in+worksheet), hyperlinks that post data to a server. Such hyperlinks act more like a button that triggers a server-side event when clicked.

The below sections describe the use of all types of hyperlinks in detail. It also discusses how to access or remove links.

### Adding Hyperlinks

#### URL Hyperlinks

URL hyperlinks look more like simple hyperlinks that you normally see on websites. A URL hyperlink works like an anchor in a cell. Whenever it is clicked, it navigates to a web page or opens a new browser window.

There are different types of URL hyperlinks:

*   Text hyperlinks.
*   Image hyperlinks.

Developers can specify an image for the hyperlink. If an image isn't specified, a text hyperlink is created; else an image hyperlink is created.

##### Text Hyperlinks

To add a text hyperlink to a worksheet:

1.  Add the Aspose.Cells.GridWeb control to your Web Form.
2.  Access a worksheet.
3.  Add a hyperlink to a cell in the worksheet.
4.  Set the text that will be shown in the cell.
5.  Set the hyperlink's URL.
6.  Set the hyperlink's target,if desired.
7.  Set a tool tip, if desired.

NOTE: The hyperlink target can be set to \_self, \_top or \_parent for opening web URLs in a new, the current or the top window respectively.

The example below adds two hyperlinks to a worksheet. One has no target while the other is set to \_parent.

**Output: text hyperlinks added to worksheet**  
![image](https://docs2.aspose.com/cells/net/attachments/5013773/5115385.png)

##### Image Hyperlinks

To add an image hyperlink:

1.  Add the Aspose.Cells.GridWeb control to your Web Form.
2.  Access a worksheet.
3.  Add a hyperlink to a cell.
4.  Set the URL of the image that will be displayed as hyperlink.
5.  Set the hyperlink URL.
6.  Set a tool tip, if desired.
7.  Set the hyperlink text, if desired.

**Output: image hyperlinks added to worksheet**  
![image](https://docs2.aspose.com/cells/net/attachments/5013773/5115386.png)

Setting the image hyperlink's AltText fills a similar function as setting an <ALT> tag in HTML. The text is displayed only if the hyperlinked image is not displayed. (For example, if the image isn't at the specified location.) If the image of the second hyperlink is not found, the output of the code snippet below would look as follows.

**The image for the image URL could not be found**  
![image](https://docs2.aspose.com/cells/net/attachments/5013773/5115387.png)

#### Cell Command Hyperlinks

A cell command hyperlink is a special type of hyperlink which triggers a server-side event instead of opening a web page. Developers can add code to the server-side event and perform any task when the hyperlink is clicked. This feature enables developers to create more interactive applications.

To add a cell command hyperlink:

1.  Add the Aspose.Cells.GridWeb control to your Web Form.
2.  Access a worksheet.
3.  Add a hyperlink to a cell.
4.  Set the hyperlink's `Command` to any desired value.  
    The value is used by the hyperlink's event handler to recognise it.
5.  Set a tool tip, if desired.
6.  Set the URL for the Image that will be displayed as a hyperlink.

**A cell command hyperlink has been added to worksheet**  
![image](https://docs2.aspose.com/cells/net/attachments/5013773/5115388.png)

##### Event Handling of Cell Command Hyperlinks

Developers need to create an event handler for the GridWeb control's `CellCommand` event to perform specific tasks when a specific cell command hyperlink is clicked. The `CellCommand` event's event handler provides an object of the `CellEventArgs` type that offers the `Argument` property. Use the `Argument` property to identify a specific hyperlink by comparing its `CellCommand` value.

The example below creates an event handler for the cell command hyperlink created in the code above. The hyperlink's `CellCommand` was set to `Click`. So, in the event handler, first check it and then add code which displays a message in the A6 cell.

The event handler is invoked when the hyperlink is clicked.

**Output: text added to A6 cell when hyperlink is clicked**  
![image](https://docs2.aspose.com/cells/net/attachments/5013773/5115389.png)

### Accessing Hyperlinks

To access an existing hyperlink:

1.  Access the cell that contains it.
2.  Get the cell reference.
3.  Pass the reference to the `Hyperlinks` collection's `GetHyperlink` method to access the hyperlink.
4.  Modify the hyperlink's properties.

### Removing Hyperlinks

To remove a hyperlink:

1.  Access the active worksheet.
2.  Remove a hyperlink using the `Hyperlinks` collection's `Remove` method.

