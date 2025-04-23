---
title: 设置命名范围公式
type: docs
weight: 20
url: /zh/net/setting-formula-for-named-range/
---

## **为命名范围设置公式**
与Excel应用程序类似，Aspose.Cells API在使用其[RefersTo](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto)属性时，提供了为命名范围指定公式的能力。这个功能可能有许多可用性场景，其中一些详细列出如下。
### **为命名范围设置简单公式**
简单公式可能是对同一（或不同）工作表中另一个单元格的引用。下面的示例创建一个新电子表格中的命名范围，并将其引用设置为另一个单元格。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **为命名范围设置复杂公式**
复杂公式可以是任何内容，例如动态范围或跨不同工作表多个单元格的公式。下面的示例使用INDEX函数创建一个动态范围，根据其位置从列表中获取值。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



这是另一个示例，使用命名范围对不同工作表中的2个单元格的值进行求和。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
{{< app/cells/assistant language="csharp" >}}
