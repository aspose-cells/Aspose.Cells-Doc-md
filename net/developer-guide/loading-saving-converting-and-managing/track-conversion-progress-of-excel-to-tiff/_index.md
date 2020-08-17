---
title: Track Conversion Progress of Excel to TIFF
type: docs
weight: 190
url: /net/track-conversion-progress-of-excel-to-tiff/
---

## **Possible Usage Scenarios**
Sometimes converting large excel files can take some time. During this time, you might want to show the document conversion progress instead of just a loading screen to enhance the usability of your application. Aspose.Cells supports tracking document conversion process by providing the [IPageSavingCallback](https://apireference.aspose.com/net/cells/aspose.cells.rendering/ipagesavingcallback) interface. The [IPageSavingCallback](https://apireference.aspose.com/net/cells/aspose.cells.rendering/ipagesavingcallback) interface provides [PageStartSaving](https://apireference.aspose.com/net/cells/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving) and [PageEndSaving](https://apireference.aspose.com/net/cells/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving) methods that you can implement in your custom class. You may also control which pages are rendered as demonstrated in the T*estPageSavingCallback* custom class.
## **Track Conversion Progress of Excel to TIFF**
The following code sample loads the [source excel file](95584311.xlsx) and prints its conversion progress in the console by using the *TestPageSavingCallback* custom class that implements the [IPageSavingCallback](https://apireference.aspose.com/net/cells/aspose.cells.rendering/ipagesavingcallback) interface. The output file generated is attached for your reference.

[Output File](95584312.tiff)
## **Sample Code**
{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

The following is the code for the *TestTiffPageSavingCallback* custom class.

{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}
## **Console Output**
Start saving page index 0 of pages 10
End saving page index 0 of pages 10
Start saving page index 1 of pages 10
End saving page index 1 of pages 10
Start saving page index 2 of pages 10
End saving page index 2 of pages 10
Start saving page index 3 of pages 10
End saving page index 3 of pages 10
Start saving page index 4 of pages 10
End saving page index 4 of pages 10
Start saving page index 5 of pages 10
End saving page index 5 of pages 10
Start saving page index 6 of pages 10
End saving page index 6 of pages 10
Start saving page index 7 of pages 10
End saving page index 7 of pages 10
Start saving page index 8 of pages 10
End saving page index 8 of pages 10
