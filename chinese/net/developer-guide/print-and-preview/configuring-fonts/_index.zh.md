---
title: 配置字体以渲染电子表格
type: docs
weight: 10
url: /zh/net/configuring-fonts-for-rendering-spreadsheets/
---

## **可能的使用场景**

Aspose.Cells API 提供了在图像格式中渲染电子表格以及将其转换为 PDF 和 XPS 格式的功能。为了最大程度地保持转换的准确性，电子表格中使用的字体应该存储在操作系统的默认字体目录中。如果所需字体不可用，则 Aspose.Cells API 将尝试使用可用的字体来替代所需字体。

## **选择字体**

以下是 Aspose.Cells API 在幕后执行的过程。

1. API试图在文件系统中找到与电子表格中使用的确切字体名称匹配的字体。
1. 如果API无法找到具有相同名称的精确字体，则尝试使用工作簿的[**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)属性下指定的默认字体。
1. 如果API无法找到工作簿的[**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)属性下定义的字体，则尝试使用[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)或[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)属性下指定的字体。
1. 如果API无法找到[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)或[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)属性下定义的字体，则尝试使用[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)属性下指定的字体。
1. 如果API无法找到[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)属性下定义的字体，则尝试从所有可用字体中选择最合适的字体。
1. 最后，如果API在文件系统中找不到任何字体，则使用Arial呈现电子表格。

{{% alert color="primary" %}}

通常，Aspose.Cells API 默认扫描Windows、Linux、MacOS操作系统的默认字体目录。从[Aspose.Cells for .NET24.7](https://releases.aspose.com/cells/net/release-notes/2024/aspose-cells-for-net-24-7-release-notes/)开始，API还会默认扫描Office缓存云字体目录。

{{% /alert %}}

## **设置自定义字体文件夹**

Aspose.Cells API会搜索操作系统的默认字体目录以获取所需的字体。如果系统的字体目录中没有所需的字体，则API将通过自定义（用户定义的）目录进行搜索。 [**FontConfigs**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs) 类已公开了许多设置自定义字体目录的方式。

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)：如果只有一个要设置的文件夹，则此方法很有用。
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)：当字体存在于多个文件夹中，而用户希望将所有文件夹分开设置而不是将所有字体合并到一个文件夹中时，此方法很有用。
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources)：当用户希望从多个文件夹加载字体或从字节数组加载单个字体文件或字体数据时，此机制很有用。

{{% alert color="primary" %}}

Both [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder) 和 [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders) 方法接受一个布尔类型的第二个参数。 将 **true** 作为第二个参数传递将指示 Aspose.Cells API 在子文件夹中搜索字体文件。

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

请在应用程序启动时使用以上任一方法，在调用 Aspose.Cells API 的其他对象之前使用。

{{% /alert %}} {{% alert color="primary" %}}

如果使用所有上述方法设置字体源，则只有最后一次设置将生效。

{{% /alert %}}

## **字体替换机制**

Aspose.Cells API 还提供了指定替代字体以进行渲染的能力。 当需要的字体在进行转换的机器上不可用时，这种机制非常有用。 用户可以提供字体名称列表作为原始所需字体的替代。 为了实现这一点，Aspose.Cells API 公开了一个接受 2 个参数的 [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes) 方法。 第一个参数是 **string** 类型，应该是需要替换的字体的名称。 第二个参数是 **string** 类型的数组。 用户可以提供字体名称列表作为原始字体名称（指定在第一个参数中）的替代。

这里是一个简单的使用场景。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **信息收集**

除上述方法外，Aspose.Cells APIs还提供了收集已设置的来源和替换信息的手段。

1. [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) 方法返回一个 [**FontSourceBase**](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase) 类型的数组，其中包含指定字体源的列表。 如果没有设置源，则 [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) 方法将返回一个空数组。
1. [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) 方法接受一个 **string** 类型的参数，允许指定已设置替代字体的字体名称。 如果为指定的字体名称设置了替换，则 [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) 方法将返回 null。

## **高级主题**
- [在将电子表格呈现为图像时设置默认字体](/cells/zh/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [设置 PdfSaveOptions 和 ImageOrPrintOptions 的 DefaultFont 属性具有优先级](/cells/zh/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [支持的字体格式](/cells/zh/net/supported-font-formats/)
- [电子表格转图像 - 设置呈现图像的像素格式](/cells/zh/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
{{< app/cells/assistant language="csharp" >}}
