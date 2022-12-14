---
title: 命名范围的设置公式
type: docs
weight: 20
url: /zh/net/setting-formula-for-named-range/
---
## **命名范围的设置公式**
与 Excel 应用程序一样，Aspose.Cells API 提供了在使用其命名范围时指定公式的能力[指的是](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto)财产。此功能可能有许多可用性场景，其中一些场景详述如下。
### **为命名范围设置一个简单的公式**
一个简单的公式可以是对相同（或不同）工作表中另一个单元格的引用。以下示例在新电子表格中创建一个命名范围并将其引用设置为另一个单元格。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **为命名范围设置复杂公式**
复杂的公式可以是任何东西，例如动态范围或跨越不同工作表中多个单元格的公式。以下示例使用 INDEX 函数创建一个动态范围，以根据其位置从列表中获取值。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



下面是另一个示例，它使用命名范围对不同工作表中 2 个单元格的值求和。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
