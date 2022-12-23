---
title: 将工作表数据导出到数据表时忽略隐藏列
type: docs
weight: 330
url: /zh/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/
---
{{% alert color="primary" %}}

有时，您希望在将工作表数据导出到数据表时忽略隐藏的列。您可以使用 Aspose.Cells 通过设置来实现它[**ExportTableOptions.PlotVisibleColumns**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblecolumns)到**真的** .默认情况下，它的值为**错误的**，所以你需要设置它**真的**忽略隐藏的列。

{{% /alert %}}

下面的示例代码解释了[**ExportTableOptions.PlotVisibleColumns**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblecolumns)在将工作表整个数据导出到数据表时忽略隐藏列的属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-IgnoreHiddenColumnsDataTable-1.cs" >}}
