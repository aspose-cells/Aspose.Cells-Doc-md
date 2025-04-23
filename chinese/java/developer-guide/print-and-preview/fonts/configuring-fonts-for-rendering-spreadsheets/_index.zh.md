---
title: 配置字体以渲染电子表格
type: docs
weight: 10
url: /zh/java/configuring-fonts-for-rendering-spreadsheets/
---

## **可能的使用场景**

Aspose.Cells API 提供了在图像格式中渲染电子表格以及将其转换为 PDF 和 XPS 格式的功能。为了最大程度地保持转换的准确性，电子表格中使用的字体应该存储在操作系统的默认字体目录中。如果所需字体不可用，则 Aspose.Cells API 将尝试使用可用的字体来替代所需字体。

## **选择字体**

以下是 Aspose.Cells API 在幕后执行的过程。

1. API试图在文件系统中找到与电子表格中使用的确切字体名称匹配的字体。
1. 如果API无法找到具有相同名称的精确字体，则尝试使用工作簿的[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font)属性下指定的默认字体。
1. 如果API无法找到工作簿的[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font)属性下定义的字体，则尝试使用[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont)或[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont)属性下指定的字体。
1. 如果API无法找到[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont)或[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont)属性下定义的字体，则尝试使用[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName)属性下指定的字体。
1. 如果API无法找到[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName)属性下定义的字体，则尝试从所有可用字体中选择最合适的字体。
1. 最后，如果API在文件系统中找不到任何字体，则使用Arial呈现电子表格。

{{% alert color="primary" %}}

 一般来说，Aspose.Cells API 默认扫描 Windows、Linux、MacOS 操作系统的字体目录。从 [Aspose.Cells for Java 24.7](https://releases.aspose.com/cells/java/release-notes/2024/aspose-cells-for-java-24-7-release-notes/) 开始，API 还会默认扫描 Office 缓存的云字体目录。

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells API 始终扫描操作系统的默认字体目录，唯一例外是在 JVM 参数中设置 **-DAspose.Cells.FontDirExc="YourFontDir"** 时。在这种情况下，API 将跳过扫描操作系统的默认字体目录，仅搜索指定的路径。

{{% /alert %}}

## **设置自定义字体文件夹**

Aspose.Cells APIs搜索操作系统的默认字体目录以获取所需的字体。如果系统字体目录中没有所需的字体，则API将通过自定义(用户定义)目录进行搜索。[**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs)类已公开了多种设置自定义字体目录的方法，如下所述。

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder-java.lang.String-boolean-)：如果只有一个要设置的文件夹，则此方法很有用。
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders-java.lang.String[]-boolean-)：当字体存在于多个文件夹中，而用户希望将所有文件夹分开设置而不是将所有字体合并到一个文件夹中时，此方法很有用。
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources-com.aspose.cells.FontSourceBase[]-)：当用户希望从多个文件夹加载字体或从字节数组加载单个字体文件或字体数据时，此机制很有用。

{{% alert color="primary" %}}

[**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder-java.lang.String-boolean-)和[**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders-java.lang.String[]-boolean-)方法都接受一个Boolean类型的第二个参数。将**true**作为第二个参数传递给Aspose.Cells API将搜索字体文件的子文件夹。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

请在应用程序启动时使用上述任何一种方法，即在调用Aspose.Cells APIs的其他对象之前。

{{% /alert %}} {{% alert color="primary" %}}

如果使用了上述多种方法来设置字体源，则只有最后的设置会生效。

{{% /alert %}}

## **字体替换机制**

Aspose.Cells APIs还提供了指定替代字体以进行呈现的功能。当需要的字体在进行转换的机器上不可用时，这种机制非常有用。用户可以提供一系列字体名称作为原始要求的字体的替代品。为了实现这一点，Aspose.Cells APIs公开了FontConfigs.setFontSubstitutes方法，该方法接受2个参数。第一个参数是**String**类型，应该是需要被替换的字体的名称。第二个参数是**String**类型的数组。用户可以提供作为原始字体的替代品的字体名称列表(指定在第一个参数中)。

这里是一个简单的使用场景。

{{< highlight java >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

## **信息收集**

除上述方法外，Aspose.Cells APIs还提供了收集已设置的来源和替换信息的手段。

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--)：此方法返回一个包含指定字体源列表的 [**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource) 类型的数组。如果未设置任何源，[**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--) 方法将返回一个空数组。
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes-java.lang.String-)：此方法接受**String**类型的参数，允许指定已设置替代的字体名称。如果为指定的字体名称未设置替代，则 [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes-java.lang.String-) 方法将返回 null。
{{< app/cells/assistant language="java" >}}
