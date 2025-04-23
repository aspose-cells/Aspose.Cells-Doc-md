---
title: 配置字体以渲染电子表格
type: docs
weight: 10
url: /zh/python-net/configuring-fonts-for-rendering-spreadsheets/
---

## **可能的使用场景**

Aspose.Cells for Python via .NET API 提供将电子表格渲染为图像格式以及转换为 PDF 和 XPS 格式的功能。为了最大化转换的准确性，确保电子表格中使用的字体可在操作系统的默认字体目录中找到。如果缺少所需字体，Aspose.Cells for Python via .NET API 将尝试用可用字体进行替代。

## **选择字体**

下面是 Aspose.Cells for Python via .NET API 在后台执行的流程。

1. API试图在文件系统中找到与电子表格中使用的确切字体名称匹配的字体。
1. 如果API无法找到具有相同名称的精确字体，则尝试使用工作簿的[**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)属性下指定的默认字体。
1. 如果API无法找到工作簿的[**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)属性下定义的字体，则尝试使用[**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/)或[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font)属性下指定的字体。
1. 如果API无法找到[**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/)或[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font)属性下定义的字体，则尝试使用[**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name)属性下指定的字体。
1. 如果API无法找到[**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name)属性下定义的字体，则尝试从所有可用字体中选择最合适的字体。
1. 最后，如果API在文件系统中找不到任何字体，则使用Arial呈现电子表格。

## **设置自定义字体文件夹**

Aspose.Cells for Python via .NET API 在操作系统的默认字体目录中搜索所需字体。若系统字体目录中没有，API 还会搜索用户定义的自定义目录。[**FontConfigs**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs) 类提供了多种设置自定义字体目录的方法，详见下文。

1. [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/)：如果只有一个要设置的文件夹，则此方法很有用。
1. [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/)：当字体存在于多个文件夹中，而用户希望将所有文件夹分开设置而不是将所有字体合并到一个文件夹中时，此方法很有用。
1. [**FontConfigs.set_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_sources/#list)：当用户希望从多个文件夹加载字体或从字节数组加载单个字体文件或字体数据时，此机制很有用。

{{% alert color="primary" %}}

[**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/) 和 [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/) 方法都接受一个布尔类型第二个参数。传入 **true** 作为第二参数将指示 Aspose.Cells for Python via .NET API 搜索子文件夹中的字体文件。

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-1.py" >}}

{{% alert color="primary" %}}

请在应用程序开始时，调用任何其他 Aspose.Cells for Python via .NET API 对象之前，使用上述任意方法。

{{% /alert %}} {{% alert color="primary" %}}

如果使用所有上述方法设置字体源，则只有最后一次设置将生效。

{{% /alert %}}

## **字体替换机制**

Aspose.Cells for Python via .NET API 还提供设置替代字体的功能。这在所需字体缺失时非常有用，用户可以提供一个字体名称列表作为替代。为实现此目的，API 提供 [**FontConfigs.set_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_substitutes/#str-list) 方法，接受两个参数。第一个参数是字符串类型，应为需要替代的字体名称。第二个参数是字符串数组，用户可以提供一组替代原字体的字体名称。

这里是一个简单的使用场景。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-FontSubstitution.py" >}}

## **信息收集**

除了上述方法，Aspose.Cells for Python via .NET 还提供了收集已设置的字体源和替代方案信息的方法。

1. [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) 方法返回一个 [**FontSourceBase**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsourcebase) 类型的数组，其中包含指定字体源的列表。 如果没有设置源，则 [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) 方法将返回一个空数组。
1. [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) 方法接受一个 **string** 类型的参数，允许指定已设置替代字体的字体名称。 如果为指定的字体名称设置了替换，则 [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) 方法将返回 null。

## **高级主题**
- [在将电子表格呈现为图像时设置默认字体](/cells/zh/python-net/set-default-font-while-rendering-spreadsheet-to-images/)
- [设置 PdfSaveOptions 和 ImageOrPrintOptions 的 DefaultFont 属性具有优先级](/cells/zh/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [支持的字体格式](/cells/zh/python-net/supported-font-formats/)
- [电子表格转图像 - 设置呈现图像的像素格式](/cells/zh/python-net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)

