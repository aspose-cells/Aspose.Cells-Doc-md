---
title: 页面设置和打印选项
type: docs
weight: 10
url: /zh/java/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

有时，开发人员需要配置页面设置和打印设置来控制打印过程。页面设置和打印设置提供各种选项，并在Aspose.Cells中得到充分支持。

本文展示如何创建一个控制台应用程序，并利用Aspose.Cells API的几行简单代码对工作表应用页面设置和打印选项。

{{% /alert %}}

## **使用页面和打印设置**

在这个示例中，我们在Microsoft Excel中创建了一个工作簿，并使用Aspose.Cells来设置页面设置和打印选项。

### **设置页面设置选项**

首先在Microsoft Excel中创建一个简单的工作表，然后应用页面设置选项。执行代码会更改页面设置选项，如下面的屏幕截图所示。

**输出文件** 

![todo:image_alt_text](page-setup-and-printing-options_1.png)

1. 在Microsoft Excel中创建带有一些数据的工作表:
   1. 在Microsoft Excel中打开一个新的工作簿。
   1. 添加一些数据。
      以下是文件的屏幕截图。

      **输入文件**

![todo:image_alt_text](page-setup-and-printing-options_2.png)

1. 设置页面设置选项:
   将页面设置选项应用于文件。下面是默认选项的屏幕截图，在应用新选项之前。

   **默认页面设置选项**

![todo:image_alt_text](page-setup-and-printing-options_3.png)

1. 下载并安装Aspose.Cells:
   1. [下载](https://downloads.aspose.com/cells/java) Aspose.Cells for Java。
   1. 在开发计算机上解压缩。
      所有[Aspose](http://www.aspose.com/)组件在安装后均以评估模式运行。评估模式没有时间限制，只会将水印注入生成的文档中。
1. 创建一个项目。
   使用Java编辑器（例如Eclipse）创建项目，或使用文本编辑器创建一个简单的程序。
1. 添加类路径。
   1. 从Aspose.Cells.zip中提取Aspose.Cells.jar和dom4j_1.6.1.jar。
   1. 在Eclipse中设置项目的类路径:
   在Eclipse中选择您的项目，然后单击**项目**，接着单击**属性**。
   选择对话框左侧的**Java构建路径**。
   选择库选项卡，单击**添加JARs**或**添加外部JARs**以选择Aspose.Cells.jar和dom4j_1.6.1.jar并将它们添加到构建路径。
      或者，您可以在Windows的DOS提示符下在运行时进行设置：

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. 编写调用API的应用程序：
   以下是本示例中组件使用的代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

### **设置打印选项**

页面设置还提供几种打印选项(也称为工作表选项)，允许用户控制如何打印工作表页。它们允许用户:

- 选择要打印的工作表区域。
- 打印标题。
- 打印网格线。
- 打印行/列标题。
- 实现草稿质量。
- 打印注释。
- 打印单元格错误。
- 定义页面排序。

下面的示例将打印选项应用于上面示例中创建的文件（PageSetup.xls）。 下面的屏幕截图显示在应用新选项之前的默认打印选项。
**输入文档**

![todo:image_alt_text](page-setup-and-printing-options_4.png)

执行代码会更改打印选项。
**输出文件**

![todo:image_alt_text](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **摘要**

{{% alert color="primary" %}}

本文展示如何使用Aspose.Cells设置页面设置和工作表打印选项。希望它能为您提供一些见解，并且您可以在自己的场景中使用这些选项。

Aspose.Cells经过多年的研究、设计和仔细调整。我们诚挚欢迎您在[Aspose.Cells论坛](https://forum.aspose.com/c/cells/9)上提出查询、评论和建议。我们将会及时回复。

{{% /alert %}}
