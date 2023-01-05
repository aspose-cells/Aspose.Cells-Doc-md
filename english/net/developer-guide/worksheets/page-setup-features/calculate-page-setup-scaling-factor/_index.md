---
title: Calculate Page Setup Scaling Factor
type: docs
weight: 300
url: /net/calculate-page-setup-scaling-factor/
description: This article provides sample code explaining how to use the C# API or .NET library to calculate Page Setup scaling factor using Fit to n page(s) wide by m tall option of Excel worksheet programmatically.
keywords: Fit to n page wide by m tall excel c#, calculate page setup scaling factor c#
---

{{% alert color="primary" %}}

When you set Page Setup Scaling using **Fit to n page(s) wide by m tall** option, Microsoft Excel calculates the Page Setup Scaling Factor. You can calculate the same thing using [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) property. This property returns a double value which can be converted to percentage value. For example, if it returns 0.5 then it means scaling factor is 50%.

{{% /alert %}}

The following sample code illustrates how to calculate page setup scaling factor using [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
