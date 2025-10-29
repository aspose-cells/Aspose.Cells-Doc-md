---
title: 用 Golang 通过 C++ 添加带有命名目标的 PDF 书签
linktitle: 使用命名目的地添加PDF书签
type: docs
weight: 20
url: /zh/go-cpp/add-pdf-bookmarks-with-named-destinations/
description: 学习如何使用 Aspose.Cells for C++ 添加带有命名目标的 PDF 书签。
---

## **可能的使用场景**

 命名目标是 PDF 中特殊类型的书签或链接，不依赖于 PDF 页。如果在 PDF 中添加或删除页面，书签可能失效，但命名目标将保持完整。要创建命名目标，请设置 [**PdfBookmarkEntry.GetDestinationName()**](https://reference.aspose.com/cells/go-cpp/pdfbookmarkentry/getdestinationname/) 属性。

## **使用命名目标添加PDF书签**

请查看以下示例代码，其 [源Excel文件](50528348.xlsx)，以及 [输出PDF文件](50528349.pdf)。屏幕截图显示了输出PDF中的书签和命名目标。屏幕截图还描述了如何查看命名目标，以及您需要Acrobat Reader的专业版。

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPdfBookmarksWithNamedDestinations.go" >}}
