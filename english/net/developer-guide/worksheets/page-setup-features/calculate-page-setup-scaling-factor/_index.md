---
title: Calculate Page Setup Scaling Factor
type: docs
weight: 300
url: /net/calculate-page-setup-scaling-factor/
description: This article provides sample code explaining how to use the C# API or .NET library to calculate the Page Setup scaling factor using the Fit to n page(s) wide by m tall option of an Excel worksheet programmatically.
keywords: Fit to n page wide by m tall excel c#, calculate page setup scaling factor c#
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

When you set Page Setup Scaling using **Fit to n page(s) wide by m tall** option, Microsoft Excel calculates the Page Setup Scaling Factor. You can calculate the same thing using [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) property. This property returns a double value that can be converted to a percentage. For example, if it returns 0.5, then it means the scaling factor is 50%.

{{% /alert %}}

The following sample code illustrates how to calculate the Page Setup Scaling Factor using [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
{{< app/cells/assistant language="csharp" >}}
