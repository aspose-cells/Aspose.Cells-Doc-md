---
title: 如何指定 TrueType 字体位置
type: docs
weight: 30
url: /zh/java/how-to-specify-truetype-fonts-location/
---
{{% alert color="primary" %}}

本文介绍：

1. [Aspose.Cells API 寻找 TrueType 字体的地方](/cells/zh/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [如何为 Aspose.Cells API 明确指定一个 TrueType 字体文件夹](/cells/zh/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [如何限制 Aspose.Cells API 仅使用一个 TrueType 字体位置](/cells/zh/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **使用字体**

### **Aspose.Cells 在 Windows 上查找 TrueType 字体的位置**

Aspose.Cells 搜索字体**Windows\字体**文件夹。此默认设置在大多数情况下都有效，因此仅在确实需要时才指定您自己的字体文件夹。

### **Aspose.Cells 在 Linux 上寻找 TrueType 字体的位置**

默认情况下，Aspose.Cells API 在以下所有位置查找字体，尽管不同的 Linux 发行版将字体存储在不同的文件夹中。

1. /usr/共享/字体
1. /usr/本地/共享/字体

{{% alert color="primary" %}}

此默认行为适用于大多数 Linux 发行版，但不保证始终有效。您可能需要明确指定 TrueType 字体的位置。

{{% /alert %}}

### **如何明确指定字体文件夹**

Aspose.Cells API 公开了 FontConfigs 类的许多工厂方法来指定字体或字体文件夹，如下所述。

1. setFontFolder 方法接受字符串类型的第一个参数以及字体目录的位置，而布尔类型的第二个参数是指示 Aspose.Cells API 以递归方式在文件夹中搜索字体文件。
1. setFontFolders 方法接受 String 类型的数组，因此您可以使用此方法指定许多字体目录。您还可以通过将 true 指定为第二个参数来指示 Aspose.Cells API 递归搜索文件夹。
1. setFontSources 方法接受一个 FontSourceBase 类型的数组，以便您指定单个字体位置的列表。

{{% alert color="primary" %}}

使用上述任何方法指定字体文件夹时，我们建议在应用程序开始时设置字体位置，否则您可能会收到格式不正确的结果。

{{% /alert %}} {{% alert color="primary" %}}

使用上述任何一种方法设置字体文件夹都不能确保 Aspose.Cells API 不会在系统的字体文件夹等默认位置查找字体。

{{% /alert %}}

### **如何限制 Aspose.Cells 仅使用一个字体文件夹**

从 Aspose.Cells for Java 8.1.0 开始，将 JVM 参数设置为**-DAspose.Cells.FontDirExc="你的字体目录**将确保 Aspose.Cells API 将仅使用指定的字体位置。

使用 System.setProperty 方法设置指定的参数，如下所示。

{{< highlight "java" >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

请注意以下事项：

- 上面的声明应该在你的应用程序的开头。
- 使用上述方法不需要使用上面讨论的任何 FontConfigs 方法设置字体目录。
- 字符串“FontDirSet”应该是包含所需字体的文件夹的完整路径。

{{% /alert %}}
