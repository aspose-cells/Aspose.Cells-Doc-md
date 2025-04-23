---
title: 刷新和计算包含计算项的数据透视表
type: docs
weight: 40
url: /zh/nodejs-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

 Aspose.Cells for Node.js via C++现在支持刷新和计算包含计算项的数据透视表。请照常使用[**PivotTable.refreshData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#refreshdata--)和[**PivotTable.calculateData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#calculatedata--)执行此功能。

{{% /alert %}}

## **刷新和计算包含计算项的数据透视表**

 以下示例代码加载了包含三个计算项（如"加法"、"除法"、"除法2"）的数据透视表的[源Excel文件](5115238.xlsx)。我们首先将单元格D2的值改为20，然后使用Aspose.Cells for Node.js via C++ API刷新并计算数据透视表，并以PDF格式保存工作簿。输出PDF(5115229.pdf)显示Aspose.Cells for Node.js via C++成功刷新并计算了含有计算项的数据透视表。你可以通过在单元格D2手动输入20，然后使用Alt+F5快捷键或点击数据透视表的刷新按钮，验证其效果。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTable-RefreshAndCalculateItems-1.js" >}}

