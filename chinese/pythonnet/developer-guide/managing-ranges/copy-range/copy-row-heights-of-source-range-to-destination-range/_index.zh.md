---
title: 将源范围行高度复制到目标范围
type: docs
weight: 590
url: /zh/python-net/copy-row-heights-of-source-range-to-destination-range/
description: 本文介绍了如何使用Aspose.Cells for Python via .NET库将源范围的行高度复制到目标范围。
keywords: Python Excel Library，Python如何将源范围的行高度复制到目标范围，Python如何仅使用Python Excel库复制源范围的行高度。
---

{{% alert color="primary" %}}

有时用户需要将源范围的行高度复制到目标范围。Aspose.Cells for Python via .NET提供了此目的的[**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype)枚举。当您使用[**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype)枚举设置[**PasteOptions.paste_type**](https://reference.aspose.com/cells/python-net/aspose.cells/pasteoptions/paste_type/)属性时，源范围内所有行的高度将被复制到目标范围。

{{% /alert %}}

以下示例代码说明了如何使用[**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype)枚举将源范围的行高复制到目标范围。一旦您在Microsoft Excel中打开由此代码生成的输出excel文件，您将看到目标范围的行高与源范围的行高完全相同。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-GetRowHeightsOfSourceRangeToDestinationRange.py" >}}
{{< app/cells/assistant language="python-net" >}}
