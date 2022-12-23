---
title: 使用通用按钮提交网格数据
type: docs
weight: 20
url: /zh/net/using-a-common-button-to-submit-grid-data/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb提供了一些内置的命令按钮，如**提交**和**救球**.使用这些按钮执行相关任务。

本文展示了如何将数据提交到服务器，而不仅仅是通过点击 GridWeb 的内置**救球**命令按钮，但通过单击一个常见的 ASP.NET 按钮（Web 控件）。本文的目的是展示 Aspose.Cells.GridWeb 的灵活性。此外，本文还使用了 Aspose.Cells.GridWeb 公开的特殊功能，用于客户端脚本。

{{% /alert %}} 
## **使用 ASP.NET 按钮提交网格数据**
Aspose.Cells.GridWeb提供了三个内置按钮（**提交**, **救球**和**撤消** ).在 GridWeb 中编辑后，用户可以单击**提交**要么**救球**选项卡栏中的按钮让 GridWeb 向服务器提交数据。如果用户单击工作表选项卡，GridWeb 控件将执行与内置命令按钮相同的任务。 Aspose.Cells.GridWeb 也支持将此功能添加到一个常见的ASP.NET Button 控件中，但您需要在应用程序中添加一些额外的代码。
### **1. 创建测试应用**
打开 Visual Studio.NET IDE 并创建一个新的 ASP.NET Web 应用程序项目。创建应用程序后，默认的 WebForm1.aspx 页面将添加到您的项目中。将 GridWeb 控件从您的工具箱拖放到 Web 窗体。如果您在工具箱中找不到 GridWeb 控件，请参阅此页面：[将 Aspose.Cells 网格控件与 Visual Studio 集成 .NET](/cells/zh/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/)以了解更多信息。将 GridWeb 控件添加到您的 Web 窗体后，还将工具箱中的 Button Web 控件添加到您的 Web 窗体。
### **2. 添加代码到 Page_Load 事件**
现在，是时候向页面添加一些代码了_Web 窗体的加载事件。您可以在设计视图中双击 Web 窗体，VS.NET IDE 将自动带您进入页面_在需要使用 Button 的 Attributes 集合来覆盖其 OnClick 事件的地方加载事件处理程序。

{{% alert color="primary" %}} 

ASP.NET 按钮控件是服务器端控件。每当单击它时，都会触发服务器端事件，但如果您想使用此 Button 控件在客户端执行一些代码（通常使用 javascript），则需要修改它在 Page_Load 事件下的 onclick 属性。 Aspose.Cells.GridWeb 提供了一些可以在javascript 中调用的函数来从客户端处理GridWeb 控件。在下面的示例中，我们使用了 GridWeb 的 updateData 和 validateAll 函数（它们是客户端函数）来更新和验证网格数据。

{{% /alert %}} 
#### **代码示例**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3.运行应用程序**
现在，您可以按 Ctrl+F5 编译并运行您的应用程序，页面将在新的浏览器窗口中打开。让我们向 GridWeb 添加一些值并按下将网格数据提交到服务器按钮，您将看到发生回发以更新和验证 GridWeb 数据。
## **结论**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 为从服务器端或客户端使用 GridWeb 控件提供了极大的灵活性。开发人员有多种选择可以在不同类型的场景中使用 GridWeb 控件，从而为他们的客户提供更好的解决方案。

{{% /alert %}}
