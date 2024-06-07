---
title: 设置表格或列表对象的注释
type: docs
weight: 60
url: /zh/python-java/set-the-comment-of-table-or-list-object/
---

## **设置工作表内表格或列表对象的注释**
通过Java的Aspose.Cells for Python支持添加列表对象的注释。为此，API提供[ListObject.Comment](https://reference.aspose.com/cells/python/asposecells.api/listobject#Comment)属性。通过[ListObject.Comment](https://reference.aspose.com/cells/python/asposecells.api/listobject#Comment)属性添加的注释将在*xl/tables/tableName.xml*文件中显示。

下面的屏幕截图显示了样本代码创建的评论，位于红色矩形中。

![todo:image_alt_text](setting-list-object-comment.png)

以下示例代码加载[source excel file](source.xlsx)，设置工作表内第一个表或列表对象的评论 

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-SetTheCommentOfTableOrListObject.py" >}}
