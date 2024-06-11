---
title: 计算页面设置缩放因子
type: docs
weight: 260
url: /zh/java/calculate-page-setup-scaling-factor/
---

{{% alert color="primary" %}} 

当您使用“按n页宽和m页高适应”选项设置页面设置缩放时，Microsoft Excel会计算页面设置缩放因子。您可以使用[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale)属性计算相同的东西。此属性返回一个double值，可以转换为百分比值。例如，如果它返回0.5079621076，则意味着缩放因子为51%。

{{% /alert %}} 
## **计算页面设置缩放因子**
以下示例代码说明了如何使用[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale)属性计算页面设置缩放因子。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **控制台输出**
这是上面示例代码的控制台输出。

{{< highlight java >}}

 0.5079621076583862

{{< /highlight >}}
