---
title: 计算页面设置缩放因子
type: docs
weight: 300
url: /zh/python-net/calculate-page-setup-scaling-factor/
description: 本文提供了一个示例代码，解释了如何使用Aspose.Cells for Python via .NET的API以程序方式计算Excel工作表Fit to n页宽度和m页高度的自适应比例。
keywords: Python Excel库，Python调整至n页宽度m页高度excel，Python计算自适应比例因子
---

{{% alert color="primary" %}}

当您使用“按n页宽和m页高适应”选项设置页面设置缩放时，Microsoft Excel会计算页面设置缩放因子。您可以使用[**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale)属性计算相同的内容。该属性返回一个Double值，可以转换为百分比值。例如，如果它返回0.5，则表示缩放因子为50%。

{{% /alert %}}

以下示例代码说明了如何使用[**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale)属性计算页面设置缩放因子。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CalculateScalingFactor-CalculatePageSetupScalingFactor.py" >}}
