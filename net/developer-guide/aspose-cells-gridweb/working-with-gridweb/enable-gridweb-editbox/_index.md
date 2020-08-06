---
title: Enable GridWeb EditBox
type: docs
weight: 110
url: /net/enable-gridweb-editbox/
---

{{% alert color="primary" %}} 

The GridWeb's Edit Box is a toolbar that is rendered at the top of control that you can use to see/enter or copy data/formula into cells. It also shows the cell's name which you are editing. After clicking the frame or when you start writing data or type an equal (=) symbol, the Edit Box will be activated.

{{% /alert %}} 
## **Setting the Edit Box of Aspose.Cells.GridWeb**
The GridWeb control provides the ShowCellEditBox property to which developers can assign it to "True" to make the toolbar on. The default value of the attribute is False. When you set its value to "True", the Edit Box will appear on the top of the GridWeb control.

{{% alert color="primary" %}} 

To enable this feature, you need to import "jquery.js" file to your project and refer it in your .aspx page(s) to make it work. You may download the jQuery archive from <https://jqueryui.com/download/all/> and put the library file(s) into some folder in the project and add reference to the library file via <script> tag in your .aspx web form as following. All the latest jQuery versions are OK.

{{< highlight csharp >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**GridWeb control with Edit Box** 

![todo:image_alt_text](enable-gridweb-editbox_1.png)
### **Example**


{{< gist "aspose-cells" "18f6c28b77ee30c773fb2199168e73ed" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
