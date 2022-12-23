---
title: 添加带有命名目标的 PDF 书签
type: docs
weight: 20
url: /zh/java/add-pdf-bookmarks-with-named-destinations/
---
## **可能的使用场景**

命名目标是 PDF 中不依赖于 PDF 页面的特殊类型的书签或链接。这意味着，如果从 PDF 添加或删除页面，书签可能会失效，但命名的目的地将保持不变。要创建命名目标，请设置[**PdfBookmarkEntry.DestinationName**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfbookmarkentry#DestinationName)财产。

## **添加带有命名目标的 PDF 书签**

请看下面的示例代码，其[源Excel文件](50528370.xlsx)及其[输出 PDF 文件](50528369.pdf).屏幕截图显示了输出 PDF 中的书签和命名目标。屏幕截图还描述了如何查看命名目标以及您需要专业版的 Acrobat Reader。

![待办事项：图片_替代_文本](add-pdf-bookmarks-with-named-destinations_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-AddPDFBookmarksWithNamedDestinations.java" >}}
