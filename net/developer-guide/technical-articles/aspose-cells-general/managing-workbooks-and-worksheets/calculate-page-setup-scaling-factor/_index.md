---
title: Calculate Page Setup Scaling Factor
type: docs
weight: 300
url: /net/calculate-page-setup-scaling-factor/
---

{{% alert color="primary" %}} 

When you set Page Setup Scaling using **Fit to n page(s) wide by m tall** option, Microsoft Excel calculates the Page Setup Scaling Factor. You can calculate the same thing using SheetRender.PageScale property. This property returns a double value which can be converted to percentage value. For example, if it returns 0.5 then it means scaling factor is 50%.

{{% /alert %}} 

The following sample code illustrates how to calculate page setup scaling factor using SheetRender.PageScale property.



{{< gist "aspose-cells" "c326c6c668fc372e30569fa9e0f6bf4b" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
