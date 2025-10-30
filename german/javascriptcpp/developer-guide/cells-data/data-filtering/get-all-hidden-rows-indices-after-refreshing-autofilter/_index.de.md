---
title: Alle versteckten Zeilenindizes nach dem Aktualisieren des Autofilters abrufen. 
type: docs  
weight: 320  
url: /de/javascript-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: Lernen Sie, wie Sie alle versteckten Zeilenindizes nach dem Aktualisieren des AutoFilters mit der Aspose.Cells for JavaScript via C++ API erhalten.  
keywords: Alle versteckten Zeilenindizes nach dem Aktualisieren des AutoFilters mit JavaScript via C++, alle versteckten Zeilenindizes nach dem Aktualisieren des AutoFilters mit JavaScript via C++, alle versteckten Zeilenindizes nach dem Aktualisieren des AutoFilters mit JavaScript via C++ abrufen  
---

## **Mögliche Verwendungsszenarien**  

Wenn Sie den AutoFilter auf Arbeitsblattzellen anwenden, werden einige Zeilen automatisch ausgeblendet. Es kann jedoch sein, dass einige Zeilen bereits manuell von Excel-Endbenutzern ausgeblendet wurden und nicht durch einen AutoFilter versteckt sind. Daher ist es schwierig zu wissen, welche Zeilen durch den AutoFilter versteckt wurden und welche manuell von Excel-Endbenutzern. Aspose.Cells for JavaScript über C++ behandelt dieses Problem mit der `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-). Diese Methode gibt die Zeilenindizes aller Zeilen zurück, die durch den AutoFilter ausgeblendet wurden und nicht manuell vom Excel-Endbenutzer.  

## **Alle versteckten Zeilenindizes nach Aktualisierung des AutoFilters abrufen**  

Siehe den folgenden Beispielcode, der die [Beispiel-Excel-Datei](64716909.xlsx) lädt, die einige Zeilen enthält, die manuell vom Excel-Endbenutzer ausgeblendet wurden. Der Code wendet den AutoFilter an und aktualisiert ihn mit der `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-)-Methode, die die Zeilenindizes aller durch den AutoFilter ausgeblendeten Zeilen zurückgibt. Anschließend werden die Indizes der ausgeblendeten Zeilen auf der Konsole zusammen mit Zellennamen und Werten ausgegeben.  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Hidden Rows After Refreshing AutoFilter</title>
    </head>
    <body>
        <h1>Get Hidden Rows After Refreshing AutoFilter</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Apply autofilter
            worksheet.autoFilter.addFilter(0, "Orange");

            // True means it will refresh autofilter and return hidden rows.
            const rowIndices = worksheet.autoFilter.refresh(true);

            console.log("Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.");
            console.log("--------------------------");

            let output = '<p>Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.</p><pre>';
            rowIndices.forEach(r => {
                const cell = worksheet.cells.get(r, 0);
                console.log(`${r}\t${cell.name}\t${cell.stringValue}`);
                output += `${r}\t${cell.name}\t${cell.stringValue}\n`;
            });
            output += '</pre>';

            resultDiv.innerHTML = output;
        });
    </script>
</html>
```


## **Konsolenausgabe**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}
