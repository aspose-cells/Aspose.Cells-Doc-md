---
title: Couper et coller une plage avec JavaScript via C++
linktitle: Couper et coller la plage
type: docs
weight: 130
url: /fr/javascript-cpp/cut-and-paste-cells/
description: Apprenez comment couper et coller des cellules dans une feuille de calcul en utilisant Aspose.Cells for JavaScript via C++.
---

## **Couper et coller des cellules**

Aspose.Cells for JavaScript via C++ vous permet de couper et coller des cellules dans une feuille de calcul en utilisant la méthode [**InsertCutCells**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) de la collection [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells/). La méthode [**InsertCutCells**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) accepte les paramètres suivants.  

- [**Range**](https://reference.aspose.com/cells/javascript-cpp/range/) : La plage de cellules à couper.  
- Index de ligne : L'index de la ligne pour insérer les cellules.  
- Index de colonne : L'index de la colonne pour insèrer les cellules.  
- [**ShiftType**](https://reference.aspose.com/cells/javascript-cpp/shifttype/) : La direction du décalage des colonnes.  

L'exemple suivant montre comment couper et coller des cellules dans une feuille de calcul.  

## **Code d'exemple**  

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
