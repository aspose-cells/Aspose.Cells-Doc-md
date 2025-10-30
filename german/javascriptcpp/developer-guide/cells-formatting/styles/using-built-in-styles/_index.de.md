---
title: Verwendung von integrierten Styles
linktitle: Verwendung von integrierten Styles
type: docs
weight: 80
url: /de/javascript-cpp/using-built-in-styles/
description: JavaScript Code, um die integrierten Excel Stile mit Aspose.Cells for JavaScript via C++ zu verwenden.
keywords: JavaScript, Verwendung der integrierten Excel Stile, Programmatisches Anwenden von Stilen im Arbeitsbuch, JavaScript, Anwendung integrierter Stile in Excel, JavaScript, Code zur Anwendung integrierter Stile im Arbeitsbuch, JavaScript Code, Anwendung integrierter Stile in Excel Arbeitsbüchern
---

{{% alert color="primary" %}}  
Aspose.Cells bietet eine umfangreiche Sammlung von wiederverwendbaren Stilen, um eine Zelle in einem Tabellendokument zu formatieren. Wir können integrierte Stile in unserer Arbeitsmappe verwenden und auch benutzerdefinierte Stile erstellen.  
{{% /alert %}}  

## **Wie man integrierte Styles verwendet**  

Die Methode [**Workbook.createBuiltinStyle(BuiltinStyleType)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createBuiltinStyle-builtinstyletype-) und die Enumeration [**BuiltinStyleType**](https://reference.aspose.com/cells/javascript-cpp/builtinstyletype) machen es bequem, integrierte Stile zu verwenden. Hier ist eine Liste aller möglichen integrierten Stile:  

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
- SeventyPercentAccent1
- SeventyPercentAccent2
- SeventyPercentAccent3
- SeventyPercentAccent4
- SeventyPercentAccent5
- SeventyPercentAccent6
- Akzent1
- Akzent2
- Akzent3
- Akzent4
- Akzent5
- Akzent6
- Schlecht
- Berechnung
- CheckCell
- Komma
- Komma1
- Währung
- Währung1
- ErläuternderText
- Gut
- Überschrift1
- Überschrift2
- Überschrift3
- Überschrift4
- Hyperlink
- FolgenderHyperlink
- Eingabe
- VerknüpfteZelle
- Neutral
- Normal
- Notiz
- Ausgabe
- Prozent
- Titel
- Total
- Warnungstext
- Zeilenebene
- Spaltenebene


## JavaScript-Code zur Verwendung integrierter Stile  
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
