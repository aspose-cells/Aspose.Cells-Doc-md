---
title: 检测循环引用
description: 本文介绍如何使用Aspose.Cells库在Microsoft Excel中检测循环引用。通过加载现有的Excel文件或创建新文件，我们可以使用Aspose.Cells提供的方法检测循环引用并获取结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells、Excel、循环引用、检测
type: docs
weight: 70
url: /zh/net/detecting-circular-reference/
---

## **介绍**

工作簿可能存在循环引用，有时需要检测是否存在循环引用。

## **检测循环引用背后的概念**

只有在计算公式时才能检测到循环引用，因为一个公式的引用通常依赖于其他部分或其他公式的计算结果。因此，我们在公式计算过程中为此需求提供了新的API（用于收集具有循环引用的单元格）：

[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell)：表示正在计算的一个单元格的相关数据的计算

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular)：在遇到循环引用时会被公式计算引擎调用，枚举器中的元素是[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell)对象，代表一个循环中的所有单元格。返回的值表示公式引擎在此调用后是否需要计算这些循环中的单元格。

用户可以在[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular)方法的实现中收集这些循环引用。

可以从以下链接下载源示例文件：

[循环公式.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

定义了* CircularMonitor *类，该类继承自[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)类，如下所示：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
