---
title: 从Grid中导出数据
type: docs
weight: 60
url: /zh/net/aspose-cells-griddesktop/export-data-from-grid/
keywords: GridDesktop，导出，数据，导出数据
description: 本文介绍如何在GridDesktop中导出数据。
---

{{% alert color="primary" %}} 

在前面的话题中，我们已经讨论了如何将DataTable的内容导入到Aspose.Cells.GridDesktop控件，但我们特意没有提到Aspose.Cells.GridDesktop也支持相反的过程。因此，在这个话题中，我们将讨论如何将Aspose.Cells.GridDesktop控件中的数据导出到DataTable中。

{{% /alert %}} 
## **导出Grid内容**
### **导出到特定的DataTable**
要将Grid内容导出到特定的DataTable对象，请按照以下步骤进行：将Aspose.Cells.GridDesktop控件添加到您的**表单**中。

- 根据您的需求创建一个特定的DataTable对象。
- 将所选的**工作表**数据导出到您指定的DataTable对象。

在下面的示例中，我们创建了一个特定的DataTable对象，该对象内部有四列。最后，我们将工作表数据（从第一个单元格开始，共69行4列）导出到由我们创建的DataTable对象中。

**示例：**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **导出到新的DataTable**
有时，开发人员可能对创建自己的DataTable对象不感兴趣，而只是需要简单地将工作表数据导出到一个新的DataTable对象。对于开发人员来说，仅仅将工作表数据导出到新的DataTable对象是更快速的方式。

在下面的示例中，我们尝试通过不同的方式来解释ExportDataTable方法的用法。我们使用了当前处于活动状态的工作表的引用，然后将该活动工作表的完整数据导出到一个新的DataTable对象中。现在，这个DataTable对象可以按照开发人员的意愿进行使用。举个例子，开发人员可以将这个DataTable对象绑定到DataGrid上以查看数据。

**示例：**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

在上述情况下，我们将使用ExportDataTable方法的重载版本，该方法将简单地返回一个包含从工作表导出的数据的新DataTable对象。

{{% /alert %}}
