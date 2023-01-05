---
title: 跟踪文档转换进度
type: docs
weight: 120
url: /zh/java/track-document-conversion-progress/
---
## **可能的使用场景**

有时转换大型 Excel 文件可能需要一些时间。在此期间，您可能希望显示文档转换进度而不仅仅是加载屏幕，以增强应用程序的可用性。 Aspose.Cells 通过提供支持跟踪文档转换过程**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**界面。这**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**接口提供**[PageStartSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs))**和**[PageEndSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs))**您可以在自定义类中实现的方法。您还可以控制呈现哪些页面，如*测试页面保存回调*自定义类。

## **跟踪文档转换进度**

以下代码示例加载[源文件](PagesBook1.xlsx)并使用*测试页面保存回调*实现的自定义类**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**界面。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

以下是代码*测试页面保存回调*自定义类。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

## **控制台输出**

开始保存第 11 页的第 0 页索引</br>
结束保存第 11 页的第 0 页索引</br>
开始保存第 11 页的第 1 页索引</br>
结束保存页面索引 1，共 11 页</br>
开始保存第 11 页的第 2 页索引</br>
结束保存第 11 页的第 2 页索引</br>
开始保存第 11 页的第 3 页索引</br>
结束保存第 11 页的第 3 页索引</br>
开始保存第 11 页的第 4 页索引</br>
结束保存页面索引 4，共 11 页</br>
开始保存第 11 页的第 5 页索引</br>
结束保存页面索引 5 of pages 11</br>
开始保存第 11 页的第 6 页索引</br>
结束保存页面索引 6 of pages 11</br>
开始保存第 11 页的第 7 页索引</br>
结束保存页面索引 7 of pages 11</br>
开始保存第 11 页的第 8 页索引</br>
结束保存页面索引 8，共 11 页
