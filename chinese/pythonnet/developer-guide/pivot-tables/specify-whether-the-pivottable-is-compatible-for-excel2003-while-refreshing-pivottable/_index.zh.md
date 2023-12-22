---
title: 刷新数据透视表时指定数据透视表是否兼容Excel2003
type: docs
weight: 80
url: /zh/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: 本文介绍如何在使用 Aspose.Cells for Python via .NET 刷新数据透视表时指定数据透视表是否与 Excel2003 兼容。
keywords: Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 提供[**数据透视表.is_excel_2003_兼容**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)刷新数据透视表时，您可以使用该属性指定数据透视表是否与 Excel2003 兼容。如果为 true，则字符串必须小于或等于 255 个字符，因此如果字符串大于 255 个字符，则会被截断。如果为“假”，则字符串将不受上述限制。默认值是true**。

{{% /alert %}}

##  **刷新数据透视表时指定数据透视表是否兼容Excel2003**

下面的示例代码解释了其用法[**数据透视表.is_excel_2003_兼容**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)财产。原始字符串长度为 383 个字符。但当[**数据透视表.is_excel_2003_兼容**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)属性已设置**真的**并且刷新数据透视表，数据透视表的单元格 B5 的数据被截断，长度变为 255 个字符。然而，当[**数据透视表.is_excel_2003_兼容**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)属性已设置**错误的**再次刷新数据透视表，数据透视表 B5 单元格的数据没有被截断，仍保留 383 个字符长。请阅读代码中的注释以更好地理解此属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
