---
title: Track Document Conversion Progress
type: docs
weight: 120
url: /java/track-document-conversion-progress/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Sometimes converting large excel files can take some time. During this time, you might want to show the document conversion progress instead of just a loading screen to enhance the usability of your application. Aspose.Cells supports tracking document conversion process by providing the [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) interface. The [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) interface provides [**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving-com.aspose.cells.PageStartSavingArgs-) and [**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving-com.aspose.cells.PageEndSavingArgs-) methods that you can implement in your custom class. You may also control which pages are rendered as demonstrated in the *TestPageSavingCallback* custom class.

## **Track Document Conversion Progress**

The following code sample loads the [source excel file](PagesBook1.xlsx) and prints its conversion progress in the console by using the *TestPageSavingCallback* custom class that implements the [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) interface.

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

The following is the code for the *TestPageSavingCallback* custom class.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

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
{{< app/cells/assistant language="java" >}}
