---
title: Track Document Conversion Progress with Golang via C++
linktitle: Track Document Conversion Progress
type: docs
weight: 970
url: /go-cpp/track-document-conversion-progress/
description: Learn how to track document conversion progress in C++ using Aspose.Cells to enhance application usability.
---

## **Possible Usage Scenarios**

Sometimes converting large Excel files can take some time. During this time, you might want to show the document conversion progress instead of just a loading screen to enhance the usability of your application. Aspose.Cells supports tracking document conversion progress by providing the [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) interface. The [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) interface provides [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) and [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/) methods that you can implement in your custom class. You may also control which pages are rendered as demonstrated in the `TestPageSavingCallback` custom class.

## **Track Document Conversion Progress**

The following code sample loads the [source Excel file](94896151.xlsx) and prints its conversion progress in the console by using the `TestPageSavingCallback` custom class that implements the [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) interface.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress.go" >}}
The following is the code for the `TestPageSavingCallback` custom class.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress-1.go" >}}
## **Console Output**

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