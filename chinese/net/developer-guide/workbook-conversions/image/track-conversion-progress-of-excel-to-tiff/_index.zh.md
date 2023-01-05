---
title: 跟踪 Excel 到 TIFF 的转换进度
type: docs
weight: 190
url: /zh/net/track-conversion-progress-of-excel-to-tiff/
---
## **可能的使用场景**

有时转换大型 Excel 文件可能需要一些时间。在此期间，您可能希望显示文档转换进度而不仅仅是加载屏幕，以增强应用程序的可用性。 Aspose.Cells 通过提供支持跟踪文档转换过程**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**界面。这**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**接口提供**[PageStartSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving)**和**[PageEndSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving)**您可以在自定义类中实现的方法。您还可以控制呈现哪些页面，如 T 中所示*estPageSavingCallback*自定义类。

## **跟踪 Excel 到 TIFF 的转换进度**

以下代码示例加载[源文件](95584311.xlsx)并使用*测试页面保存回调*实现的自定义类**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**界面。附上生成的输出文件供您参考。

[输出文件](95584312.tiff)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

以下是代码*测试 TiffPageSavingCallback*自定义类。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

## **控制台输出**

开始保存第 10 页的第 0 页索引</br>
结束保存页面索引 0 of pages 10</br>
开始保存第 10 页的第 1 页索引</br>
结束保存页面索引 1 of pages 10</br>
开始保存第 10 页的第 2 页索引</br>
结束保存第 10 页的第 2 页索引</br>
开始保存第 10 页的第 3 页索引</br>
结束保存第 10 页的第 3 页索引</br>
开始保存第 10 页的第 4 页索引</br>
结束保存页面索引 4 of pages 10</br>
开始保存第 10 页的第 5 页索引</br>
结束保存第 10 页的第 5 页索引</br>
开始保存第 10 页的第 6 页索引</br>
结束保存页面索引 6 of pages 10</br>
开始保存第 10 页的第 7 页索引</br>
结束保存页面索引 7 of pages 10</br>
开始保存第 10 页的第 8 页索引</br>
结束保存页面索引 8，共 10 页</br>

