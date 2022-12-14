---
title: 使用外部链接获取范围
type: docs
weight: 60
url: /zh/python-java/get-range-with-external-links/
---
## **使用外部链接获取范围**
在许多情况下，excel 文件通过使用外部链接从其他 excel 文件访问数据。 Aspose.Cells for Python via Java 提供了通过使用检索这些外部链接的选项[名称.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)） 方法。这[名称.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) 方法返回类型数组[推荐区域](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea).这[推荐区域](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea)类提供了一个[外部文件名](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName)返回外部文件名称的属性。

以下代码片段显示了如何获取外部链接。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
