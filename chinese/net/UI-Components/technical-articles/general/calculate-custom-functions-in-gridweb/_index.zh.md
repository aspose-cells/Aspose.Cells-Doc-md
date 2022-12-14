---
title: 在 GridWeb 中计算自定义函数
type: docs
weight: 90
url: /zh/net/calculate-custom-functions-in-gridweb/
---
## **可能的使用场景**
Aspose.Cells.GridWeb支持使用GridWeb.CustomCalculationEngine属性计算自定义函数。此属性采用 GridAbstractCalculationEngine 接口的实例。请实现 GridAbstractCalculationEngine 接口并使用您自己的逻辑计算您的自定义函数。
## **在 GridWeb 中计算自定义函数**
下面的示例代码在单元格 B3 中添加了一个名为 MYTESTFUNC() 的自定义函数。然后我们通过实现 GridAbstractCalculationEngine 接口来计算这个函数的值。我们计算 MYTESTFUNC() 的方式是将其参数乘以 2 并返回结果。所以如果它的参数是 9，它会返回 2*9 = 18。
### **示例代码**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
