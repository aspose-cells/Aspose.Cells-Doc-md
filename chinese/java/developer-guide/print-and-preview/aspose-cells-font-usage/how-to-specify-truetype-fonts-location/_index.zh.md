---
title: 如何指定TrueType字体位置
type: docs
weight: 30
url: /zh/java/how-to-specify-truetype-fonts-location/
---

{{% alert color="primary" %}}

本文描述：

1. [Aspose.Cells API寻找TrueType字体的位置](/cells/zh/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows)
1. [如何显式指定Aspose.Cells API的TrueType字体文件夹](/cells/zh/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder)
1. [如何限制Aspose.Cells API仅使用一个TrueType字体位置](/cells/zh/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder)

{{% /alert %}}

## **字体处理**

### **Aspose.Cells在Windows中查找TrueType字体位置**

Aspose.Cells在**Windows\Fonts**文件夹中搜索字体。默认设置大多数情况下都有效，因此只有在真正需要时才指定自己的字体文件夹。

### **Aspose.Cells在Linux中查找TrueType字体位置**

默认情况下，Aspose.Cells API在以下所有位置搜索字体，尽管不同的Linux发行版将字体存储在不同的文件夹中。

1. /usr/share/fonts
1. /usr/local/share/fonts

{{% alert color="primary" %}}

默认行为对于大多数Linux发行版都有效，但不保证始终有效。您可能需要明确指定TrueType字体的位置。 

{{% /alert %}}

### **如何明确指定字体文件夹**

Aspose.Cells API公开了许多FontConfigs类的工厂方法，用于指定如下字体或字体文件夹。

1. setFontFolder方法接受String类型的第一个参数，其中包含字体目录的位置，而Type Boolean的第二个参数用于指导Aspose.Cells API递归搜索字体文件夹。
1. setFontFolders方法接受String类型的数组，因此可以使用此方法指定许多字体目录。您还可以通过将true指定为第二个参数，指导Aspose.Cells API递归搜索文件夹。
1. setFontSources方法接受FontSourceBase类型的数组，供您指定一组单独字体的位置。

{{% alert color="primary" %}}

使用上述任何方法指定字体文件夹时，我们建议在应用程序开始时设置字体位置，否则可能会导致格式不良的结果。

{{% /alert %}} {{% alert color="primary" %}}

使用上述任何方法设置字体文件夹不保证Aspose.Cells API不会在默认位置（例如系统的字体文件夹）搜索字体。

{{% /alert %}}

### **如何限制Aspose.Cells仅使用一个字体文件夹**

从Aspose.Cells for Java 8.1.0开始，设置JVM参数**-DAspose.Cells.FontDirExc="YourFontDir**将确保Aspose.Cells API仅使用指定的字体位置。

使用System.setProperty方法设置指定的参数，如下所示。

{{< highlight java >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

请注意以下内容：

- 上述语句应放在应用程序的开头。
- 使用上述方法不需要使用上述讨论的FontConfigs方法设置字体目录。
- 字符串"FontDirSet"应该是包含所需字体的文件夹的完整路径。

{{% /alert %}}
