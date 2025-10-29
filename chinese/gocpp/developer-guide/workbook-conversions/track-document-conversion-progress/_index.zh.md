---
title: 使用C++通过Golang跟踪文档转换进度
linktitle: 跟踪文档转换进度
type: docs
weight: 970
url: /zh/go-cpp/track-document-conversion-progress/
description: 学习如何使用Aspose.Cells在C++中跟踪文档转换进度，以增强应用程序的可用性。
---

## **可能的使用场景**

有时转换大型Excel文件可能需要一些时间。在此期间，你可能想显示文档转换进度，而不是加载页面，以提升应用程序的用户体验。Aspose.Cells通过提供 [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) 接口支持跟踪文档转换进度。[**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) 接口提供 [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) 和 [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/) 方法，你可以在自定义类中实现这些方法。你也可以控制哪些页面被渲染，如在 `TestPageSavingCallback` 自定义类中展示的那样。

## **跟踪文档转换进度**

以下代码示例加载[源Excel文件](94896151.xlsx)，并使用实现了 [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) 接口的 `TestPageSavingCallback` 自定义类，在控制台打印其转换进度。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress.go" >}}
以下是 `TestPageSavingCallback` 自定义类的代码。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress-1.go" >}}
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
