---
title: 配置呈现电子表格的字体
type: docs
weight: 10
url: /zh/java/configuring-fonts-for-rendering-spreadsheets/
---
## **可能的使用场景**

Aspose.Cells API 提供了以图像格式呈现电子表格以及将其转换为 PDF 和 XPS 格式的工具。为了最大限度地提高转换保真度，电子表格中使用的字体必须在操作系统的默认字体目录中可用。如果所需字体不存在，则 Aspose.Cells API 将尝试用可用字体替换所需字体。

## **字体选择**

以下是 Aspose.Cells API 在幕后遵循的过程。

1. API 尝试在文件系统中查找与电子表格中使用的确切字体名称匹配的字体。
1. 如果 API 找不到名称完全相同的字体，它会尝试使用工作簿下指定的默认字体[**默认样式.字体**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font)财产。
1. 如果API找不到工作簿下定义的字体[**默认样式.字体**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font)属性，它会尝试使用下面指定的字体[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont)或者[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont)财产。
1. 如果API找不到下定义的字体[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont)或者[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont)属性，它会尝试使用下面指定的字体[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName)财产。
1. 如果API找不到下定义的字体[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName)属性，它会尝试从所有可用字体中选择最合适的字体。
1. 最后，如果 API 在文件系统上找不到任何字体，它会使用 Arial 呈现电子表格。

{{% alert color="primary" %}}

 Aspose.Cells API 始终扫描操作系统的默认字体目录，但有一个例外，即：当 JVM 参数**-DAspose.Cells.FontDirExc="你的字体目录"**被设置。在这种情况下，Aspose.Cells API 将跳过扫描操作系统的默认字体目录，只搜索上述 JVM 参数中指定的路径。

{{% /alert %}}

## **设置自定义字体文件夹**

Aspose.Cells API 在操作系统的默认字体目录中搜索所需的字体。如果所需的字体在系统的字体目录中不可用，则 API 会搜索自定义（用户定义的）目录。这[**字体配置**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs)类公开了许多设置自定义字体目录的方法，如下所述。

1. [**字体配置.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)): 如果只设置一个文件夹，此方法很有用。
1. [**字体配置.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)): 当字体位于多个文件夹中并且用户希望单独设置所有文件夹而不是将所有字体组合在一个文件夹中时，此方法很有用。
1. [**字体配置.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources(com.aspose.cells.FontSourceBase[])): 当用户希望从多个文件夹或单个字体文件或字节数组中加载字体数据时，此机制很有用。

{{% alert color="primary" %}}

两个都[**字体配置.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)) & [**字体配置.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean) 方法接受布尔类型的第二个参数。通过**真的**作为第二个参数将指示 Aspose.Cells API 在子文件夹中搜索字体文件。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

请在申请开始时使用上述任何一种方法，即；在调用 Aspose.Cells API 的任何其他对象之前。

{{% /alert %}} {{% alert color="primary" %}}

如果使用上述多种方法设置字体源，则最后的设置生效。

{{% /alert %}}

## **字体替换机制**

Aspose.Cells API 还提供了为呈现目的指定替代字体的能力。当必须进行转换的机器上所需的字体不可用时，此机制很有用。用户可以提供一个字体名称列表来替代最初需要的字体。为了实现这一点，Aspose.Cells API 公开了接受 2 个参数的 FontConfigs.setFontSubstitutes 方法。第一个参数是类型**细绳** 这应该是需要替换的字体的名称。第二个参数是类型数组**细绳**.用户可以提供字体名称列表作为原始字体（在第一个参数中指定）的替代品。

下面是一个简单的使用场景。

{{< highlight "java" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

## **信息收集**

除了上述方法外，Aspose.Cells API 还提供了收集有关已设置的源和替换信息的方法。

1. [**字体配置.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources() ): 此方法返回类型数组[**字体源库**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource)包含指定字体源的列表。如果没有设置源，则[**字体配置.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources()方法将返回一个空数组。
1. [**字体配置.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String) ): 这个方法接受一个类型的参数**细绳**允许指定已设置替换的字体名称。如果没有为指定的字体名称设置替换，则[**字体配置.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)方法将返回 null。
