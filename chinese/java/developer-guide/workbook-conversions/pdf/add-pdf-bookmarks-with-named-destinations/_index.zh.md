---
title: 使用命名目标添加PDF书签
type: docs
weight: 20
url: /zh/java/add-pdf-bookmarks-with-named-destinations/
---

## **可能的使用场景**

命名目标是PDF中不依赖于PDF页面的特殊书签或链接。 这意味着，如果从PDF中添加或删除页面，则书签可能变得无效，但命名目标将保持完整。 要创建命名目标，请设置[**PdfBookmarkEntry.DestinationName**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfbookmarkentry#DestinationName)属性。

## **使用命名目标添加PDF书签**

请参阅以下示例代码，其[source Excel file](50528370.xlsx)和其[output PDF file](50528369.pdf)。屏幕截图显示了输出PDF中的书签和命名目标。屏幕截图还描述了如何查看命名目标以及您需要Acrobat Reader的专业版本。

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-AddPDFBookmarksWithNamedDestinations.java" >}}
