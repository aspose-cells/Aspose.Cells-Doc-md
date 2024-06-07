---
title: 为渲染电子表格配置字体
type: docs
weight: 10
url: /zh/java/configuring-fonts-for-rendering-spreadsheets/
---

## **可能的使用场景**

Aspose.Cells APIs提供了将电子表格渲染为图像格式以及将其转换为PDF和XPS格式的功能。为了最大限度地提高转换精确度，电子表格中使用的字体应该在操作系统的默认字体目录中可用。如果所需字体不存在，则Aspose.Cells APIs将尝试用现有字体替换所需字体。

## **字体的选择**

以下是Aspose.Cells APIs在幕后遵循的流程。

1. API尝试在文件系统中查找与电子表格中使用的确切字体名称匹配的字体。
1. 如果API无法找到与确切字体名称匹配的字体，则尝试使用工作簿的[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font)属性中指定的默认字体。
1. 如果API无法定位工作簿的[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font)属性下定义的字体，则尝试使用在[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont)或[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont)属性下指定的字体。
1. 如果API无法定位在[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont)或[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont)属性下定义的字体，则尝试使用在[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName)属性下指定的字体。
1. 如果API无法定位在[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName)属性下定义的字体，则尝试从所有可用字体中选择最合适的字体。
1. 最后，如果API在文件系统中找不到任何字体，则使用Arial呈现电子表格。

{{% alert color="primary" %}}

Aspose.Cells APIs始终扫描操作系统的默认字体目录，但有一个例外，即;当设置JVM参数为**-DAspose.Cells.FontDirExc="YourFontDir"**时。在这种情况下，Aspose.Cells APIs将跳过扫描操作系统的默认字体目录，只搜索所述JVM参数中指定的路径。

{{% /alert %}}

## **设置自定义字体文件夹**

Aspose.Cells APIs在操作系统的默认字体目录中搜索所需的字体。如果系统字体目录中没有所需字体，那么API将通过自定义（用户定义）目录进行搜索。 [**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs)类公开了多种设置自定义字体目录的方法，如下所述。

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)): 如果只有一个文件夹要设置，则此方法很有用。
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)): 如果字体位于多个文件夹中，用户希望单独设置所有文件夹，而不是将所有字体合并到一个文件夹中，则此方法很有用。
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources(com.aspose.cells.FontSourceBase[])): 当用户希望从多个文件夹加载字体或单个字体文件或字节数组中的字体数据时，此机制很有用。

{{% alert color="primary" %}}

[**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean))和[**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean))方法都接受一个布尔类型的第二个参数。将**true**作为第二个参数传递将指导Aspose.Cells APIs搜索字体文件的子文件夹。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

请在应用程序开始时使用上述任何方法，即在调用Aspose.Cells APIs的其他对象之前使用。

{{% /alert %}} {{% alert color="primary" %}}

如果使用了最多一种上述方法来设置字体源，则只有最后的设置将生效。

{{% /alert %}}

## **字体替代机制**

Aspose.Cells APIs还提供了指定替代字体以进行渲染的能力。当要进行转换的机器上缺少所需字体时，此机制非常有用。用户可以将字体名列表作为原始所需字体的替代提供。为了实现这一点，Aspose.Cells APIs已公开了FontConfigs.setFontSubstitutes 方法，该方法接受2个参数。第一个参数是**String**类型，应该是需要替代的字体的名称。第二个参数是**String**类型的数组。用户可以提供一系列字体名称作为原始字体的替代。

这是一个简单的使用场景。

{{< highlight java >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

## **信息收集**

除了上述方法外，Aspose.Cells APIs还提供了收集已设置的源和替换信息的手段。

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources()): 此方法返回一个类型为[**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource)的数组，包含已指定的字体源列表。如果未设置任何源，则[**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources())方法将返回一个空数组。
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)): 此方法接受一个**String**类型的参数，允许指定已设置替代字体的字体名称。如果未为指定的字体名称设置替代，则[**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String))方法将返回null。
