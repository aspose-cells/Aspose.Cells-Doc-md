---
title: 从网格导出数据
type: docs
weight: 60
url: /zh/net/exporting-data-from-grid/
---
{{% alert color="primary" %}} 

在我们之前的主题中，我们谈到了将 DataTable 的内容导入到 Aspose.Cells.GridDesktop 控件，但我们故意没有提到 Aspose.Cells.GridDesktop 也支持相反的过程。因此，在本主题中，我们将讨论如何将 Aspose.Cells.GridDesktop 控件中的数据导出到 DataTable。

{{% /alert %}} 
## **导出网格内容**
### **导出到特定数据表**
要将 Grid 内容导出到特定的 DataTable 对象，请按照以下步骤操作：将 Aspose.Cells.GridDesktop 控件添加到您的**形式**.

- 根据您的需要创建特定的 DataTable 对象。
- 导出选定的数据**工作表**到您指定的 DataTable 对象。

在下面给出的示例中，我们创建了一个内部有四列的特定 DataTable 对象。最后，我们将工作表数据（从具有 69 行和 4 列的第一个单元格开始）导出到我们已经创建的 DataTable 对象。

**例子：**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **导出到新数据表**
有时，开发人员可能对创建自己的 DataTable 对象不感兴趣，可能只需要将工作表数据导出到新的 DataTable 对象。对于开发人员来说，仅导出工作表数据将是更快捷的方式。

在下面给出的示例中，我们尝试了不同的方式来解释 ExportDataTable 方法的用法。我们引用了当前活动的工作表，然后将该活动工作表的完整数据导出到新的 DataTable 对象。现在，这个 DataTable 对象可以以开发人员想要的任何方式使用。举个例子，开发人员可以将此 DataTable 对象绑定到 DataGrid 以查看数据。

**例子：**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

在上述情况下，我们将使用 ExportDataTable 方法的重载版本，该方法将简单地返回一个包含从工作表导出的数据的新 DataTable 对象。

{{% /alert %}}
