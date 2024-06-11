---
title: 获取带有外部链接的范围
type: docs
weight: 60
url: /zh/python-java/get-range-with-external-links/
---

## **获取带有外部链接的范围**
在许多情况下，Excel文件通过外部链接访问其他Excel文件的数据。Aspose.Cells for Python via Java通过使用Name.GetReferredAreas方法提供了检索这些外部链接的选项。Name.GetReferredAreas方法返回[ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea)类型的数组。[ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea)类提供了返回外部文件名称的ExternalFileName属性。

以下代码段显示了如何获取外部链接。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
