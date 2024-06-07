---
title: 为渲染电子表格配置字体
type: docs
weight: 10
url: /zh/net/configuring-fonts-for-rendering-spreadsheets/
---

## **可能的使用场景**

Aspose.Cells APIs提供了将电子表格渲染为图像格式以及将其转换为PDF和XPS格式的功能。为了最大限度地提高转换精确度，电子表格中使用的字体应该在操作系统的默认字体目录中可用。如果所需字体不存在，则Aspose.Cells APIs将尝试用现有字体替换所需字体。

## **字体的选择**

以下是Aspose.Cells APIs在幕后遵循的流程。

1. API尝试在文件系统中查找与电子表格中使用的确切字体名称匹配的字体。
1. 如果API找不到具有完全相同名称的字体，则尝试使用工作簿下**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)**属性指定的默认字体。
1. 如果API无法找到工作簿下**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)**属性定义的字体，它将尝试使用**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**或**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)**属性指定的字体。
1. 如果API无法找到**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**或**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)**属性下定义的字体，它将尝试使用**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)**属性指定的字体。
1. 如果API无法找到**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)**属性下定义的字体，它将尝试从所有可用字体中选择最合适的字体。
1. 最后，如果API在文件系统中找不到任何字体，则使用Arial呈现电子表格。

## **设置自定义字体文件夹**

Aspose.Cells API会搜索操作系统的默认字体目录以获取所需字体。如果系统的字体目录中没有所需的字体，则API会搜索自定义(用户定义)目录。**[FontConfigs](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs)**类提供了多种设置自定义字体目录的方法，如下所述。

1. **[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)**: 如果只需设置一个文件夹，则此方法很有用。
1. **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)**: 如果字体存储在多个文件夹中，并且用户希望单独设置所有文件夹，而不是将所有字体组合在一个文件夹中，则此方法很有用。
1. **[FontConfigs.SetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources)**: 当用户希望从多个文件夹加载字体或从单个字体文件或字体数据数组加载字体时，此机制非常有用。

{{% alert color="primary" %}}

**[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)**和**[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)**方法均接受布尔类型的第二个参数。将true作为第二个参数将指导Aspose.Cells API搜索字体文件的子文件夹。

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

请在应用程序启动时使用上述任一方法，即在调用Aspose.Cells API的其他对象之前。

{{% /alert %}} {{% alert color="primary" %}}

如果所有上述方法都用于设置字体源，那么只有最后的设置将生效。

{{% /alert %}}

## **字体替代机制**

Aspose.Cells API还提供了指定替代字体以用于呈现目的的功能。当所需字体在进行转换的计算机上不可用时，此机制很有用。用户可以提供字体名称列表作为原始所需字体的替代。为了实现这一点，Aspose.Cells API公开了**[FontConfigs.SetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes)**方法，该方法接受2个参数。第一个参数是string类型，应该是需要替代的字体名称。第二个参数是string类型的数组。用户可以提供字体名称列表作为原始字体名称的替代。

这是一个简单的使用场景。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **信息收集**

除了上述方法外，Aspose.Cells APIs还提供了收集已设置的源和替换信息的手段。

1. **[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)**方法返回一个类型为**[FontSourceBase](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase)**的数组，包含指定的字体源列表。如果没有设置字体源，**[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)**方法将返回一个空数组。
1. **[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)**方法接受一个string类型的参数，允许指定已设置替代的字体名称。如果没有为指定的字体名称设置替代，则**[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)**方法将返回null。

## **高级主题**
- [在将电子表格渲染为图像时设置默认字体](/cells/zh/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [设置PdfSaveOptions和ImageOrPrintOptions的DefaultFont属性以优先级](/cells/zh/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [支持的字体格式](/cells/zh/net/supported-font-formats/)
- [工作表转图像 - 为呈现的图像设置像素格式](/cells/zh/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
