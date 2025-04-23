---
title: 检测循环引用
description: 本文介绍如何使用Aspose.Cells库在Microsoft Excel中检测循环引用。 通过加载现有的Excel文件或创建一个新文件，我们可以使用Aspose.Cells提供的方法来检测循环引用并获得结果。 最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, 循环引用, 检测
type: docs
weight: 70
url: /zh/net/detecting-circular-reference/
---

## **介绍**

工作簿可能存在循环引用，有时需要检测是否存在循环引用。

## **检测循环引用的概念**

只有在计算公式时才能检测循环引用，因为一个公式的引用通常依赖于其他部分或其他公式的计算结果。因此，为满足此需求（收集具有循环引用的单元格），在公式计算过程中我们提供了新的API：

[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell)：表示正在计算的一个单元格的相关数据

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): 在遇到循环引用时，将由公式计算引擎调用此方法，枚举器中的元素是一个[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell)对象，它代表一个循环中的所有单元格。 返回的值表示公式引擎在此调用后是否需要计算这些循环中的单元格。

用户可以在[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular)方法的实现中收集这些循环引用。

源示例文件可从以下链接下载：

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

从[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)类派生的* CircularMonitor *类的定义如下：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
{{< app/cells/assistant language="csharp" >}}
