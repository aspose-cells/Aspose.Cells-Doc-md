---
title: 在GridWeb中计算自定义函数
type: docs
weight: 90
url: /zh/net/aspose-cells-gridweb/calculate-custom-functions-in-gridweb/
keywords: GridWeb，自定义函数，自定义，函数
description: 本文介绍了GridWeb中自定义函数的特性。
---


## **可能的使用场景**
Aspose.Cells.GridWeb支持使用GridWeb.CustomCalculationEngine属性计算自定义函数。该属性接受GridAbstractCalculationEngine接口的实例。请实现GridAbstractCalculationEngine接口，并使用自己的逻辑计算自定义函数。
## **在GridWeb中计算自定义函数**
以下示例代码在单元B3中添加了一个名为MYTESTFUNC()的自定义函数。然后我们通过实现GridAbstractCalculationEngine接口来计算此函数的值。我们以这样的方式计算MYTESTFUNC()，即将其参数乘以2并返回结果。所以如果它的参数是9，则会返回2*9 = 18。
### **示例代码**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
