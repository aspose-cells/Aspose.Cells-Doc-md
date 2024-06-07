---
title: 使用通用按钮提交Grid数据
type: docs
weight: 20
url: /zh/net/aspose-cells-gridweb/using-a-common-button-to-submit-grid-data/
keywords: GridWeb，提交，按钮，自定义
description: 本文介绍了在GridWeb中使用提交按钮的方法。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb提供了一些内置命令按钮，如**提交**和**保存**。使用这些按钮执行相关任务。

本文演示了如何不仅通过点击GridWeb内置的**保存**命令按钮，而且通过点击一个常用的ASP.NET按钮（Web控件）来提交数据到服务器。本文的目的是展示Aspose.Cells.GridWeb的灵活性。此外，本文还使用Aspose.Cells.GridWeb在客户端脚本中公开的特殊函数。

{{% /alert %}} 
## **使用ASP.NET按钮提交Grid数据**
Aspose.Cells.GridWeb提供了三个内置按钮（**提交**、**保存**和**撤销**）。在GridWeb中编辑后，用户可以点击标签栏中的**提交**或**保存**按钮，让GridWeb将数据提交到服务器。如果用户点击工作表选项卡，GridWeb控件执行与内置命令按钮相同的任务。Aspose.Cells.GridWeb还支持将此功能添加到常用的ASP.NET按钮控件中，但您需要在应用程序中添加一些额外的代码。
### **1. 创建测试应用程序**
打开Visual Studio.NET IDE，创建一个新的ASP.NET Web应用程序项目。创建完应用程序后，将自动向您的项目中添加一个默认的WebForm1.aspx页面。从工具箱中将GridWeb控件拖放到Web表单中。如果在工具箱中找不到GridWeb控件，请参考此页面：[将Aspose.Cells Grid控件与Visual Studio.NET集成](/cells/zh/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/)以了解更多信息。在将GridWeb控件添加到Web表单后，还可以从工具箱中将一个Button Web控件添加到Web表单中。
### **2. 向Page_Load事件添加代码**
现在，是时候向Web表单的Page_Load事件中添加一些代码了。您可以在设计视图中双击Web表单，VS.NET IDE将自动将您带到Page_Load事件处理程序，您需要在其中使用Button的Attributes集合来覆盖其OnClick事件。

{{% alert color="primary" %}} 

ASP.NET Button控件是一个服务器端控件。当点击时，将触发一个服务器端事件，但如果您想使用此Button控件在客户端执行一些代码（通常使用javascript），则需要修改它在Page_Load事件下的onclick属性。Aspose.Cells.GridWeb提供了一些可以在javascript中调用的函数来处理来自客户端的GridWeb控件。在下面的示例中，我们使用了GridWeb的updateData和validateAll函数（这些是客户端函数）来更新和验证Grid数据。

{{% /alert %}} 
#### **代码示例**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. 运行应用程序**
现在，您可以按Ctrl+F5编译和运行应用程序，页面将在新的浏览器窗口中打开。让我们向GridWeb添加一些值，然后点击提交Grid数据到服务器按钮，您将看到发生了一个回发以更新和验证GridWeb数据。
## **结论**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb为从服务器端或客户端使用GridWeb控件提供了很大的灵活性。开发人员有多种选项可以在不同的场景中使用GridWeb控件，为其客户提供更好的解决方案。

{{% /alert %}}
