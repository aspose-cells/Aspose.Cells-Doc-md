---
title: 合并或拆分单元格范围
type: docs
weight: 190
url: /zh/python-net/merge-or-unmerge-range-of-cells/
description: 本文介绍了如何在Excel中使用Aspose.Cells for Python通过.NET库合并和取消合并范围中的单元格。
keywords: Python Excel库，Python合并和取消合并单元格，Python合并和取消合并单元格在范围内，使用Python合并和取消合并范围中的单元格。
---

## **可能的使用场景**

您可以使用Aspose.Cells for Python通过.NET来合并或拆分一系列单元格。Aspose.Cells for Python通过.NET提供了此目的的[**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#)和[**Range.un_merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/un_merge/#)方法。本文解释了如何将一系列单元格合并为单个单元格。


## **如何合并或取消合并单元格范围**

下面的示例代码首先创建一个范围 - A1:D4 - 然后使用[**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#)方法将范围中的单元格合并为单个单元格。类似地，您可以通过创建范围并调用[**Range.un_merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/un_merge/#)方法来拆分单元格。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-MergeUnmergeRangeOfCells-1.py" >}}
