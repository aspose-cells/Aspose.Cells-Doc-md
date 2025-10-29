---
title: 计算页面设置缩放因子
type: docs
weight: 300
url: /zh/python-net/calculate-page-setup-scaling-factor/
description: 本文提供示例代码，演示如何使用 Aspose.Cells for Python via .NET API 程序化计算页面设置缩放比例，使用适合 n 页宽 m 页高的选项。
keywords: Python Excel 库，Python 按 n 页宽 m 页高适配，计算页面设置缩放比例。
---

{{% alert color="primary" %}}

当您使用“按n页宽和m页高适应”选项设置页面设置缩放时，Microsoft Excel会计算页面设置缩放因子。您可以使用[**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale)属性计算相同的内容。该属性返回一个Double值，可以转换为百分比值。例如，如果它返回0.5，则表示缩放因子为50%。

{{% /alert %}}

以下示例代码说明了如何使用[**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale)属性计算页面设置缩放因子。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CalculateScalingFactor-CalculatePageSetupScalingFactor.py" >}}
{{< app/cells/assistant language="python-net" >}}
