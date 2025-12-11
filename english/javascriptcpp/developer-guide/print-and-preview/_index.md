---  
title: Preview workbook with JavaScript via C++  
linktitle: Preview workbook  
type: docs  
weight: 70  
url: /javascript-cpp/workbook-and-worksheet-preview/  
description: Aspose.Cells supports printing and previewing Excel files without Microsoft Excel installation using JavaScript via C++.  
---  

## **Print Preview**  

There may be cases where Excel files with millions of pages need to be converted to PDF or images. Processing such files will consume a lot of time and resources. In such cases, the Workbook and Worksheet Print Preview feature might prove to be useful. Before converting such files, the user can check the total number of pages and then decide whether the file is to be converted or not. This article focuses on using the [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) and [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) classes to find out the total number of pages.  

Aspose.Cells provides the print preview feature. For this, the API provides [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) and [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) classes. To create the print preview of the whole workbook, create an instance of the [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) class by passing [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/) and [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) objects to the constructor. The [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) class provides an [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--) method which returns the number of pages in the generated preview. Similar to the [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) class, the [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) class is used to generate a print preview for a specific worksheet. To create the print preview of a worksheet, create an instance of the [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) class by passing [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/) and [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) objects to the constructor. The [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) class also provides an [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--) method which returns the number of pages in the generated preview.  

The following code snippet demonstrates the use of both [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) and [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) classes by using the **sample Excel file** (94896177.xlsx).  

### **Sample Code**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Printing Preview</title>
    </head>
    <body>
        <h1>Printing Preview Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, WorkbookPrintingPreview, SheetPrintingPreview } = AsposeCells;
        
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Creating image/print options
            const imgOptions = new ImageOrPrintOptions();

            // Workbook printing preview
            const preview = new WorkbookPrintingPreview(workbook, imgOptions);
            const workbookPageCount = preview.evaluatedPageCount;
            console.log("Workbook page count: " + workbookPageCount);

            // Worksheet printing preview for first worksheet
            const preview2 = new SheetPrintingPreview(workbook.worksheets.get(0), imgOptions);
            const worksheetPageCount = preview2.evaluatedPageCount;
            console.log("Worksheet page count: " + worksheetPageCount);

            document.getElementById('result').innerHTML = `<p>Workbook page count: ${workbookPageCount}</p><p>Worksheet page count: ${worksheetPageCount}</p>`;
        });
    </script>
</html>
```  

The following is the output generated by executing the above code.  

### **Console Output**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Advanced topics**  
- [Configuring Fonts for Rendering Spreadsheets](/cells/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Convert Worksheet to Image - Remove whitespace around data](/cells/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Converting Worksheet to Image and Worksheet to Image by Page](/cells/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [Converting Worksheet to Image using ImageOrPrint Options](/cells/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Export Range of Cells in a Worksheet to Image](/cells/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Export Worksheet or Chart into Image with Desired Width and Height](/cells/javascript-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [Extract Images from Worksheets using ImageOrPrintOptions](/cells/javascript-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Generate Thumbnail of the Worksheet](/cells/javascript-cpp/generate-thumbnail-of-the-worksheet/)  
- [Output Blank Page when there is Nothing to Print](/cells/javascript-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Page Setup and Printing Options](/cells/javascript-cpp/page-setup-and-printing-options/)  
- [Render Sequence of Pages using PageIndex and PageCount Properties of ImageOrPrintOptions](/cells/javascript-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Render Worksheet to Graphic Context](/cells/javascript-cpp/render-worksheet-to-graphic-context/)  
- [Specify Individual or Private Set of Fonts for Workbook Rendering](/cells/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)