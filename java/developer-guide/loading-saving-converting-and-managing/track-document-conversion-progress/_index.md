---
title: Track Document Conversion Progress
type: docs
weight: 120
url: /java/track-document-conversion-progress/
---

## **Possible Usage Scenarios**

Sometimes converting large excel files can take some time. During this time, you might want to show the document conversion progress instead of just a loading screen to enhance the usability of your application. Aspose.Cells supports tracking document conversion process by providing the **[IPageSavingCallback](https://apireference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)** interface. The **[IPageSavingCallback](https://apireference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)** interface provides **[PageStartSaving](https://apireference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs))** and **[PageEndSaving](https://apireference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs))** methods that you can implement in your custom class. You may also control which pages are rendered as demonstrated in the *TestPageSavingCallback* custom class.

## **Track Document Conversion Progress**

The following code sample loads the [source excel file](PagesBook1.xlsx) and prints its conversion progress in the console by using the *TestPageSavingCallback* custom class that implements the **[IPageSavingCallback](https://apireference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)** interface.

## **Sample Code**

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

The following is the code for the *TestPageSavingCallback* custom class.

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

## **Console Output**

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
