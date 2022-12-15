---
title: 启用 GridWeb 编辑框
type: docs
weight: 110
url: /zh/net/enable-gridweb-editbox/
---
{{% alert color="primary" %}} 

GridWeb 的编辑框是一个呈现在控件顶部的工具栏，您可以使用它来查看/输入或将数据/公式复制到单元格中。它还显示您正在编辑的单元格的名称。单击框架后或开始写入数据或键入等号 (=) 时，将激活编辑框。

{{% /alert %}} 
## **设置Aspose.Cells.GridWeb的编辑框**
GridWeb 控件提供了 ShowCellEditBox 属性，开发人员可以将其指定为“True”以启用工具栏。该属性的默认值为 False。当您将其值设置为“True”时，编辑框将出现在 GridWeb 控件的顶部。

{{% alert color="primary" %}} 

要启用此功能，您需要将“jquery.js”文件导入您的项目并在您的 .aspx 页面中引用它以使其工作。您可以从下载 jQuery 存档<https://jqueryui.com/download/all/>并将库文件放入项目中的某个文件夹中，并通过添加对库文件的引用<script>在您的 .aspx 网络表单中标记如下。所有最新的 jQuery 版本都可以。

{{< highlight "csharp" >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**带有编辑框的 GridWeb 控件** 

![待办事项：图像_替代_文本](enable-gridweb-editbox_1.png)
### **例子**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
