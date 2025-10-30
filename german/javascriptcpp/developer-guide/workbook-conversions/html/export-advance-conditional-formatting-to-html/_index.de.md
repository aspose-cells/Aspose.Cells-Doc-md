---
title: Exportieren Sie DataBar, ColorScale und IconSet Bedingte Formatierung beim Excel zu HTML Export mit JavaScript via C++
linktitle: Datenleiste, Farbskala und IconSet Bedingte Formatierung beim Konvertieren von Excel in HTML exportieren
type: docs
weight: 30
url: /de/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
---

{{% alert color="primary" %}} 

Sie können DataBar, ColorScale und IconSet Bedingte Formatierung beim Konvertieren Ihrer Excel-Datei in HTML exportieren. Diese Funktion wird von Microsoft Excel nur teilweise unterstützt, aber Aspose.Cells for JavaScript via C++ unterstützt sie vollständig.

{{% /alert %}}  

## **Datenleiste, Farbskala und IconSet-Bedingte Formatierung beim Konvertieren von Excel in HTML exportieren**  
Der folgende Screenshot zeigt die [Beispiel-Excel-Datei](5115558.xlsx) mit DataBar, ColorScale und IconSet Bedingter Formatierung. Sie können die [Beispiel-Excel-Datei](5115558.xlsx) über den angegebenen Link herunterladen.  

![todo:image_alt_text](conversion_1.png)  

Der folgende Screenshot zeigt die Aspose.Cells Ausgabe-HTML-Datei mit DataBar, ColorScale und IconSet Bedingter Formatierung. Wie Sie sehen können, sieht es genau wie die [Beispiel-Excel-Datei](5115558.xlsx) aus.  

![todo:image_alt_text](conversion_2.png)  

### **Beispielcode**  
Der folgende Beispielcode konvertiert die Beispiel-Excel-Datei in HTML, was nur eine normale [Excel zu HTML-Konvertierung](/cells/de/javascript-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml) ist.  
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
