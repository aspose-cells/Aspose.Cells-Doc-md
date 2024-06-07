---
title: 设置命名范围的公式
type: docs
weight: 20
url: /zh/net/setting-formula-for-named-range/
---

## **为命名范围设置公式**
与Excel应用程序一样，Aspose.Cells API在使用其RefersTo属性时提供了为具名范围指定公式的能力。这个功能有许多使用场景，以下是其中一些详细描述。
### **为具名范围设置简单公式**
简单公式可以是对同一工作表（或不同工作表）中另一个单元格的引用。下面的示例在新电子表格中创建了一个具名范围，并将其引用设置为另一个单元格。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **为具名范围设置复杂公式**
复杂公式可以是任何东西，比如一个动态范围或跨多个工作表的多个单元格的公式。以下示例使用INDEX函数创建一个动态范围，以根据其位置从列表中获取值。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



这里有另一个示例，使用一个具名范围来汇总来自不同工作表中2个单元格的值。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
