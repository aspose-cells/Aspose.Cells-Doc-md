---
title: Pdf with JavaScript via C++
linktitle: Pdf
type: docs
weight: 220
url: /javascript-cpp/convert-excel-to-pdf/
description: Learn how to convert Excel Workbook into PDF using Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}
Aspose.Cells supports conversion of Excel Workbook into PDF. In this example, we will see the complete conversion of an Excel Workbook into PDF.
{{% /alert %}}

## **Converting Excel Workbook to PDF**

PDF files are widely used to exchange documents between organizations, government sectors, and individuals. It is a standard document format and software developers are often asked to find a way to convert Microsoft Excel files into PDF documents.

Aspose.Cells supports converting Excel files to PDF and maintains high visual fidelity in the conversion.

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ directly writes information about the API and version number in output documents. For example, upon rendering a document to PDF, Aspose.Cells for JavaScript via C++ populates the **PDF Producer** field with a value, e.g., 'Aspose.Cells v23.2'.

Please note that you can change this information in output documents by the [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#producer--) property.
{{% /alert %}}

### **Direct Conversion**

Aspose.Cells for JavaScript via C++ supports conversion from spreadsheets to PDF independently of other software. Simply save an Excel file to PDF using the [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class's [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) method. The [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) method provides the [**SaveFormat.Pdf**](https://reference.aspose.com/cells/javascript-cpp/saveformat) enumeration member that converts the native Excel files to PDF format.

Follow the below steps to directly convert the Excel spreadsheets to PDF format:

1. Instantiate an object of the [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class by calling its empty constructor.  
2. You may open/load an existing template file or skip this step if you are creating the workbook from scratch.  
3. Do any work (input data, apply formatting, set formulas, insert pictures or other drawing objects, and so on) on the spreadsheet using Aspose.Cells' APIs.  
4. When the spreadsheet code is complete, call the [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) class's [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) method to save the spreadsheet.

The file format should be PDF, so select *Pdf* (a pre‑defined value) from the [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat) enumeration to generate the final PDF document.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        
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

            // Instantiate the Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the document in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion to PDF completed! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

### **Advanced Conversion**

You may also opt to use the [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) class to set different attributes for the conversion. Setting different properties of the [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) class gives you control over the print, font, security and compression settings for the output PDF. 

The most important property is [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--) which enables you to set the PDF standards compliance level. Currently, you can save to PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-3b, and PDF/A-3u formats. Note that with the PDF/A format, an output file size is larger than a regular PDF file size.

#### **Saving Workbook to PDF/A Compliant Files**

The below‑provided code snippet demonstrates how to use the [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) class to save Excel files to PDF/A compliant PDF format.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create PDF/A from Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfCompliance } = AsposeCells;
        
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
            // Instantiate new workbook
            const workbook = new Workbook();

            // Insert a value into the A1 cell in the first worksheet
            workbook.worksheets.get(0).cells.get(0, 0).value = "Testing PDF/A";

            // Define PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set the compliance type
            pdfSaveOptions.compliance = PdfCompliance.PdfA1b;

            // Save the file to PDF with options
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF/A File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF/A created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Please note, the [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--) property was added with the release of Aspose.Cells for JavaScript via C++ 5.3.0.
{{% /alert %}}

#### **Set the PDF Creation Time**

With the [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) class, you can get or set the PDF creation time. The following code demonstrates the use of [**PdfSaveOptions.createdTime**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#createdTime--) property to set the creation time of the PDF file.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SaveFormat, Utils } = AsposeCells;
        
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
            
            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            
            // Create an instance of PdfSaveOptions
            const options = new PdfSaveOptions();
            options.createdTime = new Date();
            
            // Save the workbook to PDF format while passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **Set ContentCopyForAccessibility option**

With the [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) class, you can get or set the PDF **PdfSecurityOptions.accessibilityExtractContent** option to control the content access in the converted PDF.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Convert to PDF with Security Options</title>
    </head>
    <body>
        <h1>Convert Excel to PDF with Security Options</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfSecurityOptions, Utils } = AsposeCells;
        
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const pdfSaveOpt = new PdfSaveOptions();

            // Create an instance of PdfSecurityOptions
            const securityOptions = new PdfSecurityOptions();

            // Set AccessibilityExtractContent to false (converted from setAccessibilityExtractContent(false))
            securityOptions.accessibilityExtractContent = false;

            // Set the security option in the PdfSaveOptions (converted from setSecurityOptions)
            pdfSaveOpt.securityOptions = securityOptions;

            // Save the workbook to PDF format while passing the PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOpt);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outFile.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

#### **Export Custom properties to PDF**

With the [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) class, you can export the custom properties in the source workbook to the PDF. The [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/javascript-cpp/pdfcustompropertiesexport/) enumerator is provided for specifying the way by which properties are exported. These properties can be observed in Adobe Acrobat Reader by clicking on **File** and then **Properties** as shown in the following image. Template file **sourceWithCustProps.xlsx** can be downloaded [here](sourceWithCustProps.xlsx) for testing and output PDF file **outSourceWithCustProps.pdf** is available [here](outSourceWithCustProps.pdf) for analysis.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF with Custom Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfCustomPropertiesExport } = AsposeCells;
        
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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
            pdfSaveOptions.customPropertiesExport = PdfCustomPropertiesExport.Standard;

            // Save the workbook to PDF format while passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourceWithCustProps.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

### **Conversion Attributes**

We work to enhance the conversion features with each new release. Aspose.Cells' Excel to PDF conversion still has a couple of limitations. MapChart is not supported when converting to PDF format. Also, some drawing objects are not supported well.

The table that follows lists all features that are fully or partially supported when exporting to PDF using Aspose.Cells. This table is not final and does not cover all the spreadsheet attributes, but it does identify those features that are not supported or partially supported for conversion to PDF.

|**Document Element**|**Attribute**|**Supported**|**Notes**|
| :- | :- | :- | :- |
|Alignment| |Yes| |
|Background settings| |Yes| |
|Border|Color|Yes| |
|Border|Line style|Yes| |
|Border|Line width|Yes| |
|Cell Data| |Yes| |
|Comments| |Yes| |
|Conditional Formatting| |Yes| |
|Document Properties| |Yes| |
|Drawing Objects| |Partially|Shadow and 3‑D effects for drawing objects are not supported well; WordArt and SmartArt are partially supported.|
|Font|Size|Yes| |
|Font|Color|Yes| |
|Font|Style|Yes| |
|Font|Underline|Yes| |
|Font|Effects|Yes| |
|Images| |Yes| |
|Hyperlink| |Yes| |
|Charts| |Partially|MapChart is not supported.|
|Merged Cells| |Yes| |
|Page Break| |Yes| |
|Page Setup|Header/Footer|Yes| |
|Page Setup|Margins|Yes| |
|Page Setup|Page Orientation|Yes| |
|Page Setup|Page Size|Yes| |
|Page Setup|Print Area|Yes| |
|Page Setup|Print Titles|Yes| |
|Page Setup|Scaling|Yes| |
|Row Height/Column Width| |Yes| |
|RTL (Right to Left) Language| |Yes| |

{{% alert color="primary" %}}
If your spreadsheet contains formulas, it is best to call [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula‑dependent values are recalculated, and the correct values are rendered in the PDF.
{{% /alert %}}

## **Advanced topics**
- [Add PDF Bookmarks with Named Destinations](/cells/javascript-cpp/add-pdf-bookmarks-with-named-destinations/)
- [Avoid Blank Page in Output PDF when there is Nothing to Print](/cells/javascript-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Change the Font on just the specific Unicode characters while saving to PDF](/cells/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Convert XLSX File to PDF Format](/cells/javascript-cpp/convert-xlsx-file-to-pdf-format/)
- [Convert Excel file to PDF format compatible with PDFA-1a](/cells/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Convert XLS File with Images or Charts to PDF](/cells/javascript-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Create PdfBookmarkEntry for Chart Sheet](/cells/javascript-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Fit All Worksheet Columns on Single PDF Page](/cells/javascript-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Get DrawObject and Bound while rendering to PDF using DrawObjectEventHandler class](/cells/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Get Warnings for Font Substitution while Rendering Excel File](/cells/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignore Errors while Rendering Excel to PDF](/cells/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Limit the Number of Pages Generated - Excel to PDF Conversion](/cells/javascript-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Print Comments while saving to PDF](/cells/javascript-cpp/print-comments-while-saving-to-pdf/)
- [Render Office Add-Ins while converting Excel to PDF](/cells/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Render One PDF Page Per Excel Worksheet - Excel to PDF Conversion](/cells/javascript-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Render Unicode Supplementary characters in output PDF by Aspose.Cells](/cells/javascript-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Resampling Added Images - Excel to PDF Conversion](/cells/javascript-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Save Each Worksheet to a Different PDF File](/cells/javascript-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Save Excel into PDF with Standard or Minimum Size](/cells/javascript-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Save Specified Worksheets to PDF](/cells/javascript-cpp/save-specified-worksheets-to-pdf/)
- [Secure PDF Documents](/cells/javascript-cpp/secure-pdf-documents/)
- [Specify how to cross string in output PDF and image](/cells/javascript-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)