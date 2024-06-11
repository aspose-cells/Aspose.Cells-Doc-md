---
title: 获取带有外部链接的范围
type: docs
weight: 120
url: /zh/python-net/get-range-with-external-links/
description: 本文介绍了如何通过Aspose.Cells for Python via .NET API获取带有外部链接的范围。
keywords: Python Excel库，Python获取带有外部链接的范围。
---

## **获取带有外部链接的范围**

许多时候，Excel文件通过外部链接访问其他Excel文件中的数据。Aspose.Cells for Python via .NET提供了使用[**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool)方法检索这些外部链接的选项。[**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool)方法返回类型为[**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea)的数组。[**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea)类提供了[**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/)属性，返回外部文件的名称。[**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea)类公开了以下成员。

- [**end_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_column/)：区域的结束列
- [**end_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_row/)：区域的结束行
- [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/)：如果这是外部引用，获取外部文件名
- [**is_area**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_area/): 表示这是否为一个区域
- [**is_external_link**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_external_link/): 表示这是否为外部链接
- [**sheet_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/sheet_name/): 表示此引用所在的工作表
- [**start_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_column): 区域的起始列
- [**start_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_row): 区域的起始行

下面给出的示例代码演示了使用 [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) 方法获取带有外部链接的范围。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Worksheets-GetRangeWithExternalLinks-1.py" >}}
