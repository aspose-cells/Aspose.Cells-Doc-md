---
title: Aspose.Cells 如何使用 TrueType 字体
type: docs
weight: 10
url: /zh/java/how-aspose-cells-uses-truetype-fonts/
---
{{% alert color="primary" %}}

Aspose.Cells 在将电子表格呈现为 PDF、XPS 和图像等格式时需要 TrueType 字体。

当 Aspose.Cells 呈现电子表格时，它需要访问电子表格中使用的 TrueType 字体。这是 PDF、XPS 和图像生成过程中的正常做法，可确保转换后的文档或图像对任何查看者都相同。

{{% /alert %}}

## **关于字体**

### **字体可用性和替换**

可以使用各种字体格式化电子表格，例如 Arial、Times New Roman、Verdana 等。当 Aspose.Cells 呈现电子表格时，它会尝试选择电子表格中使用的字体。然而，在某些情况下可能无法使用确切的字体，因此 Aspose.Cells 必须使用类似的字体来代替。

下面是Aspose.Cells在幕后跟进的过程。

1. Aspose.Cells 尝试在文件系统上查找与电子表格中使用的确切字体名称匹配的字体。
1. 如果 Aspose.Cells 找不到名称完全相同的字体，它会尝试使用工作簿的 DefaultStyle.Font 属性下指定的默认字体。
1. 如果 Aspose.Cells 找不到工作簿的 DefaultStyle.Font 属性下定义的字体，它会尝试从所有可用字体中选择最合适的字体。
1. 最后，如果 Aspose.Cells 在文件系统上找不到任何字体，它会使用 Arial 呈现电子表格。

### **Aspose.Cells 在哪里寻找字体**

Aspose.Cells 尝试在文件系统上自动查找 TrueType 字体。大多数时候，您可以依靠 Aspose.Cell 的默认行为来查找 TrueType 字体，但有时您可能需要使用 FontConfigs.setFontFolder 工厂方法指定包含 TrueType 字体的文件夹。

### **典型的字体相关问题和解决方案**

此表列出了使用 Aspose.Cells 将电子表格呈现给 PDF 时可能遇到的一些问题及其解决方案。

{{% alert color="primary" %}}

复制任何字体时请记住，大多数字体都受版权保护。首先事先找到字体的许可证，并确认它们可以自由转移到另一台机器上。

{{% /alert %}}

|**问题** |**原因** |**解决方案** |
|:- |:- |:- |
|呈现文档中的布局和字体与原始文档不同。|您在 Linux 或 Mac OS 上使用 Aspose.Cells，默认情况下 TureType 字体不存在，因此 Aspose.Cells 无法在您的计算机上找到字体。|从 Windows 机器复制 TrueType 字体文件或安装 TrueType 字体包。使用 FontConfigs.setFontFolder 工厂方法指定字体文件的位置。|

{{% alert color="primary" %}}

查看详细的文章

- [如何在 Linux 上放置 TrueType 字体](/cells/zh/java/how-to-install-truetype-fonts-on-linux/).
- [如何指定 TrueType 字体位置](/cells/zh/java/how-to-specify-truetype-fonts-location/).
- [发生字体替换时如何获得警告](/cells/zh/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
