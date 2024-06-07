---
title: Aspose.Cells如何使用TrueType字体
type: docs
weight: 10
url: /zh/java/how-aspose-cells-uses-truetype-fonts/
---

{{% alert color="primary" %}}

Aspose.Cells在将电子表格呈现为PDF、XPS和图像等格式时需要TrueType字体。

当Aspose.Cells呈现电子表格时，需要访问电子表格中使用的TrueType字体。这在生成PDF、XPS和图像时是一种正常做法，并确保转换后的文档或图像在任何查看器中显示一致。

{{% /alert %}}

## **关于字体**

### **字体可用性和替换**

电子表格可能使用各种字体，如Arial、Times New Roman、Verdana等。Aspose.Cells在呈现电子表格时尝试选择电子表格中使用的字体。但是，在某些情况下，可能无法使用确切的字体，因此Aspose.Cells必须替换类似的字体。

以下是Aspose.Cells在幕后执行的过程。

1. Aspose.Cells尝试在文件系统上查找与电子表格中使用的确切字体名匹配的字体。
2. 如果Aspose.Cells找不到确切相同名称的字体，则尝试使用工作簿DefaultStyle.Font属性下指定的默认字体。
3. 如果Aspose.Cells无法找到工作簿DefaultStyle.Font属性下定义的字体，它将尝试从所有可用字体中选择最合适的字体。
4. 最后，如果Aspose.Cells在文件系统中找不到任何字体，它将使用Arial呈现电子表格。

### **Aspose.Cells查找字体的位置**

Aspose.Cells尝试自动在文件系统上找到TrueType字体。大多数情况下，您可以依赖Aspose.Cell的默认行为来查找TrueType字体，但有时您可能需要使用FontConfigs.setFontFolder工厂方法指定包含TrueType字体的文件夹。

### **典型的字体相关问题及解决方案**

本表列出了使用Aspose.Cells将电子表格呈现为PDF时可能遇到的一些问题及其解决方案。

{{% alert color="primary" %}}

在复制任何字体时，请记住大多数字体都受版权保护。在分发之前，首先找到字体的许可证并验证它们可以自由转移到另一台机器。 

{{% /alert %}}

|**问题** |**原因** |**解决方案** |
| :- | :- | :- |
|呈现文档中的布局和字体与原始文档不同。|您正在Linux或Mac OS上使用Aspose.Cells，在这些操作系统上默认情况下没有TrueType字体，因此Aspose.Cells无法在计算机上找到字体。|从Windows机器上复制TrueType字体文件，或者安装TrueType字体包。使用FontConfigs.setFontFolder工厂方法指定字体文件的位置。|

{{% alert color="primary" %}}

查看详细文章

- [如何在Linux上放置TrueType字体](/cells/zh/java/how-to-install-truetype-fonts-on-linux/)
- [如何指定TrueType字体位置](/cells/zh/java/how-to-specify-truetype-fonts-location/)
- [在字体替换发生时如何获取警告](/cells/zh/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
