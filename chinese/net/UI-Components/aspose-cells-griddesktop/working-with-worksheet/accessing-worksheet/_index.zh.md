---
title: 访问工作表
type: docs
weight: 10
url: /zh/net/aspose-cells-griddesktop/access-worksheet/
keywords: GridDesktop，工作表
description: 本文介绍了如何在GridDesktop中处理工作表。
---

{{% alert color="primary" %}} 

工作表是Excel文件的一个组成部分。实际上，一个Excel文件由一个或多个工作表组成。每个工作表最多只能由65,536行和256列组成。工作表保存Excel文件中的数据。

Aspose.Cells.GridDesktop可以创建和操作现有的和新的Excel文件，因此，当然有一种方法可以使用Aspose.Cells.GridDesktop访问工作表。本话题讨论了如何。

{{% /alert %}} 
## **使用工作表索引**
开发人员可以通过在示例中显示的任何所需工作表的工作表索引访问任何工作表的一个实例。这种方法非常适合在Excel文件中遍历多个工作表。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **使用工作表名称**
如果知道工作表的名称，可以像下面展示的那样使用其名称访问工作表。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **访问活动工作表**
可以有多个工作表的Excel文件。用户正在使用的工作表称为活动工作表。可以访问活动工作表。

访问活动工作表有两种方法：
### **使用ActiveSheetIndex属性**
使用Aspose.Cells.GridDesktop控件访问活动工作表的一种方法是使用GridDesktop控件的ActiveSheetIndex属性。使用该属性可以获取Aspose.Cells.GridDesktop控件中活动工作表的索引。然后可以使用该索引以传统方式访问工作表。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **使用GetActiveWorksheet方法**
另一种方法是调用GridDesktop控件的GetActiveWorksheet方法。该方法显示了当前在Aspose.Cells.GridDesktop控件中活动的工作表的引用。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
