---
title: 指定在刷新数据透视表时数据透视表是否兼容Excel2003
type: docs
weight: 80
url: /zh/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells提供了[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)属性，您可以使用该属性来指定在刷新数据透视表时数据透视表是否兼容Excel2003。 如果为true，则字符串必须小于或等于255个字符，因此，如果字符串大于255个字符，它将被截断。如果为**false**，字符串将不受前述限制。默认值为**true**。

{{% /alert %}}

## **指定在刷新数据透视表时数据透视表是否兼容Excel2003**

以下示例代码解释了使用[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)属性的用法。原始字符串长度为383个字符。但是当将[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)属性设置为**true**并刷新数据透视表时，数据透视表的单元格B5的数据将被截断，并变为255个字符长。然而，当将[**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)属性设置为**false**并再次刷新数据透视表时，数据透视表的单元格B5的数据不会被截断，保持383个字符长度。请阅读代码中的注释以更好地理解此属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
