---
title: 合并函数
type: docs
weight: 20
url: /zh/java/consolidation-function/
description: 将数据字段应用于透视表的汇总函数。
---

## **合并函数**

Aspose.Cells 可用于将合并函数应用于数据透视表的数据字段（或值字段）。在 Microsoft Excel 中，您可以右键单击值字段，然后选择**值字段设置...**选项，然后选择**通过汇总值**选项卡。从那里，您可以选择任意合并函数，例如求和、计数、平均、最大值、最小值、乘积、唯一计数等。

Aspose.Cells 提供 [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) 枚举以支持以下合并函数。

- ConsolidationFunction.SUM
- ConsolidationFunction.COUNT
- ConsolidationFunction.AVERAGE
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP
- ConsolidationFunction.DISTINCT_COUNT

### **将合并函数应用于数据透视表的数据字段**

以下代码将 **AVERAGE** 汇总函数应用于第一个数据字段（或值字段），并将 **STD_DEV** 汇总函数应用于第二个数据字段（或值字段）。

可从此处下载示例源文件和输出文件进行测试示例代码:

[源 Excel 文件](source.xlsx)

[输出 Excel 文件](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

**唯一计数**合并函数仅受 Microsoft Excel 2013 支持。

{{% /alert %}}

