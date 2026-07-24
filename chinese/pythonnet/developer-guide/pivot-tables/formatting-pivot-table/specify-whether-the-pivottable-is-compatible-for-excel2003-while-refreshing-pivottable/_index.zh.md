---
title: 指定在刷新数据透视表时数据透视表是否兼容Excel2003
type: docs
weight: 80
url: /zh/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: 本文介绍如何使用Aspose.Cells for Python via .NET指定在刷新数据透视表时数据透视表是否兼容Excel2003。
keywords: Aspose.Cells for Python Excel, Excel Python库，指定在刷新数据透视表时数据透视表是否兼容Excel2003。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET提供了[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)属性，您可以使用它来指定在刷新数据透视表时数据透视表是否兼容Excel2003。如果设置为true，字符串的长度必须小于或等于255个字符，因此如果字符串大于255个字符，则会被截断。如果为false，字符串不会受到前述限制。默认值为true。

{{% /alert %}}

## **如何指定在刷新数据透视表时数据透视表是否兼容Excel2003**

以下示例代码解释了使用[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)属性的用法。原始字符串长度为383个字符。但是当将[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)属性设置为**true**并刷新数据透视表时，数据透视表的单元格B5的数据将被截断，并变为255个字符长。然而，当将[**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/)属性设置为**false**并再次刷新数据透视表时，数据透视表的单元格B5的数据不会被截断，保持383个字符长度。请阅读代码中的注释以更好地理解此属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
