---
title: Proteger o quitar protección con contraseña del libro compartido con JavaScript vía C++
linktitle: Proteger o Quitar Protección al Libro de Trabajo Compartido
type: docs
weight: 10
url: /es/javascript-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **Escenarios de uso posibles**

Puedes proteger o quitar la protección del libro compartido con Microsoft Excel como se muestra en la siguiente captura de pantalla. Aspose.Cells for JavaScript vía C++ también soporta esta función con los métodos [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#protectSharedWorkbook-string-) y [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#unprotectSharedWorkbook-string-).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Proteger o Quitar Protección al Libro de Trabajo Compartido**

El siguiente código de ejemplo crea un libro de trabajo y lo protege mientras habilita el uso compartido y lo guarda como [archivo de Excel de salida](55541777.xlsx). La captura de pantalla muestra que cuando intentas quitar la protección, Microsoft Excel te pedirá que ingreses la contraseña para quitarla.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Shared Workbook Example</h1>
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
            // Creating an empty Workbook
            const workbook = new Workbook();

            // Protect the Shared Workbook with Password
            workbook.protectSharedWorkbook("1234");

            // Uncomment this line to Unprotect the Shared Workbook
            // workbook.unprotectSharedWorkbook("1234");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputProtectSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
