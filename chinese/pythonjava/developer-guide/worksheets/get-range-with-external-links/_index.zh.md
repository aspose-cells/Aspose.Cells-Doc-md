---
title: 获取带有外部链接的范围
type: docs
weight: 60
url: /zh/python-java/get-range-with-external-links/
---

## **获取带有外部链接的范围**
有许多情况下，Excel文件通过外部链接访问其他Excel文件中的数据。Aspose.Cells for Python via Java通过使用[Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\))方法来检索这些外部链接。[Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\))方法返回[ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea)类型的数组。[ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea)类提供[ExternalFileName](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName)属性，返回外部文件的名称。

以下代码片段显示了如何获取外部链接。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
