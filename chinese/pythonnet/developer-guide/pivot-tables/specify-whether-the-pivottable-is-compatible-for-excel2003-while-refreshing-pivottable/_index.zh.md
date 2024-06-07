---
title: 指定在更新数据透视表时，数据透视表是否兼容Excel2003
type: docs
weight: 80
url: /zh/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: 本文介绍了如何在刷新数据透视表时指定数据透视表是否兼容Excel2003，使用 Aspose.Cells for Python 通过 .NET。
keywords: Aspose.Cells for Python Excel，Excel Python库，刷新数据透视表时指定数据透视表是否兼容Excel2003
---

{{% alert color="primary" %}}

Aspose.Cells for Python 通过 .NET 提供了[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)属性，您可以在刷新数据透视表时指定数据透视表是否兼容Excel2003。如果为true，字符串长度必须小于或等于255个字符，因此如果字符串长度大于255个字符，它将被截断。如果为false，则字符串不受上述限制。默认值为true。

{{% /alert %}}

## **如何在刷新数据透视表时指定数据透视表是否兼容Excel2003**

以下示例代码解释了[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)属性的用法。原始字符串长度为383个字符。但当[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)属性设置为**true**并刷新数据透视表时，数据透视表的单元格B5的数据将被截断，长度变为255个字符。然而，当[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)属性设置为**false**并再次刷新数据透视表时，数据透视表的单元格B5的数据不会被截断，仍为383个字符长。请阅读代码内的评论以更好地理解此属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
