---
title: 计算页面设置比例因子
type: docs
weight: 300
url: /zh/net/calculate-page-setup-scaling-factor/
description: 本文提供示例代码，说明如何使用 C# API 或 .NET 库以编程方式使用 Excel 工作表的适合 n 页宽乘 m 高选项计算页面设置比例因子。
keywords: Fit to n page wide by m tall excel c#, calculate page setup scaling factor c#
---
{{% alert color="primary" %}}

当您使用设置页面设置缩放时**适合 n 页宽乘以 m 高**选项，Microsoft Excel 计算页面设置比例因子。您可以使用计算相同的东西[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale)财产。此属性返回一个可以转换为百分比值的双精度值。例如，如果它返回 0.5，则表示比例因子为 50%。

{{% /alert %}}

以下示例代码说明了如何使用计算页面设置比例因子[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
