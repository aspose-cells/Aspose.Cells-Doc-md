---
title: Using Built-in Styles
linktitle: Using Built-in Styles
type: docs
weight: 80
url: /javascript-cpp/using-built-in-styles/
description: JavaScript code to use Excel built-in styles with Aspose.Cells for JavaScript via C++.
keywords: JavaScript use excel built in styles, JavaScript programmatically apply styles in workbook, programmatically apply styles in workbook, JavaScript apply built in styles in excel, JavaScript apply built in styles in workbook, JavaScript code apply built in styles in workbook, JavaScript code apply built in styles in excel workbook
---

{{% alert color="primary" %}}  
Aspose.Cells provides a vast collection of re-usable styles to format a cell in spreadsheet document. We can use built-in styles in our workbook and also create custom styles.  
{{% /alert %}}  

## **How to use Built-in Styles**  

The method [**Workbook.createBuiltinStyle(BuiltinStyleType)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createBuiltinStyle-builtinstyletype-) and the enumeration [**BuiltinStyleType**](https://reference.aspose.com/cells/javascript-cpp/builtinstyletype) make it convenient to use built-in styles. Here is a list of all possible built-in styles:  

- TwentyPercentAccent1
- TwentyPercentAccent2
- TwentyPercentAccent3
- TwentyPercentAccent4
- TwentyPercentAccent5
- TwentyPercentAccent6
- FortyPercentAccent1
- FortyPercentAccent2
- FortyPercentAccent3
- FortyPercentAccent4
- FortyPercentAccent5
- FortyPercentAccent6
- SixtyPercentAccent1
- SixtyPercentAccent2
- SixtyPercentAccent3
- SixtyPercentAccent4
- SixtyPercentAccent5
- SixtyPercentAccent6
- Accent1
- Accent2
- Accent3
- Accent4
- Accent5
- Accent6
- Bad
- Calculation
- CheckCell
- Comma
- Comma1
- Currency
- Currency1
- ExplanatoryText
- Good
- Header1
- Header2
- Header3
- Header4
- Hyperlink
- FollowedHyperlink
- Input
- LinkedCell
- Neutral
- Normal
- Note
- Output
- Percent
- Title
- Total
- WarningText
- RowLevel
- ColumnLevel


## JavaScript code to use built-in styles  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Output.xlsx</a>
        <a id="downloadLink2" style="display: none;">Download Output.out.ods</a>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Creating a new Workbook
            const workbook = new Workbook();
            
            // Creating a built-in style (Title)
            const style = workbook.createBuiltinStyle(AsposeCells.BuiltinStyleType.Title);
            
            // Accessing first worksheet, its cells, and cell A1
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");
            
            // Setting cell value and style (converted setter)
            cell.putValue("Aspose");
            cell.style = style;
            
            // Auto-fit column and row
            worksheet.autoFitColumn(0);
            worksheet.autoFitRow(0);
            
            // Save as XLSX
            const outputData1 = workbook.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'Output.xlsx';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Output.xlsx';
            
            // Save as ODS
            const outputData2 = workbook.save(SaveFormat.Ods);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'Output.out.ods';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Output.out.ods';
            
            document.getElementById('result').innerHTML = '<p style="color: green;">Files generated. Click the download links to save them.</p>';
        });
    </script>
</html>
```