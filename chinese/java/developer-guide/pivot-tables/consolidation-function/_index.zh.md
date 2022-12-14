---
title: 整合功能
type: docs
weight: 20
url: /zh/java/consolidation-function/
description: 将 ConsolidationFunction 应用于数据透视表的数据字段。
---
## **整合功能**

Aspose.Cells 可用于将 ConsolidationFunction 应用于数据透视表的数据字段（或值字段）。在Microsoft Excel中，您可以右键单击值字段，然后选择**值字段设置...**选项，然后选择选项卡**值汇总依据**.从那里，您可以选择您选择的任何 ConsolidationFunction，例如 Sum、Count、Average、Max、Min、Product、Distinct Count 等。

Aspose.Cells提供[**整合功能**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction)支持以下合并功能的枚举。

- 合并函数.SUM
- 合并函数.COUNT
- 合并函数.AVERAGE
- 合并函数.MAX
- 合并函数.MIN
- 合并函数.PRODUCT
- 合并函数.COUNT_NUMS
- 合并函数.STD_DEV
- 合并函数.STD_DEVP
- 合并函数.VAR
- 合并函数
- 合并函数.DISTINCT_COUNT

### **将 ConsolidationFunction 应用于数据透视表的数据字段**

以下代码适用**平均**合并功能到第一个数据字段（或值字段）和**标准偏差**合并功能到第二个数据字段（或值字段）。

可以从此处下载示例源文件和输出文件以测试示例代码：

[源 Excel 文件](source.xlsx)

[输出 Excel 文件](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

Microsoft 仅 Excel 2013 支持 DistinctCount 合并函数。

{{% /alert %}}

