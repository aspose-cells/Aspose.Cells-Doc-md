---  
title: Track Document Conversion Progress with Node.js via C++  
linktitle: Track Document Conversion Progress  
type: docs  
weight: 970  
url: /nodejs-cpp/track-document-conversion-progress/  
description: Learn how to track document conversion progress in Excel files using Aspose.Cells for Node.js via C++.  
---  

## **Possible Usage Scenarios**  

Sometimes converting large Excel files can take some time. During this time, you might want to show the document conversion progress instead of just a loading screen to enhance the usability of your application. Aspose.Cells for Node.js via C++ supports tracking document conversion process by providing the [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) interface. The [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) interface provides [**pageStartSaving**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-number-) and [**pageEndSaving**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-number-) methods that you can implement in your custom class. You may also control which pages are rendered as demonstrated in the *TestPageSavingCallback* custom class.  

## **Track Document Conversion Progress**  

The following code sample loads the [source excel file](94896151.xlsx) and prints its conversion progress in the console by using the *TestPageSavingCallback* custom class that implements the [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) interface.  

## **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = RunExamples.Get_SourceDirectory();
// Output directory
const outputDir = RunExamples.Get_OutputDirectory();

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "PagesBook1.xlsx"));

const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setPageSavingCallback(new TestPageSavingCallback());

workbook.save(path.join(outputDir, "DocumentConversionProgress.pdf"), pdfSaveOptions);
```  

The following is the code for the *TestPageSavingCallback* custom class.  

```javascript
const AsposeCells = require("aspose.cells.node");

class TestPageSavingCallback {
    pageStartSaving(args) {
        console.log(`Start saving page index ${args.getPageIndex()} of pages ${args.getPageCount()}`);

        // don't output pages before page index 2.
        if (args.getPageIndex() < 2) {
            args.setIsToOutput(false);
        }
    }

    pageEndSaving(args) {
        console.log(`End saving page index ${args.getPageIndex()} of pages ${args.getPageCount()}`);

        // don't output pages after page index 8.
        if (args.getPageIndex() >= 8) {
            args.setHasMorePages(false);
        }
    }
}
```  

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
  