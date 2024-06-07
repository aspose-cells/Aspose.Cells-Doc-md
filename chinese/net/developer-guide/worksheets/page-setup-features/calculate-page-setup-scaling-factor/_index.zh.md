---
title: 计算页面设置缩放系数
type: docs
weight: 300
url: /zh/net/calculate-page-setup-scaling-factor/
description: 本文提供了样本代码，解释如何使用C# API或.NET库以编程方式计算Excel工作表的页面设置缩放系数，使用Fit to n页横向，m页纵向选项。
keywords: Fit to n页面横向，m页面纵向Excel c#，计算页面设置缩放因子c#
---

{{% alert color="primary" %}}

当您使用**Fit to n页横向，m页纵向**选项设置页面设置缩放时，Microsoft Excel会计算页面设置缩放因子。使用[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale)属性可以计算相同的值。该属性返回一个double值，可将其转换为百分比值。例如，如果返回0.5，则表示缩放因子为50%。

{{% /alert %}}

以下示例代码说明了如何使用[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale)属性计算页面设置缩放因子。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
