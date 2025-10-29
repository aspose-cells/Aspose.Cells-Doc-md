---
title: 使用命名目的地添加PDF书签
type: docs
weight: 20
url: /zh/python-net/add-pdf-bookmarks-with-named-destinations/
description: 学习如何使用Aspose.Cells for Python via .NET API添加PDF书签及命名目标。
keywords: 使用Python添加PDF书签及命名目标
---

## **可能的使用场景**

命名目标是PDF中特殊类型的书签或链接，不依赖于PDF页面。这意味着，如果PDF中添加或删除页面，书签可能会失效，但命名目标将保持完整。要创建命名目标，请设置 [**PdfBookmarkEntry.destination_name**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/destination_name/) 属性。

## **使用命名目标添加PDF书签**

请查看以下示例代码，其 [源Excel文件](50528348.xlsx)，以及 [输出PDF文件](50528349.pdf)。屏幕截图显示了输出PDF中的书签和命名目标。屏幕截图还描述了如何查看命名目标，以及您需要Acrobat Reader的专业版。

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AddPDFBookmarksWithNamedDestinations.py" >}}
{{< app/cells/assistant language="python-net" >}}
