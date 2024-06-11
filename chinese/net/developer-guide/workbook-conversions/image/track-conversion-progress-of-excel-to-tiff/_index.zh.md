---
title: 跟踪Excel转换为TIFF的进度
type: docs
weight: 190
url: /zh/net/track-conversion-progress-of-excel-to-tiff/
---

## **可能的使用场景**

有时，转换大型Excel文件可能需要花费一些时间。在此期间，您可能希望显示文档转换进度，而不仅仅是加载屏幕，以增强应用程序的可用性。Aspose.Cells支持通过提供[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells/rendering/ipagesavingcallback)接口来跟踪文档转换过程。[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells/rendering/ipagesavingcallback)接口提供了[PageStartSaving](https://reference.aspose.com/cells/net/aspose.cells/rendering/ipagesavingcallback/methods/pagestartsaving)和[PageEndSaving](https://reference.aspose.com/cells/net/aspose.cells/rendering/ipagesavingcallback/methods/pageendsaving)方法，您可以在自定义类中实现。您还可以控制要呈现的页面，如*T​estPageSavingCallback*自定义类所示。

## **跟踪Excel转换为TIFF的进度**

以下代码示例加载了[source excel file](95584311.xlsx)，并通过使用实现**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**接口的*TestPageSavingCallback*自定义类在控制台中打印其转换进度。生成的输出文件附在此供参考。

[Output File](95584312.tiff)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

以下是*TestTiffPageSavingCallback*自定义类的代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

## **控制台输出**

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

