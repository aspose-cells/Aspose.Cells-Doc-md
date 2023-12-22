---
title: 检测循环参考
description: 本文介绍如何使用Aspose.Cells库检测Microsoft Excel中的循环引用。通过加载现有的Excel文件或者创建一个新的Excel文件，我们可以使用Aspose.Cells提供的方法来检测循环引用并得到结果。最后，我们将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells, Excel, circular references, detection
type: docs
weight: 70
url: /zh/net/detecting-circular-reference/
---
##  **介绍**

工作簿可以有循环引用，有时需要检测是否存在循环引用。

##  **检测循环引用背后的概念**

循环引用只有在计算公式时才能检测到，因为一个公式的引用通常依赖于其他部分或其他公式的计算结果。因此我们在公式计算过程中针对这一需求（收集具有循环引用的单元格）提供了新的API：

[**计算单元格**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell)：代表计算正在计算的某个cell的相关数据

[**AbstractCalculationMonitor.OnCircular(IEnumeratorcircularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular)：遇到循环引用时会被公式计算引擎调用，枚举器中的元素为[**计算单元格**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell)代表一圈中所有细胞的对象。返回值表示公式引擎是否需要在调用后循环计算这些单元格。

用户可以在实现时收集这些循环引用[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular)方法。

源示例文件可以从以下链接下载：

[循环公式.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

的定义*圆形监视器*派生自的类[**抽象计算监视器**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)类如下：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
