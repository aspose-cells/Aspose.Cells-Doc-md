---
title: 设置命名范围公式
type: docs
weight: 20
url: /zh/python-net/setting-formula-for-named-range/
---

## **为命名范围设置公式**
 类似Excel应用程序，Aspose.Cells for Python via .NET API提供在使用其 [**Range.refers_to**](https://reference.aspose.com/cells/python-net/aspose.cells/range/refers_to) 属性时，为命名范围指定公式的能力。这一功能具有多个应用场景，以下列举其中一些：
### **为命名范围设置简单公式**
简单公式可能是对同一（或不同）工作表中另一个单元格的引用。下面的示例创建一个新电子表格中的命名范围，并将其引用设置为另一个单元格。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSimpleFormulaForNamedRanges.py" >}}
### **为命名范围设置复杂公式**
复杂公式可以是任何内容，例如动态范围或跨不同工作表多个单元格的公式。下面的示例使用INDEX函数创建一个动态范围，根据其位置从列表中获取值。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingComplexFormulaNamedRange.py" >}}



这是另一个示例，使用命名范围对不同工作表中的2个单元格的值进行求和。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-CalculatingSumUsingNamedRangeOnDifferentSheets.py" >}}
