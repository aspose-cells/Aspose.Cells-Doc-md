---
title: 合并或取消合并单元格范围
type: docs
weight: 190
url: /zh/python-net/merge-or-unmerge-range-of-cells/
description: 本文描述了如何使用Aspose.Cells for Python via .NET库在Excel中合并和拆分单元格范围。
keywords: Python Excel库，Python合并和拆分单元格，Python合并和拆分单元格范围，使用Python合并和拆分单元格范围。
---

## **可能的使用场景**

您可以使用Aspose.Cells for Python via .NET来合并或拆分一系列单元格。Aspose.Cells for Python via .NET提供了[**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#)和[**Range.un_merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/un_merge/#)方法来实现这一目的。本文解释了如何将一系列单元格合并为单个单元格。


## **如何合并或拆分单元格范围**

以下示例代码首先创建范围 - A1:D4 - 然后使用 [**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#) 方法将范围中的单元格合并为单个单元格。类似地，您可以通过创建范围并调用 [**Range.un_merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/un_merge/#) 方法来拆分单元格。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-MergeUnmergeRangeOfCells-1.py" >}}
