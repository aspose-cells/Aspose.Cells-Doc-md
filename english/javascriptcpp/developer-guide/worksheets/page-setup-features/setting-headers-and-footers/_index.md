---
title: Setting Headers and Footers with JavaScript via C++
linktitle: Setting Headers and Footers
type: docs
weight: 30
url: /javascript-cpp/setting-headers-and-footers/
description: This article explains how to programmatically insert an image in the header and footer of Excel worksheets using Aspose.Cells for JavaScript via C++. 
keywords: insert image in excel header footer JavaScript via C++, set excel header footer script commands JavaScript via C++
---

{{% alert color="primary" %}}

Headers and footers are the lines of text displayed below the top margin or above the bottom margin respectively. It's possible to add headers and footers to the worksheets also. Headers and footers can be used to display useful information like page number, author name, topic name, or date and time. Headers and footers are managed using the page setup settings.

{{% /alert %}}

## **Setting Headers and Footers**

Aspose.Cells for JavaScript via C++ allows you to add headers and footers to worksheets at runtime but we recommend setting headers and footers manually in a pre-designed file for printing. You can use Microsoft Excel as a GUI tool to set headers and footers to save effort and development time. Aspose.Cells can import the file and save the settings.

To add headers and footers at runtime, Aspose.Cells provides special API calls and script commands to format headers and footers.

### **Script Commands**

Script commands are special commands that allow you to set header and footer formatting.

|**Script Commands**|**Description**|
| :- | :- |
|&P|The current page number|
|&G|A picture|
|&N|The total number of pages|
|&D|The current date|
|&T|The current time|
|&A|The worksheet name|
|&F|The file name without its path|
|&&Text|Shows &Text. For example: &&WO will be displayed as &WO|
|&"\<FontName>"|Represents a font name. For example: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Represents font name with style. For example: &"Arial,Bold"|
|&\<FontSize>|Represents font size. For example: “&14abc”. But, if this command is followed by a plain number to be printed in the header, this should be separated with a space character from the font size. For example: “&14 123”.|

### **Set Headers and Footers**

The [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) class provides two methods, [**header(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-string-) and [**footer(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-string-), used to add a header and footer to a worksheet. These methods take only two parameters:

- **Section** – the section where the header or footer should be placed. There are three sections: left, center and right, represented by 0, 1 and 2 respectively.
- **Script** – the script to be used for the header or footer. This script contains script commands to format headers or footers.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Set Headers and Footers Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;

            // Setting worksheet name at the left section of the header
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[0] = "&A";

            // Setting current date and current time at the central section of the header
            // and changing the font of the header
            pageSetup.header[1] = "&\"Times New Roman,Bold\"&D-&T";

            // Setting current file name at the right section of the header and changing the
            // font of the header
            pageSetup.header[2] = "&\"Times New Roman,Bold\"&12&F";

            // Setting a string at the left section of the footer and changing the font
            // of a part of this string ("123")
            pageSetup.footer = pageSetup.footer || [];
            pageSetup.footer[0] = "Hello World! &\"Courier New\"&14 123";

            // Setting the current page number at the central section of the footer
            pageSetup.footer[1] = "&P";

            // Setting page count at the right section of footer
            pageSetup.footer[2] = "&N";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetHeadersAndFooters_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers and footers set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Insert an Image into a Header or Footer**

The [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) class has two additional methods, [**headerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#headerPicture-number-numberarray-) and [**footerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footerPicture-number-numberarray-), used to add pictures into the header and footer. These methods take the parameters:

- **Section** – the header or footer section where the picture will be placed. There are three sections, left, center and right, represented by the values 0, 1 and 2 respectively.
- **Byte array** – the graphical data (the binary data should be written into the buffer of a byte array).

After executing the code below and opening the file, check the header of the worksheet by:

1. On the **File** menu, select **Page Setup**. A dialog will be displayed.
1. Select the **Header/Footer** tab.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Image in Header/Footer Example</title>
    </head>
    <body>
        <h1>Insert Image in Header/Footer Example</h1>
        <p>Select an existing Excel file to modify (optional). If none is selected, a new workbook will be used.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>Select an image to insert into the header:</p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Insert Image into Header</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;
        
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the header.</p>';
                return;
            }

            // Read image bytes
            const imageFile = imageInput.files[0];
            const imageBuffer = await imageFile.arrayBuffer();
            const binaryData = new Uint8Array(imageBuffer);

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const excelBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(excelBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet's page setup
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Set the header picture and header scripts (converted from setters to properties)
            pageSetup.headerPicture = binaryData;
            pageSetup.header = "&G";
            pageSetup.header = "&A";

            // Save the workbook as Excel97-2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertImageInHeaderFooter_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Image inserted into header successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```