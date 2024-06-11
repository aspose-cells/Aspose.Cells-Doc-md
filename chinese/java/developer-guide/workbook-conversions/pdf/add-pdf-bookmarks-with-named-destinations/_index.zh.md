---
title: 使用命名目的地添加PDF书签
type: docs
weight: 20
url: /zh/java/add-pdf-bookmarks-with-named-destinations/
---

## **可能的使用场景**

命名目标是PDF中特殊类型的书签或链接，不依赖于PDF页面。这意味着，如果PDF中添加或删除页面，书签可能会失效，但命名目标将保持完整。要创建命名目标，请设置 [**PdfBookmarkEntry.DestinationName**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfbookmarkentry#DestinationName) 属性。

## **使用命名目标添加PDF书签**

请参阅以下示例代码，其源Excel文件，和输出PDF文件。屏幕截图显示输出PDF内的书签和命名目标。屏幕截图还描述了如何查看命名目标以及您需要专业版本的Acrobat Reader。

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-AddPDFBookmarksWithNamedDestinations.java" >}}
