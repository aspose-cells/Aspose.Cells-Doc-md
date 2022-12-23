---
title: 配置呈现电子表格的字体
type: docs
weight: 10
url: /zh/net/configuring-fonts-for-rendering-spreadsheets/
---
## **可能的使用场景**

Aspose.Cells API 提供了以图像格式呈现电子表格并将其转换为 PDF 和 XPS 格式的工具。为了最大限度地提高转换保真度，电子表格中使用的字体必须在操作系统的默认字体目录中可用。如果所需字体不存在，则 Aspose.Cells API 将尝试用可用字体替换所需字体。

## **字体选择**

以下是 Aspose.Cells API 在幕后遵循的过程。

1. API 尝试在文件系统中查找与电子表格中使用的确切字体名称匹配的字体。
1. 如果 API 找不到名称完全相同的字体，它会尝试使用工作簿下指定的默认字体**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)**财产。
1. 如果API找不到工作簿下定义的字体**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)**属性，它会尝试使用下面指定的字体**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**要么**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)**财产。
1. 如果API找不到下定义的字体**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**要么**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)**属性，它会尝试使用下面指定的字体**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)**财产。
1. 如果API找不到下定义的字体**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)**属性，它会尝试从所有可用字体中选择最合适的字体。
1. 最后，如果 API 在文件系统上找不到任何字体，它会使用 Arial 呈现电子表格。

## **设置自定义字体文件夹**

Aspose.Cells API 在操作系统的默认字体目录中搜索所需的字体。如果所需的字体在系统的字体目录中不可用，则 API 会搜索自定义（用户定义的）目录。这**[字体配置](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs)**类公开了许多设置自定义字体目录的方法，如下所述。

1. **[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)**：如果只设置一个文件夹，此方法很有用。
1. **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)**：当字体位于多个文件夹中并且用户希望单独设置所有文件夹而不是将所有字体组合在一个文件夹中时，此方法很有用。
1. **[FontConfigs.SetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources)**：当用户希望从多个文件夹或单个字体文件或字节数组中加载字体数据时，此机制很有用。

{{% alert color="primary" %}}

两个都**[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)** & **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)**方法接受布尔类型的第二个参数。通过**真的**因为第二个参数将指示 Aspose.Cells API 在子文件夹中搜索字体文件。

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

请在申请开始时使用上述任何一种方法，即；在调用 Aspose.Cells API 的任何其他对象之前。

{{% /alert %}} {{% alert color="primary" %}}

如果上述所有方法都用于设置字体源，则只有最后的设置生效。

{{% /alert %}}

## **字体替换机制**

 Aspose.Cells API 还提供了为呈现目的指定替代字体的能力。当必须进行转换的机器上所需的字体不可用时，此机制很有用。用户可以提供一个字体名称列表来替代最初需要的字体。为了实现这一点，Aspose.Cells API 公开了**[FontConfigs.SetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes)**接受2个参数的方法。第一个参数是类型**细绳** 这应该是需要替换的字体的名称。第二个参数是类型数组**细绳**.用户可以提供字体名称列表作为原始字体名称（在第一个参数中指定）的替代。

下面是一个简单的使用场景。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **信息收集**

除了上述方法外，Aspose.Cells API 还提供了收集有关已设置的源和替换信息的方法。

1. **[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)**方法返回类型数组**[FontSourceBase](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase)**包含指定字体源的列表。如果没有设置源，则**[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)**方法将返回一个空数组。
1. **[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)**方法接受类型参数**细绳**允许指定已设置替换的字体名称。如果没有为指定的字体名称设置替换，则**[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)**方法将返回 null。

## **推进主题**
- [将电子表格渲染为图像时设置默认字体](/cells/zh/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [将 PdfSaveOptions 和 ImageOrPrintOptions 的 DefaultFont 属性设置为优先](/cells/zh/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [支持的字体格式](/cells/zh/net/supported-font-formats/)
- [工作表到图像 - 设置渲染图像的像素格式](/cells/zh/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
