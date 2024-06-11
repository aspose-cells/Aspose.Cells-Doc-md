---
title: 检测循环引用
type: docs
weight: 70
url: /zh/java/detecting-circular-reference/
---

## **介绍**

工作簿可能存在循环引用，有时需要检测是否存在循环引用。

## **检测循环引用的概念**

只有在计算公式时才能检测循环引用，因为一个公式的引用通常依赖于其他部分或其他公式的计算结果。因此，为满足此需求（收集具有循环引用的单元格），在公式计算过程中我们提供了新的API：

[**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell)：表示正在计算的一个单元格的相关数据

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)）：在遇到循环引用时，公式计算引擎将调用此方法，枚举器中的元素是[**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell)个对象，表示一个循环中的所有单元格。返回的值表示公式引擎是否需要在此调用后计算这些循环引用中的单元格。

用户可以在[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)方法的实现中收集这些循环引用。

源示例文件可从以下链接下载：

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

从[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)类派生的* CircularMonitor *类的定义如下：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
