---
title: 跟踪Excel转换为TIFF的进度
type: docs
weight: 190
url: /zh/net/track-conversion-progress-of-excel-to-tiff/
---

## **可能的使用场景**

有时转换大型Excel文件可能需要一些时间。在此期间，您可能希望显示文档转换进度，而不只是加载屏幕，以增强应用程序的可用性。Aspose.Cells支持通过提供[**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)接口来跟踪文档转换进程。[**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)接口提供了[**PageStartSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving)和[**PageEndSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving)方法，您可以在自定义类中实现。还可以控制呈现哪些页面，如T*estPageSavingCallback*自定义类所示。

## **跟踪Excel转换为TIFF的进度**

以下代码示例加载[源 Excel 文件](95584311.xlsx)，并通过使用实现了 [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback) 接口的 *TestPageSavingCallback* 自定义类在控制台中打印其转换进度。生成的输出文件已附上供您参考。

[Output File](95584312.tiff)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

以下是*TestTiffPageSavingCallback*自定义类的代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

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
