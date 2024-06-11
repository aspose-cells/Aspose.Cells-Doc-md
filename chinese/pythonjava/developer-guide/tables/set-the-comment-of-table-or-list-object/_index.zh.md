---
title: 设置表格或列表对象的注释
type: docs
weight: 60
url: /zh/python-java/set-the-comment-of-table-or-list-object/
---

## **设置工作表内表格或列表对象的批注**
Aspose.Cells for Python via Java支持添加列表对象注释。为此，API提供了[ListObject.Comment](https://reference.aspose.com/cells/python/asposecells.api/listobject#Comment)属性。由[ListObject.Comment](https://reference.aspose.com/cells/python/asposecells.api/listobject#Comment)属性添加的注释将显示在*xl/tables/tableName.xml*文件内。

以下截图显示了样本代码在红色矩形内创建的注释。

![todo:image_alt_text](setting-list-object-comment.png)

以下样本代码加载了[source excel file](source.xlsx)，设置了工作表内第一个表或列表对象的注释。 

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-SetTheCommentOfTableOrListObject.py" >}}
