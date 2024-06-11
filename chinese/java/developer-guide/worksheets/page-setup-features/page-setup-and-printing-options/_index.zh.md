---
title: 页面设置和打印选项
type: docs
weight: 10
url: /zh/java/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

有时，开发人员需要配置页面设置和打印设置以控制打印过程。页面设置和打印设置提供各种选项，并且在Aspose.Cells中得到充分支持。

本文演示如何创建控制台应用程序，并使用Aspose.Cells API的几行简单代码应用页面设置和打印选项到工作表。

{{% /alert %}}

## **处理页面和打印设置**

在本示例中，我们在Microsoft Excel中创建了一个工作簿，并使用Aspose.Cells来设置页面设置和打印选项。

### **设置页面设置选项**

首先在Microsoft Excel中创建一个简单的工作表。然后将页面设置选项应用于它。执行代码将更改页面设置选项，如下面的屏幕截图所示。

**输出文件** 

![todo:image_alt_text](page-setup-and-printing-options_1.png)

1. 在Microsoft Excel中创建一个带有一些数据的工作表：
   1. 在Microsoft Excel中打开一个新的工作簿。
   1. 添加一些数据。
      以下是文件的屏幕截图。

      输入文件

![todo:image_alt_text](page-setup-and-printing-options_2.png)

1. 设置页面设置选项：
   将页面设置选项应用于文件。以下是应用新选项之前的默认选项的屏幕截图。

   默认页面设置选项

![todo:image_alt_text](page-setup-and-printing-options_3.png)

1. 下载并安装 Aspose.Cells：
   1. [下载](https://downloads.aspose.com/cells/java) Aspose.Cells for Java。
   1. 在开发计算机上解压缩。
      所有 [Aspose](http://www.aspose.com/) 组件在安装后都是以评估模式运行。 评估模式没有时间限制，只会在生成的文档中添加水印。
1. 创建一个项目。
   可以使用 Java 编辑器（例如 Eclipse）创建项目，也可以使用文本编辑器创建简单的程序。
1. 添加一个类路径。
   1. 从 Aspose.Cells.zip 中提取 Aspose.Cells.jar 和 dom4j_1.6.1.jar。
   1. 在 Eclipse 的项目中设置类路径：
   在 Eclipse 中选择您的项目，然后单击 **Project**，接着单击 **Properties**。
   在对话框的左侧选择 **Java Build Path**。
   选择 Libraries 选项卡，单击 **Add JARs** 或 **Add External JARs** 以选择 Aspose.Cells.jar 和 dom4j_1.6.1.jar，并将它们添加到构建路径中。
      或者，您也可以在 Windows 的 DOS 提示符处在运行时进行设置：

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1.编写调用API的应用程序:
   以下是此示例中组件使用的代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

### **设置打印选项**

页面设置还提供了几个打印选项(也称为工作表选项)，允许用户控制工作表页面的打印方式。它们允许用户:

- 选择工作表的特定打印区域。
- 打印标题。
- 打印网格线。
- 打印行/列标题。
- 获得草稿质量。
- 打印注释。
- 打印单元格错误。
- 定义页面排序。

下面的示例将打印选项应用于上面示例中创建的文件(PageSetup.xls)。下面的屏幕截图显示了应用新选项之前的默认打印选项。
**输入文档**

![todo:image_alt_text](page-setup-and-printing-options_4.png)

执行代码会更改打印选项。
**输出文件**

![todo:image_alt_text](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **摘要**

{{% alert color="primary" %}}

本文介绍了如何使用Aspose.Cells设置页面设置和工作表打印选项。希望它能给您一些启示，并且您可以在自己的场景中使用这些选项。

Aspose.Cells受益于多年的研究、设计和精心调优。我们诚挚地欢迎您在[Aspose.Cells论坛](https://forum.aspose.com/c/cells/9)上提出疑问、评论和建议。我们保证会及时回复。

{{% /alert %}}
