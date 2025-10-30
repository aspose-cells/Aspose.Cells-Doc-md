---
title: Exportera DataBar, ColorScale och IconSet Conditional Formatting vid konvertering av Excel till HTML med JavaScript via C++
linktitle: Exportera DataBar, ColorScale och IconSet Villkorlig formatering vid konvertering av Excel till HTML
type: docs
weight: 30
url: /sv/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
---

{{% alert color="primary" %}} 

Du kan exportera villkorsstyrd formatering för DataBar, ColorScale och IconSet när du konverterar din Excel-fil till HTML. Denna funktion stöds delvis av Microsoft Excel men Aspose.Cells for JavaScript via C++ stöder den fullt ut.

{{% /alert %}}  

## **Exportera DataBar, ColorScale och IconSet villkorlig formatering vid Excel till HTML-omvandling**  
Den följande skärmbilden visar [provexelfilen](5115558.xlsx) med DataBar, ColorScale och IconSet Conditional Formatting. Du kan ladda ner [provexelfilen](5115558.xlsx) från den angivna länken.  

![todo:image_alt_text](conversion_1.png)  

Den följande skärmbilden visar Aspose.Cells utdata-HTML-fil som visar DataBar, ColorScale och IconSet Conditional Formatting. Som du kan se ser den ut precis som [provexelfilen](5115558.xlsx).  

![todo:image_alt_text](conversion_2.png)  

### **Exempelkod**  
Följande exempel kod konverterar exempel-Excel-filen till HTML, vilket är en vanlig [Excel till HTML-konvertering](/cells/sv/javascript-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Converting Excel to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in HTML format
            const outputData = workbook.save(SaveFormat.Html);

            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToHTMLFiles_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
