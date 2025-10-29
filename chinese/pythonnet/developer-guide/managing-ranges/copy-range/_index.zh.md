---
title: 复制Excel的范围
linktitle: 复制范围
type: docs
weight: 105
url: /zh/python-net/copy-ranges-of-excel/
description: 本文描述了如何使用Aspose.Cells for Python via .NET库复制Excel的范围。
keywords: Python Excel库，Python如何复制Excel的范围，Python如何只复制Python Excel库的范围数据，Python如何带有选项粘贴范围，Python如何仅复制数据的范围。
---

## **介绍**

在Excel中，您可以选择一个范围，复制该范围，然后以特定选项粘贴到同一工作表、其他工作表或其他文件。

## **使用Aspose.Cells for Python Excel库复制范围**

Aspose.Cells for Python via .NET提供了一些重载的[**Range.copy**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range)方法来复制范围。
和[**Range.copy_style**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_style/#aspose.cells.Range)仅复制范围的样式；[**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range)仅复制范围的值

## **复制范围**

创建两个范围：源范围、目标范围，然后使用[**Range.copy**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range)方法将源范围复制到目标范围。

查看以下代码：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range.py" >}}

## **使用选项粘贴范围**

Aspose.Cells for Python via .NET支持粘贴具有特定类型的范围。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Paste-Range.py" >}}

## **仅复制数据的范围**
您还可以使用[**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range)方法复制数据，如下面的代码所示:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range-Data.py" >}}

## **高级主题**
- [将源范围的行高复制到目标范围](/cells/zh/python-net/copy-row-heights-of-source-range-to-destination-range/)


{{< app/cells/assistant language="python-net" >}}
