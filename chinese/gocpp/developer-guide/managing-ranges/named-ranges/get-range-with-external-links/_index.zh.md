---
title: 使用C++通过Golang获取带有外部链接的范围
linktitle: 获取带有外部链接的范围
type: docs
weight: 120
url: /zh/go-cpp/get-range-with-external-links/
description: 学习如何使用Aspose.Cells通过Golang获取带有外部链接的Excel文件中的范围。
---

## **获取带有外部链接的范围**

许多时候，Excel 文件通过外部链接访问其他 Excel 文件的数据。Aspose.Cells 提供通过 [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) 方法检索这些外部链接的选项。[**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) 方法返回类型为 [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) 的数组。[**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) 类提供一个 [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/) 属性，用于返回外部文件的名称。[**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) 类暴露以下成员。

- [**GetEndColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendcolumn/): 区域的结束列
- [**GetEndRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendrow/): 区域的结束行
- [**GetExternalFileName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getexternalfilename/): 获取外部文件名（如果这是外部引用）
- [**IsArea**](https://reference.aspose.com/cells/go-cpp/referredarea/isarea/): 表示这是否是一个区域
- [**IsExternalLink**](https://reference.aspose.com/cells/go-cpp/referredarea/isexternallink/): 表示这是不是外部链接
- [**GetSheetName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getsheetname/): 表示这引用在哪个工作表中
- [**GetStartColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartcolumn/): 区域的起始列
- [**GetStartRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartrow/): 区域的起始行

下面的示例代码演示了如何使用 [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) 方法获取带外部链接的范围。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRangeWithExternalLinks.go" >}}
