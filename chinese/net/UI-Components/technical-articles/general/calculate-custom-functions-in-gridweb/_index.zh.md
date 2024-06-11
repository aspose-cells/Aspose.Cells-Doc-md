---
title: 在 GridWeb 中计算自定义函数
type: docs
weight: 90
url: /zh/net/aspose-cells-gridweb/calculate-custom-functions-in-gridweb/
keywords: GridWeb、custom functions、custom、function
description: 本文介绍了 GridWeb 中自定义函数的特性。
---


## **可能的使用场景**
Aspose.Cells.GridWeb 支持使用 GridWeb.CustomCalculationEngine 属性计算自定义函数。该属性接受 GridAbstractCalculationEngine 接口的实例。请使用自己的逻辑实现 GridAbstractCalculationEngine 接口并计算您的自定义函数。
## **在 GridWeb 中计算自定义函数**
下面的示例代码在单元格 B3 中添加了名为 MYTESTFUNC() 的自定义函数。然后我们通过实现 GridAbstractCalculationEngine 接口计算了该函数的值。我们以这样的方式计算 MYTESTFUNC()，即将其参数乘以 2 并返回结果。因此，如果其参数为 9，则返回 2*9 = 18。
### **示例代码**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
