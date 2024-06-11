---
title: 使用通用按钮提交 Grid 数据
type: docs
weight: 20
url: /zh/net/aspose-cells-gridweb/using-a-common-button-to-submit-grid-data/
keywords: GridWeb, 提交, 按钮, 自定义
description: 本文描述了在 GridWeb 中使用提交按钮的用法。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 提供了一些内置的命令按钮，比如**提交**和**保存**。使用这些按钮执行相关任务。

本文展示了如何通过单击 GridWeb 的内置**保存**命令按钮以外，还可以通过单击通用 ASP.NET 按钮（Web 控件）来向服务器提交数据。本文目的是展示 Aspose.Cells.GridWeb 的灵活性。此外，本文还使用了 Aspose.Cells.GridWeb 在客户端脚本中提供的特殊函数。

{{% /alert %}} 
## **使用 ASP.NET 按钮提交 Grid 数据**
Aspose.Cells.GridWeb 提供了三个内置按钮（**提交**、**保存**和**撤销**）。在 GridWeb 中进行编辑后，用户可以在选项卡栏中单击**提交**或**保存**按钮，让 GridWeb 提交数据到服务器。如果用户单击一个工作表标签，GridWeb 控件将执行与内置命令按钮相同的任务。Aspose.Cells.GridWeb 还支持将此功能添加到通用的 ASP.NET 按钮控件上，但您需要向应用程序添加一些额外的代码。
### **1. 创建一个测试应用程序**
打开 Visual Studio.NET IDE，并创建一个新的 ASP.NET Web Application 项目。创建完应用程序后，会添加一个默认的 WebForm1.aspx 页面到您的项目中。从工具箱中将 GridWeb 控件拖放到 Web Form 中。如果您在工具箱中找不到 GridWeb 控件，可以参考此页面：[将 Aspose.Cells Grid 控件集成到 Visual Studio.NET](/cells/zh/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/) 了解更多。在将 GridWeb 控件添加到 Web Form 后，还需从工具箱中将一个按钮 Web 控件拖放到 Web Form 中。
### **2. 在 Page_Load 事件中添加代码**
现在，可以在 Web Form 的设计视图中双击 Page_Load 事件，VS.NET IDE 将自动带您到 Page_Load 事件处理程序，您需要使用按钮的 Attributes 集合来重写其 OnClick 事件。

{{% alert color="primary" %}} 

ASP.NET 按钮控件是一个服务器端控件。每当单击它时，都会触发一个服务器端事件，但如果您想要使用此按钮控件在客户端执行一些代码（通常使用 javascript），则需要在 Page_Load 事件下修改其 onclick 属性。Aspose.Cells.GridWeb 提供一些函数，可以在 javascript 中调用，以便从客户端处理 GridWeb 控件。在下面的示例中，我们使用了 GridWeb 的 updateData & validateAll 函数（这些是客户端函数）来更新和验证 Grid 数据。

{{% /alert %}} 
#### **代码示例**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. 运行应用程序**
现在，您可以按 Ctrl+F5 编译和运行应用程序，页面将在新的浏览器窗口中打开。让我们向 GridWeb 添加一些值，然后单击提交 Grid 数据到服务器按钮，您会看到发生了一个 postback 以更新和验证 GridWeb 数据。
## **结论**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb提供了很大的灵活性，可以从服务器端或客户端来处理GridWeb控件。开发人员有很多选项来在不同的场景中使用GridWeb控件，为他们的客户提供更好的解决方案。

{{% /alert %}}
