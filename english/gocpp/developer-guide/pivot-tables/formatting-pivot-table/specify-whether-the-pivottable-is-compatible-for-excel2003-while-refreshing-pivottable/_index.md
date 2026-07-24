---
title: Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable with Golang via C++
linktitle: Specify Compatibility for Excel2003 in PivotTable
type: docs
weight: 80
url: /go-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Learn how to specify PivotTable compatibility for Excel2003 using Aspose.Cells for C++ while refreshing the PivotTable.
---

{{% alert color="primary" %}}

Aspose.Cells provides the [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/) property, which you can use to specify whether the PivotTable is compatible with Excel2003 while refreshing the PivotTable. If **true**, a string must be less than or equal to 255 characters, so if the string is greater than 255 characters, it will be truncated. If **false**, a string will not have the aforementioned restriction. The default value is **true**.

{{% /alert %}}

## **Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable**

The following sample code explains the usage of the [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/go-cpp/pivottable/isexcel2003compatible/) property. The original string is 383 characters long. However, when the **PivotTable.IsExcel2003Compatible** property is set to **true** and the pivot table is refreshed, the data in cell **B5** of the pivot table is truncated to 255 characters. Conversely, when the property is set to **false** and the pivot table is refreshed again, the data in cell **B5** is not truncated and remains 383 characters long. Please read the comments inside the code for a better understanding of this property.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyWhetherThePivottableIsCompatibleForExcel2003WhileRefreshingPivottable.go" >}}