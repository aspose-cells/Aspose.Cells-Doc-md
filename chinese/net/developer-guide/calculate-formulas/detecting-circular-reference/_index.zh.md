---
title: 检测循环引用
type: docs
weight: 70
url: /zh/net/detecting-circular-reference/
---
## **介绍**

工作簿可以有循环引用，有时需要检测是否存在循环引用。

## **检测循环引用背后的概念**

循环引用只有在计算公式时才能检测到，因为一个公式的引用通常依赖于其他部分或其他公式的计算结果。所以我们在公式计算的过程中针对这个需求（收集循环引用的单元格）提供了新的API：

[**计算单元格**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell)代表正在计算一个cell的相关数据的计算

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular)遇到循环引用时会被公式计算引擎调用，枚举器中的元素为[**计算单元格**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell)代表一个圆圈中所有单元格的对象。返回值表示在本次调用后公式引擎是否需要循环计算这些单元格。

用户可以在执行时收集那些循环引用[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular)方法。

可以从以下链接下载源示例文件：

[循环公式.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

的定义*圆形显示器*派生自的类[**抽象计算监视器**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)类如下：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
