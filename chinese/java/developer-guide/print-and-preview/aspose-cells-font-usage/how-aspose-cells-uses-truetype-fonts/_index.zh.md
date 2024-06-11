---
title: Aspose.Cells如何使用TrueType字体
type: docs
weight: 10
url: /zh/java/how-aspose-cells-uses-truetype-fonts/
---

{{% alert color="primary" %}}

Aspose.Cells在将电子表格渲染为PDF、XPS和图像等格式时需要TrueType字体。 TrueType字体是一种压缩文件，其中包含了所有格式、大小和样式的字体。

当Aspose.Cells渲染电子表格时，需要访问电子表格中使用的TrueType字体。这在生成PDF、XPS和图像时是正常操作，可以确保转换后的文档或图像对于任何查看者都是相同的。

{{% /alert %}}

## **关于字体**

### **字体可用性和替代**

电子表格可能使用各种字体，比如Arial、Times New Roman、Verdana等。当Aspose.Cells渲染电子表格时，它会尝试选择电子表格中使用的字体。然而，有时可能无法使用完全相同的字体，因此Aspose.Cells不得不替换为类似的字体。

下面是Aspose.Cells在后台执行的过程。

1. Aspose.Cells尝试在文件系统中找到与电子表格中使用的确切字体名称匹配的字体。
2. 如果Aspose.Cells找不到具有完全相同名称的字体，它会尝试使用工作簿的DefaultStyle.Font属性下指定的默认字体。
3. 如果Aspose.Cells无法找到工作簿DefaultStyle.Font属性下定义的字体，它会尝试从所有可用字体中选择最合适的字体。
4. 最后，如果Aspose.Cells在文件系统上找不到任何字体，它将使用Arial渲染电子表格。

### **Aspose.Cells查找字体的位置**

Aspose.Cells会自动在文件系统中查找TrueType字体。大多数情况下，您可以依赖Aspose.Cells的默认行为来查找TrueType字体，但有时您可能需要通过FontConfigs.setFontFolder工厂方法指定包含TrueType字体的文件夹。

### **常见与字体相关的问题及解决方案**

此表列出了使用Aspose.Cells将电子表格渲染为PDF时可能遇到的一些问题及其解决方案。

{{% alert color="primary" %}}

请记住，当复制任何字体时，大多数字体都受版权保护。在提前找到字体的许可证并验证其是否可以自由转移到另一台机器之前，首先定位字体的许可证。 

{{% /alert %}}

|**问题** |**原因** |**解决方案** |
| :- | :- | :- |
| 渲染文档中的布局和字体与原始文档不同。|您正在Linux或Mac OS上使用Aspose.Cells，这些系统默认没有安装TrueType字体，因此Aspose.Cells无法在您的计算机上找到字体。 |从Windows计算机复制TrueType字体文件或安装TrueType字体包。使用FontConfigs.setFontFolder工厂方法来指定字体文件的位置。|

{{% alert color="primary" %}}

检查详细文章

- [如何在Linux上安装TrueType字体](/cells/zh/java/how-to-install-truetype-fonts-on-linux/).
- [如何指定TrueType字体位置](/cells/zh/java/how-to-specify-truetype-fonts-location/).
- [当发生字体替换时如何获得警告](/cells/zh/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
