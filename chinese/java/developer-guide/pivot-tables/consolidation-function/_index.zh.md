---
title: 合并函数
type: docs
weight: 20
url: /zh/java/consolidation-function/
description: 将合并函数应用于数据透视表的数据字段
---

## **合并函数**

Aspose.Cells 可用于将合并函数应用于数据透视表的数据字段（或值字段）。在 Microsoft Excel 中，您可以右键单击值字段，然后选择“值字段设置...”选项，然后选择选项卡“按以下方式汇总值”。从那里，您可以选择任何您喜欢的合并函数，如求和、计数、平均值、最大值、最小值、乘积、去重计数等。

Aspose.Cells提供[**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction)枚举以支持以下合并功能。

-ConsolidationFunction.SUM
-ConsolidationFunction.COUNT
-ConsolidationFunction.AVERAGE
-ConsolidationFunction.MAX
-ConsolidationFunction.MIN
-ConsolidationFunction.PRODUCT
-ConsolidationFunction.COUNT_NUMS
-ConsolidationFunction.STD_DEV
-ConsolidationFunction.STD_DEVP
-ConsolidationFunction.VAR
-ConsolidationFunction.VARP
-ConsolidationFunction.DISTINCT_COUNT

### **应用合并功能到数据字段的数据透视表**

以下代码将**AVERAGE**合并函数应用于第一个数据字段（或值字段），并将**STD_DEV**合并函数应用于第二个数据字段（或值字段）。

可从此处下载示例源文件和输出文件以测试示例代码：

[源Excel文件](source.xlsx)

[输出Excel文件](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

Microsoft Excel 2013仅支持去重计数合并功能。

{{% /alert %}}

