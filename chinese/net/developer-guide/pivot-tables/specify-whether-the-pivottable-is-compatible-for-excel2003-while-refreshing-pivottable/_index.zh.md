---
title: 刷新数据透视表时指定数据透视表是否兼容Excel2003
type: docs
weight: 80
url: /zh/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}}

Aspose.Cells 提供了[**数据透视表.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)刷新数据透视表时可用于指定数据透视表是否与 Excel2003 兼容的属性。如果为 true，则字符串必须小于或等于 255 个字符，因此如果字符串大于 255 个字符，它将被截断。如果**错误的**，字符串不会有上述限制。默认值为**真的**.

{{% /alert %}}

## **刷新数据透视表时指定数据透视表是否兼容Excel2003**

下面的示例代码解释了[**数据透视表.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)财产。原始字符串的长度为 383 个字符。但当[**数据透视表.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)属性已设置**真的**数据透视表刷新后，数据透视表B5单元格的数据被截断，变成255个字符长。然而，当[**数据透视表.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)属性已设置**错误的**再次刷新数据透视表，数据透视表B5单元格的数据没有被截断，仍然是383个字符长。请阅读代码中的注释以更好地理解此属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
