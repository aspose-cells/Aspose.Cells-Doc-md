---
title: 访问工作表
type: docs
weight: 10
url: /zh/net/aspose-cells-griddesktop/access-worksheet/
keywords: GridDesktop，工作表
description: 本文介绍如何在GridDesktop中处理工作表。
---

{{% alert color="primary" %}} 

工作表是Excel文件的一个重要部分。事实上，一个Excel文件由一个或多个工作表组成。每个工作表最多只能由65,536行和256列组成。正是工作表在Excel文件中保存数据。

Aspose.Cells.GridDesktop可以创建和操作现有和新的Excel文件，因此当然有一种方法可以使用Aspose.Cells.GridDesktop访问工作表。本主题讨论了如何操作。

{{% /alert %}} 
## **使用工作表索引**
开发人员可以使用所需工作表的工作表索引来访问任何工作表的实例，如下例所示。这种方法非常适合在Excel文件中迭代多个工作表。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **使用工作表名称**
如果知道工作表的名称，则可以使用其名称访问工作表，如下所示。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **访问活动工作表**
Excel文件可能具有多于一个的工作表。用户正在操作的工作表称为活动工作表。可以访问活动工作表。

要访问活动工作表，Aspose.Cells.GridDesktop提供了两种方法：
### **使用AcriveSheetIndex属性**
使用Aspose.Cells.GridDesktop控件访问活动工作表的一种方法是使用GridDesktop控件的ActiveSheetIndex属性。使用此属性可以获取Aspose.Cells.GridDesktop控件中活动工作表的索引。然后可以像下面所示那样使用该索引访问工作表。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **使用GetActiveWorksheet方法**
另一种方法是调用GridDesktop控件的GetActiveWorksheet方法。该方法提供了Aspose.Cells.GridDesktop控件中当前活动的工作表的引用，如下所示。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
