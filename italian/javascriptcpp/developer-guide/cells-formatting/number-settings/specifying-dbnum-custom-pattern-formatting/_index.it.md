---
title: Specificare la formattazione del modello personalizzato DBNum
linktitle: Specificare la formattazione del modello personalizzato DBNum
description: Aspose.Cells è una libreria per JavaScript via C++ che supporta la formattazione di date e numeri usando pattern di formattazione personalizzati. Questo articolo mostra come specificare il pattern di formato personalizzato dbnum per un migliore controllo sulla visualizzazione dei numeri.
keywords: Aspose.Cells, JavaScript via C++, foglio elettronico, pattern di formato personalizzato, formattazione, dbnum , controllo visualizzazione
type: docs
weight: 110
url: /it/javascript-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells for JavaScript via C++ supporta la formattazione con pattern personalizzato *DBNum*. Ad esempio, se il valore della cella è 123 e si specifica il formato personalizzato come [DBNum2][$-804]General, verrà visualizzato come 壹佰贰拾叁. È possibile specificare la formattazione personalizzata della cella usando il metodo [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) e il metodo [**Style.custom(string)**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-).

## **Codice di Esempio**

Il codice esempio seguente illustra come specificare il formato di pattern personalizzato *DBNum*. Si prega di controllare il [output PDF](43352081.pdf) per ulteriori aiuti.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - DBNum Custom Formatting Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Access cell A1 and put value 123.
            const cell = ws.cells.get("A1");
            cell.value = 123;

            // Access cell style.
            const st = cell.style;

            // Specifying DBNum custom pattern formatting.
            st.custom = "[DBNum2][$-804]General";

            // Set the cell style.
            cell.style = st;

            // Set the first column width.
            ws.cells.columns.get(0).width = 30;

            // Save the workbook in output pdf format.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDBNumCustomFormatting.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
