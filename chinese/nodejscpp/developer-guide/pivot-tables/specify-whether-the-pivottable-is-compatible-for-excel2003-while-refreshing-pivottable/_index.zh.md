---
title: 指定在刷新数据透视表时数据透视表是否兼容Excel2003
type: docs
weight: 80
url: /zh/nodejs-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

 Aspose.Cells for Node.js via C++提供[**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-)属性，可用来指定在刷新数据透视表时是否兼容Excel2003。如果为true，字符串长度必须小于等于255字符，如果超过，字符将被截断。若为**false**，则没有上述限制。默认值为**true**。

{{% /alert %}}

## **指定在刷新数据透视表时数据透视表是否兼容Excel2003**

以下示例代码解释了使用[**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-)属性的用法。原始字符串长度为383个字符。但是当将[**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-)属性设置为**true**并刷新数据透视表时，数据透视表的单元格B5的数据将被截断，并变为255个字符长。然而，当将[**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-)属性设置为**false**并再次刷新数据透视表时，数据透视表的单元格B5的数据不会被截断，保持383个字符长度。请阅读代码中的注释以更好地理解此属性。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyCompatibility-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
