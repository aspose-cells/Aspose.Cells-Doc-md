---
title: Calculate Page Setup Scaling Factor
type: docs
weight: 260
url: /java/calculate-page-setup-scaling-factor/
---

{{% alert color="primary" %}} 

When you set Page Setup Scaling using **Fit to n page(s) wide by m tall** option, Microsoft Excel calculates the Page Setup Scaling Factor. You can calculate the same thing using [SheetRender.getPageScale()](https://apireference.aspose.com/java/cells/com.aspose.cells/sheetrender#PageScale) property. This property returns a double value which can be converted to a percentage value. For example, if it returns 0.5079621076 then it means the scaling factor is 51%.

{{% /alert %}} 
#### **Calculate Page Setup Scaling Factor**
The following sample code illustrates how to calculate page setup scaling factor using [SheetRender.getPageScale()](https://apireference.aspose.com/java/cells/com.aspose.cells/sheetrender#PageScale) property.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
#### **Console Output**
Here is the console output of the above sample code.

{{< highlight java >}}

 0.5079621076583862

{{< /highlight >}}
