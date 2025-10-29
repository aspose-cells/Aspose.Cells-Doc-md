---
title: 使用 Golang 通过 C++ 跟踪 Excel 转 TIFF 的转换进度
linktitle: 跟踪Excel转换为TIFF的进度
type: docs
weight: 190
url: /zh/go-cpp/track-conversion-progress-of-excel-to-tiff/
description: 学习如何使用Aspose.Cells for C++跟踪Excel文件转换为TIFF格式的进度。
---

## **可能的使用场景**

有时转换大型Excel文件可能需要一些时间。在此期间，你可能想显示文件转换的进度，而不是仅显示加载屏幕，以增强应用程序的可用性。Aspose.Cells支持通过提供[**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/)接口来跟踪文档转换进度。[**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/)接口提供[**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/)和[**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/)方法，你可以在自定义类中实现。你也可以控制哪些页面被渲染，具体演示请参考*TestPageSavingCallback*自定义类。

## **跟踪Excel转换为TIFF的进度**

以下代码示例加载了[源Excel文件](95584311.xlsx)，并利用实现了[**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/)接口的*TestPageSavingCallback*自定义类在控制台打印其转换进度。生成的输出文件已附在参考资料中。

[Output File](95584312.tiff)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff.go" >}}
以下是*TestTiffPageSavingCallback*自定义类的代码。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff-1.go" >}}
## **控制台输出**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
