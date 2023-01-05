---
title: 访问工作表
type: docs
weight: 10
url: /zh/net/accessing-worksheet/
---
{{% alert color="primary" %}} 

工作表是 Excel 文件的组成部分。事实上，一个 Excel 文件是由一个或多个工作表组成的。每个工作表只能由最多 65,536 行和 256 列组成。它是将数据保存在 Excel 文件中的工作表。

Aspose.Cells.GridDesktop 可以创建和操作现有的和新的 Excel 文件，因此当然可以使用 Aspose.Cells.GridDesktop 访问工作表。本主题讨论如何。

{{% /alert %}} 
## **使用工作表索引**
开发人员可以使用任何所需工作表的工作表索引来访问任何工作表的实例，如下例所示。这种方法适用于遍历 Excel 文件中的多个工作表。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **使用工作表名称**
如果工作表的名称已知，则可以使用其名称访问工作表，如下所示。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **访问活动工作表**
一个 Excel 文件可能有多个工作表。用户正在处理的工作表称为活动工作表。可以访问活动工作表。

要访问活动工作表，Aspose.Cells.GridDesktop 提供了两种方法：
### **使用 AcriveSheetIndex 属性**
使用 Aspose.Cells.GridDesktop 控件访问活动工作表的一种方法是使用 GridDesktop 控件的 ActiveSheetIndex 属性。使用此属性，可以获得 Aspose.Cells.GridDesktop 控件中活动工作表的索引。然后可以使用该索引以传统方式访问工作表，如下所示。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **使用 GetActiveWorksheet 方法**
另一种方法是调用 GridDesktop 控件的 GetActiveWorksheet 方法。此方法提供对当前在 Aspose.Cells.GridDesktop 控件中处于活动状态的工作表的引用，如下所示。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
