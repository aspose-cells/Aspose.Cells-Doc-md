---
title: 结合 C++ 和 Golang 实现汇总函数
linktitle: 合并函数
type: docs
weight: 20
url: /zh/go-cpp/consolidation-function/
description: 学习如何结合 C++ 和 Golang 使用 Aspose.Cells 将汇总函数应用到数据透视表字段
---

## **合并函数**

Aspose.Cells 可用于将合并函数应用于数据透视表的数据字段（或值字段）。在 Microsoft Excel 中，您可以右键单击值字段，然后选择“值字段设置...”选项，然后选择选项卡“按以下方式汇总值”。从那里，您可以选择任何您喜欢的合并函数，如求和、计数、平均值、最大值、最小值、乘积、去重计数等。

Aspose.Cells提供[**ConsolidationFunction**](https://reference.aspose.com/cells/go-cpp/consolidationfunction/)枚举以支持以下合并功能。

- 汇总函数::平均值
- 汇总函数::计数
- 汇总函数::计数字符串
- 汇总函数::唯一计数
- 汇总函数::最大值
- 汇总函数::最小值
- 汇总函数::乘积
- 汇总函数::标准偏差
- 汇总函数::总体标准偏差
- 汇总函数::总和
- 汇总函数::方差
- 汇总函数::总体方差

### **应用合并功能到数据字段的数据透视表**

以下代码将**平均值**整合函数应用于第一个数据字段（或数值字段），将**不重复计数**整合函数应用于第二个数据字段（或数值字段）。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConsolidationFunction.go" >}}
{{% alert color="primary" %}}

Microsoft Excel 2013仅支持去重计数合并功能。

{{% /alert %}}
