---
title: 添加带有命名目标的 PDF 书签
type: docs
weight: 20
url: /zh/net/add-pdf-bookmarks-with-named-destinations/
---
## **可能的使用场景**

命名目标是 PDF 中不依赖于 PDF 页面的特殊类型的书签或链接。这意味着，如果在 PDF 中添加或删除页面，书签可能会失效，但命名目标将保持不变。要创建命名目标，请设置[**PdfBookmarkEntry.DestinationName**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry/properties/destinationname)财产。

## **添加带有命名目标的 PDF 书签**

请看下面的示例代码，其[源Excel文件](50528348.xlsx) , 及其[输出PDF文件](50528349.pdf).屏幕截图显示了输出 PDF 中的书签和命名目的地。屏幕截图还描述了如何查看命名目标以及您需要专业版的 Acrobat Reader。

![待办事项：图像_替代_文本](add-pdf-bookmarks-with-named-destinations_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-AddPDFBookmarksWithNamedDestinations.cs" >}}
