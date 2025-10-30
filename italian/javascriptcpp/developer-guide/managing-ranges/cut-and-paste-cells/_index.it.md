---
title: Taglia e incolla intervallo con JavaScript via C++
linktitle: Taglia e Incolla Intervallo
type: docs
weight: 130
url: /it/javascript-cpp/cut-and-paste-cells/
description: Impara come tagliare e incollare celle all interno di un foglio di lavoro usando Aspose.Cells for JavaScript via C++.
---

## **Taglia e Incolla Celle**

Aspose.Cells for JavaScript via C++ ti permette di tagliare e incollare celle all'interno di un foglio di lavoro usando il metodo [**InsertCutCells**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) della collezione [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells/). Il [**InsertCutCells**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) accetta i seguenti parametri.  

- [**Range**](https://reference.aspose.com/cells/javascript-cpp/range/): L'intervallo di celle da tagliare.  
- Indice riga: L'indice della riga in cui inserire le celle.  
- Indice colonna: L'indice della colonna in cui inserire le celle.  
- [**ShiftType**](https://reference.aspose.com/cells/javascript-cpp/shifttype/): La direzione di spostamento delle colonne.  

L'esempio seguente mostra come tagliare e incollare celle all'interno di un foglio di lavoro.  

## **Codice di Esempio**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Cut and Paste Cells Example</title>
    </head>
    <body>
        <h1>Cut and Paste Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ShiftType } = AsposeCells;

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

            // Create a new workbook
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);

            // Set cell values (columns are zero-based; C is column 2)
            worksheet.cells.get(0, 2).value = 1;
            worksheet.cells.get(1, 2).value = 2;
            worksheet.cells.get(2, 2).value = 3;
            worksheet.cells.get(2, 3).value = 4;

            // Create a named range for the block starting at row 0, column 2, 3 rows, 1 column
            worksheet.cells.createRange(0, 2, 3, 1).name = "NamedRange";

            // Create a range for entire column C and cut/paste it
            const cut = worksheet.cells.createRange("C:C");
            worksheet.cells.insertCutCells(cut, 0, 1, ShiftType.Right);

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CutAndPasteCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
