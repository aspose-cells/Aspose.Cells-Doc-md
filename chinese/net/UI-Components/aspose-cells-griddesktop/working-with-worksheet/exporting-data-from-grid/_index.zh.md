---
title: 从Grid中导出数据
type: docs
weight: 60
url: /zh/net/aspose-cells-griddesktop/export-data-from-grid/
keywords: GridDesktop,导出,数据,导出数据
description: 本文介绍了如何在GridDesktop中导出数据。
---

{{% alert color="primary" %}} 

在我们上一个主题中，我们已经讨论了将DataTable的内容导入到Aspose.Cells.GridDesktop控件中，但故意没有提到Aspose.Cells.GridDesktop也支持相反的过程。因此，在本主题中，我们将讨论如何将Aspose.Cells.GridDesktop控件中的数据导出到一个DataTable中。

{{% /alert %}} 
## **导出网格内容**
### **导出到特定DataTable**
要将网格内容导出到特定的DataTable对象，请按照以下步骤操作：将Aspose.Cells.GridDesktop控件添加到您的**Form**中。

- 根据需要创建一个特定的DataTable对象。
- 将所选**Worksheet**的数据导出到您指定的DataTable对象。

在下面的示例中，我们创建了一个具有四列的特定DataTable对象。最后，我们将工作表数据（从第一个包含69行和4列的单元格开始）导出到我们已经创建的DataTable对象。

**示例：**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **导出到新DataTable**
有时候，开发人员可能对创建自己的DataTable对象不感兴趣，只想将工作表数据导出到一个新的DataTable对象。对于开发人员来说，只需将工作表数据导出到新的DataTable对象可能是更快的方式。

在下面的示例中，我们尝试一种不同的方法来解释ExportDataTable方法的使用。我们引用了当前活动的工作表，然后将该活动工作表的所有数据导出到一个新的DataTable对象。现在，这个DataTable对象可以按开发人员的需要使用。仅举一个例子，开发人员可能会将此DataTable对象绑定到DataGrid以查看数据。

**示例：**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

在上述情况下，我们将使用ExportDataTable方法的一个重载版本，该方法将简单地返回一个包含从工作表导出的数据的新DataTable对象。

{{% /alert %}}
