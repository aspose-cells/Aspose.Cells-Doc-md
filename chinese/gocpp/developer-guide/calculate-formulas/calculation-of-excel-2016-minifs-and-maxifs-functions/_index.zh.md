---
title: 使用C++和Golang计算Excel 2016的MINIFS和MAXIFS函数
description: 本文介绍如何使用Aspose.Cells库在C++中计算Microsoft Excel 2016的MINIFS和MAXIFS函数。
keywords: Aspose.Cells, Excel, 2016, MINIFS函数, MAXIFS函数, 计算
type: docs
weight: 300
url: /zh/go-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **可能的使用场景**
Microsoft Excel 2016支持MINIFS和MAXIFS函数。这些函数在Excel 2013或更早版本中不支持。Aspose.Cells也支持这些函数的计算。以下截图展示了这些函数的用法。请阅读截图中的红色注释，了解它们是如何工作的。

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **计算Excel 2016的MINIFS和MAXIFS函数**
下面的示例代码加载[示例Excel文件](5115149.xlsx)，调用[Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)方法通过Aspose.Cells执行公式计算，然后将结果保存为[输出PDF](5115154.pdf)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculationOfExcel2016MinifsAndMaxifsFunctions.go" >}}
