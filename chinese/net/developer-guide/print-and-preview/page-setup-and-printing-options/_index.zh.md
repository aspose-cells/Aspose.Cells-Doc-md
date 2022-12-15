---
title: 页面设置和打印选项
type: docs
weight: 60
url: /zh/net/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

有时，开发人员需要配置页面设置和打印设置来控制打印过程。页面设置和打印设置提供各种选项，并在 Aspose.Cells 中得到完全支持。

本文介绍如何在 Visual Studio.Net 中创建控制台应用程序，并使用 Aspose.Cells API 通过几行简单的代码将页面设置和打印选项应用于工作表。

{{% /alert %}}

## **使用页面和打印设置**

对于此示例，我们在 Microsoft Excel 中创建了一个工作簿，并使用 Aspose.Cells 设置页面设置和打印选项。

### **使用 Aspose.Cells 设置页面设置选项**

首先在 Microsoft Excel 中创建一个简单的工作表。然后对其应用页面设置选项。执行代码会更改页面设置选项，如下面的屏幕截图所示。

|**输出文件。**|
|:- |
|![待办事项：图像_替代_文本](page-setup-and-printing-options_1.png)|

1. 在 Microsoft Excel 中创建包含一些数据的工作表：
 1.在Microsoft Excel中打开一个新的工作簿。
 1.添加一些数据。
1. 设置页面设置选项：
将页面设置选项应用于文件。下面是默认选项的屏幕截图，在应用新选项之前。

|**默认页面设置选项。**|
|:- |
|![待办事项：图像_替代_文本](page-setup-and-printing-options_2.png)|

1. 下载并安装 Aspose.Cells：
   1. [下载](https://downloads.aspose.com/cells/net) .Net 的 Aspose.Cells。
 1. 在您的开发计算机上安装它。
所有 Aspose 组件在安装后都在评估模式下工作。评估模式没有时间限制，它只在生成的文档中注入水印。
1. 创建一个项目：
 1. 启动视觉工作室。网。
 1. 创建一个新的控制台应用程序。
此示例将显示 C# 控制台应用程序，但您也可以使用 VB.NET。
1. 添加参考资料：
 1. 此示例使用 Aspose.Cells，因此将对该组件的引用添加到项目中。例如：
 …\程序文件\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. 编写调用 API 的应用程序：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPageSetup-1.cs" >}}

### **设置打印选项**

页面设置设置还提供了几个打印选项（也称为工作表选项），允许用户控制工作表页面的打印方式。它们允许用户：

- 选择工作表的特定打印区域。
- 打印标题。
- 打印网格线。
- 打印行/列标题。
- 达到草稿质量。
- 打印评论。
- 打印单元错误。
- 定义页面排序。

下面的示例将打印选项应用于在上例中创建的文件 (PageSetup.xls)。下面的屏幕截图显示了应用新选项之前的默认打印选项。

|**输入文档**|
|:- |
|![待办事项：图像_替代_文本](page-setup-and-printing-options_3.png)|
执行代码会更改打印选项。

|**输出文件**|
|:- |
|![待办事项：图像_替代_文本](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PageSetupAndPrintingOptions-SettingPrintingOptions-1.cs" >}}
