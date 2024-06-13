---
title: 跟踪文档转换进度
type: docs
weight: 120
url: /zh/java/track-document-conversion-progress/
---

## **可能的使用场景**

有时，转换大型Excel文件可能需要一些时间。在此期间，您可能希望显示文档转换进度，而不仅仅是一个加载屏幕，以增强应用程序的可用性。Aspose.Cells支持通过提供[**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)接口来跟踪文档转换过程。[**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)接口提供[**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs))和[**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs))方法，您可以在自定义类中实现这些方法。您还可以控制渲染哪些页面，就像*TestPageSavingCallback*自定义类中所演示的那样。

## **跟踪文档转换进度**

以下代码示例通过使用实现了[**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)接口的*TestPageSavingCallback*自定义类，在控制台中打印出[source excel file](PagesBook1.xlsx)的转换进度。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

以下是*TestPageSavingCallback*自定义类的代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

## **控制台输出**

{{< highlight java >}}

Start saving page index 0 of pages 11</br>
End saving page index 0 of pages 11</br>
Start saving page index 1 of pages 11</br>
End saving page index 1 of pages 11</br>
Start saving page index 2 of pages 11</br>
End saving page index 2 of pages 11</br>
Start saving page index 3 of pages 11</br>
End saving page index 3 of pages 11</br>
Start saving page index 4 of pages 11</br>
End saving page index 4 of pages 11</br>
Start saving page index 5 of pages 11</br>
End saving page index 5 of pages 11</br>
Start saving page index 6 of pages 11</br>
End saving page index 6 of pages 11</br>
Start saving page index 7 of pages 11</br>
End saving page index 7 of pages 11</br>
Start saving page index 8 of pages 11</br>
End saving page index 8 of pages 11

{{< /highlight >}}
