---
title: 页面设置和打印选项
type: docs
weight: 10
url: /zh/java/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

有时，开发人员需要配置页面设置和打印设置来控制打印过程。页面设置和打印设置提供各种选项，并在 Aspose.Cells 中得到完全支持。

本文介绍如何使用 Aspose.Cells API 通过几行简单的代码创建控制台应用程序并将页面设置和打印选项应用于工作表。

{{% /alert %}}

## **使用页面和打印设置**

对于此示例，我们在 Microsoft Excel 中创建了一个工作簿，并使用 Aspose.Cells 设置页面设置和打印选项。

### **设置页面设置选项**

首先在 Microsoft Excel 中创建一个简单的工作表。然后对其应用页面设置选项。执行代码会更改页面设置选项，如下面的屏幕截图所示。

**输出文件** 

![待办事项：图像_替代_文本](page-setup-and-printing-options_1.png)

1. 在 Microsoft Excel 中创建包含一些数据的工作表：
 1.在Microsoft Excel中打开一个新的工作簿。
 1.添加一些数据。
下面是该文件的屏幕截图。

      **输入文件**

![待办事项：图像_替代_文本](page-setup-and-printing-options_2.png)

1. 设置页面设置选项：
将页面设置选项应用于文件。下面是默认选项的屏幕截图，在应用新选项之前。

   **默认页面设置选项**

![待办事项：图像_替代_文本](page-setup-and-printing-options_3.png)

1. 下载并安装 Aspose.Cells：
   1. [下载](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
1. 在您的开发计算机上解压它。
全部[Aspose](http://www.aspose.com/)组件在安装后以评估模式工作。评估模式没有时间限制，它只在生成的文档中注入水印。
1. 创建一个项目。
使用 Java 编辑器（例如 Eclipse）创建一个项目，或者使用文本编辑器创建一个简单的程序。
1. 添加类路径。
1. 从 Aspose.Cells.zip 中提取 Aspose.Cells.jar 和 dom4j_1.6.1.jar。
 1、在Eclipse中设置项目的类路径：
 1.在Eclipse中选择你的项目然后点击**项目**其次是**特性**.
1. 选择**Java 构建路径**在对话框的左侧。
 1. 选择库选项卡，单击**添加 JAR**或者**添加外部 JAR**选择 Aspose.Cells.jar 和 dom4j_1.6.1.jar 并将它们添加到构建路径中。
或者您可以在运行时在 DOS 提示符下在 Windows 中设置它：

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. 编写调用 API 的应用程序：
以下是此示例中组件使用的代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

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
**输入文档**

![待办事项：图像_替代_文本](page-setup-and-printing-options_4.png)

执行代码会更改打印选项。
**输出文件**

![待办事项：图像_替代_文本](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **概括**

{{% alert color="primary" %}}

本文介绍如何使用 Aspose.Cells 设置页面设置和工作表打印选项。希望它能给您一些见解，并且您可以在自己的场景中使用这些选项。

 Aspose.Cells 得益于多年的研究、设计和精心调整。我们热忱欢迎您的查询、意见和建议[Aspose.Cells论坛](https://forum.aspose.com/c/cells/9).我们保证及时回复。

{{% /alert %}}
