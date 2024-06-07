---
title: 跟踪Excel到TIFF的转换进度
type: docs
weight: 190
url: /zh/net/track-conversion-progress-of-excel-to-tiff/
---

## **可能的使用场景**

有时转换大型Excel文件可能需要一些时间。在此期间，您可能希望显示文档转换进度，而不仅仅是一个加载屏幕，以增强您的应用程序的可用性。Aspose.Cells支持通过提供[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)接口来追踪文档转换过程。IPageSavingCallback接口提供了PageStartSaving和PageEndSaving方法，您可以在自定义类中实现这些方法。您还可以控制渲染哪些页面，就像在TestPageSavingCallback自定义类中演示的那样。

## **跟踪Excel到TIFF的转换进度**

以下代码示例加载了源Excel文件，并通过实现[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)接口的TestPageSavingCallback自定义类，在控制台中打印其转换进度。生成的输出文件附在此处供您参考。

[输出文件](95584312.tiff)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

以下是TestTiffPageSavingCallback自定义类的代码。

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

