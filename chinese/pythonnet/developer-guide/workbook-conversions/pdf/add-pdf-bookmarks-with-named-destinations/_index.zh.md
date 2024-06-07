---
title: 使用命名目标添加PDF书签
type: docs
weight: 20
url: /zh/python-net/add-pdf-bookmarks-with-named-destinations/
description: 了解如何使用Aspose.Cells for Python通过.NET API添加具有命名目标的PDF书签
keywords: 使用Python向具有命名目标的PDF文件添加PDF书签
---

## **可能的使用场景**

命名目标是PDF中不依赖于PDF页面的特殊书签或链接。 这意味着，如果从PDF中添加或删除页面，则书签可能变得无效，但命名目标将保持完整。 要创建命名目标，请设置[**PdfBookmarkEntry.destination_name**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfbookmarkentry/destination_name/)属性。

## **使用命名目标添加PDF书签**

请查看以下示例代码、其[source Excel file](50528348.xlsx)和[output PDF file](50528349.pdf)。屏幕截图显示了输出PDF内的书签和命名目标。该截图还描述了如何查看命名目标以及您需要Acrobat Reader的专业版。

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AddPDFBookmarksWithNamedDestinations.py" >}}
