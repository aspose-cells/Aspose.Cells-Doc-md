---
title: Track Conversion Progress of Excel to TIFF with Node.js via C++
linktitle: Track Conversion Progress of Excel to TIFF
type: docs
weight: 190
url: /nodejs-cpp/track-conversion-progress-of-excel-to-tiff/
description: Learn how to track the conversion progress of Excel files to TIFF using Aspose.Cells for Node.js via C++. Enhance user experience during the conversion process.
---

## **Possible Usage Scenarios**

Sometimes converting large Excel files can take some time. During this time, you might want to show the document conversion progress instead of just a loading screen to enhance the usability of your application. Aspose.Cells for Node.js via C++ supports tracking document conversion process by providing the [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) interface. The [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) interface provides [**PageStartSaving**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/methods/pagestartsaving) and [**PageEndSaving**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/methods/pageendsaving) methods that you can implement in your custom class. You may also control which pages are rendered as demonstrated in the *TestPageSavingCallback* custom class.

## **Track Conversion Progress of Excel to TIFF**

The following code sample loads the [source excel file](95584311.xlsx) and prints its conversion progress in the console by using the *TestPageSavingCallback* custom class that implements the [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) interface. The output file generated is attached for your reference.

[Output File](95584312.tiff)

## **Sample Code**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = RunExamples.Get_SourceDirectory();

// Output directory
const outputDir = RunExamples.Get_OutputDirectory();

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setPageSavingCallback(new TestTiffPageSavingCallback());
opts.setImageType(AsposeCells.ImageType.Tiff);

const wr = new AsposeCells.WorkbookRender(workbook, opts);
wr.toImage(path.join(outputDir, "DocumentConversionProgressForTiff_out.tiff"));
```

The following is the code for the *TestTiffPageSavingCallback* custom class.

```javascript
const AsposeCells = require("aspose.cells.node");

class TestTiffPageSavingCallback {
    pageStartSaving(args) {
        console.log(`Start saving page index ${args.pageIndex} of pages ${args.pageCount}`);

        // Don't output pages before page index 2.
        if (args.pageIndex < 2) {
            args.setIsToOutput(false);
        }
    }

    pageEndSaving(args) {
        console.log(`End saving page index ${args.pageIndex} of pages ${args.pageCount}`);

        // Don't output pages after page index 8.
        if (args.pageIndex >= 8) {
            args.setHasMorePages(false);
        }
    }
}
```

## **Console Output**

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
