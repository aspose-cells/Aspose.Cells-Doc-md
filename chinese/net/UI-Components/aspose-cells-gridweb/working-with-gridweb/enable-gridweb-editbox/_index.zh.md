---
title: 启用GridWebEditBox
type: docs
weight: 110
url: /zh/net/aspose-cells-gridweb/enable-gridweb-editbox/
keywords: GridWeb，editbox，公式栏
description: 本文介绍了如何在GridWeb中使用公式栏或编辑框。
---

{{% alert color="primary" %}} 

GridWeb的编辑框（在Excel中称为公式栏）是一个工具栏，渲染在控件顶部，您可以使用它来显示或输入值或复制数据/公式到焦点单元格。它还显示您正在编辑的单元格名称。单击框架或开始输入数据或输入等于(=)符号后，编辑框将被激活。

{{% /alert %}} 
## **设置Aspose.Cells.GridWeb的编辑框**
GridWeb控件提供ShowCellEditBox属性，开发人员可以将其分配为"True"以激活工具栏。该属性的默认值为False。当将其值设置为"True"时，编辑框将出现在GridWeb控件顶部。

{{% alert color="primary" %}} 

To enable this feature, you need to import "jquery.js" file to your project and refer it in your .aspx page(s) to make it work. You may download the jQuery archive from <https://jqueryui.com/download/all/> and put the library file(s) into some folder in the project and add reference to the library file via <script> tag in your .aspx web form as following. All the latest jQuery versions are OK.

{{< highlight csharp >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**带编辑框的GridWeb控件** 

![todo:image_alt_text](enable-gridweb-editbox_1.png)
### **例子**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
